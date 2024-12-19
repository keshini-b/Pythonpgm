arr=list(map(int,input("Enter the numbers: ").split()))
lst1=[]
lst2=[]
lst3=[]
n = len(arr)
for i in range(0,n//2):
    lst1.append(arr[i])
lst1.sort()
print(lst1)
for j in range(n//2,n):
    lst2.append(arr[j])
lst2.sort()
print(lst2)
for ele in lst1:
    lst3.append(ele)
for ele in lst2:
    lst3.append(ele)
lst3.sort()
print(lst3)
print("The Resultant Sorted array is:")
for res in lst3:
    print(res)

