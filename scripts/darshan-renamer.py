#!/usr/bin/python
# This script parses darshan files and renames them according to the 
# list of runs in PTrunIndex.txt assuming the following directory 
# structure: run/dir/inner_dir/PTrunIndex.txt where this script is in
# the 'run' directory

import os

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

dirlist = [d for d in os.listdir('.') if os.path.isdir(d)]

for d in dirlist:
  subdirlist = [s for s in os.listdir(d) if os.path.isdir(d + '/' + s) and \
    'darshan' in s]
  for s in subdirlist:
    pathname = d + '/' + s
    runs = []
    with open(pathname + '/PTrunIndex.txt', 'r') as f:
      line = f.readline()
      while line:
        parts = line.split()
        runs.append(parts[0])
        line = f.readline()
    darshan_files = [df for df in os.listdir(pathname) \
                     if df.endswith('.darshan')]
    darshan_files.sort(key=lambda df: os.path.getmtime(os.path.join(pathname, df)))
    if len(darshan_files) != len(runs):
      print 'ERROR! Count of darshan files and runs does not match in ' + \
            pathname + '!'
      continue
    for i,df in enumerate(darshan_files):
      fname = pathname + '/' + df 
      cmd = 'darshan-parser --total ' + fname + '>' + pathname + '/' + \
            runs[i] + '.darshan_parsed'
      #print cmd
      os.system(cmd)
      print 'Parsed ' + fname 
