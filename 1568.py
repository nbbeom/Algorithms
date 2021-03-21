n =int(input())

14
1 , 2, 3, 4,1,2,
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
