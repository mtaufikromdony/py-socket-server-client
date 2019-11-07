#!/usr/bin/env python3

import socket
import tailer

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def socket_client():
    server_ip = '192.168.100.100'
    local_hostname = socket.gethostname()

    server_addr = (server_ip, 54321)
    sock.connect(server_addr)

    print ("(%s) connected to %s" % (local_hostname, server_ip))
    initial = 0
    for line in tailer.follow(open("/var/log/secure")):
        if 'ssh2' in line:
            login_attempt = initial + 1
            message = (str(local_hostname) + " had " + str(login_attempt) + " attempt").encode("utf-8")
            sock.send(message)
            initial = login_attempt
    sock.close()

if __name__ == '__main__':
    socket_client()