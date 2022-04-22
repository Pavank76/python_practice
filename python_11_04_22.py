##var = 10/0
##print (var)
##print ('welcome')

##try:
##    var = 10/0
##    print (var)
##
##except:
##    print ('sorry')
##    
##print ('welcome')

##var = 'a' + 10
##print (var)

##try:
##    var = "a" + 10
##    print (var)
##except :
##    print ('sorry')
##
##print ('welcome')

##try:
##    var = 10/1
##    print (var)
##
##except typeerror:
##    print('sorry try again')
##
##except zerodivisionerror:
##    print('sorry for the error')
##except:
##    print ('sorry')

##try:
##    var = 10/0
##    print (var)
##except TypeError as exi:
##    print (exi)
##except ZeroDivisionError as hello:
##    print(hello)
##except :
##    print('sorry')

##try:
##    var = 10/0
##    print (var)
##except (TypeError , ZeroDivisionError)as exi:
##    print (exi)
##
##except :
##    print('sorry')
##
##try:
##    var = 10/0
##    print (var)
##except Exception as ex:
##    print (ex)
##
##
##try:
##    var = 10/0
##    print(var)
##except Exception as ex:
##    print(ex)
##else:
##    print('my else block')
##finally:
##    print ('my block of finally')
##
##
##
##try:
##    var = 10/4
##    print(var)
##except Exception as ex:
##    print(ex)
##else:
##    print('my else block')
##finally:
##    print ('my block of finally')

##var = 10
##try:
##    if var>5:
##        raise IndexError ()
##except IndexError:
##    print ('sorry')
##
##var = 10
##try:
##    if var>5:
##        raise IndexError ('raising an error')
##
##except IndexError as ex:
##    print (ex)

##class netzwerk_error (Exception):
##    pass
##var = 10
##try :
##    if var>5:
##        raise netzwerk_error()
##except netzwerk_error:
##    print('sorry')

class netzwerk_error (Exception):
    my_error = 'user defined exception'
var = 10
try :
    if var>5:
        raise netzwerk_error()
except netzwerk_error as ex:
    print(ex.my_error)




























































