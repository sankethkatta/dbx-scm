"""
Dropbox datastore API interaction
"""

from dropbox import rest
from os import path
from dropbox.client import DropboxClient, DropboxOAuth2FlowNoRedirect
from dropbox.datastore import DatastoreError, DatastoreManager, Date, Bytes
from ConfigParser import ConfigParser

class Datastore(object):

  def __init__(self):
    APP_KEY = 'oqnyxvnwr67ebpc'
    APP_SECRET = 'd5qiseh1lnfzayh'
    CONFIG_PATH = '~/.dbxrc'

    self.parser = ConfigParser()
    self.path = path.expanduser(CONFIG_PATH)
    if path.exists(self.path):
      self.parser.read(self.path)

    if 'datastore' not in self.parser.sections():
      self.parser.add_section('datastore')

    if self.parser.has_option('datastore', 'token'):
      access_token = self.parser.get('datastore', 'token')

    else:

      auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
      authorize_url = auth_flow.start()
      print "1. Go to: " + authorize_url
      print "2. Click \"Allow\" (you might have to log in first)."
      print "3. Copy the authorization code."
      auth_code = raw_input("Enter the authorization code here: ").strip()

      try:
        access_token, user_id = auth_flow.finish(auth_code)
        print 'Authenticated user: %s' % user_id
      except rest.ErrorResponse, e:
        print('Error: %s' % (e,))
        return

      self.parser.set('datastore', 'token', access_token)
      with open(self.path, 'w') as writer:
        self.parser.write(writer)

    self.client = DropboxClient(access_token)

if __name__ == '__main__':
  ds = Datastore()
