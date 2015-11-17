#!/usr/bin/python

import socket

host = ''
port = 18000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
conn,addr = s.accept()

print 'Got connection from:',addr

while 1:
    data = conn.recv(4096)
    if not data:break
    conn.sendall(data)

conn.close()

