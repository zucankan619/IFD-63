"""
Class
=========
A class is a blue print for the object 

An object has two characteristics:
1. attributes
2. behaviour

syntax of creating a class
=============================
class ClassName(object):
    snipet

making an instance(object) of a class
==================================
objectName=className(arguments)
"""

class MyClass:
    x=10
    def myFunc(self):
        print('Hello')


mc=MyClass()
print(mc.x) 
mc.myFunc()




