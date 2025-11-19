def hello():
    print("Hello World")

hello()


#

def add(x,y): 
    print(x*y)
add(2,3)
add(6,8)
add(14,26)

#

def hello(*name):
    print("hello my name is ",name[1])
hello("john","petter","jass")
#

def hello():
    return("hi Nihal how are you")
print(hello())

#Recurion
def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print(fact(4))


#
a= lambda b:b*5
print(a(4))
x=lambda a,b,c:(a+b)*c
print(x(3,7,2))

#
#def maximum_num(val1,val2,val3)
 #   if val1>val2 and val1>val3:
  #      print(val1,"is the greatest number")
   # elif val2 >val1 and val2 > val3:
    #    print(val2,"is the greates number ")

#
def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())


#

def check_prime(num):
    if num==1:
        print("it is not prime number")
    if num==2:
        print("it is a prime number")
    for i in range(2,num):
        if num % i==0:
            print("it is not a prime number")
            break

    else:
        print("it is a prime number")
check_prime(17)
#

#
def add(number):
    total=0
    for i in number:
        total = total+i
        return(total)
print(add([4,5,6,7,8]))


#
import datetime
date=datetime.datetime.now()
print(date)
#
import random
x=random.randint(1,10)
print(x)
#
import math
x=min (13,67,45)
print(x)
#power
a=pow(2,4)
print(a)
#square root
b=math.sqrt(256)
print(b)




