$(function () {
	const acc_switch1_s = $("#account_switch1");
	const acc_switch2_s = $("#account_switch2");
	const acc_switch3_s = $("#account_switch3");
	const acc_switch4_s = $("#account_switch4");
	const btn1_s = $("#button1");
	const btn1pro_s = $("#button1pro");
	const sub_s = $("#submit");
	const reg = $("#register");
	const term1_s = $("#term1");
	const term2_s = $("#term2");

	const card2_s = $("#card2");
	const input_form_s = $("#input_form");
	const user_code_form_s = $("#user_code_form");
	const fzyz_form_s = $("#fzyz_form");
	const fyexam_form_s = $("#fzyz_exam_form");
	const jk_form_s = $("#jk_form");
	const grades_s = $("#grades");
	
	const form_s = $("#form");

	var using_code = "0";
	var api_url = "http://127.0.0.1:8000/"; //于此修改API网址

	btn1_s.on("click", function () {
		if( $("#username").val() == "" || $("#passwd").val() == "" ) {
			$("#warn-input-error").modal("show");
			card2_s.fadeOut();
		} else {
			card2_s.fadeIn();
		}
	});

	btn1pro_s.on("click", function () { 
		if( $("#ident_code").val() == "" ) {
			console.log($("#ident_code").val());
			$("#warn-input-error").modal("show");
			card2_s.fadeOut();
		} else {
			console.log($("#ident_code").val());
			card2_s.fadeIn();
		}
	});

	reg.on("click", function () { 
		$.ajax({
			type: "get",
			url: api_url + "firebase/",
			dataType: 'html',
			data: form_s.serialize(),
		}).then(function (data) { //【成功回调】
			console.log("success");
			reg.attr('class','btn btn-success');
			reg.attr('value','注册成功');
			return;
		}, function (xhr, type) { //【失败回调】
			console.log("error");
			reg.attr('class','btn btn-danger');
			reg.attr('value','注册失败');
			return;
		});
	})

	acc_switch1_s.on("click", function () {
		btn1_s.fadeIn();
		btn1pro_s.fadeOut(0);
		input_form_s.fadeIn(0);
		user_code_form_s.fadeOut();
		acc_switch1_s.addClass("active");
		acc_switch2_s.removeClass("active");
	});

	acc_switch2_s.on("click", function () {
		btn1pro_s.fadeIn(0);
		btn1_s.fadeOut(0);
		input_form_s.fadeOut();
		user_code_form_s.fadeIn();
		acc_switch2_s.addClass("active");
		acc_switch1_s.removeClass("active");
		using_code = "1"
	});

	acc_switch3_s.on("click", function () {
		fzyz_form_s.fadeIn();
		jk_form_s.fadeOut();
		acc_switch3_s.addClass("active");
		acc_switch4_s.removeClass("active");
		sub_s.fadeOut();
	});

	acc_switch4_s.on("click", function () {
		fzyz_form_s.fadeOut();
		jk_form_s.fadeIn();
		acc_switch4_s.addClass("active");
		acc_switch3_s.removeClass("active");
		sub_s.fadeIn();
	});

	term1_s.on("click", function () {
		term1_s.addClass("active");
		term2_s.removeClass("active");
		$.ajax({
			type: "get",
			url: api_url,
			dataType: 'html',
			data: form_s.serialize() + "&using_code=" + using_code + "&para_KEY=1&exam_or_grades=1",
		}).then(function (data) { //【成功回调】
			console.log("success");
			$('#select2').empty();
			fyexam_form_s.fadeIn();
			const json = eval(data);
			for (let i = 0; i < json.length; i++) {
				$('#select2').append(
					"<option value='" + json[i]["KEY"] + "'>" +
					json[i]["TEXT"] +
					"</option>");
			};
			sub_s.fadeIn();
			return;
		}, function (xhr, type) { //【失败回调】
			console.log("error");
			fyexam_form_s.fadeOut();
			sub_s.fadeOut();
			$("#warn-net-error").modal("show");
			return;
		});
	});

	term2_s.on("click", function () {
		term2_s.addClass("active");
		term1_s.removeClass("active");

		$.ajax({
			type: "get",
			url: api_url,
			dataType: 'html',
			data: form_s.serialize() + "&using_code=" + using_code + "&para_KEY=2&exam_or_grades=1",
		}).then(function (data) { //【成功回调】
			console.log("success");
			$('#select2').empty();
			fyexam_form_s.fadeIn();
			const json = eval(data);
			for (let i = 0; i < json.length; i++) {
				$('#select2').append(
					"<option value='" + json[i]["KEY"] + "'>" +
					json[i]["TEXT"] +
					"</option>");
			};
			sub_s.fadeIn();
			return;
		}, function (xhr, type) { //【失败回调】
			console.log("error");
			fyexam_form_s.fadeOut();
			sub_s.fadeOut();
			$("#warn-net-error").modal("show");
			return;
		});
	});

	sub_s.on("click", function () {
		$.ajax({
			type: "get",
			url: api_url,
			dataType: 'html',
			data: form_s.serialize() + "&using_code=" + using_code + "&exam_or_grades=0",
		}).then(function (data) { //【成功回调】
			console.log("success");
			$("#table1").empty();
			$("#table1").append(data);
			grades_s.fadeIn();
			return;
		}, function (xhr, type) { //【失败回调】
			console.log("error");
			$("#warn-net-error").modal("show");
			return;
		});
	});

	btn1_s.on("click", function () {
		var date = new Date();
		year = date.getFullYear();
		document.getElementById('year1').innerHTML = (year - 1) + ' - ' + year;
		document.getElementById('year2').innerHTML = (year - 2) + ' - ' + (year - 1);
		document.getElementById('year3').innerHTML = (year - 3) + ' - ' + (year - 2);
		document.getElementById('year1').value = (year - 1) + '-' + year;
		document.getElementById('year2').value = (year - 2) + '-' + (year - 1);
		document.getElementById('year3').value = (year - 3) + '-' + (year - 2);
	});

});