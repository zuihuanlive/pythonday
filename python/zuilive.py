#coding:utf-8
import socket
HOST = '10.10.30.29'
PORT = 43001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
data='''
{"Request":{"BusiParams":{"SubjectId":"","SubjectLevel":"3","BillingCycle":"201504","ServiceNum":"17083017777"},"BusiCode":"OI_GetUserBillDetail"},"PubInfo":{"InterfaceId":"","TransactionId":"WEB20150515172159033085","InterfaceType":"04","OpId":"40051860","CountyCode":"4001","OrgId":"40051860","ClientIP":"","TransactionTime":"20150515172159","RegionCode":"400"}}
'''
s.send(data)
data = s.recv(1024)
s.close()

