##var={}
##print(var)
##print(type(var))

##var={'dhoni',33}
##print(var)
##print(type(var))

##var={'name':'dhoni','age':33}
##print(var)

##var={'name':'dhoni','age':33}
##print(var[0]) #no index based data retrival in dictnary

##in dictionary data are manupulated or used via key
##dictioary is called key value pair
##because each data we needs to bs stored with specific key
##sorting data with key is genraly called as hashing or Hashtable

##var={'name':'dhoni','age':33}
##print(var['age'])

##var={'name':'dhoni','age':33}
##var['name']= 'kohili'
##print(var)

#Dictionary is mutable type

##var={'name':'dhoni','age':33,'name':'pavan'}
##print(var)
##

##var={'name':'dhoni',9:33,98.9:'pavan',('A','b'):'pavann', True:'kumar'}
##var['name']='jai'
##print(var)

##var={'name':'dhoni'}
##var['country'] = 'India'
##print(var)

##var={'name':'dhoni','team':'csk'}
##var1={'age' : 33}
##output = var+var1
##print(output)# NOT POSSIBLE

##var={'name':'dhoni','team':'csk'}
##var1={'age' : 33}
##var2={'LAN':'HINDI'      }
##output = {**var,**var1,**var2}
##print(output)

##var={'name':['dhoni','kohli'],'team':['csk','RCB'],'Sports':{'cricket':['sachin']}}
##print(var)
##
##var={'name':['dhoni','kohli'],'team':['csk','RCB'],'Sports':{'cricket':['sachin']}}
##output = var['team'][1]
##print(output)

##var={'name':['dhoni','kohli'],'team':['csk','RCB'],'Sports':{'cricket':['sachin']}}
##var['team'][1] = 'kumar'
##print (var)

##var={'name':['dhoni','kohli'],'team':['csk','RCB'],'Sports':{'cricket':['sachin']}}
##output=var['country']
##print (output)
##prinr ('welcome')

var={'name':['dhoni','kohli'],'team':['csk','RCB'],'Sports':{'cricket':['sachin']}}
output=var.get['country','sorry key not found']
print (output)
print ('welcome')
