# x=10
# x=5
# x=9

# print(x)

from types import FunctionType


x= [2,10,1,13,7]
print(x)


x= [2,10,1,13,7]
print(x,end='\n')


for i in x:
    print(i,end='\t')

# for x in [2,10,1,13,7]:
#     print(x,end='\t\n')


fruits= ['Mango' , 'Lichi' , 'Jack Fruit' , 'Apple' , 'Banana']
for i in fruits:
    print(i,end='\n\t')
#add items in list
fruits.append('Orange')
print(fruits)
#extending list
fruits.extend(['Strawberry' , 'Grape' , 'Carrot'])
print(fruits)
#indexing
fruits.insert(2,'Guava')
print(fruits)
#removing Objet
fruits.remove('Banana')
print(fruits)
#removing index wise
del fruits[6]
print(fruits)
#only item slicing (-num means last)
print(fruits[-1])
print(fruits[-5])
print(fruits[-7])
#a selected list

print(fruits[0:3])
print(fruits[4:7])
print(fruits[3:5])

#sorting
fruits.sort()
print(fruits)
#Revers
fruits.reverse()
print(fruits)



