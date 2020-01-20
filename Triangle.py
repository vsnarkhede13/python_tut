N=int(input("Enter Height of equilateral triangle:"))
for i in range(1,N+1):
  j=0
  for j in range(1,(N-i)+1):
    print(end=" ")
  j=0  
  for j in range(1,(N-(N-i)+1)):
    print(end="* ")
  print()     