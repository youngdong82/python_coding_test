# 플로이드
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n) for _ in range(n)]

for a in range(n):
  for b in range(n):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a-1][b-1] = min(graph[a-1][b-1],c)

for k in range(n):
  for a in range(n):
    for b in range(n):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
  print(graph[i])

# 정확한 순위 28분 컷!
INF = int(7)
n,m = map(int,input().split())
graph = [[INF] * (n) for _ in range(n)]

for a in range(n):
  for b in range(n):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a,b = map(int,input().split())
  graph[a-1][b-1] = 1

for k in range(n):
  for a in range(n):
    for b in range(n):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

def check(result):
  for i in range(n):
    if i not in result:
      return False
  return True

count = 0
for k in range(n):
  result = []
  for i in range(n):
    if graph[k][i] != INF:
      result.append(i)
    if graph[i][k] != INF:
      result.append(i)
  if check(result):
    count += 1

print(count)

# 35분
# 화성탐사 40분
import heapq

INF = int(1e9)
t = int(input())

for ts in range(t):
  n = int(input())
  field = []
  for i in range(n):
    field.append(list(map(int,input().split())))
  visited = [[False] * (n) for _ in range(n)]

  graph = [[INF] * (n) for _ in range(n)]

  dx = [-1,0,1,0]
  dy = [0,1,0,-1]

  def find_next(now):
    x,y = now
    connect = []
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx <n and 0 <= ny <n:
        connect.append(((nx,ny),field[nx][ny]))
    return connect

  def dijkstra(start):
    q = []
    heapq.heappush(q,(field[start[0]][start[1]] ,start))
    graph[start[0]][start[1]] = field[start[0]][start[1]]
    visited[start[0]][start[1]] = True
    while q:
      dist, now = heapq.heappop(q)
      connect = find_next(now)
      for i in connect:
        if visited[i[0][0]][i[0][1]] == False:
          cost = dist + i[1]
          graph[i[0][0]][i[0][1]] = cost
          visited[i[0][0]][i[0][1]] = True
          heapq.heappush(q,(cost, i[0]))

  start = (0,0)

  dijkstra(start)
  print(graph[n-1][n-1])

# 숨바꼭질 24분 컷!
import heapq

INF = int(1e9)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist,now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(q,(cost, i))

dijkstra(1)

max_value = 0
index = 0
for i in range(1,n+1):
  if max_value < distance[i]:
    max_value = distance[i]
    index = i

many = distance.count(max_value)

print(index, max_value, many)
