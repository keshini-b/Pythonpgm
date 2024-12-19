from datetime import date
print("Enter year,month and days making sure that m1,y1,d1 occur earlier than m2,y2,d2")
year1 = int(input('Enter year1: '))
month1 = int(input('Enter month1: '))
day1 = int(input('Enter day1: '))
d1 = date(year1, month1, day1)
print(d1)
year2=int(input('Enter year2: '))
month2 = int(input('Enter month2:'))
day2 = int(input('Enter day2:'))
d2=date(year2,month2,day2)
print(d2)
d0 = d2-d1
print("The number of days between given dates are:",d0.days)
y0 = year2-year1
print("Years between the given dates:",y0)
if(year1==year2):
    m0=month2-month1
    print("Months between the given dates:",m0)
    if(m0==0):
        print("Less than 1 month apart")
    elif(m0==1):
        if(day1==day2):
            print("Exactly 1 month apart")
    else:
        print("The given dates are not 1 month apart")
elif(y0==1):
    if(month1==12 and month2==1):
        m1=1
        print("Months between the given dates:",m1)
        if(day1==day2):
            print("Exactly 1 month apart")
        else:
            print("The given dates are not 1 month apart")
    else:
        print("The given dates are not 1 month apart")
else:
    print("The dates doesn't belong to same years and hence are not 1 month apart")
        
        
    



       




