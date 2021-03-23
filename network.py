# def solution(n,computers):
#     def dfs(s):
#         ch[s]=1
#         for i in a[s]:
#             if ch[i]== 0:
#                 dfs(i)

#     a =[[] for i in range(n)]
#     for i in range(n):
#         for j in range(i,n):
#             if computers[i][j] ==1:
#                 a[i].append(j)
#                 a[j].append(i)

#     ch=[0]*n
#     c =0
#     for i in range(n):
#         if ch[i]==0:
#             c+=1
#             dfs(i)
#     return c

def solution(n, computers):
    answer = 0
    bfs = []
    visited = [0]*n

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1
        
        while bfs:
            node = bfs.pop(0)
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer

n=3
computers =[[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n,computers))