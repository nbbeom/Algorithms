# n ,a,b =8,4,7
# def sol(n,a,b):
#     for i in range(n//2):
#         if a == b :
#             return i
#         if a >1 :
#             if a%2 != 0:
#                 a+=1
#             a = a//2
#         if b>1 :
#             if b%2 != 0:
#                 b+=1
#             b = b//2
# print(
# sol(n,a,b))

from collections import defaultdict
import heapq

def solution(N,road,K):
    graph = defaultdict(list)
    for u,v,w in road:
        graph[u].append((v,w))
        graph[v].append((u,w))

    dist ={node : float('inf') for node in range(1,N+1)}
    dist[1] = 0

    queue = []
    heapq.heappush(queue, [dist[1],1])

    while queue : 
        d, node = heapq.heappop(queue)
        if dist[node]<d:
            continue
        for adjacent,d2 in  graph[node]:
            distance =d +d2
            if distance <dist[adjacent]:
                dist[adjacent] = distance
                heapq.heappush(queue,[distance,adjacent])
    return sum(1 if i <= K else 0 for i in dist.values())