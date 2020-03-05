$(document).ready(function () {

    $("#next1").click(function () {
        document.getElementById("panel1").style.display = "inline";
    });

    $("#next2").click(function () {
        document.getElementById("panel2").style.display = "inline";
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
                json = eval(data.data);
                for (var i = 0; i < json.length; i++) {
                    $('#select2').append("<option value='" + json[i].KEY + "'>" + json[i].TEXT + "</option>");
                };
            },
            error: function (xhr, type) { //【失败回调】
                console.log("error");
                $("#panel1_inside").attr("class","panel panel-danger");
                document.getElementById("panel2").style.display = "none";
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
                $("#table1 tr").eq(-1).remove();
            },
            error: function (xhr, type) { //【失败回调】
                console.log("error");
                $("#panel2_inside").attr("class","panel panel-danger");
            }
        });
    });
});
