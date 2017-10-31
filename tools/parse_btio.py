#!/usr/bin/python
import os

dirlist = [d for d in os.listdir('.') if os.path.isdir(d)]
print dirlist
for d in dirlist:
  subdirlist = [s for s in os.listdir(d) if os.path.isdir(d + '/' + s) and s != 'machines']
  lists = []
  for s in subdirlist:
    overall = {'name': s}
    files = [f for f in os.listdir(d + '/' + s) if f.endswith('.bt-io')]
    processes = []
    data_class = []
    timing = []
    for file in files:
      with open(d + '/' + s + '/' + file) as f:
        line = f.readline()
        while line:
          if 'I/O timing in seconds' in line:
            parts = line.split()
            timing.append(parts[-1])
          line = f.readline()
        
    overall['timing'] = timing
    lists.append(overall)
  with open(d + '/' + d + '.txt', 'w') as f:
    f.write('Timings (s) Dataset A\n---------\n')
    for subdir in lists:
      if 'A' in subdir['name']: 
        f.write(subdir['name'].ljust(20))
        for data in subdir['timing']:
          f.write(data + '\t')
        f.write('\n') 

    f.write('\nTimings (s) Dataset B\n---------\n')
    for subdir in lists:
      if 'B' in subdir['name']: 
        f.write(subdir['name'].ljust(20))
        for data in subdir['timing']:
          f.write(data + '\t')
        f.write('\n') 
