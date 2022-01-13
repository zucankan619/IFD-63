
"""
Problem
"""
# a = 97 and z = 122
for alpha in range(97, 123):
    print(chr(alpha), end=" ")

for x in range(65,91):
    print(chr(x),end=" ")
# Factorial Loop 
# ---------------------------
# 3! = 3x2x1

fact =1
num =3
for i in range(1,num+1):
    fact = fact * i

print("The factorial of {num} is {fact}")


# Fibonacci Series Loop 
# ---------------------------

fibo =[0,1]
# fibo[n] = fibo[n-1] + fibo[n-2]
# fibo[i] = fibo[i-1] + fibo[i-2]

n=5
for i in range(2,n+1):
  nextElem = fibo[i-1] + fibo[i-2]
  fibo.append(nextElem)

print('The Fibonacci Series',fibo)


# Prime Number 
# ---------------------------
n=11
for i in range(2,n):
      if n%i==0:
         print("Not a prime number")
         break
      else:
        print("Prime Number")
        break

####################################################

rev = 0
num=int(input("\n\nENTER A NUMBER----: "))
n = num

while num>0:

    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

print(rev)

if n == rev:
    print("\nGIVEN NUMBER IS A PALINDROME")
else:
    print("\nGIVEN NUMBER IS NOT A PALINDROME")


# Printing a - z
print("Alphabets from a - z are : ")





