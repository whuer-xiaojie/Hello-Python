# the first test of python start at 2018-1-20
#!/usr/bin/python3.3
print('''my first python program
start at 2018-1-20
learn the input()and print()function''')

#print integer and print the result of a mathematical expressions
print('the print int num is:',520)
print('the mathematical expressions 100+200=',100+200)

#print the special or escaped characters
print("I'm very happy! thanks Daizeyang ")
print('I\'m very happy! thanks so much \"Daizeyang\"')
print(r'I\\love and miss you so much \\\"Daizeyang"')

#use the input() to get keyboard input information
print('please input your favorite program language:')
name=input();
print('you must really like \'%s\'p and you will grasp it '%name)

number1=int(input('please input number1:'))
number2=int(input('please input number2:'))
print('you input number is %d and %d and %d+%d='%(number1,number2,number1,number2),number1+number2 )
