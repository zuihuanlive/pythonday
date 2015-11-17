#coding:utf-8
import cx_Oracle

db = cx_Oracle.connect('system/abc123@10.10.30.20:1521/ystdb2')

cr = db.cursor()

sql = 'select * from oip.oip_send_2_err t  where t.oip_send_id=190000074833 order by t.create_date desc'

cr.execute(sql)

#row = cr.fetchall()
for i in cr:
    print i,'\n'
cr.close()
db.close()
#row2=list(row)
flag1=0
'''
for i in row:
    flag2=0
    for t in i:
        if t==190000074833:
            row2[flag1][flag2]=11111
        flag2=flag2+1
    flag1=flag1+1
'''
#print row
#print row[0][8]
