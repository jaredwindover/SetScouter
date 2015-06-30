app.controller('LoginController',
	       ['$scope', 'Session', 'Auth', 'User',
		function($scope, Session, Auth, User){
		    $scope.login = function(){
			console.log("Trying to login");
			Session.login($scope.user.email, $scope.user.password)
			    .success(function(result){
				if (result.status === "success") {
				    console.log("Logged in successfully");
				    $scope.user = result.data.User;
				    $scope.authToken = result.data.Token;
				    Auth.setUser($scope.user);
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
					$scope.user = result.data.User;
					$scope.authToken = result.data.Token;
					Auth.setUser($scope.user);
				    }
				})
			}
		    };
		}]);
