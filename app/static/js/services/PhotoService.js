app.factory('Photo', ['$http', function($http){
    var urlBase = '/api/photo'
    var Photo = {}
    Photo.getUrl = function(id, tok){
	return $http.get(urlBase + '/' + id,
			 {'headers' : {
			     'Authorization' : tok
			 }});
    };
    return Photo;
}]);
