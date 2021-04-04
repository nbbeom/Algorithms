from collections import deque

def solution(n,vertex):
    def bfs():
        de = deque()
        de.append(1)

        while de :
            x = de.popleft()
            for i in a[x]:
                if ch[i]==-1:
                    ch[i]=ch[x]+1
                    de.append(i)

    a=[[] for i in range(n+1)]
    ch=[-1]*(n+1)

    for i,j in vertex:
        a[i].append(j)
        a[j].append(i)
    
    ch[1]=0
    bfs()
    return ch.count(max(ch))