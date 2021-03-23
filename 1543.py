T = input()
C = input()
i = 0
temp =0
while i<= len(T):
    if T[i:i+len(C)] ==C:
        temp +=1
        i+=len(C)
    else : 
        i+=1
print(temp)
