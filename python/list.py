#!/usr/bin/python3
#coding: utf-8

#列表
shoplist = ['apple','mango','carrot','banana']

print 'I have ',len(shoplist),'items to purchase.'

print 'These  items are:',
for item in shoplist:
	print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now',shoplist

print 'I will  sort  my list now'
shoplist.sort()
print 'Sorted shopping list is ', shoplist

print 'The first  item  I will  buy  is ',shoplist[0]
olditem = shoplist[0]
del shoplist[0]

print 'I bought the ',olditem
print  'My  shopping list  is now',shoplist


#元组
zoo = ('wolf','elephant','penguin')
print 'Number of animals in the zoo is ',len(zoo)

new_zoo = ('monkey','dolphin',zoo)
print 'Number of animals in the new zoo is',len(new_zoo)
print 'All animals in new zoo are ',new_zoo
print 'Animals  brought from old zoo are ',new_zoo[2]
print 'Last animal brought from old zoo is',new_zoo[2][2]

