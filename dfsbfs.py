# dfs
n = int(input())
graph = [[]]
for i in range(n):
  graph.append(list(map(int,input().split())))

visited = [False] * (n + 1)


def dfs(graph, v,visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if visited[i] == False:
      dfs(graph,i,visited)

dfs(graph,1,visited)