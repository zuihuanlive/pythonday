#!/usr/bin/python

import socket

host = '127.0.0.1'
port = 18000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.send('Hello world!')
received_data = s.recv(1024)

s.close()
print 'Received from server:',received_data
