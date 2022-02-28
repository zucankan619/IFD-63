rev=0
num=int(input("Enter what the value is: "))
original=num

while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

print(rev)
if original==rev:
    print('The number is palindrom')
else:
    print('The number is not palindrom')