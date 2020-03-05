$(document).ready(function () {

    $("#next1").click(function () {
        document.getElementById("panel2").style.display = "inline";
    });

    $("#submit").click(function () {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/jk/",
            dataType: 'html',
            data: $('#form').serialize(),
            success: function (data) { //【成功回调】
                console.log("success");
                $("#table1").append(data);
            },
            error: function (xhr, type) { //【失败回调】
                console.log("error");
                $("#panel2_inside").attr("class","panel panel-danger");
            }
        });
    });
});