n , a = int(input()),list(map(int,input().split()))
b=[a[0]]
for i in range(1,n):
    b.append(a[i]*(i+1)-sum(b))

for i in b : print(i , end= ' ')