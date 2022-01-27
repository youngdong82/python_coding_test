# # 특정 거리의 도시 찾기
# from collections import deque

# INF = int(1e9)
# n,m,k,x = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# for i in range(m):
#   a,b = map(int,input().split())
#   graph[a].append(b)

# visited = [INF] * (n+1)

# def bfs(graph,v,visited):
#   q = deque([v])
#   count = 0
#   visited[v] = count
#   while q:
#     now = q.popleft()
#     count += 1
#     for i in graph[now]:
#       if visited[i] == INF:
#         visited[i] = count
#         q.append(i)

# bfs(graph,x,visited)

# for i in range(1,n+1):
#   if visited[i] == k:
#     print(i)
# if k not in visited:
#   print(-1)

# # 연구소
# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input().split())))
# after = [[0] * m for _ in range(n)]

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def spread_dfs(x,y):
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx <n and 0 <= ny < m:
#       if after[nx][ny] == 0:
#         after[nx][ny] = 2
#         spread_dfs(nx,ny)


# def count_safe():
#   count = 0
#   for i in range(n):
#     for j in range(m):
#       if after[i][j] == 0:
#         count += 1
#   return count


# result = 0
# def dfs(count):
#   global result
#   if count == 3:
#     for i in range(n):
#       for j in range(m):
#         after[i][j] = graph[i][j]
#     for i in range(n):
#       for j in range(m):
#         if after[i][j] == 2:
#           spread_dfs(i,j)
#     result = max(result, count_safe())
#     return
#   for i in range(n):
#     for j in range(m):
#       if graph[i][j] == 0:
#         graph[i][j] = 1
#         count += 1
#         dfs(count)
#         graph[i][j] = 0
#         count -= 1

# dfs(0)
# print(result)

# # 경쟁적 전염
# INF = int(1e9)
# n,k = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input().split())))
# s,qx,qy = map(int,input().split())

# visited = [[INF] * n for _ in range(n)]
# for i in range(n):
#   for j in range(n):
#     if graph[i][j] != 0:
#       visited[i][j] = 0


# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def spread(x,y,num,sec):
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx < n and 0 <= ny < n:
#       if graph[nx][ny] == 0:
#         graph[nx][ny] = num
#         visited[nx][ny] = sec

# for sec in range(1,s+1):

#   for num in range(1,k+1):  
#     for i in range(n):
#       for j in range(n):
#         if graph[i][j] == num and visited[i][j] == (sec-1):
#           spread(i,j,num,sec)


# if graph[qx-1][qy-1] == 0:
#   print(0)
# else:
#   print(graph[qx-1][qy-1])

# # 괄호변환
# data = str(input())

# def balanced_index(data):
#   count = 0
#   for i in range (len(data)):
#     if data[i] == '(':
#       count += 1
#     else:
#       count -= 1
#     if count == 0:
#       return i

# def is_right(data):
#   count = 0
#   for i in data:
#     if i == '(':
#       count += 1
#     else:
#       if count == 0:
#         return False
#       count -= 1
#   return True

# def routin(data):
#   answer = ''
#   if data == '':
#     return answer
#   index = balanced_index(data)
#   u = data[0:index+1]
#   v = data[index+1:]

#   if is_right(u) == True:
#     answer = u + routin(v)
#   else:
#     answer = '('
#     answer += routin(v)
#     answer += ')'
#     u = list(u[1:-1])
#     for i in range(len(u)):
#       if u[i] == '(':
#         u[i] = ')'
#       else:
#         u[i] = '('
#     answer += ''.join(u)
#   return answer

# print(routin(data))

# # 연산자 끼워넣기
# INF = int(1e9)
# n = int(input())
# array = list(map(int,input().split()))
# add,sub,mul,div = map(int,input().split())

# min_value = INF
# max_value = -INF

# def dfs(i, now):
#   global add,sub,mul,div,min_value,max_value

#   if i == n:
#     min_value = min(min_value, now)
#     max_value = max(max_value, now)
#   else:
#     if add > 0:
#       add -= 1
#       dfs(i+1,now + array[i])
#       add += 1
#     if sub > 0:
#       sub -= 1
#       dfs(i+1, now - array[i])
#       sub += 1
#     if mul > 0:
#       mul -= 1
#       dfs(i+1, now * array[i])
#       mul += 1
#     if div > 0:
#       div -= 1
#       dfs(i+1, int(now / array[i]))
#       div += 1

# dfs(1,array[0])

# print(max_value)
# print(min_value)

