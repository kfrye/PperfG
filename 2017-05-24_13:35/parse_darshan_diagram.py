#!/usr/bin/python
import json
import os
import sys 

diagram = {}

letter = ord(sys.argv[2])
diagram['dataset'] = []

try:
   with open(sys.argv[1]) as f:
      files = {}
      line = f.readline()
      while line:
         if 'POSIX_BYTES_READ' in line:
            parts = line.split('\t')
 	    name = parts[5]
            name = os.path.basename(name)
            value = parts[4]
	    files[name] = {['POSIX_BYTES_READ']: value}

	 elif 'MPIIO_F_READ_TIME' in line:
            parts = line.split('\t')
 	    name = parts[5]
            name = os.path.basename(name)
            value = parts[4]
	    files[name] = {['MPIIO_F_READ_TIME']: value}

	 elif 'MPIIO_F_WRITE_TIME' in line:
            parts = line.split('\t')
 	    name = parts[5]
            name = os.path.basename(name)
            value = parts[4]
	    files[name] = {['MPIIO_F_WRITE_TIME']: value}

         line = f.readline()

      for d in files:
         diagram['dataset'].append({ 
            chr(letter): {
               'size': d['POSIX_BYTES_READ'],
               'type': 'binary file',
               'createdLayer': 'Memory',
               'usedLayer': ['Application'],
               'accessMethod': ['Storage'],
               'writeTime': d['MPIIO_F_WRITE_TIME'],
               'readTime': d['MPIIO_F_READ_TIME']
            }
         })
         letter += 1
      
except IOError as err:
   exc_type, exc_value, exc_traceback = sys.exc_info()
   print err
   traceback.print_tb(exc_traceback)

print json.dumps(diagram) 
