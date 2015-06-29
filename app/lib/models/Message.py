import webapp2

from google.appengine.ext import ndb

class Message(ndb.Model):
    content = ndb.StringProperty(required=True)
    from_firstname = ndb.StringProperty(required=True)
    from_lastname = ndb.StringProperty(required=True)
    to_userid = ndb.StringProperty(required=True)
