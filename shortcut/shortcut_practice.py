# # 미래 도시 15분 컷!
INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a,b = map(int,input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x,k = map(int,input().split())

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


if graph[1][k] == INF or graph[k][x] == INF:
  print(-1)
else:
  print(graph[1][k] + graph[k][x])

# 전보 16분 컷!
import heapq
from unittest import result

INF = int(1e9)
n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist,now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count = 0
result = 0
for i in distance:
  if i != INF:
    result = max(result,i)
    count += 1


print(count-1,result)
