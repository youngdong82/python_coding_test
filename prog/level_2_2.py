# -------------------------------------------------------------------------------- 백트랙킹
# https://chanhuiseok.github.io/posts/algo-23/

# -------------------------------------------------------------------------------- 1. 다음 큰 숫자 - 복습!
#  2진수로 변환했을 때 1의 갯수가 같다
# 조건 1, 2를 만족하는 수 중 가장 작은 수
# ------------------------------------------- 내꺼 35분 컷! 너무 수학적으로 풀려고 하지 말자!
# def solution(n):
#   b_n = bin(n)[2:]
#   n1 = b_n.count('1')
#   next = 0
#   while True:
#     n += 1
#     aa = bin(n)[2:]
#     if aa.count('1') == n1:
#       next = n
#       break
#   return next

# print(solution(78))
# print(solution(15))

# -------------------------------------------------------------------------------- 2. 피로도
# ------------------------------------------- 내꺼 14분 컷!!
# from itertools import combinations, permutations

# def solution(k, dungeons):
#   candidates = list(permutations(dungeons, len(dungeons)))
  
#   max_count = 0
#   for candidate in candidates:
#     fatigue = k
#     count = 0
#     for dun in candidate:
#       if fatigue < dun[0]:
#         break
#       else:
#         fatigue -= dun[1]
#         count += 1
#     max_count = max(max_count, count)
      
#   return max_count

# ------------------------------------------- 커뮤니티 뭔가 재귀 dfs하면서 최대값 설정하는 것이 좋아보임.
# answer = 0
# N = 0
# visited = []

# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt
#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0

# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer


# print(solution(80, [[80,20],[50,40],[30,10]]))




# -------------------------------------------------------------------------------- 1. 
# ------------------------------------------- 내꺼 