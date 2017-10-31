#!/usr/bin/python
# This script finds the .bt-io files in a directory and looks for their corresponding
# darshan log. When found, the darshan file is parsed and the output is put into the 
# directory with the bt-io files
#
import os
import datetime
import shutil
import sys
import re

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

dir_list = [d for d in os.listdir('.') if os.path.isdir(d)]

for f in dir_list:
  inner_dirs = [d for d in listdir_fullpath(f) if 'oss' in d and os.path.isdir(d)]

  for input_dir in inner_dirs:

    # Get sorted list of btio results
    file_list = [d for d in listdir_fullpath(input_dir) if '.bt-io' in d]
    file_list = sorted(file_list, key=os.path.getctime)
    
    # Get sorted list of darshan files
    openss_list = [d for d in listdir_fullpath(input_dir) if d.endswith('.openss')]
    openss_list = sorted(openss_list, key=os.path.getctime)

    if len(openss_list) != len(file_list):
      print openss_list
      print file_list
      print "Error in length of lists"
      exit(1)
    
    for i,f in enumerate(file_list):
      basename = os.path.basename(f)
      stripped_name = basename.split('.bt-io')[0]
      
      os.system('darshan-parser ' + darshan_list[i] + '>' + input_dir + '/' + \
                stripped_name + '.darshan_parsed')
