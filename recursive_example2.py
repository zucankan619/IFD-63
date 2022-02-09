#sum of series

def sum_num(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    
    return total

x= int(input('Enter a value: '))
print(sum_num(x))

#sum of series using recursive function

def sum_num2(n):
    if n==0:
        return 0
    return n+sum_num2(n-1)

print(sum_num2(x))
