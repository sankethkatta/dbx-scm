# dbx-scm

Dropbox based revision control system.

**WARNING: This code was written at a hackathon**

The code works as a proof of concept, but would need to be cleaned up for real use.

## Motivation

Git is hard to use, there are lots of commands and many concepts to grasp. 
Dropbox, however, is easy, you add files by dropping them into a folder, and delete them by 
removing them from the folder.

Git and tools services such as github are great for code and text files, but are pretty bad at other file types.
Dropbox, on the other hand, is great at handling powerpoints, videos, photoshop files, etc.

This is an attempt to bring together the best of Dropbox and Git to build an easier revision control system that 
works on more than just text files.

## How it works

Create your dbx repository:

```bash
$ cd myphotoproject
$ dbx init
```

Commit your dropbox state:

```bash
$ dbx commit "removed redeye on all the photos"
```

Revert back at a later time:

```bash
$ dbx log
removed redeye on all the photos  rJuiHQ5wRdmmO-b8G2VGvw
initial commit                    B1XZVKYRSaqEpM3AxfnBCg

$ dbx checkout rJuiHQ5wRdmmO-b8G2VGvw
```

## How it really works

Dropbox already provides revisions on files. However rarely are you working on just one file.
What dbx-scm saves the revision ids of all file in your  "repository" a Dropbox Datastore along with your commit message. 
When you need to revert, it uses the Dropbox Core API to restore files to a certain state.

