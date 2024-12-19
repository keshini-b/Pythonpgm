def primedig(x,y):
    number=0
    count=0
    for n in range (x,y+1):
        number =n
        count =0
        while(number>0):
            num = number%10
            if (num!=1 and num!=0):
                x=prime(num)
                #print(x)
                if(x==num):
                    count = count+1
                #elif (number == 1):
            number = number//10
        if(count>=1):
            print(n)
def prime(num):
    n1=num
    for n in range (2, n1):  
        if ((n1 % n) == 0):
            break
    else:
        return n1
x=int(input("Enter lower bound value:"))
y=int(input("Enter upper bound value:"))
print(f"Strange numbers between {x} and {y} are:")
primedig(x,y)
