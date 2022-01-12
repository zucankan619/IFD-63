"""
while loop
================
initialize variable
while condition:
    statements
    increment

"""

#initialize variable
x=1
while x<=5 : #x<=5 - Condition
    print(x,end='\t') #statements
    x=x+1 #increment

#initialize variable
x=50
while x>40 : #x>40 - Condition
    print(x,end="\t") #statements
    x=x-1 #decrement

# #initialize variable
# x=50
# while x>=40 : #x>=40 - Condition
#     print(x) #statements
#     x=x-1 #decrement



x=1
while x<=30 :
    if x%2==0:
        print(x,end="\t")
    x=x+1

x=5
while x<=30 :
    if x%2==0:
        print(x,end="\t")
    x=x+1
print("\n\n###########################\n\n")


#Checking Prime
num=15
x=2
isPrime=True

while x<num :
    if num % x==0: 
        isPrime=False
        break
    x=x+1

if isPrime :
      print(num, "is a prime number")   
else:
      print(num, "is not a prime number")

print("\n\n###########################\n\n")



#Sum of Series    
sum=0
x=1
while x<=10:
     sum=sum+x
     x +=1
    
print(sum)
print("\n\n###########################\n\n")


sum=0
x=1
while x<=10:
     sum=sum+x**3
     x +=1
    
print(sum)

print("\n\n###########################\n\n")


# Reverse Number

rev=0
num=456
n=num

while num>0:
    digit=num%10
    rev= rev * 10 + digit
    num= num//10
    
print(rev)

print("\n\n###########################\n\n")

rev=0
num=5866
n=num

while num>0:
    digit=num%10
    rev= rev * 10 + digit
    num= num//10
    
print(rev)