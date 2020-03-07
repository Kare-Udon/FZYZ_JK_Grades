$(document).ready(function () {

    $("#next1").click(function () {
        $("#card1").fadeIn();
    });

    $("#next2").click(function () {
        $("#card2").fadeIn();
    });


    $("#next2").click(function () {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/fzyz_net_exam/",
            async: true,
            dataType: 'json',
            data: $('#form').serialize(),
            success: function (data) { //【成功回调】
                console.log("success");
                $("#next2").attr("class","btn btn-success");
                $("#next2").html("成功");
                $("#card2").fadeIn();
                $("#warning").remove();
                json = eval(data.data);
                for (var i = 0; i < json.length; i++) {
                    $('#select2').append("<option value='" + json[i].KEY + "'>" + json[i].TEXT + "</option>");
                };
            },
            error: function (xhr, type) { //【失败回调】
                console.log("error");
                $("#next2").attr("class","btn btn-danger");
                $("#next2").html("请重试");
                $("#card2").fadeOut();
                $("#warning").append("<p style='color: red;'>账号/密码错误或服务器/网络问题,<br />若一直出现此问题请联系网站管理员。</p>");
            }
        });
    });

    $("#submit").click(function () {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/fzyz_net/",
            dataType: 'html',
            data: $('#form').serialize(),
            success: function (data) { //【成功回调】
                console.log("success");
                $("#tbody1").find("tr").remove();
                $("#tbody1").append(data);
                document.querySelectorAll('tr').forEach(
                    tr => [
                        "width", "height", "class", "bgcolor", "align"
                    ].forEach(
                        attr => tr.removeAttribute(attr)
                    )
                );
                document.querySelectorAll('td').forEach(
                    td => [
                        "width", "height", "class", "bgcolor", "align"
                    ].forEach(
                        attr => td.removeAttribute(attr)
                    )
                );
                $("#table1 tr").eq(0).remove();
                $("#table1 tr").eq(0).remove();
                $("#table1 tr").eq(-1).remove();
                $("#card3").fadeIn();
            },
            error: function (xhr, type) { //【失败回调】
                console.log("error");
                $("#submit").attr("class","btn btn-danger");
                $("#submit").attr("value","请重试");
                $("#warning2").append("<br /><p style='color: red;'>服务器/网络问题，<br />若一直出现此问题请联系网站管理员。</p>");
            }
        });
    });
});
