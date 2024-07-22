list=[1,2,3,4,5,6,7]
exists=5
found=False
for i in list:
    if i==exists:
        found=True
        break
print(found)