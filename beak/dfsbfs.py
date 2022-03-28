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
# from collections import deque

# # x = 높이
# # y = 세로
# # z = 가로
# dx = [0,0,0,0,1,-1]
# dy = [-1,0,1,0,0,0]
# dz = [0,1,0,-1,0,0]

# m,n,h = map(int,input().split())
# graph = []
# for k in range(h):
#   tmp = []
#   for j in range(n):
#     tmp.append(list(map(int,input().split())))
#   graph.append(tmp)

# def bfs(graph,x,y,z):
#   q = deque([(x,y,z)])
#   while q:
#     now_x,now_y,now_z = q.popleft()
#     for i in range(6):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       nz = now_z + dz[i]
#       if 0<= nx < h and 0<= ny < n and 0<= nz < m:
#         if graph[nx][ny][nz] == -1:
#           continue
#         elif graph[nx][ny][nz] == 0 or graph[nx][ny][nz] > graph[now_x][now_y][now_z] +1:
#           graph[nx][ny][nz] = graph[now_x][now_y][now_z] +1
#           q.append((nx,ny,nz))

# for k in range(h):
#   for j in range(n):
#     for i in range(m):
#       if graph[k][j][i] == 1:
#         bfs(graph, k,j,i)

# def find_answer(graph):
#   answer = 0
#   for k in range(h):
#     for j in range(n):
#       for i in range(m):
#         answer = max(answer,graph[k][j][i])
#         if graph[k][j][i] == 0:
#           return -1
#   return answer-1

# print(find_answer(graph))

# for k in graph:
#   for j in k:
#     print(j)
#   print()

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

# -------------------------------------------------------------------------------- 9. 2206 번 복습필수
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

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, list(input()))))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0] * 2 for i in range(m)] for i in range(n)]

def bfs(graph,x,y,visited):
  q = deque([(x, y, 1)])
  visited[x][y][1] = 1

  while q:
    now_x, now_y, w = q.popleft()
    if now_x == n - 1 and now_y == m - 1:
      return visited[now_x][now_y][w]
    for i in range(4):
      nx = now_x + dx[i]
      ny = now_y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        # w가 1이라면 벽을 부술 수 있는 상태
        if graph[nx][ny] == 1 and w == 1:
          visited[nx][ny][0] = visited[now_x][now_y][1] + 1
          q.append([nx, ny, 0])
        elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
          visited[nx][ny][w] = visited[now_x][now_y][w] + 1
          q.append([nx, ny, w])

  return -1


print(bfs(graph,0,0,visited))
# for i in visited:
#   print(i)
# print()


# -------------------------------------------------------------------------------- 9. 7562 번 
# ------------------------------------------- 내꺼 25분 컷! 뭔가 괜히 오래 끈 것 같은 느낌
# from collections import deque
# INF = int(1e9)


# test_case = int(input())

# dx = [-2,-1,1,2,2,1,-1,-2]
# dy = [1,2,2,1,-1,-2,-2,-1]


# def bfs(x,y,target_x, target_y):
#   q = deque([(x,y)])
#   if x == target_x and y == target_y:
#     return 0
#   graph[x][y] = 1
#   while q:
#     now_x,now_y = q.popleft()
#     for i in range(8):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0 <= nx < n and 0 <= ny < n:
#         if graph[nx][ny] > graph[now_x][now_y]+1:
#           graph[nx][ny] = graph[now_x][now_y]+1
#           if nx == target_x and ny == target_y:
#             return graph[nx][ny]-1
#           q.append((nx,ny))


# for _ in range(test_case):
#   n = int(input())
#   x,y = map(int,input().split())
#   target_x,target_y = map(int,input().split())
#   graph = [[INF] * n for _ in range(n)]
#   answer = bfs(x,y,target_x,target_y)
#   print(answer)

# -------------------------------------------------------------------------------- 9. 1707 번 복습
# 음수를 이용해서 무방향 그래프에서 그룹을 확인한다.
# 같은 길로 왔다 가는 것은 -1 => 1 => -1 이기 때문에 문제가 되지 않는다.
# 다른 길로 특정 노드에 도착했는데, 이미 도착해 있으며, -1 => -1이거나 1 => 1이라면
# 끝
# ------------------------------------------- 내꺼 
# 사이클이 존재하면 No
# from collections import deque
# import sys
# input = sys.stdin.readline

# k = int(input())

# def bfs(start, group):
#   q = deque([start])
#   visited[start] = group
#   while q:
#     now = q.popleft()
#     for i in graph[now]:
#       if visited[i] == False:
#         visited[i] = -1 * visited[now]
#         q.append(i)
#       elif visited[i] == visited[now]:
#         return False
#   return True

# for _ in range(k):
#   v,e = map(int,input().split())
#   graph = [[] for _ in range(v+1)]
#   visited = [False] * (v+1)

#   for i in range(e):
#     v_1,v_2 = map(int,input().split())
#     graph[v_1].append(v_2)
#     graph[v_2].append(v_1)

#   for i in range(1,v+1):
#     if visited[i] == False:
#       result = bfs(i,1)
#       if result == False:
#         break
#   if result:
#     print('YES')
#   else:
#     print('NO')


