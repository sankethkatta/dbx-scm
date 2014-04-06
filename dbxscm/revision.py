"""
Revision Manager for dbx
"""

import dropbox
import os
from base import BaseDropbox

class Revision(BaseDropbox):

  def snapshot_revisions(self, path):
    files = {}
    def recurse(path):
      folder_metadata = self.client.metadata(path)
      for item in folder_metadata['contents']:
        if item['icon'] == 'folder':
          recurse(item['path'])
        else:
          files[item['path']] = item['rev']
    recurse(path)
    print files

  def checkout_revisions(self, files):
    pass

