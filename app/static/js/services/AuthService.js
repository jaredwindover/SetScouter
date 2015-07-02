app.factory('Auth', function(){
    var user;
    var token
    return {
	setUser : function(aUser){
	    user = aUser;
	},
	setToken : function(aToken){
	    token = aToken;
	},
	getUser : function(){
	    return user;
	},
	getToken : function(){
	    return token;
	},
	isLoggedIn : function(){
	    return(user)? true: false;
	}
    }
});
