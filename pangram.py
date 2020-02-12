alpha="The quick brown fox jumps over the lazy dog"
s1=input("Enter String: ")
l=len(s1)
for i in alpha:
    if i not in s1:
        print("Not pangrams")
        break
else:
    print("Pangrams")
