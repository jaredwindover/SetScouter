app.directive('userDisplay', function() {
    return {
	restrict: 'E',
	scope: {
	    fromid: '=',
	    token: '=',
	    list:'='
	},
	templateUrl: 'js/directives/userDisplay.html'
    };
});
