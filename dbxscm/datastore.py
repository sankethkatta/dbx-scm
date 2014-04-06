"""
Dropbox datastore API interaction
"""

import json
from base import BaseDropbox
from dropbox import rest
from os import path
from dropbox.client import DropboxClient, DropboxOAuth2FlowNoRedirect
from dropbox.datastore import DatastoreError, DatastoreManager, Date, Bytes
from ConfigParser import ConfigParser

class Datastore(BaseDropbox):

  def add_commit(self, repo, message, files):
    record = self.commit_table.insert(repo=repo, message=message, files=json.dumps(files))
    self.datastore.commit()
    return record.get_id()

  def get_commit(self, commit):
    record = self.commit_table.get(commit)
    return {'id': record.get_id(), 'files': json.loads(record.get('files'))}

  def delete_datastore(self):
    self.manager.delete_datastore('default')

if __name__ == '__main__':
  ds = Datastore()
  #id = ds.add_commit({"fname": 1234})
  #print "commit %s" % id
  #ds.delete_datastore()
  #print ds.get_commit('1GCzBelUQXG5P6fIkUwS2Q')
