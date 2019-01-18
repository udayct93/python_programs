

#one dimention array

from array  import *
val=[2,3,4,5,6,7,7,8,9,]
for e in val:
    print(e)

from array  import *
arr=array('i',[])
n=(int(input("enter the n values")))

for i in range(n):
    x = (int(input("enter the next value")))
    arr.append(x)
print(arr)

val=(int(input("enter the search value")))
k=0
for e in arr:
    if e==val:
        print(k)
    k+=1

arr=[11,2,2,3,4]
arr1=[11,3,4,5,6]
ar=arr+arr1
print(ar)
























#multi dimention array
from numpy import *
arr=[11,2,2,3,4]
arr1=[11,3,4,5,6]

print(concatenate([arr,arr1]))

arr=arr1
print(id(arr))
print(id(arr1))

arr2=arr1.copy()
print(arr2)


arr=array([
        [1,2,3,4,4,6],
        [5,6,7,8,5,2]]


   )
print(arr.size)

arr2=arr.flatten()
arr3=arr2.reshape(2,2,3)
print(arr3)



m=matrix('1,2,3;4,5,6;7,8,1')
print(m.max())


def add(x,y):
    z=x+y
    return z
a=add(4,5)
print(a)


def add(a,*b):
    c=a
    for i in b:
        c+=i

    print(c)

add(5,4,3,2)



def count(list1):
    even = 0
    odd = 0

    for i in list1:

        if i%2==0:
             even+=1
        else:
             odd+=1

    return even,odd

list1=[1,2,3,4,5,6]

even,odd = count(list1)

print("Even : {} and Odd : {}".format(even,odd))

def assign(string):

    for i in string:
        if len(i)>5:
            return i
        else:
            continue
    i+=1

string=["naveen","uday","akash","shailesh"]
c=assign(string)
print(c)



def fact(n):
    f=1
    for i in range[1,n+1]:
        f=f*i
    return f
n=4
res=fact(n)



def fact(n):

    if n==0:

        return 1

    return n * fact(n-1)

result=fact(5)

print(result)


f=lambda a,b:a+b
result=f(4,5)
print(result)


