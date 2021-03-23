n =int(input())

i = 1
temp= 0
while n > 0 :
    if n >=i :
        n-=i
        i+=1
        temp +=1
    else : 
        i=1
print(temp)
