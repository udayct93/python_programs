x=[]
n: int=10
for i in range(1, n):
    print(x)
    ist1=['i', []]
n = (int(input("enter the size of n")))

for i in range(n):
    x = (int(input("enter the next value")))
    list.insert(x)

print(list)


input_string=(input("enter the values seperted by commas"))
list1=input_string.split()
sum=0
for num in list1:
    sum=sum+int(num)

    print("SUm",sum)


tuple1 = (23, 333, 22, 2)
a = tuple1.count(2)
print(a)

set1 = {34, 55, 44, 33, 22, 44, 33, 54}
set2 = {34, 55, 44, 33, 22, 44, 33}
set1.update([41, 3, 4, 5, 6, 4, 5, 43])
print(set1)
z = set1.isdisjoint(set2)
print(z)

# dictionaries#
thisdict= {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x=thisdict.get("model")


thisdict.popitem()
print(x)
thisdict["color"]="red"
print(x)



def my_function(f):
  for x in f:
    print(x)

fruits = ["apple", "banana", "cherry","cherry"]

my_function(fruits)

def one_function(x,y):
    if x>y :
        print("a is greater")
    elif x==y:
        print("equal")
    else:
        print("b greater")
one_function(11,34)

def second_function(x,y):
    if x>y or x<y:
        print("dddd")
    else:
        print("equal")
second_function(12,12)

def my_function(n):
    return lambda a:a*n
mydoubler=my_function(3)
print(mydoubler(22))


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
r=fact(10)
print(r)

from functools import reduce
f=lambda a,b:a+b
result=f(4,5)
print(result)

li.remove(22)
print(li)
sd=li.copy()
print(sd)
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)


class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(abc):
        print("my name is " +abc.name)
p1=myclass('jhon',32)
p1.myfunc()


class A:
    def __init__(self):
        print("in init A")
    def feature1(self):
        print("in feature1")
    def feature2(self):
        print("in feature2")

class B:

    def __init__(self):
        print("in init B")
        super().__init__()
    def feature3(self):
        print("in feature3")
    def feature4(self):
        print("in feature4")

class C(A,B):
    def __init__(self):
        print("in init C")
        super().__init__()                                #method resolution order(MRO)
    def feature5(self):
        print("in feature5")
    def feature6(self):
        print("in feature6")


a1=C()
a1.feature1()

a1.feature3()



class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        print("hi bro")

    def display(self):
        print(self.name)
        print(self.idnumber)



class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        print(salary)
        print(post)
        Person.__init__(self, name, idnumber)


a = Employee("vinay", 886012,56666,"SE")
a.display()


nums=[1,2,3,4,5,6,7,8]
evens = list(filter(lambda n:(n%2==0),nums))
print(evens)

import re

str = "The rain in Spain"
x = re.findall("ra", str)
print(x)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {} dollars for {} pieces of item {}."
print(myorder.format(itemno,quantity, price))


try:
    print(p)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")




import sys
rlist=['a',0,2,4]
for e in rlist:
    try:
        c=1/int(e)
    except :
        print("the value is",e)
        print(sys.exc_info()[0],"occured")
        print("next value ")
        print()
print("inverse of the number is",c)

import re

str = "The rain in Spain09"

#Check if "ain" is present at the end of a WORD:

x = re.findall("\d",str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
