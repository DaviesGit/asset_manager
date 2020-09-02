from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from dzkd.settings import BASE_DIR
import re
import smtplib
from email.mime.text import MIMEText
from .models import *
import json
import qrcode
import xlrd


def command(req):
    try:
        com = req.POST.get("command")
        if com == "get_device":
            data = json.loads(req.POST.get("data"))
            msg = get_device(data["device_id"])
            return JsonResponse(msg)

        elif com == 'borrow_device':
            data = json.loads(req.POST.get('data'))
            result = borrow_device(data)
            return JsonResponse(result)

        elif com == "get_devices":
            all_msg = {"status": 0, "data": []}
            data = json.loads(req.POST.get("data"))
            msg = Device.objects.all()[(int(data["page"])-1)*int(data["devices_per_page"]):(int(data["page"]))*int(data["devices_per_page"])]
            for i in msg:
                x = get_device(i.pk)
                all_msg["data"].append(x["data"])
            return JsonResponse(all_msg)

        elif com == "add_device":
            data = json.loads(req.POST.get("data"))
            if 'device_pic' in req.FILES:
                pic = req.FILES.get("device_pic")
            else:
                pic = ''
            msg = add_Device(data, pic)
            return JsonResponse(msg)

    except:
        return JsonResponse({"status": 1})


def erweima(req):
    com = req.GET.get("device_id")
    if len(Device.objects.filter(device_id=com)) != 0:
        c = crQrcode(com)
        return HttpResponse(c, content_type="image/png")
    else:
        return JsonResponse({"status": 1})

# 生成二维码
def crQrcode(com):
    msg = "192.168.43.212?device_id=" + com
    img = qrcode.make(msg)
    img.save('erweima.png')
    with open('erweima.png', 'rb')as f:
        c = f.read()
    return c


# 查找二维码里的信息内容
def search(req):
    id = req.GET.get("device_id")
    msg = Device.objects.filter(device_id=id).values()
    return HttpResponse(msg)


def h(req):
    return render(req, 'tmp.html')


# 处理上传的excel表，目前只支持device的信息
def upload(req):
    f = req.FILES.get("image")
    if f.size < 10000000:
        with open(BASE_DIR + "/static/excel/" + f.name, "wb")as file:
            for chunk in f.chunks():  # 分块写入文件
                file.write(chunk)
        excel = xlrd.open_workbook(BASE_DIR + "/static/excel/" + f.name)
        table = excel.sheet_by_index(0)
        key_list = table.row_values(0)
        err_load = []
        for i in range(1, len(table.col(0))):
            dic = dict(zip(key_list, table.row_values(i)))
            d = device2excel(dic)
            if d is False:
                err_load.append(i + 1)
        return JsonResponse({"err": err_load})


# 出错大概率是归属科室belong不存在，应该先建立科室信息
def device2excel(dic):
    try:
        if dic["device_id"] == "":
            return False
        if (dic.get("warranty_date") is None) or dic["warranty_date"] == "":
            dic["warranty_date"] = None
        if (dic.get("purchase_date") is None) or dic["purchase_date"] == "":
            dic["purchase_date"] = None
        if (dic.get("registry_date") is None) or dic["registry_date"] == "":
            dic["registry_date"] = None
        if (dic.get("status") is None) or dic["status"] == "":
            dic["status"] = "空闲"
        for i in dic:
            if type(dic[i]) is float:
                dic[i] = str(int(dic[i]))
        if len(Device.objects.filter(device_id=dic["device_id"])) == 0:
            Device.objects.create(
                device_id=dic.get("device_id"),
                device_name=dic.get("device_name"),
                device_pic=dic.get("device_pic"),
                device_type=dic.get("device_type"),
                specifications=dic.get("specifications"),
                device_model=dic.get("device_model"),
                warranty_date=dic.get("warranty_date"),
                purchase_date=dic.get("purchase_date"),
                registry_date=dic.get("registry_date"),
                location=dic.get("location"),
                supplier=dic.get("supplier"),
                status=dic.get("status"),
                comment=dic.get("comment"),
            )
            if (dic.get("belong") != "") and (dic.get("belong") is not None):
                Device.objects.filter(device_id=dic["device_id"]).update(belong=str(dic["belong"]))

        else:
            Device.objects.filter(device_id=dic["device_id"]).update(
                device_name=dic.get("device_name"),
                device_pic=dic.get("device_pic"),
                device_type=dic.get("device_type"),
                specifications=dic.get("specifications"),
                device_model=dic.get("device_model"),
                warranty_date=dic.get("warranty_date"),
                purchase_date=dic.get("purchase_date"),
                registry_date=dic.get("registry_date"),
                location=dic.get("location"),
                supplier=dic.get("supplier"),
                status=dic.get("status"),
                comment=dic.get("comment")
            )
            if (dic.get("belong") != "") and (dic.get("belong") is not None):
                Device.objects.filter(device_id=dic["device_id"]).update(belong=dic["belong"])
        return True

    except:
        return False


