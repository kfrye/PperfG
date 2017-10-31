#!/usr/bin/python
# This script performs PTdFgen.py on all data files assuming the
# following directory structure: run/dir/inner_dir/PTrunIndex.txt
# where this script is in the 'run' directory

import os

file_list = [d for d in os.listdir('.') if os.path.isdir(d)] 

for f in file_list:
    machine_files = [d for d in os.listdir(f + '/machines') \
                     if d.endswith('.ptdf')]
    for machine in machine_files:
        cmd = 'ptdf_entry.py ' + f + '/machines/' + machine + \
              ' -D perftrack -U kfrye -w pw -H localhost' 
        print cmd
        os.system(cmd)

    inner_files = [d for d in os.listdir(f) if d != 'machines' and \
        os.path.isdir(f + '/' + d)]
    for inner in inner_files:
        cmd = 'PTdFgen.py --exec_data -d ' + f + '/' + inner +\
              ' -D perftrack -H localhost -U kfrye -w pw -v'
        print cmd
        os.system(cmd)
