app.directive('showMessage', function(){
    return {
	restrict:'E',
	scope:{
	    message:'='
	},
	templateUrl: 'js/directives/showMessage.html'
    };
});
