$.post('http://172.19.110.89:8000/command', {
    command: "get_device",
    data: JSON.stringify({
        device_id: '2016'
    })
}, function (response) {
    debugger;
    if (response.status) {
        return alert('获取设备信息失败，错误信息是：' + response.error);
    }

    console.log(response);
    return;
    var device = response.date;
    for (var property in device) {
        if ('device_pic' === property) {
            $('#' + property).attr('src', device[property]).removeCalss('loading');
            continue;
        }
        $('#' + property).text(device[property]).removeCalss('loading');
    }
});





$.post('http://192.168.1.105:8080/command', {
    command: 'borrow_device',
    data: JSON.stringify(
        {
            "borrow_device_id": "100",
            "borrow_user_id": "201613150803",
            "borrow_user_name": "王国强",
            "borrow_user_tel": "15187989769",
            "borrow_user_email": "wangguoqaing@foxmail.com",
            "borrow_lend_time": "1234",
            "borrow_pre_return": "1234",
            "borrow_reason": "科学研究"
        }
    )
}, function (response) {
    console.log(response);
    response = JSON.stringify(response);
    // if (!response.status) {
    //     alert('借用失败');
    // } else {
    //     alert('借用成功');
    // }
});

