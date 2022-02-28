#Sum of series using recursive method
def sumOfDigit(n):
    if n==1:
        return 1
    else:
        return n+sumOfDigit(n-1)

print(sumOfDigit(10))

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

print(recur_sum(10))