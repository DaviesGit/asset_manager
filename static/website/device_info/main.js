var devices = [
    {
        "device_id": "3452354",
        "device_name": "矢量分析仪",
        "device_type": "分析仪",
        "specifications": "10MHz-26.5GHz",
        "device_model": "8510SX",
        "location": "一号科研办公楼C-306",
        "status": "在库",
        "device_pic": "http://dygkpt.uestc.edu.cn/order-portlet/images/14010060.jpg",
        "warranty_date": "2022年11月21日",
        "purchase_date": "2018年11月21日",
        "registry_date": "2018年11月22日",
        "supplier": "德国SPECS",
        "comment": "此设备由王经理购买于德国",
        "belong": "成都**科技有限公司",
        "user_id": "201634523",
        "user_name": "王国强",
        "user_tel": "15187989769",
        "user_email": "wangguoqaing@foxmail.com"
    },
    {
        "device_id": "7547653",
        "device_name": "台式电脑",
        "device_type": "电子设备",
        "specifications": "0.01nm~1nm/min",
        "device_model": "EBE-4",
        "location": "二号计算机机房C-306",
        "status": "在库",
        "device_pic": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1542284885&di=12ee11b4dacdf80ebacb46edcc2dc493&imgtype=jpg&er=1&src=http%3A%2F%2Fp1.pccoo.cn%2Fyp%2F20130625%2F201306251128206286.jpg",
        "warranty_date": "2024年11月21日",
        "purchase_date": "2017年1月2日",
        "registry_date": "2017年1月2日",
        "supplier": "联想",
        "comment": "此设备由采购购买于电脑城",
        "belong": "成都**科技有限公司",
        "user_id": "2017034658",
        "user_name": "张国凡",
        "user_tel": "17187969234",
        "user_email": "zhangguofan@foxmail.com"
    }
]


var borrow_property = [
    'borrow_device_id',
    'borrow_user_id',
    'borrow_user_name',
    'borrow_user_tel',
    'borrow_user_email',
    'borrow_lend_time',
    'borrow_pre_return',
    'borrow_reason'
]


function init() {
    var search = new URLSearchParams(window.location.search);
    var device_id = search.get('device_id');
    if (!device_id) {
        alert('request url error!');
        return;
    }
    $.post('/command', {
        command: "get_device",
        data: JSON.stringify({
            device_id: device_id
        })
    }, function (response) {
        if (response.status) {
            return alert('获取设备信息失败，错误信息是：' + response.error);
        }
        var device = response.data;
        for (var property in device) {
            switch (property) {
                case 'device_pic':
                    $('#' + property).attr('src', device[property]).removeClass('loading');
                    break;
                case 'belong_id':
                    $('#' + 'belong').text(device[property]).removeClass('loading');
                    break;
                default:
                    $('#' + property).text(device[property]).removeClass('loading');
            }
        }
    });
    // var device = devices[1];
    // for (var property in device) {
    //     if ('device_pic' === property) {
    //         $('#' + property).attr('src', device[property]).removeClass('loading');
    //         continue;
    //     }
    //     $('#' + property).text(device[property]).removeClass('loading');
    // }


    var dialog_borrow = $('#borrow_confirm').dialog({
        autoOpen: false,
        height: 600 > document.documentElement.clientHeight ? document.documentElement.clientHeight : 600,
        width: 800 > document.documentElement.clientWidth ? document.documentElement.clientWidth : 800,
        modal: true,
        show: {
            effect: "fold",
            duration: 1000
        },
        close: function () {

        },
        open: function (event, ui) {
            dialog_borrow.dialog({
                hide: {
                    effect: "explode",
                    duration: 1000
                }
            });
            $("body").css({ overflow: 'hidden' })
        },
        beforeClose: function (event, ui) {
            $("body").css({ overflow: 'inherit' })
        }
    });
    var dialog_qrcode = $('#img_qrcode').dialog({
        autoOpen: false,
        height: 442,
        width: 402,
        modal: true,
        resizable: false,
        show: {
            effect: "fold",
            duration: 1000
        },
        hide: {
            effect: "explode",
            duration: 1000
        },
        close: function () {

        },
        open: function (event, ui) {
            $("body").css({ overflow: 'hidden' })
        },
        beforeClose: function (event, ui) {
            $("body").css({ overflow: 'inherit' })
        }
    });

    $('#button_qrcode').on('click', function (event) {
        event.preventDefault();
        $('#img_qrcode').attr('src', '/qrcode?device_id=' + $('#device_id').text());
        dialog_qrcode.dialog("open");
    });

    $('#button_repair').on('click', function (event) {
        event.preventDefault();
    });
    $('#button_borrow').on('click', function (event) {
        event.preventDefault();
        dialog_borrow.dialog("open");
        $('#borrow_device_id').val($('#device_id').text());
        var date = new Date();
        var str_borrow_date = date.getFullYear() + '年' + (date.getMonth() + 1) + '月' + date.getDate() + '日' + date.getHours() + '时' + date.getMinutes() + '分';
        date.setDate(date.getDate() + 7);
        var str_pre_return_date = date.getFullYear() + '年' + (date.getMonth() + 1) + '月' + date.getDate() + '日' + date.getHours() + '时' + date.getMinutes() + '分';
        $('#borrow_lend_time').val(str_borrow_date);
        $('#borrow_pre_return').val(str_pre_return_date);
        $("#borrow_user_id").val('201613150803');
        $("#borrow_user_name").val('王科');
        $("#borrow_user_tel").val('15187694596');
        $("#borrow_user_email").val('wangke@mail.com');

    });
    $('#button_scrap').on('click', function (event) {
        event.preventDefault();
    });

    $('#button_borrow_confirm').on('click', function (event) {
        var borrow_info = {};
        var valid = true;
        event.preventDefault();
        for (var property of borrow_property) {
            borrow_info[property] = $('#' + property).val();
        }
        borrow_info.borrow_lend_time = + new Date(Date(borrow_info.borrow_lend_time.replace(/[年月日时]/g, '-').replace(/[分]/g, '')));
        borrow_info.borrow_pre_return = + new Date(Date(borrow_info.borrow_pre_return.replace(/[年月日时]/g, '-').replace(/[分]/g, '')));

        $.post('/command', {
            command: 'borrow_device',
            data: JSON.stringify(borrow_info)
        }, function (response) {
            if (response.status) {
                alert('借用失败');
            } else {
                alert('借用成功');
            }
            location.reload();
        });

        dialog_borrow.dialog({
            hide: {
                effect: "clip",
                duration: 1000
            }
        });
        dialog_borrow.dialog("close");

        // setTimeout(function () { alert('借用成功'); }, 1000);
    });
    $('#button_borrow_cancel').on('click', function (event) {
        event.preventDefault();
        dialog_borrow.dialog("close");
    });
}



$(function () {
    init();
});




