$(function () {
    const next1_s = $("#next1");
    const card1_s = $("#card1");
    const next2_s = $("#next2")
    const card2_s = $("#card2");
    const card3_s = $("#card3");
    const form_s = $("#form");
    const progress1_s = $("#progress1");
    const progress1_inside_s = $("#progress1_inside");
    const progress2_s = $("#progress2");
    const progress2_inside_s = $("#progress2_inside");
    const warning_s = $("#warning");
    const submit_s = $("#submit");

    next1_s.on("click", function () {
        card1_s.fadeIn();
    });

    next2_s.on("click", function () {
        card2_s.fadeIn();

        if (!/^\d{11}$/.test(form_s.serializeArray()[0]["value"])) {
            console.log("error");
            progress1_s.fadeOut();
            next2_s.attr("class", "btn btn-danger btn-sm");
            next2_s.html("请重试");
            card2_s.fadeOut();
            warning_s.html("<p style='color: red;'>账号格式错误</p>");
            return;
        }

        if (!form_s.serializeArray()[1]["value"]) {
            console.log("error");
            progress1_s.fadeOut();
            next2_s.attr("class", "btn btn-danger btn-sm");
            next2_s.html("请重试");
            card2_s.fadeOut();
            warning_s.html("<p style='color: red;'>密码未输入</p>");
            return;
        }

        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/fzyz_net_exam/",
            async: true,
            dataType: 'json',
            data: form_s.serialize(),
        }).then(function (data) { //【成功回调】
            console.log("success");
            progress1_s.fadeOut();
            next2_s.attr("class", "btn btn-success btn-sm");
            next2_s.html("成功");
            card2_s.fadeIn();
            warning_s.remove();
            const json = eval(data.data);
            for (let i = 0; i < json.length; i++) {
                $('#select2').append(
                    "<option value='" + json[i]["KEY"] + "'>" +
                    json[i]["TEXT"] +
                    "</option>");
            }
        }, function (xhr, type) { //【失败回调】
            console.log("error");
            progress1_s.fadeOut();
            next2_s.attr("class", "btn btn-danger btn-sm");
            next2_s.html("请重试");
            card2_s.fadeOut();
            warning_s.html(
                "<p style='color: red;'>账号/密码错误或服务器/网络问题," +
                "<br />若一直出现此问题请联系网站管理员。</p>");
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

    submit_s.on("click", function () {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/fzyz_net/",
            dataType: 'html',
            data: $('#form').serialize(),
        }).then(function (data) { //【成功回调】
            console.log("success");
            submit_s.attr("class", "btn btn-success btn-sm");
            submit_s.val("再次查询");
            progress2_s.fadeOut();
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
            card3_s.fadeIn();
        }, function () { //【失败回调】
            // function (xhr, type) { //【失败回调】
            console.log("error");
            progress2_s.fadeOut();
            submit_s.attr("class", "btn btn-danger btn-sm");
            submit_s.attr("value", "请重试");
            $("#warning2").append("<br /><p style='color: red;'>服务器/网络问题，<br />若一直出现此问题请联系网站管理员。</p>");
        });
        progress2_s.fadeIn();
        setTimeout(timeout1, 1500)
        setTimeout(timeout2, 4000)
        setTimeout(timeout3, 6000)
        setTimeout(timeout4, 10000)

        function timeout1() {
            progress2_inside_s.attr("style", "width: 65%");
            progress2_inside_s.html("很多浏览器的进度条都是假的");
        }

        function timeout2() {
            progress2_inside_s.attr("style", "width: 25%");
            progress2_inside_s.html("比如这样");
        }

        function timeout3() {
            progress2_inside_s.attr("style", "width: 85%");
            progress2_inside_s.html("只有少数浏览器是按照步骤显示进度的");
        }

        function timeout4() {
            progress2_inside_s.attr("style", "width: 100%");
            progress2_inside_s.html("还没好吗？？？");
        }
    });
});
