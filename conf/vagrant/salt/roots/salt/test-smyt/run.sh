#!/bin/bash

set -e
LOGFILE={{ log_file }}
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS={{ workers }}
# user/group to run as
USER={{ user }}
GROUP={{ group }}
PORT={{ port }}
cd {{ path }}
test -d $LOGDIR || mkdir -p $LOGDIR
exec {{ env_path }}/bin/gunicorn -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE \
  --bind 127.0.0.1:$PORT {{ wsgi_app }}