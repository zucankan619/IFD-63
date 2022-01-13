from tkinter import X
from unicodedata import digit


rev=0
num=int(input("Enter what you want: "))
n=num

while num>0:
    digit=num%10
    rev=rev*10+ digit
    num=num//10

print(rev)