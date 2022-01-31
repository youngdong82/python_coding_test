# # 여행계획
# # 다른 집합일 경우 안돼
# def find_root(parent,x):
#   if parent[x] != x:
#     parent[x] = find_root(parent,parent[x])
#   return parent[x]

# def union(parent,x,y):
#   x = find_root(parent,x)
#   y = find_root(parent,y)
#   if x < y:
#     parent[y] = x
#   else:
#     parent[x] = y


# n,m = map(int,input().split())
# parent = [0] * (n+1)

# for i in range(1,n+1):
#   parent[i] = i

# edges = []

# for i in range(1,n+1):
#   array = list(map(int,input().split()))
#   for j in range(i,n):
#     if array[j] == 1:
#       edges.append((i,j+1))

# for edge in edges:
#   a,b = edge
#   union(parent,a,b)


# itinery = list(map(int,input().split()))

# def check():
#   for i in range(1,len(itinery)):
#     if find_root(parent,itinery[i]) != find_root(parent,itinery[i-1]):
#       return False
#   return True

# if check():
#   print('YES')
# else:
#   print('NO')

# 탑승구
# g = int(input())
# p = int(input())

# gates = [0] * (g+1)


# for _ in range(p):
#   x = int(input())
#   count = 0
#   for i in range(x,0,-1):
#     if gates[i] == 0:
#       gates[i] = 1
#       break
#     else:
#       count +=1
#   if count == x:
#     break

# print(gates.count(1))

# 동빈나 ver
# 이걸보고 서로소 판별을 어떻게 떠올리지...?
# def find_root(parent,x):
#   if parent[x] != x:
#     parent[x] = find_root(parent,parent[x])
#   return parent[x]

# def union(parent,x,y):
#   x = find_root(parent,x)
#   y = find_root(parent,y)
#   if x < y:
#     parent[y] = x
#   else:
#     parent[x] = y
  
# g = int(input())
# p = int(input())
# parent = [0] * (g+1)

# for i in range(1,g+1):
#   parent[i]=i

# result = 0
# for _ in range(p):
#   data = find_root(parent,int(input()))
#   if data == 0:
#     break
#   union(parent,data,data-1)
#   result += 1
# print(result)

# # 어두운 길 
# # 14분 컷!
# def find_root(parent,x):
#   if parent[x] != x:
#     parent[x] = find_root(parent, parent[x])
#   return parent[x]

# def union(parent,x,y):
#   x = find_root(parent,x)
#   y = find_root(parent,y)
#   if x < y:
#     parent[y] = x
#   else:
#     parent[x] = y

# n,m = map(int,input().split())
# parent = [0]*(n)

# for i in range(n):
#   parent[i] = i

# edges = []
# for _ in range(m):
#   x,y,z = map(int,input().split())
#   edges.append((z,x,y))
# edges.sort()

# result = 0
# summ = 0
# for edge in edges:
#   cost,x,y = edge
#   summ += cost
#   if find_root(parent,x) != find_root(parent,y):
#     union(parent,x,y)
#     result += cost


# print(summ-result)

# 행성터널 
# 이건 진짜 미친 문제다.

# def find_root(parent,x):
#   if parent[x] != x:
#     parent[x] = find_root(parent, parent[x])
#   return parent[x]

# def union(parent,x,y):
#   x = find_root(parent,x)
#   y = find_root(parent,y)
#   if x < y:
#     parent[y] = x
#   else:
#     parent[x] = y

# n = int(input())
# parent = [0] * (n+1)

# for i in range(1, n+1):
#   parent[i] = i

# x = []
# y = []
# z = []

# for i in range(1, n+1):
#   data = list(map(int,input().split()))
#   x.append((data[0],i))
#   y.append((data[1],i))
#   z.append((data[2],i))

# x.sort()
# y.sort()
# z.sort()

# print(x)
# print(y)
# print(z)

# edges = []
# # 간선 4개 고른다
# for i in range(n-1):
#                 #여기가 거리 값            인덱스 1    인덱스 2
#   edges.append((x[i+1][0] - x[i][0],   x[i][1], x[i+1][1]))
#   edges.append((y[i+1][0] - y[i][0],   y[i][1], y[i+1][1]))
#   edges.append((z[i+1][0] - z[i][0],   z[i][1], z[i+1][1]))

# edges.sort()
# for i in edges:
#   print(i)

# result = 0
# for edge in edges:
#   cost,a,b = edge
#   if find_root(parent,a) != find_root(parent,b):
#     union(parent,a,b)
#     result += cost

# for i in edges:
#   print(i)

# 최종 순위
from collections import deque

n = int(input())
indgree = [0] * (n+1)
graph = [[False] * (n+1) for _ in range(n+1)]

data = list(map(int,input().split()))
for i in range(n):
  for j in range(i+1, n):
    graph[data[i]][data[j]] = True
    indgree[data[j]] += 1

m = int(input())
for i in range(m):
  a,b = map(int,input().split())
  if graph[a][b] == True:
    graph[a][b] = False
    graph[b][a] = True
    indgree[a] += 1
    indgree[b] -= 1
  else:
    graph[a][b] = True
    graph[b][a] = False
    indgree[a] -= 1
    indgree[b] += 1

result = []
q = deque()

for i in range(1,n+1):
  if indgree[i] == 0:
    q.append(i)

certain = True
cycle = False

for i in range(n):
  if len(q) == 0:
    cycle = True
    break
  if len(q) >= 2:
    certain = False
    break
  now = q.popleft()
  result.append(now)
  for j in range(1,n+1):
    if graph[now][j]:
      indgree[j] -= 1
      if indgree[j] == 0:
        q.append(j)

if cycle == True:
  print('IMPOSSIBLE')
elif certain == False:
  print('?')
else:
  for i in result:
    print(i,end=' ')
  print()

# 내꺼
# n = int(input())
# data = list(map(int,input().split()))
# indegree = [0] * (n+1)

# for i in range(1,n+1):
#   indegree[data[i-1]] = n-i

# result = 0
# s = int(input())
# for _ in range(s):
#   a,b = map(int,input().split())
#   if indegree[a] > indegree[b]:
#     result = 1
#   indegree[a]+=1
#   indegree[b]-=1

# order = []
# for i in range(1,n+1):
#   order.append((indegree[i],i))
# order.sort(reverse=True)

# if result != 1:
#   for i in range(1,n):
#     if order[i][0] != order[i-1][0]-1:
#       result = 2


# if result == 0:
#   for i in order:
#     print(i[1], end=' ')
# elif result == 1:
#   print('IMPOSIBLE')
# else:
#   print('?')




