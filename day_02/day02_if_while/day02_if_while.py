#!/usr/bin/python3
# -*-coding:utf-8 -*-

# the test of if and else
age=int(input("please input your age:"))
if age<12:
    print("you are still a kid!")
elif age<18:
    print("you are a teenager!")
elif age<40:
    print("you a an adult but you still young ")
else:
    print("you are an adult !")

# the test of for
sum=0
for x in range(101):
    sum+=x
print("1+2+...+100=%d"%sum)

l=['Xiao','Zhu',"Wu","Lin"]
for name in l:
    print(name)

n=100
sum=0
while n>0:
    if sum>1000:
        print("sum=%d"%sum)
        break
    elif n%3==0:
        print("n=%d"%n)
        n=n-1
        continue
    else:
        sum+=n
        n=n-1
print("end of the while n=%d sun=%d"%(n,sum))