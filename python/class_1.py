# coding:utf-8
class Monk:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speech(self):
        print('你好')

    def net(self):
        print('世界')
# 实例化
ye = Monk('zuilive',23)

# 调用方法
ye.speech()

ye.net()

# 指定超类


class Fiter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Fiter): # SPAMFilter是Filter的子类
	def init(self): # 重写Filter超类中的init方法
		self.blocked = ['SPAM']

s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'Spam', 'sPam', 'SPAM', 'egg', 'bacon']))


# 构造方法
class FooBar:
    def __init__(self, value=42):
        self.somevar = value

f = FooBar()
print(f.somevar)
