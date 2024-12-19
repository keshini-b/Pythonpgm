a=int(input("Enter a number: "))
n=int(input("Enter its power: "))
count=0
product=1
while(n>0):
    if(n%2==1):
        product*=a
        count+=1
    a*=a
    count+=1
    n=n//2
print("The number of multiplications used:",count)

