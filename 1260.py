from collections import deque

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited_list = [0] * (N+1)
for i in range(M):
	x, y = map(int, input().split())
	graph[x][y] = graph[y][x] = 1

def dfs(v):
	visited_list[v] = 1
	print(v, end=' ')
	for i in range(1, N+1):
		if graph[v][i] == 1 and visited_list[i] == 0:
			dfs(i)

def bfs(v):
	visited_list[v] = 0
	q = deque()
	q.append(v)
	while q:
		v = q.popleft()
		print(v, end=' ')
		for i in range(1, N+1):
			if graph[v][i] == 1 and visited_list[i] == 1:
				q.append(i)
				visited_list[i] = 0

dfs(V)
print()
bfs(V)

