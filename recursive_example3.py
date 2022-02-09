#fibonacci number
#fibonacci= 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 + 55 + 89 + 144

def fibo_recursive(n):
    if n<=1:
        return n
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)

n_terms=int(input('Enter a number:'))
for i in range(n_terms):

    print(fibo_recursive(i),end='\t')



