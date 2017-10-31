#!/bin/bash
# usage:
# srun getslurminfo.sh jobid datadirpath
# capture env vars on each node in job, as propagated via srun.
#
#
# set sefdebug to nonempty string to suppress rm by the clean call.
sefdebug=
jobid=$1
edir=$2/slurm-pdsh-envs
mkdir -p $edir
if ! test -d $edir; then
	echo $0: unable to create directory $edir
	exit 1
fi
slurmenvfile=$edir/`hostname`
(set -o posix; set) |grep -E -v '(BASH|UID|PID|SHELL)' > $slurmenvfile
(set -o posix; set) | grep -i -E '(ldms|slurm|zap)' \
	| sed -e 's/=.*//g' \
		-e 's/^/export /' \
	 >> $slurmenvfile
