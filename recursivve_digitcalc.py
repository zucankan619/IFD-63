#calculate the number of digit

def digit_counter(n):
    if n==0:
        return 0
    return 1+digit_counter(n//10)

print(digit_counter(0))

#value of x^y

def exponent1(x,y):
    if y==0:
        return 1
    else:
        return x*exponent1(x,y-1)
    
print(exponent1(4,4))

#value of x^y using recursive

def exponent2(x,y):
    if y==0:
        return 1
    elif y%2==0:
        return exponent2(x,y//2)*exponent2(x,y//2)
    else:
        return x*exponent2(x,y//2)*exponent2(x,y//2)

print(exponent2(9,2))





