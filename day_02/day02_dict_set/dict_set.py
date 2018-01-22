#!/usr/bin/python3
# -*- coding:utf-8 -*-

# the test of a dictionary

d={'马云':'100亿','雷军':'80亿','马化腾':'120亿','比尔盖茨':'300亿'}
print('马化腾每年赚：',d['马化腾'])

d['马云']='150亿'
print('马云收入变为：',d['马云'])

if '李嘉诚'in d:
    print('李嘉诚收入是：',d['李嘉诚'])
else:
    print("李嘉诚没有列入字典中！ 请加入李嘉诚的收入：")
    key='李嘉诚'
    value=input()
    if not '亿' in value:
        value=value+'亿'
    #d[key]=value
    d.setdefault(key,value)
    print(d)


if d.get('比尔盖茨',True):
    print("比尔盖茨的收入为：",d["比尔盖茨"])
else:
    print('比尔盖茨没有被列入字典中！')


# the test of set
list1=[1,2,3]
list2=[1,3,4,5,2]
s=set(list1)
s2=set(list2)
print('s=:',s)
s.add(4)
print('s.add(4):',s)
s.add(3)
print('s.add(3):',s)
s.remove(3)
print('s.remove(3):',s)
print('s&s2:',s&s2)
print('s|s2:',s|s2)

t=(1,2,3)
s3=set(t)
print(s3)

t2=(1,[2,3],3)
#s4=set(t2) #here is error because [2,3]is changeable
#print(s4)