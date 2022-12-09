#PROJECT
#Question
#In this project you have to enter a range [A, B] and system will randomly pick any number from your given range and check the status of that given number.
#The properties to be checked are:
#1.	Is that number is odd or even
#2.	Is that number is positive or negative number
#3.	Is that number is prime number or composite number.




import random
import sys


def check_num(x):
    if x[0]=='-':
        for i in range(1,len(x)):
            if x[i]=='.':
                pass
            elif x[i].isnumeric()==True:
                pass
            else:
                sys.exit("Please enter a valid number")
        
        count=countChar(x,'.')
        if count>1:
            sys.exit("Please enter a valid number")

    else:
        for i in range(len(x)):
            if x[i]=='.':
                pass
            elif x[i].isnumeric()==True:
                pass
            else:
                sys.exit("Please enter a valid number")
        count=countChar(x,'.')
        if count>1:
            sys.exit("Please enter a valid number")

def countChar(str, x):
    count = 0
    for i in range(len(str)):
        if (str[i] == x) :
            count += 1
    return count

a=input("enter first number: ")
b=input("enter second number: ")
check_num(a)
check_num(b)

a=int(float(a))
b=int(float(b))
if a<=b:
    y=random.randint(a,b)
else:
    y=random.randint(b,a)
print("selected integer is: ",y)
if y%2==0:
    print(y,"is an even number")
else:
    print(y,"is an odd number")
if y>0:
    print(y,"is an positive number")
elif y<0:
    print(y,"is an negative number")
elif y==0:
    print(y,"is neither negative nor positive")

if y<=1:
    print(y,"is neither prime nor composite") 
elif y>=2:
    c=int(y/2)+1
    for i in range(2,c):
        rem=y%i
        if rem==0:
            print(y,"is a composite number")
            break
    else:
        print(y,"is a prime number")
