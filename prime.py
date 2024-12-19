def prime_check(num):  
    if num > 1:  
        for i in range(2,(num//2) + 1):  
            if (num % i) == 0:  
                return 0
        else:  
            return 1
    else:  
        return 0
n = int(input("Enter a number: "))
num = n+1
while True:
    if prime_check(num):
        print(f"{num} is the smallest prime number greater than {n}")
        break
    num += 1
