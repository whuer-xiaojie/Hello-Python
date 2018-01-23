#!/usr/bin/python3
# -*- coding:utf-8 -*-

# the list
list1=['a','b',1,2,3]
list2=['c','b','a',1,4,5]
print("cmp(list1,list2)=",list1>list2)
print("list1=list2",list1==list2)
print("list1<list2=",list1<list2)

list3=[1,2,3,4,5,6,7]
print("list3's length is:",len(list3))
print("list3's max number is:",max(list3))
print("list3's min number is :",min(list3))

list4=[1,2,3,2,3,4,5,2,1,4]
print("the firsr 3 index is:",list4.index(3))
print("the count of 2 is:",list4.count(2))

list4.reverse()
print("the reversed list4 is:",list4)

list4.sort()
print("the sorted list4 is:",list4)

#the tuple
tuple1=("a","b",1)
print(tuple1)
tuple0=()
tuple2=(1,)