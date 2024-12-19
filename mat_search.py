row=int(input("Enter no.of rows:"))
col=int(input("Enter no.of columns:"))
mat=[]
print("Enter matrix elements:")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    mat.append(a)
for i in range(row):
    for j in range(col):
        print(mat[i][j],end=" ")
    print()
x=int(input("Enter an element to search:"))
for i in range(row):
    for j in range(col):
        if(x==mat[i][j]):
            print("found at",i,",",j)
if(i==row and j==col):
    print("0")
