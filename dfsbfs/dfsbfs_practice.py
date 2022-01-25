# 음류수 얼려먹기
n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))

def dfs(x,y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

count = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      count += 1

print(count)

# 미로탈출
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx,ny))
  return graph[n-1][m-1]

print(bfs(0,0))