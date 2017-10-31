#!/usr/bin/python
import sys
sys.path.append('/usr/projects/workflow_perf/oss_install_dirs/openss/lib64/openspeedshop')
import openss
import os
import datetime
import getpass

def extract_oss(filename):
  try:
    oss_file = openss.FileList(filename)
    exp = openss.expRestore(oss_file)
    # Make sure the experiment has pcsamp and get data
    exp_type = openss.list(openss.ModifierList('types'))
    exp_data = ''
    if 'pcsamp' in exp_type:
      exp_data = openss.expData(exp)
    else:
      print 'pcsamp experiment not detected'
      exit(1)
    openss.exit()
  except openss.error:
    openss.exit()
    exit(1)
  
  # Print results
  timestamp = os.path.getmtime(filename)
  date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
  uid = os.stat(filename).st_uid
  username = getpass.getuser()
  jobid = os.environ['SLURM_JOBID']
  host = os.environ['HOSTNAME']
  taskid = os.environ['SLURM_TASK_PID']
  jobname = os.environ['SLURM_JOB_NAME']
  #
  ret = ''
  for line in exp_data:
    ret += str(date) + ' ' + \
           str(jobid) + ' ' + \
           jobname + ' ' + \
           taskid + ' ' + \
           username + ' ' + \
           host + ' ' + \
           line[2].replace(' ', '_') + ' '  + \
           str(line[0]) + ' ' + \
           str(line[1]) + '\n' 
  return ret
