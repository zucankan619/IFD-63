


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
#5*4*3*2*1
print(fact(4))

fact=1
num=4
for x in range(1,num+1):
    fact=fact*x

print(fact)

fact=1
num=5
for x in range(1,num+1):
    fact=fact*x

print(fact)