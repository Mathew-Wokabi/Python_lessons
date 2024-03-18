#python comments-this is a single line comment
"""
this is a multiline comment in python
"""

#variables
student_name ="Mathew"  #data type is string
student_age = 20    #data type is integer
student_fee= 100.0   #data type is float
student_mark= 100   #data type is boolean
is_male=True

#outputting the values in the variables
print(student_name)
print(student_age)
print(is_male)


student_name="Mathew"
student_name="Allan"

print(student_name)


STUDENT_NAME="Ryan"
student_name="James"
print(student_name)

#variable naming in python
book_price=20.0 #valid variable name
_book_price=20.0 #valid variable name


book_price_123=40

x=y=z=10 #assigning one value to multiple variables
x,y,z=30,40,50 #multiples values assigned multiple variables


a=1 #x will be 1
b="1"
c=a+int(b)
print("the sum of a and b is:" ,c)

firstname="Mathew"
secondname="wokabi"
thirdname=firstname+""+str(secondname)
print("my third name is:",thirdname)


price=60
qty=15
total=price*qty
print("the total is:"+str(total)+"kenyan shillings")

print(3%7)


x=5
print(x) #output is 5

x+=5  #x=x+5
print(x) #output is 10

x-=4  #x=x-4
print(x) #output is 1

x*=3  #x=x*3
print(x) #output is 15

x/=2  #x=x/2
print(x) #output is 9

#COMPARISON OPERATORS
a=20
b=8
print(a==b)

print(a>b)


#LOGICAL OPERATOR
age=50
nationality="KENYAN"

if nationality=="KENYAN" and age>=35:
    print("you can be a president")
else:
    print("you cannot be president")




x=60
w=2
ans=w%x
print(ans)
if ans==0:
    print("the number is even")
else:
    print("the number is odd")


#LOOPS
#while loops -- testing for break
x=1
while x <= 5:
    if x == 3:
        break
    print(x)
    x+=1

#the continue statement in the while loop
i=1
while i < 6:
        if i == 3:
         i += 1

        continue
        print (i)
        i += 1
        
































