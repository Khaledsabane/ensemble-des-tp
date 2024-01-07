L1= [0]*3
L1[1]+=1
print(L1)
print(type(L1))
print(id(L1))
print(id(L1[0]))
print(id(L1[1]))
print(id(L1[2]))

a="machaine"
print(type(a))
print(id(a))

for i in range(len(a)):
    print(f"{id(a[i])}")