#!/usr/bin/env python

import sys
import os
import datetime

LOG_FILE = '/usr/projects/workflow_perf/kris/tools/LDMS_meminfo.log'

if len(sys.argv) != 2:
  print "Syntax is: 'extract_LDMS_meminfo.py <meminfo file>'"
  exit(1)

file_name = sys.argv[1]
if not file_name.startswith('meminfo'):
  print "Specified file is not a meminfo file"
  exit(1)

if 'HEADER' in file_name:
  print "Specified file cannot be a HEADER file"
  exit(1)

file_name_base = os.path.basename(file_name) 
file_name_dir = os.path.dirname(file_name)
if not file_name_dir:
  file_name_dir = '.'
parts = file_name_base.split('.')
file_name_header = file_name_dir + '/' + parts[0] + '.HEADER.' + parts[1]

headers = []

with open(file_name_header) as f:
  headers = f.readline().split(',')

with open(file_name) as f:
  f.seek(-2, os.SEEK_END)
  while f.read(1) != b"\n":
    f.seek(-2, os.SEEK_CUR)
  data = f.readline().split(',')

if len(headers) != len(data):
  print 'Header length is not the same as the data length'
  exit(1)

data_dict = {}

for i, header in enumerate(headers):
  data_dict[header] = data[i]

date = datetime.datetime.fromtimestamp(float(data_dict['#Time'])).strftime('%Y-%m-%d %H:%M:%S')
jobid = data_dict['job_id']
machine = data_dict['ProducerName']
mem_total = data_dict['MemTotal']
mem_free = data_dict['MemFree']
mem_avail = data_dict['MemAvailable']

with open(LOG_FILE, 'a') as f:
  f.write(date + ' ' + jobid + ' ' +  machine + ' ' +  mem_total + ' ' +  mem_free + ' ' +  
          mem_avail + '\n')
