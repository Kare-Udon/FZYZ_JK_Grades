

$(document).ready(function () {
    $("#btn").click(function () {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/fzyz_net_exam",
            dataType: 'jsonp', //【jsonp进行跨域请求 只支持get】
            jsonp: "jsonpcallback",
            data: $('#form').serialize(),
            success: function (data) { //【成功回调】
                console.log(data);
            },
            error: function (xhr, type) { //【失败回调】
            }
        });
    });
});
