def string(s):
   res = ""
   count = 1
   for i in range(1, len(s)):
      if s[i - 1] == s[i]:
         count += 1
      else:
         res = res + s[i - 1]
         if count > 1:
            res += str(count)
         count = 1
   res = res + s[-1]
   if count > 1:
      res += str(count)
   return res

s = input("Enter your string:")
print(string(s))
