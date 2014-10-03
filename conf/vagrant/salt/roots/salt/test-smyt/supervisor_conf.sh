#!/bin/bash

sudo touch /etc/supervisord.conf && sudo chmod 777 /etc/supervisord.conf \
&& echo_supervisord_conf > /etc/supervisord.conf \
&& sudo mkdir /etc/supervisor/ && sudo mkdir /etc/supervisor/conf.d/ \
&& sudo echo "[include]
    files = /etc/supervisor/conf.d/*" >> /etc/supervisord.conf