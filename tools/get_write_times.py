#!/usr/bin/python

try:
    with open('darshan_parsed.txt') as f:
        line = f.readline()
        total_write_time = 0
        write_count = 0
        stdio_writes = 0
        while line:
            if line.startswith('# '):
                line = f.readline()
                continue
            elif line.startswith('#<'):
                names = line.split('\t')
                names = [s.replace('<', '').replace('>', '') for s in names]
                names = [s.replace('#', '') for s in names]
            else:
                parts = line.split('\t')
                if len(parts) < 2:
                    line = f.readline()
                    continue
                value_index = names.index('value')
                counter_index = names.index('counter')
                if parts[counter_index] == 'POSIX_F_WRITE_TIME':
                    total_write_time += float(parts[value_index])
                if parts[counter_index] == 'POSIX_WRITES':
                    write_count += int(parts[value_index])
                if parts[counter_index] == 'STDIO_WRITES':
                    stdio_writes += int(parts[value_index])
            line = f.readline()
        print "Total write time: ", total_write_time
        print "Total write count: ", write_count
        print "Total stdio write count: ", stdio_writes 
except IOError as err:
    print err
    traceback.print_exc()
