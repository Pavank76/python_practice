##import csv
##with open ('python.csv','w') as file_obj:
##    file_obj_csv = csv.writer(file_obj)
##    file_obj_csv.writerow(['Name','age','runs'])
##    file_obj_csv.writerows([['pavan','25','50'],['jai','25','100']])
##
##import csv
##with open ('python.csv','w',newline='') as file_obj:
##    file_obj_csv = csv.writer(file_obj)
##    file_obj_csv.writerow(['Name','age','runs'])
##    file_obj_csv.writerows([['pavan','25','50'],['jai','25','100']])


##import csv
##with open ('jai.csv','w',newline='') as file_obj:
##    file_obj_csv = csv.DictWriter(file_obj,['name','age','runs'])
##    file_obj_csv.writeheader()
##    file_obj_csv.writerows([{'name':'pavan','age':'25','runs':'50'}])

import pandas

my_input = [['name','age','runs'],['Pavan',25,100],['jai',25,101]]
my_final_input = pandas.DataFrams(my_input)
print (my_final_input)
my_final_input.to_csv ('mydata.csv')
