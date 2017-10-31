#!/usr/bin/python
# This script grabs LDMS data from the meminfo module.
#
# For this script to work, you need to set the environmental variables
# 'job_start_time' and 'job_stop_time'. 'ldmsdatadir' should be set with the location
# of the LDMS directory. The actual memdata file is assumed to be found in
# $ldmsdatadir/store/store_csv. Update below if necessary.
# 
# It is assumed that slurm has also set
# SLURM_JOBID, SLURM_TASK_PID, SLURM_JOB_NAME. HOSTNAME is also used.
# output for this script goes to the file defined in 'out_file' local variable below.
#
# The outfile will contain data for each time interval (default 1 sec) while the program
# is running. LDMS data before and after the program time interval is discarded. The
# following data is included: 
# date, time, jobid, jobname, taskid, username, host, MemTotal, MemFree, MemAvailable
import getpass
import os
import datetime

out_file = os.environ['SCRIPTS_DIR'] + '/ldms-meminfo.log'

start_time = float(os.environ['job_start_time'])
stop_time = float(os.environ['job_stop_time'])
date = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S'
)

username = getpass.getuser()
jobid = os.environ['SLURM_JOBID']
host = os.environ['HOSTNAME']
taskid = os.environ['SLURM_TASK_PID']
jobname = os.environ['SLURM_JOB_NAME']

write_data = ''

with open(os.environ['ldmsdatadir'] + '/store/store_csv/meminfo', 'r') as f:
  line = f.readline()
  line = f.readline()
  print 'start_time: ' + str(start_time) + ', stop_time: ' + str(stop_time)
  while(line):
    parts = line.split(',')
    if float(parts[0]) > start_time and float(parts[0]) < stop_time:
      write_data += str(date) + ' ' + \
           str(jobid) + ' ' + \
           jobname + ' ' + \
           taskid + ' ' + \
           username + ' ' + \
           host + ' ' + \
           parts[5] + ' ' + \
           parts[6] + ' ' + \
           parts[7] + '\n'
    line = f.readline() 

print 'writing data to file ' + out_file
with open(out_file, 'a') as f:
  f.write(write_data)
