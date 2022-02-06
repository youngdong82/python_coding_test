#아기 상어
# 
#  from collections import deque

# INF = int(1e9)
# n = int(input())
# graph = []
# for _ in range(n):
#   graph.append(list(map(int,input().split())))

# now_x,now_y = 0,0
# scale = 2

# # 아기상어 위치 찾기
# for i in range(n):
#   for j in range(n):
#     if graph[i][j] == 9:
#       now_x, now_y = i,j
#       graph[now_x][now_y] = 0

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def bfs():
#   dist = [[-1] * n for _ in range(n)]
#   q = deque([(now_x,now_y)])
#   dist[now_x][now_y] = 0
#   while q:
#     x,y = q.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0 <= nx < n and 0 <= ny < n:
#         if dist[nx][ny] == -1 and graph[nx][ny] <= scale:
#           dist[nx][ny] = dist[x][y] + 1
#           q.append((nx,ny))
#   return dist


# def find(dist):
#   x,y = 0,0
#   min_dist = INF
#   for i in range(n):
#     for j in range(n):
#       if dist[i][j] != -1 and 1 <= graph[i][j] < scale:
#         if dist[i][j] < min_dist:
#           x,y = i,j
#           min_dist = dist[i][j]
#   if min_dist == INF:
#     return None
#   else:
#     return x,y,min_dist

# eat_count = 0
# time = 0

# while True:
#   dist = bfs()
#   for i in dist:
#     print(i, end=' ')
#     print()
#   print(eat_count,scale)
#   value = find(dist)
#   if value == None:
#     print(time)
#     break
#   else:
#     now_x,now_y = value[0],value[1]
#     time += value[2]
#     graph[now_x][now_y] = 0
#     eat_count += 1
#     if eat_count >= scale:
#       scale += 1
#       eat_count = 0

# 청소년 상어
# 물고기의 각기 다른 번호(1-16)와 8가지 방향이 있다.

# 물고기 사이클
# 번호 순서 대로 물고기가 이동,
# 이동이란 위치를 서로 바꾼다.
# 상어, 범위 벗어나면 못움직임.
# 방향이 이동할 수 있는 칸이 나올 때 까지 45도 반시계 방향으로 회전
# 이동할 수 있는 칸이 없으면 이동 안함

# 상어 사이클
# 현재 위치는 0,0 방향도 주어진 방향
# 방향 내에서 한번에 여러 칸 이동 가능
# 물고기가 없는 칸으로 이동할 수 없고
# 지나가는 칸에 있는 물고기는 먹지 않는다.
# 물고기를 먹은 후엔 물고기가 지녔던 방향
# 이동할 수 있는 칸이 없으면 끝

# 물고기, 상어사이클 반복
# import copy

# graph = [[None] * 4 for _ in range(4)]
# for i in range(4):
#   a = list(map(int,input().split()))
#   for j in range(4):
#     graph[i][j] = [a[j*2],a[j*2+1] -1]

# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,-1,-1,-1,0,1,1,1]

# def turn_left(direc):
#   return (direc + 1) % 8

# def find_fish(graph, order):
#   for x in range(4):
#     for y in range(4):
#       if graph[x][y][0] == order:
#         return (x,y)
#   return None

# def fish_move(graph, now_x, now_y):
#   for i in range(1,17):
#     position = find_fish(graph,i)
#     if position != None:
#       x,y = position[0],position[1]
#       direc = graph[x][y][1]
#       for _ in range(8):
#         nx = x + dx[direc]
#         ny = y + dy[direc]
#         if 0 <= nx < 4 and 0 <= ny < 4:
#           if not (nx == now_x and ny == now_y):
#             graph[x][y][1] = direc
#             graph[x][y],graph[nx][ny] = graph[nx][ny],graph[x][y]
#             break
#         direc = turn_left(direc)

# def can_eat_fish(graph, now_x, now_y):
#   fish_box = []
#   direc = graph[now_x][now_y][1]
#   for i in range(4):
#     now_x += dx[direc]
#     now_y += dy[direc]
#     if 0 <= now_x < 4 and 0 <= now_y < 4:
#       if graph[now_x][now_y][0] != -1:
#         fish_box.append((now_x,now_y))
#   return fish_box


# result = 0
# def dfs(graph,now_x, now_y, total):
#   global result
#   graph = copy.deepcopy(graph)

#   total += graph[now_x][now_y][0]
#   graph[now_x][now_y][0] = -1

#   fish_move(graph, now_x, now_y)

#   fish_box = can_eat_fish(graph,now_x,now_y)
#   if len(fish_box) == 0:
#     result = max(result,total)
#     return
#   for next_x, next_y in fish_box:
#     dfs(graph,next_x,next_y, total)

# dfs(graph,0,0,0)
# print(result)

# 어른 상어(답 봐도 모르겠다. 답 도출이 안돼)

n,m,k = map(int,input().split())
# 상어 위치 그래프
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

# m개의 상어에 대한 초기 위치 값
direc_store = list(map(int,input().split()))
scent = [[[0,0]] * n for _ in range(n)]

prioritys = [[] for _ in range(m)]
for i in range(m):
  for j in range(4):
    prioritys[i].append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


# 사이클 돌고 나서 냄새 빼주기
def update_scent():
  for i in range(n):
    for j in range(n):
      if scent[i][j][1] > 0:
        scent[i][j][1] -= 1
      if graph[i][j] != 0:
        scent[i][j] = [graph[i][j], k]

def move():
  new_graph = [[0] * n for _ in range(n)]
  for x in range(n):
    for y in range(n):
      if graph[x][y] != 0:
        direc = direc_store[graph[x][y] -1]
        found = False
        for i in range(4):
          nx = x + dx[prioritys[graph[x][y] - 1][direc - 1][i] -1]
          ny = y + dy[prioritys[graph[x][y] - 1][direc - 1][i] -1]
          if 0 <= nx < n and 0 <= ny < n:
            if scent[nx][ny][1] == 0:
              direc_store[graph[x][y] - 1] = prioritys[graph[x][y] - 1][direc - 1][i]
              if new_graph[nx][ny] == 0:
                new_graph[nx][ny] = graph[x][y]
              else:
                new_graph[nx][ny] = min(new_graph[nx][ny], graph[x][y])
              found = True
              break
        if found:
          continue
        for i in range(4):
          nx = x + dx[prioritys[graph[x][y] - 1][direc - 1][i] -1]
          ny = y + dx[prioritys[graph[x][y] - 1][direc - 1][i] -1]
          if 0 <= nx < n and 0 <= ny < n:
            if scent[nx][ny][0] == graph[x][y]:
              direc_store[graph[x][y]-1] = prioritys[graph[x][y] - 1][direc - 1][i]
              new_graph[nx][ny] = graph[x][y]
              break
  return new_graph

time = 0

while True:
  update_scent()
  new_graph = move()
  graph = new_graph
  time += 1

  check = True
  for i in range(n):
    for j in range(n):
      if graph[i][j] > 1:
        check = False

  if check:
    print(time)
    break
  if time >= 1000:
    print(-1)
    break