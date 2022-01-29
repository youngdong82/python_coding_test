# 금광
# t = int(input())
# for i in range(t):
#   n,m = map(int,input().split())
#   array = list(map(int,input().split()))

#   dp = []
#   index = 0
#   for i in range(n):
#     dp.append(array[index:index + m])
#     index += 1

  # for y in range(1,m):
  #   for x in range(n):
  #     if x == 0:
  #       left_up = 0
  #     else:
  #       left_up = dp[x-1][y-1]
  #     if x == n-1:
  #       left_down = 0
  #     else:
  #       left_down = dp[x+1][y-1]
  #     left = dp[x][y-1]
  #     dp[x][y] = dp[x][y] + max(left_up,left,left_down)

  # result = 0
  # for i in range(n):
  #   result = max(result, dp[i][m-1])
  
  # print(result)



# 정수 삼각형
# 가장 최근
# n = int(input())
# graph = [[0] * (n+1) for _ in range(n)]

# for i in range(n):
#   data = list(map(int,input().split()))
#   for j in range(len(data)):
#     graph[i][j+1] = data[j]

# for i in range(1,n):
#   for j in range(i+2):
#       graph[i][j] = graph[i][j] + max(graph[i-1][j],graph[i-1][j-1])

# print(max(graph[n-1]))


# 버전 2
# n = int(input())
# graph = [[-1] * n for _ in range(n)]

# for i in range(n):
#     push = list(map(int, input().split()))
#     for j in range(len(push)):
#         graph[i][j] = push[j]

# # 두번째부터 밑으로 이동
# for i in range(1, n):
#     # n층의 갯수에 따라 반복
#     for j in range(i + 1):
#         if j == 0:
#             down_right = 0
#         else:
#             down_right = graph[i - 1][j - 1]
#         down = graph[i - 1][j]
#         graph[i][j] = graph[i][j] + max(down, down_right)


# print(max(graph[n - 1]))

# 퇴사 40분 컷!!
# n = int(input())
# ts = []
# ps = []
# d = [-1] * n

# for i in range(n):
#   t,p = map(int,input().split())
#   ts.append(t)
#   ps.append(p)


# for i in range(n-1,-1,-1):
#   if ts[i] > n-i:
#     d[i] = 0
#   else:
#     cost = 0
#     for j in range(1,ts[i]):
#       cost += d[i + j]
#     if cost > ps[i]:
#       d[i] = 0
#     else:
#       d[i] = ps[i]
#       for j in range(1,ts[i]):
#         d[i+j] = 0

# print(sum(d))

# # 거꾸로 간다!
# for i in range(len(graph) - 1, -1, -1):
#     # 날짜 가능해?
#     if dp[(i - 1) + graph[i][0]] != -1:
#         # 날짜만큼 플러스한것보다 크다면 오케이
#         # 현재의 날짜만큼 반복
#         # 이후 날짜들의 합 구하기
#         sum = 0
#         for j in range(1, graph[i][0]):
#             sum += dp[i + j]
#         # 현재 날짜의 보상과 이후 날짜들의 보상의 합 비교 후 큰 것 담기

#         if graph[i][1] > sum:
#             dp[i] = graph[i][1]
#             for j in range(1, graph[i][0]):
#                 dp[i + j] = 0

# result = 0
# for i in dp:
#     if i != -1:
#         result += i

# print(result)

# 병사 배치하기 실패!!ㅠ 재도전!! 이거 굉장히 생각해내기 정말 어렵다.... 쫒아가기도 어려워
# 여기서 dp의 값은 자기보다 작은것이 몇개 있어? 그 값에 +1

# n = int(input())
# array = list(map(int, input().split()))
# # 이건 그냥 편의 상 한 것
# array.reverse()

# dp = [1] * n

# for i in range(1, n):
#     for j in range(0, i):
#         if array[i] > array[j]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(dp)

# 못생긴 수
# n = int(input())
# dp = [0]* (n+1)
# dp[1] = 1


# result2 = 1
# result3 = 1
# result5 = 1
# for i in range(2, n+1):
#   min_value = min(result2 * 2, result3 * 3, result5 * 5)
#   if min_value == result2 * 2:
#     result2 += 1
#   if min_value == result3 * 3:
#     result3 += 1
#   if min_value == result5 * 5:
#     result5 += 1
#   dp[i] = min_value

# print(dp[n])


# 편집거리
# 일단 오키.....ㅠ
# 일단 구현 연습은 해봤다.
# 버전2 - 최신
# word1 = str(input())
# word2 = str(input())

# n = len(word1)
# m = len(word2)

# dp = [[10001] * (m+1) for _ in range(n+1)]
# dp[0][0] = 0

# for i in range(1,n+1):
#   for j in range(1,m+1):
#     if word1[i-1] == word2[j-1]:
#       dp[i][j] = dp[i-1][j-1]
#     insert = 10001
#     remove = 10001
#     replace = 10001
#     if j-1 >= 0:
#       insert = dp[i][j-1] + 1
#     if i-1 >= 0:
#       remove = dp[i-1][j] + 1
#       print(remove)
#     if j-1 >= 0 and i-1 >= 0:
#       replace = dp[i-1][j-1] + 1
#     dp[i][j] = min(dp[i][j],insert,remove,replace)

# for i in dp:
#   print(i)

# 버전 1
# str1 = input()
# str2 = input()

# n = len(str1)
# m = len(str2)

# dp = [[0] * (m + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     dp[i][0] = i
# for j in range(1, m + 1):
#     dp[0][j] = j

# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if str1[i - 1] == str2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1]
#         else:
#             dp[i][j] = (
#                 min(
#                     dp[i][j - 1],
#                     dp[i - 1][j],
#                     dp[i - 1][j - 1],
#                 )
#                 + 1
#             )
# print(dp[n][m])
