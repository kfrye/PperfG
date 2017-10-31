#!/usr/bin/python
import json
import os
import sys 
import subprocess
import StringIO

diagram = {}

diagram['layers'] = ['Storage', 'Network', 'Memory', 'Job Run Layer']
diagram['tasks'] = ['Application']
letter = ord('A')

if len(sys.argv) != 3:
  print "Syntax is: diagram_output.py <darshan file> <ossmem file>"
  exit(1)

darshan_out = StringIO.StringIO()
subprocess.call(['parse_darshan_diagram.py', sys.argv[1]], stdout=darshan_out)
darshan = output.getvalue() 
darshan_out.close()

print darshan
#    with open(sys.argv[1]) as f:
#       line = f.readline()
#       while line:
#          if 'POSIX_BYTES_READ' in line:
#             parts = line.split('\t')
#  	    name = parts[5]
#             name = os.path.basename(name)
#             value = parts[4]
# 
#             diagram['dataset'] = { 
#                chr(letter): {
#                   'size': value,
#                   'type': 'binary file',
#                   'createdLayer': 'Memory',
#                   'usedLayer': ['Application'],
#                   'accessMethod': ['Storage']
#                }
#             }
#             break
#          line = f.readline()
# except IOError as err:
#    exc_type, exc_value, exc_traceback = sys.exc_info()
#    print err
#    traceback.print_tb(exc_traceback)
# 
# print json.dumps(diagram) 
