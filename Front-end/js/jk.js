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
                $("#progress1").fadeOut();
                $("#submit").attr("class","btn btn-success btn-sm");
                $("#submit").attr("value","再次查询");
                $("#table1").append(data);
                $("#card3").fadeIn();
                $("#warning").remove();
            },
            error: function (xhr, type) { //【失败回调】
                console.log("error");
                $("#progress1").fadeOut();
                $("#submit").attr("class","btn btn-danger btn-sm");
                $("#submit").attr("value","请重试");
                $("#warning").append("<br /><p style='color: red;'>账号/密码错误或服务器/网络问题,<br />若一直出现此问题请联系网站管理员。</p>");
            }
        });

        $("#progress1").fadeIn();
        setTimeout(timeout1, 1500)
        setTimeout(timeout2, 4000)
        setTimeout(timeout3, 6000)
        setTimeout(timeout4, 10000)

        function timeout1() {
            $("#progress1_inside").attr("style", "width: 65%");
            $("#progress1_inside").html("很多浏览器的进度条都是假的");
        }
        function timeout2() {
            $("#progress1_inside").attr("style", "width: 25%");
            $("#progress1_inside").html("比如这样");
        }
        function timeout3() {
            $("#progress1_inside").attr("style", "width: 85%");
            $("#progress1_inside").html("只有少数浏览器是按照步骤显示进度");
        }
        function timeout4() {
            $("#progress1_inside").attr("style", "width: 100%");
            $("#progress1_inside").html("还没好吗？？？");
        }
    });
});