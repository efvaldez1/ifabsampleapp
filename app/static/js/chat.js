 $(function() {

 $("#chatheader").click(function(){
	$("#chatlogs").slideToggle();
});
$("#send").click(function(){
   message= $('#message').val();
   var div = document.createElement('div')
   div.setAttribute('class', 'chat self');
   div.innerHTML = '<p class='+ 'chat-message'+'>'+ message+'</p>';
   $("#chatlogs").append(div);   
	// $.get(
	// "http://localhost:8080/get/"+message,    //using localhost since app is not yet deployed
	// function(data) {
	// 	var botdiv = document.createElement('div')
	// 	botdiv.setAttribute('class', 'chat bot');
	// 	botdiv.innerHTML = '<p class='+ 'chat-message'+'>'+data+'</p>';
	//    $("#chatlogs").append(botdiv);
	//    console.log(botdiv);
	// }
 // );

});
});