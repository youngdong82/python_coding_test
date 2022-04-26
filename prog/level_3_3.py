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

# -------------------------------------------------------------------------------- 6. 가장 긴 팰린드롬
# 앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬
# s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return

# s의 길이 : 2,500 이하

# 왼쪽부터 양옆을 확인하다가 
# 양옆이 팰린드롬이라면 더 키워보기
# 그 다음 확인할 때는 커진 크기로 확인하기

# 짝수일 경우도 확인해야해
# [ababbc]
# index = 1
# left = [index-p_size]
# toggle = True:
# right = [index+p_size]

# toggle = False:
# right = [index+p_size+1]

# b
# a
# b
# aa

# ------------------------------------------- 내꺼 너무 복잡하게 짠다...
# def solution(s):
#   p_size = 1
#   index = 1
#   # 짝수일때/ 홀수면 False
#   toggle = 1
#   answer_reck = [(0,-1)]

#   while True:
#     if index == len(s):
#       break
#     now = s[index]
#     left = s[index-p_size: index]

#     if toggle == 1:
#       right = s[index: index+p_size]
#     else:
#       right = s[index+1: index+p_size+1]


#     if len(left) == 0 and len(right) == 0:
#       break
#     if left == right[::-1]:
#       p_size +=1
#       answer_reck.append((p_size,toggle))
#       continue

#     if toggle == 1:
#       toggle = -toggle
#     else:
#       index += 1
#       toggle = -toggle
    
#   # print(answer_reck)
#   answer = answer_reck[-1]
#   if answer[1] == 1:
#     return (p_size-1)*2
#   else:
#     return (p_size-1)*2 + 1

# ------------------------------------------- 커뮤니티 일단 오키...
# def palindrome(s, left, right):
#     while 0 <= left and right <= len(s) and s[left] == s[right-1]:
#         left -= 1
#         right += 1
#     return s[left+1:right-1]

# def solution(s):
#     if len(s) < 2 or s == s[::-1]:
#         return len(s)
    
#     result = ""
#     # i가 기준점이다.
#     for i in range(len(s)-1):
#         # 길이 기준으로 result update
#         # 홀수 / 짝수 두가지로 진행된다.
#         result = max(result, palindrome(s, i, i+1), palindrome(s, i, i+2), key = len)
#         print(result)
    
#     return len(result)

# print(solution("aa"))
# print(solution("a"))
# print(solution("abcde"))
# print(solution("abcd"))

# print(solution("abba"))
# print(solution("abcdcba"))
# print(solution("abacde"))
# print(solution("abcba"))

# print(solution("aaaaaa")) # 6
# print(solution("aaaaa"))
# print(solution("abacdedcbaa"))
# print(solution("b")) #1
# print(solution("abbb"))


# print(solution("abcabcdcbae")) #7
# print(solution("aaaa")) #4
# print(solution("abcbaqwertrewqq")) #9
# print(solution("abcbaqwqabcba")) #13

# -------------------------------------------------------------------------------- 7. 금과 은 운반하기
#  각 도시의 트럭을 최적으로 운행했을 때, 새로운 도시를 건설하기 위해 금 a kg과 은 b kg을 전달할 수 있는 가장 빠른 시간을 구해
# 뭐 어떻게 해야하니....? 감도 안오네
# 변수 따로따로 두고
# 시간에 따라 남은 양 보면서 채우면 되나??
# 이거 뭔가 입국심사 문제랑 비슷한 느낌인데 - 비슷한거 맞음

# 시간을 기준으로 이분탐색
# 시간에 따라 각 트럭별로 최대로 움직일 수 있는 만큼 움직여
# 기준치보다 넘어가거나 부족하다면
# 시간으로 조절하면된다.
# ------------------------------------------- 커뮤니티
# def solution(a, b, g, s, w, t):
#     answer = (10**9) * (10**5) * 4
    
#     start = 0
#     end = (10**9) * (10**5) * 4
    
#     while start <= end:
#         mid = (start + end) // 2
#         gold = 0
#         silver = 0 
#         total = 0
        
#         for i in range(len(g)):
#             # 현재 정보
#             now_gold = g[i]
#             now_silver = s[i]
#             now_weight = w[i]
#             now_time = t[i]
            
#             # 주어진 시간내에서 이동할 수 있는 횟수(왕복으로 계산)
#             move_cnt = mid // (now_time * 2)
            
#             # 편도 추가
#             if mid % (now_time * 2) >= now_time:
#                 move_cnt += 1
            
#             # 총 운반할 수 있는 양이 현재 도시의 금의 양보다 
#             # 많다면 현재도시 양을 추가하고
#             if (now_gold < move_cnt * now_weight):
#               gold += now_gold 
#             # 적다면 총 운반 가능한 양을 추가
#             else:
#               gold += move_cnt * now_weight

#             # 금이랑 같다.
#             if (now_silver < move_cnt * now_weight):
#               silver += now_silver 
#             else:
#               silver += move_cnt * now_weight

#             # 전체 양(이건 왜하는거지??)
#             # 둘의 무게를 더한것이 한번에 나를 수 있는 제한보다 큰지 확인
#             if (now_gold + now_silver < move_cnt * now_weight):
#               total += now_gold + now_silver
#             else:
#               total += move_cnt * now_weight 
        
#         if gold >= a and silver >= b and total >= a + b:
#             end = mid - 1
#             answer = min(answer, mid)
#         else:
#             start = mid + 1
        
#     return answer

# print(solution(10,10,[100],[100],[7],[10]))
# print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))

