# s='Daffodil International Academy'[::-1]
# print(s)

# Python code to reverse a string
# using loop

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    
    return str

s = "DIA"
rs=reverse(s)
print ("The original string is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (rs)

if s==rs:
    print('The string is palindrom')
else:
    print('The string is not palindrom')


