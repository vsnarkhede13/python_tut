import copy
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [15,16,17,18,19,20]
print(l1)
print(l2)
print("Original lists")

l3 = copy.deepcopy(l1)
l4 = copy.copy(l1)
print(l3 , "Deep copy list")
print(l4 , "Shallow copy list")

l4.append([20,21,22,23,24,25])
l3.extend([30,31,32,33,34,35])
print (l4,"appended l4")
print (l3,"extended l3")

l3.remove(3)
l4.pop()
print (l4,"pop")
print (l3, "removal of 3")

l4.insert(0,3)
print(l4,"Insert")
l4.append(l3[4:7])
print(l4,"appended sliced list")

