def solution(enroll, referral, seller, amount):

    sell = {}
    for i in range(len(amount)):
        sell[seller[i]] =amount[i]*100

    graph = [[] for i in range(len(enroll))]
    for i in range(len(enroll)):
        graph[i].extend([referral[i],enroll[i]])
    graph2 = {}

    print(graph)
    print(sell)
    


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

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],
[12, 4, 2, 5, 10])