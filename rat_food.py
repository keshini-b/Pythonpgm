def rat_food(r, unit, arr,n):
    if(n==0):
        return -1
    s = r * unit
    print("Amount of food required for all rats:"+str(s))
    s_arr = 0
    i=0
    for i in range(n):
        s_arr += arr[i]
        if s_arr >= s:
            break
    if s > s_arr:
        return 0
    return i+1
   
r=int(input("Enter no.of rats: "))
unit=int(input("Enter units:"))
n=int(input("Enter number of elements in array: "))
arr=list(map(int,input("Number of houses: ").split()))
print("The amount of food in " + str(rat_food(r,unit,arr,n))+" houses is sufficient")



