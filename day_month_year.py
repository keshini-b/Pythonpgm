from datetime import date,datetime
print("Enter year,month and days making sure that m1,y1,d1 occur earlier than m2,y2,d2")
list1 = input("Enter date1: ").split()
print("Date1: ",list1)
list2 = input("Enter date2: ").split()
print("Date2", list2)
date1=int(list1[1])
date2=int(list2[1])
month1=list1[0]
month2=list2[0]
m1 = datetime.strptime(month1, '%b').month
m2 = datetime.strptime(month2, '%b').month
year1=int(list1[2])
year2=int(list2[2])
d1=date(year1,m1,date1)
print(d1)
d2=date(year2,m2,date2)
print(d2)
d0 = d2-d1
print("The number of days between given dates are:",d0.days)
y0 = year2-year1
print("The number of years between given dates are:",y0)
month = m2-m1
m0 = month + y0*12
print("The number of months between given dates are:",m0)
if(year1==year2):
    if(m0==0):
        print("Less than 1 month apart")
    elif(m0==1):
        if(date1==date2):
            print("Exactly 1 month apart")
        else:
            print("Not 1 month apart")
    else:
        print("The given dates are not 1 month apart")
elif(y0==1):
    if(m0==1):
        if(date1==date2):
            print("Exactly 1 month apart")
        else:
            print("Not 1 month apart")
    else:
        print("The given dates are not 1 month apart")
else:
    print("THE GIVEN DATES ARE NOT 1 MONTH APART!!!")
        

