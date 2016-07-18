$(document).ready(function(){

	function showmessage() {
	$('.button_message').html("An email confirmation has been sent.");
	}

	$('.button').click(showmessage);
});