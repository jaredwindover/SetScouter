app.controller('MainController',
	       ['$scope',
		'$location',
		'Auth',
		'Session',
		'User',
		'Message',
		'Photo',
		function($scope,
			 $location,
			 Auth,
			 Session,
			 User,
			 Message,
			 Photo){
		    $scope.$watch(Auth.isLoggedIn, function(val, oldVal){
			if (! val && oldVal){
			    console.log('Logged Out');
			    $location.path('#/login');
			}
		    }), true;
		    $scope.PicturePage = function(){
			$scope.page = 'Picture';
		    }
		    $scope.UsersPage = function(){
			$scope.page = 'Users';
			$scope.refreshUsers();
		    }
		    $scope.MessagesPage = function(){
			$scope.page = 'Messages';
			$scope.refreshMessages();
		    }
		    $scope.user = Auth.getUser();
		    $scope.token = Auth.getToken();
		    $scope.logout = function() {
			Session.logout($scope.user.id, $scope.token)
			    .success(function(data){
				if (data.status==="success") {
				    Auth.setUser(null);
				    Auth.setToken(null);
				}
			    });
		    }
		    $scope.refreshUsers = function(){
			User.getList($scope.user.id,$scope.token)
			    .success(function(data){
				console.log("Refreshed Users");
				if (data.status==="success") {
				    $scope.userList = data.data;
				}
			    });
		    };
		    $scope.refreshMessages = function(){
			Message.getList($scope.user.id,$scope.token)
			    .success(function(data){
				console.log("Refreshed Messages");
				if (data.status==="success") {
				    $scope.messageList = data.data;
				}
			    });
		    };
		    Photo.getUrl($scope.user.id,$scope.token)
			.success(function(data){
			    if (data.status==="success"){
				console.log(data.data.url);
				$scope.pictureUrl = data.data.url;
				var myDropzone = new Dropzone(
				    "form#dzone",
				    {
					url: $scope.pictureUrl,
					maxFiles: 1,
					dictDefaultMessage:"Drop files here, or click to upload."
				    }
				);
				$("form#dzone").addClass('dropzone');
			    }
			});
		    $scope.PicturePage();
		}]);
