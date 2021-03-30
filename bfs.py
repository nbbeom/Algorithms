graph = dict()

graph['A'] = ['B','C'] 
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C']

def bfs(graph, start):
    visited = []
    needVisted=[]

    needVisted.append(start)

    while needVisted:
        node = needVisted.pop(0)
        if node not in visited:
            visited.append(node)
            needVisted.extend(graph[node])

    print(visited)

def dfs(graph, start):
    visited = []
    needVisted=[]

    needVisted.append(start)

    while needVisted:
        node = needVisted.pop()
        if node not in visited:
            visited.append(node)
            needVisted.extend(graph[node])

    print(visited)

bfs(graph,'A')
dfs(graph,'A')
