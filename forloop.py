"""
For Loop
=============

for variable in collection :
    statements
        ...
"""
# for x in [1,2,3,4,5,6,7]:
#     print(x,end='\t')



for x in range(6):
    print(x,end='\t')

print("\n\n###########################\n\n")

for x in range(3,15):
    print(x,end='\t')

print("\n\n###########################\n\n")

for x in range(3,101,2):
    print(x,end='\t')

print("\n\n###########################\n\n")


# Sum of Series

sum=0
for x in range(5,9):
     sum=sum+x**2
    
print(sum)

print("\n\n###########################\n\n")

#Factorial

fact=1
num=4
for i in range(1,num+1):
     fact= fact * i

print(f"the factorial of {num} is {fact}")   

print("\n\n###########################\n\n")


fact=2
num=6
for x in range(1,num+1):
     fact= fact * x

print(f"the factorial of {num} is {fact}")   

print("\n\n###########################\n\n")

# Prime Number Loop

n=11
for i in range(2,n):
    if n%i==0:
        print(n, "is not a prime number")
        break
    else:
        print(n, "is a prime number")
        break

print("\n\n###########################\n\n")

n=14
for i in range(2,n):
    if n%i==0:
        print(n, "is not a prime number")
        break
    else:
        print(n, "is a prime number")
        break

print("\n\n###########################\n\n")

