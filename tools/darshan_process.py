#!/usr/bin/python
import sys
import cStringIO
import subprocess
import re


def parse_line(line, darshan_dict, section):
  if section == 'header':
    n = re.search('#\s+uid:\s+(\S+)',line)
    if n:
      darshan_dict['uid'] = n.group(1) 
    n = re.search('#\s+jobid:\s+(\S+)',line)
    if n:
      darshan_dict['jobid'] = n.group(1)
    n = re.search('#\s+start_time:\s+(\S+)',line)
    if n:
      darshan_dict['start_time'] = n.group(1)
    n = re.search('#\s+end_time:\s+(\S+)',line)
    if n:
      darshan_dict['end_time'] = n.group(1)
    n = re.search('#\s+nprocs:\s+(\S+)',line)
    if n:
      darshan_dict['nprocs'] = n.group(1)

  elif section == 'POSIX':
    n = re.search('#\s+total_bytes:\s+(\S+)',line)
    if n:
      darshan_dict['total_bytes_POSIX'] = float(n.group(1)) 
    n = re.search('#\s+unique files: slowest_rank_io_time:\s+(\S+)',line)
    if n:
      darshan_dict['local_iotime_POSIX'] = float(n.group(1))
    n = re.search('#\s+shared files: time_by_cumul_io_only:\s+(\S+)',line)
    if n:
      darshan_dict['global_iotime_POSIX'] = float(n.group(1))
    n = re.search('#\s+agg_perf_by_cumul:\s+(\S+)',line)
    if n:
      darshan_dict['agg_perf_by_cumul_POSIX'] = float(n.group(1))

  elif section == 'STDIO':
    n = re.search('#\s+total_bytes:\s+(\S+)',line)
    if n:
      darshan_dict['total_bytes_STDIO'] = float(n.group(1)) 
    n = re.search('#\s+unique files: slowest_rank_io_time:\s+(\S+)',line)
    if n:
      darshan_dict['local_iotime_STDIO'] = float(n.group(1))
    n = re.search('#\s+shared files: time_by_cumul_io_only:\s+(\S+)',line)
    if n:
      darshan_dict['global_iotime_STDIO'] = float(n.group(1))
    n = re.search('#\s+agg_perf_by_cumul:\s+(\S+)',line)
    if n:
      darshan_dict['agg_perf_by_cumul_STDIO'] = float(n.group(1))

  return darshan_dict

def darshan_parse(data_list, outfile):
  darshan_dict = {}
  section = 'header'
  for line in data_list:
    if 'POSIX module data' in line:
      section = 'POSIX'
    elif 'STDIO module data' in line:
      section = 'STDIO'
    darshan_dict = parse_line(line, darshan_dict, section)
  with open(outfile, "a") as f:
    f.write(str(darshan_dict))

# --- main script starts here ---
if len(sys.argv) != 3:
  print 'Syntax is: darshan_process.py <file> <output file>'
  sys.exit(1)

file_name = sys.argv[1]
outfile = sys.argv[2]
if file_name.endswith('darshan_partial'):
  sys.exit(1)
output = cStringIO.StringIO()
command = ['darshan-parser', '--perf', '--file', '--file-list-detailed', file_name]

p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
output, err = p.communicate()
output_list = output.split('\n')

darshan_parse(output_list, outfile)


