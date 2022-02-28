


def isPrime(n):
    find=True
    for i in range(2,n):
        if n%i==0:
            find=False
    return find

x=int(input('Enter strat range: '))
y=int(input('Enter end range: '))
count=0   
for i in range(x,y):       
    if isPrime(i):
        print(i,end='\t')
        count+=1
    # else:
    #     print('Not prime number')

print(f'\nTotal number of prime is : {count}')
