def fact(n):

    if n==0:

        return 1

    return n * fact(n-1)

result=fact(5)

print(result)





def assign(string):

    for i in string:
        if len(i)>5:
            return i

        else:
            continue


string=["naveen","uday","akash","shailesh"]
c=assign(string)
print(c)




f=lambda a,b:a+b
result=f(4,5)
print(result)

from functools import reduce

num=[1,2,3,4,5,6]
even=list(filter(lambda n:n%2==0,num))
print(even)

doubles=list(map(lambda a:a*2,num))
print(doubles)


sum=reduce(lambda a,b:a+b,doubles)
print(sum)




