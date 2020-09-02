var properties = [
    'device_id',
    'device_name',
    'device_type',
    'specifications',
    'device_model',
    'location',
    'status',
    'device_pic',
    'warranty_date',
    'purchase_date',
    'registry_date',
    'supplier',
    'comment',
    'belong',
    'user_id',
    'user_name',
    'user_tel',
    'user_email'
]
var device = {
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
};

function get_time_stamp(data) {
    return +new Date(Date(data.replace(/[年月]/g, '-').replace(/[日]/g, '')));
}

$(function () {
    for (property in device) {
        if ('device_pic' === property) continue;
        $('#' + property).val(device[property]);
    }
    $('#button_cancel').on('click', function (event) {
        event.preventDefault();
        window.location.href = '../all_devices/all_devices.html';
    });
    $('#button_empty').on('click', function (event) {
        event.preventDefault();
        for (property of properties) {
            $('#' + property).val('');
        }
    });
    $('#button_submit').on('click', function (event) {
        event.preventDefault()
        var device = {};
        var form_data = new FormData();
        for (property of properties) {
            device[property] = $('#' + property).val();
        }
        device.warranty_date = get_time_stamp(device.warranty_date);
        device.purchase_date = get_time_stamp(device.purchase_date);
        device.registry_date = get_time_stamp(device.registry_date);
        form_data.append('command', 'add_device');
        form_data.append('data', JSON.stringify(device));
        form_data.append('device_pic', $('#device_pic')[0].files[0]);

        $.ajax({
            url: '/command',
            type: 'POST',
            data: form_data,
            processData: false,
            contentType: false,
            success: function (response) {
                if (!response || response.status) {
                    alert('上传失败！');
                } else {
                    alert('上传成功！');
                    location.href = '../all_devices/all_devices.html';
                }
            },
        });
    });

    $('#device_pic').change(function () {
        var file = $('#device_pic')[0].files[0];
        var reader = new FileReader();
        reader.onloadend = function () {
            $('#img_preview').attr('src', reader.result);
        }
        if (file) {
            if (file.name.match(/\.(jpg|jpeg|png|gif)$/)) {
                reader.readAsDataURL(file);
            } else {
                alert('必须选择jpg|jpeg|png|gif图片文件！');
            }
        }
    });


});
