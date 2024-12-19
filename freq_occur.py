istring=[]
while True:
    temp=input()
    if(temp==""):
        break
    else:
        istring.append(temp)
for i in range(0,len(istring)):
    temp=[]
    chara=[]
    no=[]
    for ele in istring[i]:
        if(ele!=" " and ele not in chara):
            chara.append(ele)
            no.append(istring[i].count(ele))
    nooo=max(no)
    for char,noo in zip(chara,no):
        if(nooo==noo):
            temp.append(char)
    temp.sort()
    print(i+1,' Line: ')
    for string in temp:
        print(string)
    print(" ")
