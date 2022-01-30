# # 사이클 판별
# def find(parent,x):
#   if parent[x] != x:
#     parent[x] = find(parent,parent[x])
#   return parent[x]

# def union(parent,x,y):
#   a = find(parent,x)
#   b = find(parent,y)
#   if a < b:
#     parent[y] = a
#   else:
#     parent[x] = b

# n,m = map(int,input().split())

# parent = [0] * (n+1)

# for i in range(1, n+1):
#   parent[i] = i

# cycle = False

# for i in range(m):
#   x,y = map(int,input().split())
#   if find(parent,x) == find(parent,y):
#     cycle = True
#     break
#   else:
#     union(parent,x,y)

# print(cycle)

# 크루스칼 알고리즘
# n,m = map(int,input().split())
# parent = [0] * (n+1)

# for i in range(1, n+1):
#   parent[i] = i

# edges = []
# for _ in range(m):
#   a,b,cost = map(int,input().split())
#   edges.append((cost,a,b))
# edges.sort()

# def find_root(parent,x):
#   if parent[x] != x:
#     parent[x] = find_root(parent,parent[x])
#   return parent[x]

# def union(parent, x, y):
#   a = find_root(parent,x)
#   b = find_root(parent,y)
#   if a < b:
#     parent[y] = a
#   else:
#     parent[x] = b
  
# result = 0
# for edge in edges:
#   cost,a,b = edge
#   if find_root(parent,a) != find_root(parent,b):
#     union(a,b)
#     result += cost

# print(result)




# # 위상 정렬
# from collections import deque

# n,m = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# indegree = [0] * (n+1)

# for _ in range(m):
#   a,b = map(int,input().split())
#   graph[a].append(b)
#   indegree[b] += 1

# def topology():
#   result = []
#   q = deque()
#   for i in range(1,n+1):
#     if indegree[i] == 0:
#       q.append(i)
#   while q:
#     now = q.popleft()
#     result.append(now)
#     for i in graph[now]:
#       indegree[i] -= 1
#       if indegree[i] == 0:
#         q.append(i)
#   for i in result:
#     print(i, end=' ')

