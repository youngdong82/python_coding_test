# dfs
n = int(input())
graph = [[]]
for i in range(n):
  graph.append(list(map(int,input().split())))

visited = [False]*(n+1)

def dfs(graph, start, visited):
  visited[start] = True
  print(start, end=' ')
  for i in graph[start]:
    if visited[i] == False:
      dfs(graph, i, visited)

dfs(graph,1,visited)

# bfs
from collections import deque

n = int(input())
graph = [[]]
for i in range(n):
  graph.append(list(map(int,input().split())))

visited = [False] * (n+1)

def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = True
  while q:
    now = q.popleft()
    print(now, end=' ')
    for i in graph[now]:
      if visited[i] == False:
        visited[i] = True
        q.append(i)

bfs(graph,1,visited)