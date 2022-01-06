"""
Relational Operator
====================
> Greater Than
>= Greater Than or Equal
< Less Than
<= Less Than or Equal
== Equal
!= Not Equal

If Else Statement
====================
if condition1 :
    statement true
elif condition2:
    statement 2   

elif condition3:
    statement 3  
else:
    statement false
"""

x=int(input("Enter x : "))
y=int(input("Enter y : "))

if x>y :
    print("X is Big")
elif x==y :  
    print("Both are Equal")
else:
    print("Y is Big")