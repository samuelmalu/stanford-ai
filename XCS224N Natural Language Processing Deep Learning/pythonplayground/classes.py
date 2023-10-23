# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Foo:
    def __init__(self, x):
        self.x =x
        
    def printX(self):
        print(self.x)
        
    @classmethod
    def printHello(cls):
        print("hello I am a %s" %cls)
        
obj = Foo(6)
obj.printX()
Foo.printHello()

class FooSubclass(Foo):
    pass

FooSubclass.printHello()


    