x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

print(bin(x), "Binary of ", x)
print(bin(y), "Binary of ", y)

print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x<<4)
print(y>>3)