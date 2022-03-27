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

# -------------------------------------------------------------------------------- 7. 7569 번 
# ------------------------------------------- 내꺼

# -------------------------------------------------------------------------------- 8. 1697 번 
# k가 n보다 더 클 수도 있다.
# k와 n이 둘 다 0일수도 있다.
# ------------------------------------------- 내꺼 20분 컷!
# from collections import deque
# import sys

# INF = int(1e9)
# input = sys.stdin.readline
# n,k = map(int,input().split())
# if n == 0 and k == 0:
#   print(0)
# else:
#   big_one = max(n,k)
#   visited = [INF] * (big_one*2)

#   def bfs(start):
#     q = deque([start])
#     visited[start] = 0
#     while q:
#       now_x = q.popleft()
#       for i in range(3):
#         if i == 0:
#           nx = now_x + 1
#         elif i == 1:
#           nx = now_x - 1
#         elif i == 2:
#           nx = now_x * 2
#         if 0 <= nx < big_one*2:
#           if visited[nx] > visited[now_x]+1:
#             visited[nx] = visited[now_x]+1
#             q.append(nx)
#   bfs(n)
#   print(visited[k])

# -------------------------------------------------------------------------------- 9. 2206 번 
# 완전탐색은 불가능해
# bottleneck을 찾고 개선점을 찾자.
# 굳이 벽을 하나하나 다 부숴봐야하는가?

# ------------------------------------------- 내꺼 시간초과
# from collections import deque
# from copy import deepcopy
# import sys

# input = sys.stdin.readline
# INF = int(1e9)


# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input().strip())))

# walls = []
# for i in range(n):
#   for j in range(m):
#     if graph[i][j] == 1:
#       walls.append((i,j))

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def bfs(graph,x,y):
#   q = deque([(x,y)])
#   graph[x][y] = 1
#   while q:
#     now_x, now_y = q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0<= nx < n and 0<= ny < m:
#         if graph[nx][ny] == 0:
#           graph[nx][ny] = graph[now_x][now_y] + 1
#           q.append((nx,ny))

# answer = INF
# for i in walls:
#   graph_c = deepcopy(graph)
#   wall_x,wall_y = i
#   graph_c[wall_x][wall_y] = 0
#   bfs(graph_c, 0,0)

#   final = graph_c[n-1][m-1]
#   if final != 0 and final < answer:
#     answer = final

# if answer == INF:
#   print(-1)
# else:
#   print(answer)

# ------------------------------------------- 커뮤니티
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0] * 2 for i in range(m)] for i in range(n)]
for i in visited:
  print(i)
print()

def bfs(graph,x,y,visited):
  q = deque()
  q.append([x, y, 1])
  visited[x][y][1] = 1

  while q:
    now_x, now_y, w = q.popleft()
    print(now_x,now_y,w)
    if now_x == n - 1 and now_y == m - 1:
      return visited[now_x][now_y][w]
    for i in range(4):
      nx = now_x + dx[i]
      ny = now_y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 1 and w == 1:
          visited[nx][ny][0] = visited[now_x][now_y][1] + 1
          q.append([nx, ny, 0])
        elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
          visited[nx][ny][w] = visited[now_x][now_y][w] + 1
          q.append([nx, ny, w])

  return -1


print(bfs(graph,0,0,visited))
for i in visited:
  print(i)
print()


# -------------------------------------------------------------------------------- 9. 7562 번 
# ------------------------------------------- 내꺼
# -------------------------------------------------------------------------------- 9. 1707 번 
# ------------------------------------------- 내꺼


