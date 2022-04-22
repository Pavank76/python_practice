##def student_passed (*names):
##    print (names)
##student_passed('Pavan')
##student_passed('Jai')

##def student_passed (**names):
##    print (names)
##student_passed(name='Pavan')
##student_passed(name='Jai',age=25)

##def student_mark(English,maths,student_name):
##    total=English+maths
##    return total
##output= student_mark(40,50,'pavan')
##print(output)

##def student_mark(English,maths,student_name):
##    total=English+maths
##    return total,student_name
##output= student_mark(40,50,'pavan')
##print(output)

##def student_mark(English,maths,student_name):
##    total=English+maths
##    return total,student_name
##output,output1= student_mark(40,50,'pavan')
##print(output)
##print(output1)

##var= 100
##def fun():
##    var = 10
##    print(var)
##print(var)
##fun()
##print(var)

##var= 100
##def fun():
##    global var
##    var= 10
##    print(var)
##print(var)
##fun()
##print(var)

##def fun():
##    print('Hi Pavan')
##    fun()
##        
##        
##    
##fun()    


##counter = 0
##def fun():
##    global counter
##    print('Hello',counter)
##    counetr = counter + 1
##    if counter ==101:
##        return
##    fun()
##fun()

counter = 0
def fun():
    global counter
    print('Hello',counter)
    counetr = counter + 1
    while counter < 101:
        fun()
fun()














