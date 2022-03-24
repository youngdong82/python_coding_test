# -------------------------------------------------------------------------------- 1. 1260번
# ------------------------------------------- 내꺼
# from collections import deque


# def bfs(start):
#   q = deque([start])
#   visited_b[start] = True
#   while q:
#     now = q.popleft()
#     print(now, end=' ')
#     for i in graph[now]:
#       if visited_b[i] != True:
#         visited_b[i] = True
#         q.append(i)

# def dfs(start):
#   visited_d[start] = True
#   print(start,end = ' ')
#   for i in graph[start]:
#     if visited_d[i] == False:
#       dfs(i)
  
# n,m,v = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# visited_d = [False] * (n+1)
# visited_b = [False] * (n+1)

# for i in range(m):
#   a,b = map(int,input().split())
#   graph[a].append(b)

# dfs(1)
# print()
# bfs(1)

# -------------------------------------------------------------------------------- 2. 2606번
# ------------------------------------------- 내꺼
# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#   a,b = map(int,input().split())
#   graph[a].append(b)

# answer = []
# def dfs(graph, start, visited):
#   visited[start] = True
#   answer.append(start)
#   for i in graph[start]:
#     if visited[i] == False:
#       dfs(graph, i, visited)

# dfs(graph, 1, visited)
  
  
# print(len(answer)-1)

# -------------------------------------------------------------------------------- 3. 2667번
# ------------------------------------------- 내꺼
# from collections import deque


# n = int(input())

# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# count = 1   
# def bfs(x,y):
#     global count
#     if graph[x][y] != 1:
#         return
#     else:
#         count += 1
#     answer_c = 0
#     q = deque([(x,y)])
#     graph[x][y] = count
#     while q:
#         now_x,now_y = q.popleft()
#         answer_c += 1
#         for i in range(4):
#             nx = now_x + dx[i]
#             ny = now_y + dy[i]
#             if 0 <= nx < n and 0<= ny < n:
#                 if graph[nx][ny] == 1:
#                     graph[nx][ny] = count
#                     q.append((nx,ny))
#     return answer_c

# answer = []             

# for i in range(n):
#     for j in range(n):
#         a = bfs(i,j)
#         if a != None:
#           answer.append(a)

# print(len(answer))
# for i in answer:
#   print(i)

# -------------------------------------------------------------------------------- 4. 1012번
# ------------------------------------------- 내꺼
# from collections import deque


# test_n = int(input())

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# def bfs(x,y):
#   q = deque([(x,y)])
#   graph[x][y] = 0
#   while q:
#     now_x, now_y = q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0 <= nx < n and 0 <= ny < m:
#         if graph[nx][ny] == 1:
#           graph[nx][ny] = 0
#           q.append((nx,ny))


# for _ in range(test_n):
#   m,n,k = map(int,input().split())
#   graph = [[0] * m for _ in range(n)]
#   for i in range(k):
#     y,x = map(int,input().split())
#     graph[x][y] = 1
  
#   count = 0
#   for i in range(n):
#     for j in range(m):
#       if graph[i][j] == 1:
#         bfs(i,j)
#         count += 1
  
#   print(count)

# -------------------------------------------------------------------------------- 5. 2178번 
# ------------------------------------------- 내꺼 15분 컷!
# from collections import deque


# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input())))

# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# def bfs(x,y):
#   q = deque([(x,y)])
#   graph[x][y] = 2
#   while q:
#     now_x, now_y = q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0 <= nx < n and 0 <= ny < m:
#         if graph[nx][ny] == 1:
#           graph[nx][ny] = graph[now_x][now_y] + 1
#           q.append((nx,ny))

# bfs(0,0)

# print(graph[n-1][m-1]-1)
# -------------------------------------------------------------------------------- 6. 7576번 
# ------------------------------------------- 내꺼
# from collections import deque


# n,m = map(int,input().split())
# graph = []
# for i in range(m):
#   graph.append(list(map(int,input().split())))

# q = deque([])
# for i in range(m):
#   for j in range(n):
#     if graph[i][j] == 1:
#       q.append((i,j))

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# while q:
#   now_x, now_y = q.popleft()
#   for i in range(4):
#     nx = now_x + dx[i]
#     ny = now_y + dy[i]
#     if 0 <= nx < m and 0 <= ny < n:
#       if graph[nx][ny] == 0:
#         graph[nx][ny] = graph[now_x][now_y]+1
#         q.append((nx,ny))

# answer = 0
# toggle = False
# for i in range(m):
#   for j in range(n):
#     if graph[i][j] > 0 and toggle == False:
#       answer = max(answer, graph[i][j])
#     elif graph[i][j] == 0:
#       toggle = True

# if toggle:
#   print(-1)
# else:
#   print(answer-1)




# -------------------------------------------------------------------------------- 7. 2178번 
# ------------------------------------------- 내꺼
# -------------------------------------------------------------------------------- 8. 2178번 
# ------------------------------------------- 내꺼
# -------------------------------------------------------------------------------- 9. 2178번 
# ------------------------------------------- 내꺼

