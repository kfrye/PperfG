#!/usr/bin/python
import json
import os
import sys 
import subprocess
import StringIO

diagram = {}

diagram['layers'] = ['Storage', 'Network', 'Memory', 'Job Run Layer']
diagram['tasks'] = ['Application']

if len(sys.argv) != 3:
  print "Syntax is: diagram_output.py <darshan file> <ossmem file>"
  exit(1)

output, err = subprocess.Popen(['./parse_darshan_diagram.py', sys.argv[1], 'A'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
data = json.loads(output)
diagram['dataset'] = data['dataset']
letter = ord(data['dataset'][0].keys()[-1]) + 1

output, err = subprocess.Popen(['./parse_ossmem_diagram.py', sys.argv[2], chr(letter)], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
diagram['dataset'].append(json.loads(output))

print diagram
