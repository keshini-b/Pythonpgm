def long_substr(s):
        def check(start,end):
            chars = [0] * 128
            for i in range(start,end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i,j):
                    res = max(res, j - i + 1)
        return res
s = input("Enter any string:")
a=int(input("Number of elements in the array:-"))
n=list(map(int, input("elements of array:-").strip().split()))
print(n)
print(long_substr(s))
