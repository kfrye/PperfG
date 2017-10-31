#!/usr/bin/python
# This script grabs the latest darshan log file from the log directory, 
# copies it to the test directory, and then parses it
#
import os
import datetime
import shutil
import sys

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

now = datetime.datetime.now()
darshan_directory = '/usr/projects/darshan/logs/' + str(now.year) + '/' + \
                    str(now.month) + '/' + str(now.day)
file_list = listdir_fullpath(darshan_directory)
if len(sys.argv) > 1:
    c = int(sys.argv[1])
else:
    c = 1
file_list = sorted(file_list,key=os.path.getctime)[-c:]
for f in file_list:
    basename = os.path.basename(f)
    newdir = os.environ['RUN_DIR']
    shutil.copy(f, newdir)
    os.system('darshan-parser ' + basename + '>' + basename + '.parsed')
