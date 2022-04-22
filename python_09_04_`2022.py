##class My_Class(object):
##    def __init__(self):
##        print ('hello')
##
##    def fun(self):
##        print ('welcome to python')
##
##    def fun(self):
##        print ('my second function')
##
##my = My_Class()
##my.fun()

##class My_Class(object):
##    def __init__(self):
##        print ('hello')
##
##    def fun(self):
##        print ('welcome to python')
##
##    def __new(self):
##        print ('my second function')
##
##my = My_Class()
##my.fun()
##my.new()

##class My_class:
##    def __init__ (self,name,age):
##        self.name = name
##        self.age = age
##
##    def one (self):
##        print ('one',self.name)
##
##class Second_Class (My_class):
##    def two(self):
##        print ('two',self.name,self.age)
##
##my = Second_Class('dhoni',33)
##my.one()
##my.two()

##class My_class:
##    def __init__ (self,name,age):
##        self.name = name
##        self.age = age
##
##    def two (self):
##        print ('one',self.name)
##
##class Second_Class (My_class):
##    def two(self):
##        print ('two',self.name,self.age)
##
##my = Second_Class('dhoni',33)
##my.two()

##class My_class:
##    def __init__ (self,name,age):
##        self.name = name
##        self.age = age
##
##    def two (self):
##        print ('one',self.name)
##
##class Second_Class (My_class):
##    def two(self):
##        print ('two',self.name,self.age)
##
##my = Second_Class('dhoni',33)
##my.two()
##my_parent = My_class('dhoni',34)
##my.two()

##class A:
##    def fun (self):
##        print ('A')
##
##class B(A):
##    def fun(self):
##        print('B')
##
##class C(A):
##    def fun(self):
##        print ('C')
##class D(C,B):
##    def fun(self):
##        print ('d')
##d=D()
##d.fun()

class A:
    def fun (self):
        print ('A')

class B(A):
    def fun(self):
        print('B')

class C(A):
    def fun(self):
        print ('C')
class D(C,B):
    pass
##    def fun(self):
##        print ('d')
d=D()
d.fun()

















