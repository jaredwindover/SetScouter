app.factory('User', ['$http', function($http){
    var urlBase = '/api/user';
    var User = {};
    User.getList = function(id, tok){
	return $http.get(urlBase + '?userid=' + id,
			 {'headers' : {
			     'Authorization' : tok
			 }});
    };
    User.register = function(firstname, lastname, email, password){
	return $http.post(urlBase,
			  $.param({
			      'firstname' : firstname,
			      'lastname' : lastname,
			      'email' : email,
			      'password' : password
			  }),
			  {'headers':{'Content-Type': 'application/x-www-form-urlencoded'}});
    };
    return User;
}]);