# ----220126
# 감시 피하기
# n = int(input())
# graph = []
# for i in range(n):
#   graph.append(list(input().split()))

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def check(x,y):
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx < n and 0<= ny < n and graph[nx][ny] != 'o':
#       if graph[nx][ny] == 's':
#         return True
#       if graph[nx][ny] == 'x':
#         while 1 <= nx < n-1 and 1<= ny < n-1 and graph[nx][ny] != 'o':
#           nx += dx[i]
#           ny += dy[i]
#           if graph[nx][ny] == 's':
#             return True
#   return False

# result = False

# def dfs(count):
#   global result
#   if count == 3:
#     for i in range(n):
#       for j in range(n):
#         if graph[i][j] == 't':
#           if check(i,j):
#             return
#     result = True
#     return
            
#   for i in range(n):
#     for j in range(n):
#       if graph[i][j] == 'x':
#         graph[i][j] = 'o'
#         count += 1
#         dfs(count)
#         graph[i][j] = 'x'
#         count -= 1

# dfs(0)
# print(result)

# 인구이동
# dfs 느낌
# n,l,r = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input().split())))

# visited = [[False] * n for _ in range(n)]

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]


# def find_unite(x,y):
#   if (x,y) in united:
#     return
#   united.append((x,y))
#   visited[x][y] = True
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx < n and 0<= ny < n:
#       diff = abs(graph[x][y] - graph[nx][ny])
#       if l <= diff <= r:
#         find_unite(nx,ny)
#   return

# def allocate(united):
#   sum = 0
#   for i in united:
#     x,y = i
#     sum += graph[x][y]
#   for i in united:
#     x,y = i
#     if int(sum/len(united)) != graph[x][y]:
#       graph[x][y] = int(sum/len(united))
#     else:
#       return True
  

# result = 0

# while True:
#   count = 0
#   for i in range(n):
#     for j in range(n):
#       if visited[i][j] == False:
#         united = []
#         find_unite(i,j)
#         if united != [(i,j)]:
#           count += 1
#           allocate(united)
#         else:
#           count +=1
#   if count == n*n:
#     break
#   else:
#     result += 1
    
#   for i in range(n):
#     for j in range(n):
#       visited[i][j] = False
      

# print(result)

# --나동빈 버젼
# from collections import deque

# n,l,r = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input().split())))

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]


# def find_unite(x,y, index):
#   united = []
#   united.append((x,y))
#   q = deque()
#   q.append((x,y))
#   union[x][y] = index
#   summ = graph[x][y]
#   while q:
#     x,y = q.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0 <= nx < n and 0<= ny < n and union[nx][ny] == -1:
#         diff = abs(graph[x][y] - graph[nx][ny])
#         if l <= diff <= r:
#           q.append((nx,ny))
#           union[nx][ny] = index
#           summ += graph[nx][ny]
#           united.append((nx,ny))
#   for i, j in united:
#     graph[i][j] = summ//len(united)
#   print(united)
#   return 

# result = 0

# while True:
#   union = [[-1] * n for _ in range(n)]
#   index = 0
#   for i in range(n):
#     for j in range(n):
#       if union[i][j] == -1:
#         find_unite(i,j,index)
#         index += 1
#   if index == n*n:
#     break
#   result += 1

# print(result)

# 블록 이동하기
from collections import deque

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))

new_graph = [[1] * (n+2) for _ in range(n+2)]
for i in range(n):
  for j in range(n):
    new_graph[i+1][j+1] = graph[i][j]

visited = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def move(now, graph):
  can_go = []
  (x1,y1),(x2,y2) = now
  for i in range(4):
    nx1 = x1 + dx[i]
    ny1 = y1 + dy[i]
    nx2 = x2 + dx[i]
    ny2 = y2 + dy[i]
    if graph[nx1][ny1] == 0 and graph[nx2][ny2] == 0:
      new_now = {(nx1,ny1),(nx2,ny2)}
      can_go.append(new_now)
  if x1 == x2:
    for i in [-1,1]:
      if graph[x1 + i][y1] == 0 and graph[x2 + i][y2] == 0:
        can_go.append({(x1,y1),(x1 + i, y1)})
        can_go.append({(x2,y2),(x2 + i, y2)})
  elif y1 == y2:
    for i in [-1,1]:
      if graph[x1][y1 + i] == 0 and graph[x2][y2 + i] == 0:
        can_go.append({(x1,y1),(x1,y1 + i)})
        can_go.append({(x2,y2),(x2,y2 + i)})
  return can_go


def bfs():
  noww = {(1,1),(1,2)}
  q = deque()
  q.append((noww,0))
  visited.append(noww)
  while q:
    noww,cost = q.popleft()
    if (n,n) in noww:
      return cost
    for new_noww in move(noww, new_graph):
      if new_noww not in visited:
        q.append((new_noww, cost + 1))
        visited.append(new_noww)
  return 0


print(bfs())
