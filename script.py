import os
import sys

repo = os.environ['GITHUB_REPOSITORY']
print('Repo is ' + repo)
[owner,name] = repo.split('/')
print('Name is ' + name)
filename = './' + name + '/WebApp.yml'
isFile = os.path.isfile(filename)
print('Config file ' + filename + ' exists? ' + str(isFile))
if isFile:
  sys.exit(0)
else:
  sys.exit(1)
