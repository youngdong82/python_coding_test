# 완전 탐색
# --------------------------------------------------- 블랙잭 15분 컷!
# from itertools import combinations

# INF = int(1e9)
# n,m = map(int,input().split())
# cards = list(map(int,input().split()))

# candidates = list(combinations(cards,3))

# min_value = INF
# for candidate in candidates:
#   if sum(candidate) >m:
#     continue

#   if m-sum(candidate) < min_value:
#     min_value = m-sum(candidate)

# print(m - min_value)

# --------------------------------------------------- 분해 합 25분 컷!!
# 문제 확인 좀 잘하자
# INF = int(1e9)
# n = int(input())

# min_value = INF
# for x in range(1,n):
#   summ = x
#   for i in str(x):
#     summ += int(i)
#   if summ == n:
#     min_value = min(min_value,x)

# if min_value == INF:
#   print(0)
# else:
#   print(min_value)

# --------------------------------------------------- 덩치 14분 컷!!
# n = int(input())

# array = []
# people = []
# for i in range(n):
#   kg,tall = map(int,input().split())
#   people.append((kg,tall))

# for i in range(n):
#   count = 1
#   for j in range(n):
#     if i == j:
#       continue
#     if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
#       count += 1
#   array.append(count)

# for i in array:
#   print(i, end=' ')

# --------------------------------------------------- 체스판 다시 칠하기 와우 너무 기뻐!!! 33분 컷!!! 대견하다!!!영동!!
# 0이 black 1이 white
# INF = int(1e9)
# n,m = map(int,input().split())
# graph = []
# for _ in range(n):
#   int_data = []
#   datas = str(input())
#   for i in datas:
#     if i == "W":
#       int_data.append(1)
#     else:
#       int_data.append(0)
#   graph.append(int_data)

# # 8x8 에서 몇개를 바꿔야하는지 확인
# def how_many_convert(x,y):
#   count = 0
#   for i in range(x,x+8):
#     for j in range(y,y+8):
#       if i%2 == 0:
#         if j%2 == 0:
#           if graph[i][j] != 0:
#             count += 1
#         else:
#           if graph[i][j] != 1:
#             count +=1
#       else:
#         if j%2 == 0:
#           if graph[i][j] != 1:
#             count +=1
#         else:
#           if graph[i][j] != 0:
#             count +=1
#   return min(count, 64-count)

# min_value = INF
# for i in range(n-7):
#   for j in range(m-7):
#     result = how_many_convert(i,j)
#     min_value = min(min_value, result)

# print(min_value)

# how_many 만들기 위한 함수
# first_black = [[0] * 8 for _ in range(8)]
# def make_chess(graph):
#   for i in range(8):
#     for j in range(8):
#       if i%2 == 0:
#         if j%2 == 0:
#           graph[i][j] = 0
#         else:
#           graph[i][j] = 1
#       else:
#         if j%2 == 0:
#           graph[i][j] = 1
#         else:
#           graph[i][j] = 0
#   return graph

# first_black = make_chess(first_black)

# --------------------------------------------------- 영화감독 숌 28분 컷!
# n = int(input())

# count = 1
# start = 666

# while True:
#   if count == n:
#     print(start)
#     break
#   start += 1
#   if '666' in str(start):
#     count += 1
