#!/usr/bin/python

import json
import os
import sys 

diagram = {}

diagram['layers'] = ['Storage', 'Network', 'Memory', 'Job Run Layer']
diagram['tasks'] = ['Application']
letter = ord('A')
diagram['dataset'] = {}
try:
   with open(sys.argv[1]) as f:
      line = f.readline()
      while line:
         if 'The restored experiment identifier is' in line:
            line = f.readline()
            line = f.readline()
            line = f.readline()
            line = f.readline()
            line = f.readline()
            line = f.readline()
            while line:
               parts = line.split()
               if len(parts) < 9:
                  line = f.readline()
                  continue
               value = parts[6]
               diagram['dataset'][chr(letter)] = {
                  'size': value,
                  'type': 'binary file',
                  'createdLayer': 'Memory',
                  'usedLayer': ['Application'],
                  'accessMethod': ['Memory']
               }
               letter += 1
               line = f.readline()
         line = f.readline()
except IOError as err:
   exc_type, exc_value, exc_traceback = sys.exc_info()
   print err
   traceback.print_tb(exc_traceback)

print json.dumps(diagram) 
