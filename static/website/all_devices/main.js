$(function () {



    $.post('/command', {
        "command": "get_devices",
        "data": JSON.stringify({
            "page": 1,
            "devices_per_page": 36
        })
    }, function (response) {
        if (response.status || !response.data.length) {
            return alert('获取设备失败！');
        }
        response.data.forEach(function (device, index) {
            html = `
                	<li class="list-detail" onclick="location.href='../device_info/device_info.html?device_id=` + device.device_id + `';">
                        <div class="img list-detail-left"><a href="javascript:void(0)"><img class="lazy" src="`+ device.device_pic + `" style="display: inline;"></a></div>
                        <div class="info list-detail-right">
                            <p class="name">`+ device.device_name + `</p><span class="sort"><span>生产商： ` + device.device_name + `</span> 型号：` + device.device_model + `</span>
                        </div>
                    </li>`;
            $('#_order_WAR_orderportlet_INSTANCE_7bUugyvIvMt3_shppingInfo').prepend(html);
        });
        var devices_html = $('#_order_WAR_orderportlet_INSTANCE_7bUugyvIvMt3_shppingInfo>li');
        for (var i = 0, len = devices_html.length % 4; i < len; ++i) {
            devices_html.get(devices_html.length - i - 1).remove();
        }
    });


});