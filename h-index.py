c =[21,3,4,11,5]
c.sort(reverse =True)

print(c)
temp = 0
for i in c:
    if temp > i :
        print(temp)
    elif temp ==i :
        print(temp)
    temp+=1
print(temp)
