app.controller('LoginController',
	       ['$scope', 'Session', 'Auth', 'User', '$location',
		function($scope, Session, Auth, User, $location){
		    $scope.login = function(){
			console.log("Trying to login");
			Session.login($scope.user.email, $scope.user.password)
			    .success(function(result){
				if (result.status === "success") {
				    console.log("Logged in successfully");
				    Auth.setUser(result.data.User);
				    Auth.setToken(result.data.Token);
				    $location.path('#/');
				}
			    })
		    };
		    
		    $scope.register = function(){
			console.log("Trying to register")
			if ($scope.user.passwordA === $scope.user.passwordB){
			    User.register($scope.user.firstname,
					  $scope.user.lastname,
					  $scope.user.email,
					  $scope.user.passwordA)
				.success(function(result){
				    if (result.status === "success") {
					console.log("Registered successfully");
					Auth.setUser(result.data.User);
					Auth.setToken(result.data.Token);
					$location.path('#/');
				    }
				})
			}
		    };
		}]);
