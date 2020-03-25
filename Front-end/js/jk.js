$(function () {
    const next1_s = $("#next1");
    const card2_s = $("#card2");
    const card3_s = $("#card3");
    const form_s = $("#form");
    const progress1_s = $("#progress1");
    const progress1_inside_s = $("#progress1_inside");
    const warning_s = $("#warning");
    const submit_s = $("#submit");

    next1_s.on("click", function () {
        card2_s.fadeIn();
    });

    submit_s.on("click", function () {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/jk/",
            dataType: 'html',
            data: form_s.serialize(),
        }).then(function (data) { //【成功回调】
            console.log("success");
            progress1_s.fadeOut();
            submit_s.attr("class", "btn btn-success btn-sm");
            submit_s.attr("value", "再次查询");
            $("#table1").append(data);
            card3_s.fadeIn();
            warning_s.remove();
        }, function (xhr, type) { //【失败回调】
            console.log("error");
            progress1_s.fadeOut();
            submit_s.attr("class", "btn btn-danger btn-sm");
            submit_s.attr("value", "请重试");
            warning_s.html("<br /><p style='color: red;'>账号/密码错误或服务器/网络问题,<br />若一直出现此问题请联系网站管理员。</p>");
        });

        progress1_s.fadeIn();
        setTimeout(timeout1, 1500)
        setTimeout(timeout2, 4000)
        setTimeout(timeout3, 6000)
        setTimeout(timeout4, 10000)

        function timeout1() {
            progress1_inside_s.attr("style", "width: 65%");
            progress1_inside_s.html("很多浏览器的进度条都是假的");
        }

        function timeout2() {
            progress1_inside_s.attr("style", "width: 25%");
            progress1_inside_s.html("比如这样");
        }

        function timeout3() {
            progress1_inside_s.attr("style", "width: 85%");
            progress1_inside_s.html("只有少数浏览器是按照步骤显示进度");
        }

        function timeout4() {
            progress1_inside_s.attr("style", "width: 100%");
            progress1_inside_s.html("还没好吗？？？");
        }
    });
});