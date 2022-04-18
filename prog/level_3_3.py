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

# -------------------------------------------------------------------------------- 3. 멀리뛰기
# 점화식 알아내는 문제
# n은 1 이상, 2000 이하
# 가장 갯수가 많을 때 = 1칸씩만 가기
# 가장 갯수가 적을 때 = 짝) 2칸 계속 가기, 홀) 2칸 계속가고 마지막 1칸 가기

# 1/10     총 10개 10-0 **0 = 1
# -----여기까지하고 +1
# 1/8, 2/1 총 9개 9-1 **1 = 8 + 1
# 1/6, 2/2 총 8개 8-2 ** 2 = 36 + 1
# 1/4, 2/3 총 7개 7-3 ** 3 = 64 + 1
# 1/2, 2/4 총 6개 6-4 ** 4  = 16 + 1
#       2/5 총 5개 5-5 ** 5 = 1

# 1/4     총 4개 4-0 **0 = 1
# -----여기까지하고 +1
# 1/2, 2/1 총 3개 3-1 **1 = 2 + 1
#       2/2 총 2개 2-2 ** 2 = 0 + 1


# 1/5     총 5개 5-0 **0 = 0 + 1
# -----여기까지하고 +1
# 1/2, 2/1 총 4개 4-1 **1 = 3 + 1
# 1/1  2/2 총 5개 3-2 ** 2 = 1 + 1

# 1/3     총 3개 3-0 **0 = 0 + 1
# -----여기까지하고 +1
# 1/1, 2/1 총 2개 2-1 **1 = 1 + 1
# ------------------------------------------- 내꺼 실패!!
# def solution(n):
#   max_value = n
#   if n%2 == 0:
#     min_value = n//2
#     number_of_2 = min_value
#     answer = 1
#     for i in range(min_value, max_value):
#       answer += ((i-number_of_2) ** number_of_2)+1
#       number_of_2 -= 1
#   else:
#     min_value = (n+1)//2
#     number_of_2 = min_value-1
#     answer = 1
#     for i in range(min_value,max_value):
#       answer += ((i-number_of_2) ** number_of_2)+1
#       number_of_2 -= 1

#   return answer%1234567

# ------------------------------------------- 커뮤니티 이게 뭐여 ㅅㅂ
# 이걸 어떻게 알아내지???
# 1 1
# 2 2
# 3 3
# 4 5

# def solution(n):
#   if n<3:
#       return n
#   d=[0]*(n+1)
#   d[1]=1
#   d[2]=2
#   for i in range(3,n+1):
#       d[i]=d[i-1]+d[i-2]
#   return d[n]%1234567

# print(solution(10))
# print(solution(4))
# print(solution(3))
# print(solution(5))

# -------------------------------------------------------------------------------- 5. 풍선 터트리기
# 단 1개만 남을 때까지 계속 터트리려고 합니다.
# 번호가 더 작은 풍선을 터트리는 행위는 최대 1번만
# 최후까지 남기는 것이 가능한 풍선들의 개수를 return

# a의 길이는 1 이상 1,000,000 이하
# 각 값은 -1,000,000,000 이상 1,000,000,000 이하인 정수

# 보니까 하나하나 계산하는 건 아닌듯...?
# 점화식...?
# 자기 왼쪽에서 가장 작은수,
# 자기 오른쪽에서 가장 작은 수
# 이 둘이 자기보다 작다면 못나감
# ------------------------------------------- 내꺼 풀었는데 시간초과 당연히 시간초과
# def solution(a):
#   n = len(a)
#   answer = 0
#   for i in range(1,n-1):
#     left_min = min(a[:i])
#     right_min = min(a[i+1:])
#     if a[i] > max(left_min,right_min):
#       answer += 1

#   return n - answer

# ------------------------------------------- 커뮤
# 자신의 왼쪽 혹은 오른쪽 어느 한 쪽 방향에
# 자기보다 큰 수만 존재할 시,
# 마지막까지 남기는 것이 가능

# def solution(a):
#     result = [False for _ in range(len(a))]
#     minFront, minRear = float("inf"), float("inf")
#     for i in range(len(a)):
#         if a[i] < minFront:
#             minFront = a[i]
#             result[i] = True
#         if a[-1-i] < minRear:
#             minRear = a[-1-i]
#             result[-1-i] = True
#         print(a[i],a[-1-i])
#         print(minFront,minRear)
#         print(result)
#     return sum(result)

# print(solution([9,-1,-5]))
# print(solution([-16,27,65,-2,58,-92,-68,-71,-61,-33]))






