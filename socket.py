#!/usr/bin/env python2.7

import socket
import sys

if len(sys.argv) != 3:
    print("Usage:{0} <ip_address> <power_port> <port_operation>".format(sys.argv[0]))
    sys.exit(-1)
ip_address = sys.argv[1]
port = 502
power_port = sys.argv[2]
port_operation = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to creat socket.Error code: '+str(msg[0])+',Error message:'+msg[1])
    sys.exit();
print('Socket Created')
s.connect((ip_address, port))
if sys.argv[2] == '0' and sys.argv[3] == 'stop':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x00\x02\x00\x01\x02\x00\x00")
elif sys.argv[2] == '0' and sys.argv[3] == 'start':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x00\x02\x00\x01\x02\x00\x01")
elif sys.argv[2] == '0' and  sys.argv[3] == 'restart':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x00\x02\x00\x01\x02\x00\x02")
if sys.argv[2] == '1' and sys.argv[3] == 'stop':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x01\x02\x00\x01\x02\x00\x00")
elif sys.argv[2] == '1'and sys.argv[3] == 'start':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x00\x02\x00\x01\x02\x00\x01")
elif sys.argv[3] == '1' and sys.argv[3] == 'restart':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x00\x02\x00\x01\x02\x00\x02")
if sys.argv[2] == '2' and sys.argv[3] == 'stop':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x02\x02\x00\x01\x02\x00\x00")
elif sys.argv[2] == '2' and sys.argv[3] == 'start':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x02\x02\x00\x01\x02\x00\x01")
elif sys.argv[2] == '2' and sys.argv[3] == 'restart':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x02\x02\x00\x01\x02\x00\x02")
if sys.argv[2] == '3' and sys.argv[3] == 'stop':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x03\x02\x00\x01\x02\x00\x00")
elif sys.argv[2] == '3' and sys.argv[3] == 'start':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x03\x02\x00\x01\x02\x00\x01")
elif sys.argv[2] == '3' and sys.argv[3] == 'restart':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x03\x02\x00\x01\x02\x00\x02")
if sys.argv[2] == '4' and sys.argv[3] == 'stop':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x04\x02\x00\x01\x02\x00\x00")
elif sys.argv[2] == '4' and sys.argv[3] == 'start':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x04\x02\x00\x01\x02\x00\x01")
elif sys.argv[2] == '4' and sys.argv[3] == 'restart':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x04\x02\x00\x01\x02\x00\x02")
if sys.argv[2] == '5' and sys.argv[3] == 'stop':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x05\x02\x00\x01\x02\x00\x00")
elif sys.argv[2] == '5' and sys.argv[3] == 'start':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x05\x02\x00\x01\x02\x00\x01")
elif sys.argv[2] == '5' and sys.argv[3] == 'restart':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x05\x02\x00\x01\x02\x00\x02")
if sys.argv[2] == '6' and sys.argv[3] == 'stop':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x06\x02\x00\x01\x02\x00\x00")
elif sys.argv[2] == '6' and sys.argv[3] == 'start':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x06\x02\x00\x01\x02\x00\x01")
elif sys.argv[2] == '6' and sys.argv[3] == 'restart':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x06\x02\x00\x01\x02\x00\x02")
if sys.argv[2] == '7' and sys.argv[3] == 'stop':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x07\x02\x00\x01\x02\x00\x00")
elif sys.argv[2] == '7' and sys.argv[3] == 'start':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x07\x02\x00\x01\x02\x00\x01")
elif sys.argv[2] == '7' and sys.argv[3] == 'restart':
    s.sendall(b"\x00\x01\x00\x00\x00\x09\x00\x45\x07\x02\x00\x01\x02\x00\x02")
