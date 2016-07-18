var add = (function(){
	$("title_error_message").hide();
	var error_title=false;

	$("#form_title").focusout(function(){
		check_title();
	});

	$("#felul1").focusout(function(){
		check_title();
	});

function check_title()
{
	var title_length=$("#form_title").val().length;
	if(title_length<5 || title_length>50){
		$("#title_error_message").html("Should between 5-50 characters.");
		$("#title_error_message").show();
		error_title=true;
	}
	else {
		$("#title_error_message").hide();
	}
	}
});
add();








// var test = (function(){
// 	$input = $('#form_title');

// 	$input.focusout(function(){
// 		if($(this).val().length < 5 || $(this).val().length >=30 ) {
// 			$('.necessary').html("Campul trebuie sa contina intre 5 - 30 caractere.");
// 		//	alert("asd");
// 		}
// 		else
// 		{
// 			$('.necessary').html("");

// 		}
// 	//	console.log($(this).val().length);
// 	});
// });

// test();