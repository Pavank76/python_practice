class my_class:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def one (self):
        print ('one',self.name)

class second_class(my_class):
    def two (self):
        print ('two',self.name,self.age)

my = second_class('dhoni',33)
my.one()
my.two()
