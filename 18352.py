from collections import deque

n,m,k,x =map(int,input().split())

def bfs(v):
    q = deque()
    q.append(v)
    
    while q :
        temp = q.popleft()
        g[temp]

    

# 도시개수 n 도로 m  거리정보 k  출발 x
grp =[[0 for i in range(m+1)] for i in range(m+1)]
for i in range(m):
    a ,b =map(int,input().split())
    grp[a][b] =1
    grp[b][a]=1

