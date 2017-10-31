#!/usr/bin/python
import os

dirlist = [d for d in os.listdir('.') if os.path.isdir(d)]
print dirlist
for d in dirlist:
  subdirlist = [s for s in os.listdir(d) if os.path.isdir(d + '/' + s) and s != 'machines']
  lists = []
  for s in subdirlist:
    overall = {'name': s}
    files = [f for f in os.listdir(d + '/' + s) if f.endswith('.ior')]
    write = []
    read = []
    for file in files:
      with open(d + '/' + s + '/' + file) as f:
        line = f.readline()
        while line:
          if 'Max Write' in line:
            parts = line.split()
            write.append(parts[2])
          if 'Max Read' in line:
            parts = line.split()
            read.append(parts[2])
          line = f.readline()
    overall['write'] = write
    overall['read'] = read
    lists.append(overall)
  with open(d + '/' + d + '.txt', 'w') as f:
    f.write('Writes\n------\n')
    for subdir in lists:
      f.write(subdir['name'].ljust(15))
      for data in subdir['write']:
        f.write(data + '\t')
      f.write('\n') 
         
    f.write('\nReads\n------\n')
    for subdir in lists:
      f.write(subdir['name'].ljust(15))
      for data in subdir['read']:
        f.write(data + '\t')
      f.write('\n') 
