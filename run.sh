#!/bin/bash

set -e
LOGFILE=/test_smyt/log/log.txt
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=vagrant
GROUP=vagrant
PORT=8000
cd /test_smyt
test -d $LOGDIR || mkdir -p $LOGDIR
exec /home/vagrant/env/test-smyt-env/bin/gunicorn -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE \
  --bind 127.0.0.1:$PORT test_smyt_project.wsgi:application