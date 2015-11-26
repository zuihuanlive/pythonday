#!/usr/bin/python
import os
import re
import time

cmd1='export LD_LIBRARY_PATH=/apps/ysjs/center/lib:/apps/billing/lib:/usr/java/lib:/apps/oracle/product/11.2.0/db_1/lib:/apps/billing/release/lib:'
cmd2='export PATH=/apps/billing/jboss/bin:/apps/ysjs/center/bin:/apps/ysjs/center/scripts:/apps/billing/bin:/apps/billing/scripts/java_scripts:/apps/billing/scripts/tools:/apps/billing/scripts/nrm:/apps/billing/scripts/srm:/usr/java/bin:/apps/oracle/product/11.2.0/db_1/bin:/apps/billing/release/bin:/usr/lib64/qt-3.3/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/apps/billing/bin'
cmd3='export OB_REL=/apps/billing'
mdb_alert='/usr/local/zabbix/script/rasmdb_alert.log'
mdb_sql="select * from CRasMdbParam;"

cmd_line=cmd3+";"+cmd1+";"+cmd2+"; echo '"+mdb_sql+"' |/apps/billing/bin/mdb_client 192.168.130.16 25200 > "+mdb_alert

os.popen(cmd_line).read()


file_mdb_alert=open(mdb_alert,'r')
# content_mdb=file_mdb_alert.readlines()
# file_mdb_alert.close()

r = re.compile(r'\W+')

for i in file_mdb_alert:
    # content_mdb = file_mdb_alert.readline()
    t = r.split(i)
    if t[1] == 'CurrentDate':
        result = t[2]


today = time.strftime("%Y%m%d")

if today == result:
    print '0'
else:
    print '1'

