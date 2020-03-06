$(document).ready(function () {

    $("#next1").click(function () {
        $("#card2").fadeIn();
    });

    $("#submit").click(function () {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/jk/",
            dataType: 'html',
            data: $('#form').serialize(),
            success: function (data) { //【成功回调】
                console.log("success");
                $("#submit").attr("class","btn btn-primary");
                $("#submit").attr("value","提交查询");
                $("#table1").append(data);
                $("#card3").fadeIn();
                $("#warning").remove();
            },
            error: function (xhr, type) { //【失败回调】
                console.log("error");
                $("#submit").attr("class","btn btn-danger");
                $("#submit").attr("value","请重试");
                $("#warning").append("<br /><p style='color: red;'>账号/密码错误或服务器/网络问题,<br />若一直出现此问题请联系网站管理员。</p>");
            }
        });
    });
});