#!/bin/sh

/usr/sbin/sshd -D -E /var/log/secure &
python3 ./socket-client.py