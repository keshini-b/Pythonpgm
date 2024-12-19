def anagram(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are ANAGRAMS!!!")
    else:
        print("The strings are not anagrams")		
s1 =input("Enter string 1: ")
s2 =input("Enter string 2: ")
anagram(s1, s2)
