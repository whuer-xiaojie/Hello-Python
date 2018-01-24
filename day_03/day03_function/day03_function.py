#!/usr/bin/python3
# -*- coding:utf-8 -*-

# use the python function to convert an int to a hexadecimal string
def int_2_hex_str(a):
    if not isinstance(a,(int,float)):
        print("TypeError:%s is not a int number!!!"%a)
        return
    else:
        print("the int number:%d convert to a hexadecimal string is:\'%s\'"%(a,str(hex(a))))

#the test function to solve a quadratic equation
import math
def quadratic(a,b,c):
    for x in(a,b,c):
        if not isinstance(x,(int,float)):
            print("TypeError:the parameter is not correct")
            return
    if a==0:
        if b==0:
            print("the parameter is ont correct:%d=0?"%c)
            return
        else:
            print("the quadratic is :%dx+(%d)=0"%(b,c))
            return -c/b
    elif (b*b-4*a*c)>0:
        print("the quadratic is:%dx^2+(%d)x+(%d)=0"%(a,b,c))
        det=math.sqrt(b*b-4*a*c)
        return (-b+det)/2*a,(-b-det)/2*a
    else:
        print("the quadratic is :%dx^2+(%d)x+(%d)=0"%(a,b,c))
        print("the quadratic without solution")
        return
a,b,c=input("please input 3 number of the quadratic equation:").strip().split(',')
x1=quadratic(a,b,c)
if x1!=None:
    print("x1=%f x2=%f"%(x1[0],x1[1]))
d,e,f=map(float,input("please input 3 number of the quadratic equation:").split())
x1=quadratic(d,e,f)
if x1!=None:
    print("x1=%f x2=%f"%(x1[0],x1[1]))



