from collections import deque

def solution(tickets):

    graph = {}
    for i ,j in tickets:
        graph[i] =j 
    print(graph)
    bfs(graph,"ICN")

def bfs(graph, s):
    visited = []
    needVisited = []
    
    needVisited.append(s)
    while needVisited : 
        node = needVisited.pop(0)
        if node not in visited :
            visited.append(node)
            if len(graph[node]) == 3:
                n = [str(graph[node])]
                
            needVisited.extend(n)


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])