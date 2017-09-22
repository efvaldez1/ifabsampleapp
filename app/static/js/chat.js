 $(function() {
$("#send").click(function(){
   console.log('hi');
   message= $('#message').val();
   var yourmessage=$('<p>'+message+'</p>');
   $("#chatlogs").append(yourmessage);   
   $.get(
	"http://localhost:8080/get/"+message,
	function(data) {
		botresponse='<b>'+data+'</b>';
	   $("#chatlogs").append(botresponse);
	}
);
});
});