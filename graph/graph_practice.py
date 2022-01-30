# 팀 결성 13분컷
# n,m = map(int,input().split())
# parent = [0] * (n+1)

# for i in range(1,n+1):
#   parent[i] = i
  

# def find_root(parent, x):
#   if parent[x] != x:
#     parent[x] = find_root(parent,parent[x])
#   return parent[x]

# def union(parent,x,y):
#   a = find_root(parent,x)
#   b = find_root(parent,y)
#   if a<b:
#     parent[y] = a
#   else:
#     parent[x] = b

# def check(x,y):
#   if find_root(parent,x) == find_root(parent,y):
#     return True
#   else:
#     return False


# for _ in range(m):
#   x,a,b = map(int,input().split())
#   if x == 0:
#     union(parent,a,b)
#   else:
#     if check(a,b) == True:
#       print('YES')
#     else:
#       print('NO')

# 도시 분할 계획
def find_root(parent,x):
  if parent[x] != x:
    parent[x] = find_root(parent,parent[x])
  return parent[x]

def union(parent,a,b):
  a = find_root(parent,a)
  b = find_root(parent,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


n,m = map(int,input().split())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1,n+1):
  parent[i] = i

for _ in range(m):
  a,b,c = map(int,input().split())
  edges.append((c,a,b))

edges.sort()
max_cost = 0

for i in range(m):
  cost,a,b = edges[i]
  if find_root(parent,a) != find_root(parent,b):
    union(parent,a,b)
    result += cost
    max_cost = cost

print(result-max_cost)


