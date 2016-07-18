// $(document).ready(function(){
//     $('.cart__default').click(function()
//     {
//         $('.panel').slideToggle('slow');});
//     });

// $(document).ready(function(){
//     $('.cart').click(function(){
//     	debugger;
//        $(this).find('.panel').slideToggle('slow');

//     });


$(document).ready(function(){

	function togglePanel() {
		// debugger;
		$(this).next('.panel').slideToggle('slow');
	}

	$('.cart').click(togglePanel);
});