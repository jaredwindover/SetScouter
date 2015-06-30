app.factory('Message', ['$http', function($http){
    var urlBase = '/api/message'
    var Message = {}
    Message.getList = function(id, tok){
	return $http.get(urlBase + '/' + id,
			 {'headers' : {
			     'Authorization' : tok
			 }});
    };
    Message.send = function(from_id, tok, to_id, content){
	return $http.post(urlBase + '/' + to_id,
			  $.param({
			      'content' : content,
			      'from_id' : from_id
			  }),
			  {
			      'headers':{
				  'Authorization' : tok,
				  'Content-Type': 'application/x-www-form-urlencoded'
			      }
			  })
    };
    return Message;
}]);
