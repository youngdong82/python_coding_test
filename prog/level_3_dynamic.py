# -------------------------------------------------------------------------------- 1. 등굣길 - 다이나믹
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수
# dfs 돌리면 되는거 아님?

# ------------------------------------------- 커뮤
# dx = [-1,0]
# dy = [0,-1]

# def solution(n, m, puddles):
#   graph = [[0] * m for _ in range(n)]

#   for puddle in puddles:
#     no_x,no_y = puddle
#     graph[no_x-1][no_y-1] = -1
#   graph[0][0] = 1

#   # for i in graph:
#   #   print(i)
#   # print()

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

#   # for i in graph:
#   #   print(i)
#   return graph[n-1][m-1] % 1000000007

# print(solution(4,3,[[2, 2]]))

# -------------------------------------------------------------------------------- 2. N으로 표현
# ------------------------------------------- 커뮤
# def solution(N, number):
#   answer = -1
#   dp = []
#   for i in range (1,9) : 
#     # i = N의 개수
#     all_case = set()
#     check_number = int(str(N)* i)
#     all_case.add(check_number)
    
#     for j in range(0,i-1):
#     # //j 개를 사용해서 만든 값들
#       for op1 in dp[j]:
#         for op2 in dp[-j-1] :
#           all_case.add(op1 - op2)
#           all_case.add(op1 + op2)
#           all_case.add(op1 * op2)
#           if op2 != 0:
#             all_case.add(op1 // op2)
#     print(all_case)    
#     if number in all_case:
#       answer = i
#       break
#     dp.append(all_case) 
#   return answer


# print(solution(5,12))
# print(solution(2,11))

# -------------------------------------------------------------------------------- 3. 정수 삼각형
# ------------------------------------------- 커뮤
# def solution(triangle):
#   for i in range(1,len(triangle)):
#     for j in range(len(triangle[i])):
#       if (j-1)>=0 and len(triangle[i-1]) > j:
#         triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
#       elif len(triangle[i-1]) == j:
#         triangle[i][j] += triangle[i-1][j-1]
#       else:
#         triangle[i][j] += triangle[i-1][j]
#   return max(triangle[-1])

# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# -------------------------------------------------------------------------------- 3. 섬 연결하기
# ------------------------------------------- 커뮤







# -------------------------------------------------------------------------------- 7. 보석 쇼핑
# ------------------------------------------- 내꺼
# def solution(gems):
#   gem_reck = len(set(gems))

#   shortest = len(gems)+1
#   left = 0
#   right = 0
#   contained = {}
#   answer = []

#   while right < len(gems):
#     if gems[right] not in contained:
#       contained[gems[right]] = 1
#     else:
#       contained[gems[right]] += 1
#     right += 1
#     # 다 포함하고 있는 애들 중에서, 
#     if len(contained) == gem_reck:
#       while left < right:
#         if contained[gems[left]] > 1:
#           contained[gems[left]] -= 1
#           left +=1
#         elif shortest > right - left:
#           shortest = right - left
#           answer = [left+1, right]
#           break
#         else:
#           break
#   return answer


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

# print(solution(["A","A","A","B","B"]))
# print(solution(["A"]))
# print(solution(["A","B","B","B","B","B","B","C","B","A"] ))
# print(solution(["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"] ))

# print(solution(["A", "B", "C", "B", "A"] ))
# print(solution(['A','B','B','C','B','A','B','B','B','C']))

# -------------------------------------------------------------------------------- 8. 외벽 점검
# ------------------------------------------- 내꺼
# from itertools import permutations


# def solution(n, weak, dist):
#   length = len(weak)
#   for i in range(length):
#     weak.append(weak[i] + n)

#   answer = len(dist) + 1

#   for start in range(length):
#     print(start)
#     for friends in list(permutations(dist, len(dist))):
#       count = 1
#       # 시작 포인트
#       position = weak[start] + friends[count - 1]
#       for index in range(start, start + length):
#         if position < weak[index]:
#           count += 1
#           if count > len(dist):
#             break
#           position = weak[index] + friends[count - 1]
#       answer = min(answer, count)

#   if answer > len(dist):
#     return -1
#   else:
#     return answer
    

# print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
# print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))


