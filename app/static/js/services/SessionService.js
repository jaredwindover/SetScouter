app.factory('Session', ['$http', function($http){
    var urlBase = '/api/session';
    var Session = {};
    Session.login = function(email, password){
	return $http.post(urlBase,
			  $.param({'email':email,'password':password}),
			  {'headers':{'Content-Type': 'application/x-www-form-urlencoded'}});
    };
    Session.logout = function(id, tok){
	return $http.delete(urlBase + '/' + id, {
	    'headers':{
		'Authorization' : tok
	    }
	});
    };
    return Session;
}]);
