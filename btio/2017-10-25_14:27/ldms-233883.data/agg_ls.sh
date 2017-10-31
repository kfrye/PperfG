#! /usr/bin/bash
# job was 233883
export PATH=/usr/projects/workflow_perf/ovis/install/sbin:/usr/projects/workflow_perf/ovis/install/bin:/usr/projects/hpcsoft/toss3/woodchuck/openmpi/2.1.2-gcc-4.8.5/bin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/usr/bin:/opt/dell/srvadmin/bin:/usr/local/sbin:/usr/sbin:/usr/projects/workflow_perf/PerfTrack/build/bin:/usr/projects/workflow_perf/postgres/bin:/usr/projects/workflow_perf/PerfTrack/build/bin:/usr/projects/workflow_perf/postgres/bin:/usr/projects/workflow_perf/PerfTrack/build/bin
export LD_LIBRARY_PATH=/usr/projects/workflow_perf/ovis/install/lib:/usr/projects/workflow_perf/ovis/install/lib:/usr/projects/workflow_perf/ovis/install/lib/ovis-ldms:/usr/projects/workflow_perf/ovis/install/lib/ovis-lib:/usr/projects/hpcsoft/toss3/woodchuck/openmpi/2.1.2-gcc-4.8.5/lib
set -x
ldms_ls -h wc112.localdomain -p 60412 -x sock -m 8M -a /users/kfrye/.ldmsauth.conf $*
