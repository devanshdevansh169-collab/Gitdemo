k=['Rabi',10.4,10,True,False]
print(k)
k.insert(2,'Rabi')
print(k)
k.remove('Rabi')
print(k)
k.pop(3)
print(k)
k.index('Rabi')
print(k)
k.count('Rabi')
print(k)
for i in range(0,len(k)):
    if (k[i]=='Rabi'):
        print(k[i],"found at index",i)
