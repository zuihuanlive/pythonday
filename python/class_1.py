#coding:utf-8
class Monk:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speech(self):
        print '你好'

    def net(self):
        print '世界'
#实例化
ye = Monk('zuilive',23)

#调用方法
ye.speech()

ye.net()