def get_device(id):
    try:
        msg_device = Device.objects.filter(device_id=id).values()[0]
        msg_department = Department.objects.filter(belong=msg_device.get("belong_id")).values()
        if len(msg_department) != 0:
            msg_user = User.objects.filter(user_id=msg_department[0].get("belong_contact_id")).values()
            if len(msg_user) != 0:
                msg = {**msg_device, **msg_user[0]}
            else:
                msg = msg_device
        else:
            msg = msg_device

        url = msg.get("device_pic")
        if url is None:
            url = ''
        msg["device_pic"] = "/static/images/" + url
        x = {"status": 0, "data": msg}
        return x
    except:
        return {"status": 1, "error": "device not found"}


def send_email(message):
    msg_from = 'gscalpel@163.com'
    passwd = '19981115l'
    mail_host = "smtp.163.com"
    port = 465
    subject = "设备借用"
    content = "【设备借用】用户{} {} 请求借用{} {}".format(
        message.get("user_id"),
        message.get("user_name"),
        message.get("device_id"),
        message.get("device_name")
    )
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    # 创建连接对象并连接到服务器
    s = smtplib.SMTP_SSL(mail_host, port)
    # 登录服务器
    mail_list = ["18512855939@wo.cn"]
    s.login(msg_from, passwd)
    for i in range(0, len(mail_list)):
        msg_to = mail_list[i]
        msg['To'] = msg_to
        s.sendmail(msg_from, msg_to, msg.as_string())


def borrow_device(data):
    try:
        BorrowManage.objects.create(
            device_id_id=data["borrow_device_id"],
            user_id=data['borrow_user_id'],
            lend_time=data['borrow_lend_time'],
            pre_return=data['borrow_pre_return'],
            reason=data['borrow_reason'],
        )

        user = User.objects.filter(user_id=data["borrow_user_id"]).values("user_name", "user_email")
        device = Device.objects.filter(device_id=data["borrow_device_id"]).values("device_name")
        message = {"user_id": data['borrow_user_id'],
                   "user_name": user[0]["user_name"],
                   "user_email": user[0]["user_email"],
                   "device_id": data["borrow_device_id"],
                   "device_name": device[0]["device_name"]
                   }
        Device.objects.filter(device_id=data["borrow_device_id"]).update(status="借出")
        send_email(message)
        return {'status': 0}
    except:
        return {'status': 1}


def add_Device(msg, pic):
    try:
        if pic == '' or re.match(r'^[0-9a-zA-Z\_]+\.(jpg|png|jpeg)$', pic.name) is None:
            Device.objects.create(
                device_id=msg.get("device_id"),
                device_name=msg.get("device_name"),
                device_type=msg.get("device_type"),
                specifications=msg.get("specifications"),
                device_model=msg.get("device_model"),
                warranty_date=msg.get("warranty_date"),
                purchase_date=msg.get("purchase_date"),
                registry_date=msg.get("registry_date"),
                location=msg.get("location"),
                supplier=msg.get("supplier"),
                status=msg.get("status"),
                comment=msg.get("comment"),
            )
        else:
            Device.objects.create(
                device_id=msg.get("device_id"),
                device_name=msg.get("device_name"),
                device_type=msg.get("device_type"),
                device_pic=pic,
                specifications=msg.get("specifications"),
                device_model=msg.get("device_model"),
                warranty_date=msg.get("warranty_date"),
                purchase_date=msg.get("purchase_date"),
                registry_date=msg.get("registry_date"),
                location=msg.get("location"),
                supplier=msg.get("supplier"),
                status=msg.get("status"),
                comment=msg.get("comment"),
            )
        return {"status": 0}
    except:
        return {"status": 1}
