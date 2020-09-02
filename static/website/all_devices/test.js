$.ajax({
    url: 'http://192.168.43.212:8080/command',
    type: 'POST',
    data: {
        "command": "get_devices",
        "data": JSON.stringify({
            "page": 2,
            "devices_per_page": 3
        })
    },
    success: function (response) {
        console.log(response);
    }
})

$.post('http://192.168.43.212:8080/command', {
    "command": "get_devices",
    "data": JSON.stringify({
        "page": 1,
        "devices_per_page": 5
    })
}, function (response) {
    console.log(response);
})
    // (page - 1) * devices_per_page :(page ) * devices_per_page