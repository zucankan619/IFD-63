class Calculator:
    
    def Add(self,x,y):
        return (x+y)
    
    def Sub(self,x,y):
        return (x-y)
    
    def Multi(self,x,y):
        return (x*y)

    def Div(self,x,y):
        return (x/y)

cal=Calculator()
result= cal.Add(15,25)   
print(result)

result= cal.Sub(50,25)
print(result)

result= cal.Multi(10,5)
print(result)

result= cal.Div(2,5)
print(result)

