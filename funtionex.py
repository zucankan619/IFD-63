"""
Function
=====================================
def functionName(parametres):
    statements
    ...
"""

def welcome():
    print("Hello Ankan Good Morning")

#calling function
welcome()

def welcome(name):
    print(f"Hello {name} Good Morning")

welcome('Parvez') 
welcome('Muntakim') 
welcome('Rafi') 

def welcome(name, message):
    print(f"Hello {name} {message}")

welcome('Parvez','How are you?') 
welcome('Muntakim','Good Evening') 
welcome('Rafi','Good Night') 

#python arbitrary arguments

def greetings(*names):
    for n in names:
        print("Hello ", n)

greetings('Rajjo', 'Dider', 'Ankan', 'Muntakim' )
