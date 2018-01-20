#the python date type learning
#!/usr/bin/python3
# -*- coding:utf-8 -*-

# the int type
print('the python date type of int could be any size ')
num=100
print('the positive integer num such as :',num)
num=-125
print('the negative integer num such as :',num)

# the float type
print('the python date type of float could be any size too')
num=1.23
print('the positive float such as:',num)
num=-1.34
print('the nagative float such as:',num)

num=1.2e10
print('the very large number such as:',num)
num=2.5e-10
print('the very small number such as:',num)

#the character type
s='I\'m a char'
print('the char such as :\'%s\' or \"%s\"'%(s,s))
s="我"
print('\'%s\' is a char too'%s)

#the bool type
b=1>2
c=1>0
print('the bool type is only can be true or false,such as 1>2=%s 1>0=%s'%(b,c))
a=True
b=False
print('a and b=%s ,not a=%s not b=%s a or b=%s'%(a and b,not a,not b,a or b))

a=None
print('the value of a is:',a)

#the list type
need_list=['money','friend','family','lover']
print(need_list)
need_list.append('power')
print(need_list)
print("the second need is:",need_list[1])
need_list.insert(2,'children')
print(need_list)
need_list[2]='freedom'
print(need_list)
need_list.pop(2)
print(need_list)

#the tuple type
test_tuple=('children','teenager',"adult",need_list,"elder","death")
print('the tuple is:',test_tuple)
test_tuple[3].append('dream')
print(test_tuple)
