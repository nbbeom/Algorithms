dx ,dy =[0,0,-1,1],[1,-1,0,0]
def ck(lst):
    ret =  0
    for flower in lst:
        

seed = int(input())

G = [list(map(int,input().split())) for i in range(seed)]

for i in range(seed*seed):
    for j in range(seed*seed):
        for k in range(seed*seed):
            ans =min(ans,ck(i,j,k))

print(ans)