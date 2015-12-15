# coding:utf-8

# m1 = '201512'
# m2 = '201511'
# m3 = '201510'

f = open('ad.sql', 'r')
content = f.readlines()

for i in content:
    for t in range(10):
        if 1 < t < 10:
            r = str(i)+'0'+str(t)
        else:
            r = str(i)+str(t)
        print(r)
