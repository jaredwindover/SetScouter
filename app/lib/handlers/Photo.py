import webapp2

from ..util.Authorization import authenticate
from ..util import Response as resp

from webapp2_extras.appengine.auth.models import User

from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore

class Handler(blobstore_handlers.BlobstoreUploadHandler):
    def get(self,userid):
        user = authenticate(self.request, int(userid))
        print user
        if not user:
            self.response.write(resp.fail_auth())
        else:
            self.response.write(resp.success({
                'url':blobstore.create_upload_url(self.request.path)
            }))

    def post(self,userid):
        print userid
        url = images.get_serving_url(self.get_uploads()[0].key())
        user = User.get_by_id(int(userid))
        print user
        user.img = url;
        user.put();
        self.response.write(resp.success())
