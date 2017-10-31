#!/usr/bin/python
# This script performs ptdf_entry.py on all ptdf files assuming the 
# following directory structure: run/dir/inner_dir/file.ptdf where
# this script is in the 'run' directory

import os

PATH = os.getcwd() + '/'
file_list = [d for d in os.listdir('.') if os.path.isdir(d)]

for f in file_list:
    inner_files = [d for d in os.listdir(f) if os.path.isdir(f + '/' + d) \
                  and d != 'machines']
    for subdir in inner_files:
        indiv_files = [fi for fi in os.listdir(f + '/' + subdir) if fi.endswith('.ptdf')]
        for indiv in indiv_files:
            cmd = 'ptdf_entry.py ' + f + '/' + subdir + '/' + indiv + \
                 ' -D perftrack -H localhost -U kfrye -w pw -j 1'
            print cmd
            os.system(cmd)
