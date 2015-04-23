$(document).ready(function() {
	$("#select_week1").click(function () {
		$("#week2").hide();
		$("#week3").hide();
		$("#week4").hide();
		$("#week1").show();
	});

	$("#select_week2").click(function () {
		$("#week3").hide();
		$("#week4").hide();
		$("#week1").hide();
		$("#week2").show();
	});

	$("#select_week3").click(function () {
		$("#week4").hide();
		$("#week1").hide();
		$("#week2").hide();
		$("#week3").show();
	});

	$("#select_week4").click(function () {
		$("#week1").hide();
		$("#week2").hide();
		$("#week3").hide();
		$("#week4").show();
	});
})