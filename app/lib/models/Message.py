import webapp2

from google.appengine.ext import ndb

class Message(ndb.Model):
    content = ndb.StringProperty()
    from_firstname = ndb.StringProperty()
    from_lastname = ndb.StringProperty()
