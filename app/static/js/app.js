var app = angular.module('SetScouterApp', ['ngRoute']);

app.config(function ($routeProvider){
    $routeProvider
	.when('/',{
	    controller: 'MainController',
	    templateUrl: 'views/main.html'
	})
	.when('/login', {
	    controller: 'LoginController',
	    templateUrl: 'views/login.html'
	})
	.otherwise({
	    redirectTo:'/'
	});
});

app.run(['$rootScope','$location','Auth',function($rootScope,
						  $location,
						  Auth){
    $rootScope.$on('$routeChangeStart',function(event, next, current){
	if  (!Auth.isLoggedIn()) {
	    $location.path('/login');   
	}
    });
}]);
