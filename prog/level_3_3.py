# -------------------------------------------------------------------------------- 1. 등굣길
# 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return
# 최단경로의 갯수????
# ------------------------------------------- 내꺼 시간초과
# def solution(n, m, puddles):
#   m = int(m)
#   n = int(n)
#   graph = [[0] * m for _ in range(n)]
#   for puddle in puddles:
#     no_x,no_y = puddle
#     graph[no_x-1][no_y-1] = -1

#   dfs(graph,0,0)

#   return graph[n-1][m-1]
  
# def dfs(graph,x,y):
#   if x == len(graph) and y == len(graph[0]):
#     count += 1
#   if x+1 < len(graph):
#     if graph[x+1][y] !=- 1:
#       graph[x+1][y] += 1
#       dfs(graph,x+1,y)
  
#   if y+1 < len(graph[0]):
#     if graph[x][y+1] !=-1:
#       graph[x][y+1] += 1
#       dfs(graph,x,y+1)

# ------------------------------------------- 내꺼 16분 컷!!
# dp를 사용해보자
# dx = [-1,0]
# dy = [0,-1]

# def solution(n, m, puddles):
#   graph = [[0] * m for _ in range(n)]

#   for puddle in puddles:
#     no_x,no_y = puddle
#     graph[no_x-1][no_y-1] = -1
#   graph[0][0] = 1


#   for i in range(n):
#     for j in range(m):
#       if graph[i][j] != -1:
#         tmp = 0
#         for k in range(2):
#           nx = i + dx[k]
#           ny = j + dy[k]
#           if 0 <= nx < n and 0<= ny < m:
#             if graph[nx][ny] != -1:
#               tmp += graph[nx][ny]
#         graph[i][j] += tmp

#   return graph[n-1][m-1] % 1000000007


# print(solution(4,3,[[2,2]]))

# -------------------------------------------------------------------------------- 2. 가장 먼 노드 
# ------------------------------------------- 내꺼 27분 컷!
# from collections import deque


# def solution(n, edge):
#   graph = [[] for _ in range(n+1)]
#   dp = [0] * (n+1)
#   visited = [False] * (n+1)

#   for i in edge:
#     start, end = i
#     graph[start].append(end)
#     graph[end].append(start)
  
#   bfs(dp,graph,1,visited)

#   return dp.count(max(dp))


# def bfs(dp,graph,start,visited):
#   visited[start] = True
#   dp[start] = 1
#   q = deque([start])
#   while q:
#     now = q.popleft()
#     for i in graph[now]:
#       if visited[i] == False:
#         visited[i] = True
#         dp[i] = dp[now] + 1
#         q.append(i)


# print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

# -------------------------------------------------------------------------------- 2. 순위 복습;;;
# ------------------------------------------- 내꺼
# def solution(n, results):
#   chart = [[0] * n for _ in range(n)]
#   WIN, LOSE = 1, -1

#   for i, j in results: # 내입장 wind = 상대방 lose
#     chart[i-1][j-1] = WIN
#     chart[j-1][i-1] = LOSE

#   for i in chart:
#     print(i)
#   print()

#   for me in range(n):
#     wins = []
#     for opp, rst in enumerate(chart[me]):
#       if rst == WIN:
#         wins.append(opp)
#     while wins:
#       loser = wins.pop()
#       for opp, rst in enumerate(chart[loser]):
#         if rst == WIN and chart[me][opp] == 0:
#           chart[me][opp] = WIN
#           chart[opp][me] = LOSE
#           wins.append(opp)

#   for i in chart:
#     print(i)

#   answer = []
#   for x in chart:
#     if x.count(0) == 1:
#       answer.append('know')

#   return len(answer)

# print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(5,[[1,2], [2,3], [3,4], [4,5]]))
