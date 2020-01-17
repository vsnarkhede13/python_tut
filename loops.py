n=int(input("Enter No "))
res=0
for i in range(1,n+1):
    res=res+i
print("Result by For Loop: %s" %res)
res=0
i=1
while i<=n:
    res=res+i
    i+=1
    print("Result by While Loop: %s" %res)