from django.db import models


class Device(models.Model):
    device_id = models.TextField(primary_key=True, verbose_name="设备编号")
    device_name = models.TextField(verbose_name='设备名称', blank=True, null=True)
    device_pic = models.ImageField(verbose_name="设备图片", blank=True, upload_to="device/", null=True)
    device_type = models.TextField(verbose_name='设备类型', blank=True, null=True)
    specifications = models.TextField(verbose_name='规格', blank=True, null=True)
    device_model = models.TextField(verbose_name='设备型号', blank=True, null=True)
    warranty_date = models.IntegerField(verbose_name='保修日期', blank=True, null=True)
    purchase_date = models.IntegerField(verbose_name='采购日期', blank=True, null=True)
    registry_date = models.IntegerField(verbose_name='登记日期', blank=True, null=True)
    location = models.TextField(verbose_name='存放位置', blank=True, null=True)
    supplier = models.TextField(verbose_name='供应商', blank=True, null=True)
    status = models.TextField(verbose_name='设备状态', blank=True, null=True)
    comment = models.TextField(verbose_name='备注', blank=True, null=True)
    belong = models.ForeignKey('Department', on_delete=models.DO_NOTHING, blank=True, verbose_name="归属科室", null=True)


class Department(models.Model):
    belong = models.TextField(primary_key=True, verbose_name='归属科室', blank=True)
    belong_contact = models.ForeignKey('User', verbose_name='科室联系人', blank=True, on_delete=models.DO_NOTHING, null=True)
    comment = models.TextField(verbose_name='备注', blank=True, null=True)


class User(models.Model):
    user_id = models.TextField(verbose_name="用户编号", primary_key=True)
    user_name = models.TextField(verbose_name="用户名字", blank=True, null=True)
    user_tel = models.TextField(verbose_name='用户电话', blank=True, null=True)
    user_email = models.TextField(verbose_name='用户邮箱', blank=True, null=True)


class BorrowManage(models.Model):
    device_id = models.ForeignKey('Device', on_delete=models.DO_NOTHING, verbose_name="设备编号")
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, verbose_name="借出者")
    lend_time = models.IntegerField(verbose_name='借出时间', blank=True, null=True)
    pre_return = models.IntegerField(verbose_name='预归还时间', blank=True, null=True)
    return_time = models.IntegerField(verbose_name='归还时间', blank=True, null=True)
    reason = models.TextField(verbose_name='借出原因', blank=True, null=True)


class Repair(models.Model):
    device_id = models.ForeignKey('Device', on_delete=models.DO_NOTHING, verbose_name="设备编号")
    repair_time = models.IntegerField(verbose_name='维修时间', blank=True, null=True)
    repair_fin = models.IntegerField(verbose_name='维修完成时间', blank=True, null=True)
    repair_man = models.TextField(verbose_name='维修人', blank=True, null=True)
    repair_money = models.TextField(verbose_name='维修金额', blank=True, null=True)
    repair_num = models.TextField(verbose_name='维修人电话', blank=True, null=True)
    comment = models.TextField(verbose_name='备注', blank=True, null=True)


class Scrap(models.Model):
    device_id = models.OneToOneField('Device', primary_key=True, on_delete=models.DO_NOTHING, verbose_name="设备编号")
    scrap_reason = models.TextField(verbose_name='报废原因', blank=True, null=True)
    available_year = models.IntegerField(verbose_name='使用年限', blank=True, null=True)
    comment = models.TextField(verbose_name='备注', blank=True, null=True)
