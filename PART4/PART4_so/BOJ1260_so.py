from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(graph, start):
    global dfs_answer, visited
    visited[start] = True
    dfs_answer.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i)
            visited[i] = True

def bfs(graph, start):
    global bfs_answer, visited
    visited[start] = True
    queue = deque([start])

    while(queue):
        x = queue.popleft()
        bfs_answer.append(x)
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs_answer = []
bfs_answer = []

dfs(graph, v)
visited = [False for _ in range(n+1)]
bfs(graph, v)

for elem in dfs_answer:
    print(elem, end=' ')

print()

for elem in bfs_answer:
    print(elem, end=' ')