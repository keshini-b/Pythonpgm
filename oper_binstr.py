def oper_binstr(string):
    x=int(string[0])
    i=1
    while i< len(string):
        if string[i]=='A':
            x&=int(string[i+1])
        elif string[i]=='B':
            x|=int(string[i+1])
        else:
            x^=int(string[i+1])
        i+=2
    return x
string=input("Enter a string:")
print(oper_binstr(string))