# -------------------------------------------------------------------------------- 8. 거스름돈
# n은 100,000 이하의 자연수
# 화폐종류 100종류 이하
# 1,000,000,007로 나눈 나머지를 return
# 방법의 경우의 수
# 각 화폐 갯수는 무한
# dp

# 각 코인 별 최대 갯수 (n//코인)
# ------------------------------------------- 내꺼
# def solution(n, money):
#   dp = [1] + ([0] * n)
#   for coin in money:
#     for price in range(coin,n+1):
#       print(price)
#       if price >= coin:
#         dp[price] += dp[price-coin]
#     print(dp)
#   return dp[n] % 1000000007


# print(solution(5,[1,2,5]))
# print(solution(14,[1,2,5,7]))
# print(solution(4,[2,1]))

# -------------------------------------------------------------------------------- 9. 공 이동 시뮬레이션
# 열 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(0, dx))
# 열 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(1, dx))
# 행 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(2, dx))
# 행 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(3, dx)

# 움직이지 말고 그대로 더해버리기...???안돼
# n, m 가 너무큰데...
# query 20만개
# query로 네모 박스 만들기

# # ------------------------------------------- 내꺼 시간초과
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# def solution(n, m, x, y, queries):
#   answer = 0
#   for i in range(n):
#     for j in range(m):
#       if move(n,m,i,j,queries, x,y):
#         answer += 1
#   return answer

# def move(n,m,x,y,queries, tx,ty):
#   for q in queries:
#     index = q[0]
#     much = q[1]
#     nx = x + (dx[index] * much)
#     ny = y + (dy[index] * much)
#     if 0<= nx < n and 0<= ny < m:
#       x,y = nx,ny
#   if (x,y) == (tx,ty):
#     return True
#   else:
#     return False
# ------------------------------------------- 내꺼 시간초과
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solution(n, m, x, y, queries):
  box_range = make_box_range(queries)
  # x,y를 기준으로 사방으로 range 잡고
  answer = 0
  for i in range(n-box_range[0], n+ box_range[0]+1):
    for j in range(m-box_range[1], m+ box_range[1]+1):
      if move(n,m,i,j,queries, x,y):
        answer += 1
  return answer

def make_box_range(queries):
  x, y = 0,0
  answer = [(x,y)]
  for q in queries:
    index = q[0]
    much = q[1]
    nx = x + (dx[index] * much)
    ny = y + (dy[index] * much)
    answer.append((nx,ny))
    x,y = nx,ny

  max_x = 0
  max_y = 0
  min_x = int(1e9)
  min_y = int(1e9)
  for i in answer:
    max_x = max(max_x, i[0])
    min_x = min(min_x, i[0])
    max_y = max(max_y, i[1])
    min_y = min(min_y, i[1])
  return [max_x - min_x, max_y - min_y]

def move(n,m,x,y,queries, tx,ty):
  for q in queries:
    index = q[0]
    much = q[1]
    nx = x + (dx[index] * much)
    ny = y + (dy[index] * much)
    if 0<= nx < n and 0<= ny < m:
      x,y = nx,ny
  if (x,y) == (tx,ty):
    return True
  else:
    return False
  



# print(solution(2,2,0,0,[]))
print(solution(2,2,0,0,[[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2,5,0,1,[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))






# -------------------------------------------------------------------------------- 10. 줄 서는 방법
# example = [1,2,3,4]

# 4를 3!로 나누면:
# 몫 0 나머지 4
# example[몫]을 answer에 넣기 answer = [1,]
# example.remove[1]        example = [2,3,4]

# 4를 2!로 나누면
# 몫 2, 나머지 0
# =>
# 몫 1, 나머지 2
# example[몫]을 answer에 넣기 answer = [1,3,]
# example.remove(3)        example = [2,4]

# 2를 1!로 나누면:
# 몫 2, 나머지 0
# =>
# 몫 1, 나머지 1
# example[몫]을 answer에 넣기 answer = [1,3,4]
# example.remove(2)        example = [2]

# 1개 남았으면 그냥 넣기

# 나머지가 0이라면,
# 몫 -1 나머지 = 해당 수

# 5를 3!로 나누면:
# 몫 0 나머지 5
# example[몫]을 answer에 넣기 answer = [1,]
# example.remove[1]        example = [2,3,4]

# 5를 2!로 나누면
# 몫 2, 나머지 1
# example[몫]을 answer에 넣기 answer = [1,4,]
# example.remove(4)         example = [2,3]

# 1를 1!로 나누면:
# 몫 1, 나머지 0
# =>
# 몫 0, 나머지 1
# example[몫]을 answer에 넣기 answer = [1,4,2]
# example.remove(2)        example = [3]

# 1개 남았으면 그냥 넣기

# 나머지가 0이라면,
# 몫 -1 나머지 = 해당 수

# ------------------------------------------- 내꺼 시간초과
# from itertools import permutations

# def solution(n, k):
#   candidates = list(permutations(range(1,n+1),n))
#   return candidates[k-1]

# print(solution(4,4))

# ------------------------------------------- 내꺼 오예!!!
# from math import factorial


# def solution(n, k):
#   example = [i for i in range(1,n+1)]

#   answer = []
#   while n >0:
#     time, rest = divmod(k,factorial(n-1))
#     if rest == 0:
#       rest = factorial(n-1)
#       time -= 1
#     add_value = example[time]
#     answer.append(add_value)
#     example.remove(add_value)
#     k = rest
#     n -= 1

#   return answer

# print(solution(4,4))
