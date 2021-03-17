def dfs(x,y):
    if x<= -1  or y<=-1:
        return False
    
    if g[x][y] == 0:
        g[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

n , m = map(int,input().split())

g = []
for j in range(n):
    g.append(list(map(int,input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True :
            result+=1

print(result)
