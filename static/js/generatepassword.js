$(document).ready(function(){


$('#save_account').click(function(){

	var password = $('.password').text();
	var account_id = $('meta[name="account_id"]').attr('content')
	var csrftoken = $('meta[name="token"]').attr('content')

	var data = {'password':password,'account_id':account_id,'csrfmiddlewaretoken':csrftoken}
	

	console.log('password', password)
	console.log('csrftoken', csrftoken)


	$.ajax({
    url: "/account/generate-password/"+account_id,
    method: "POST",
    datatype: "json",
    data:data,
    headers: 
    {
        'X-CSRF-TOKEN': $('meta[name="token"]').attr('content')
    },
    success: function(url) {
    	window.location=url
    }
    
});


});

$('#generate_password').click(function(){

	window.location.reload();
})
	

});