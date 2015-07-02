app.directive('messageUser', ['Message', function(Message){
    return {
	restrict:'E',
	scope:{
	    fromid: '=',
	    token: '=',
	    user: '='
	},
	templateUrl: 'js/directives/messageUser.html',
	link: function(scope,element,attrs){
	    scope.sendMessage = function(){
		Message.send(
		    scope.fromid,
		    scope.token,
		    scope.user.id,
		    scope.content
		).success(function(data){
		    if (data.status==="success"){
			scope.sent=true;
			scope.content="";
			setTimeout(function(){
			    scope.sent=false;
			},2000);
		    }
		});
	    };
	}
    };
}])
