def dec_bin(num):
    if num >= 1:
        dec_bin(num // 2)
    print(num % 2, end = '')
dec = int(input("Enter a decimal number: "))
dec_bin(dec)
