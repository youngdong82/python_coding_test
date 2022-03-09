# -------------------------------------------------------------------------------- level 2 느끼는 점
# level 1의 대부분이 너 이거 사용할 줄 알아? 였다면
# level 2는 너 이거 어떤 유형 문제인줄 알아? + 규칙을 찾아낼 수 있어? 느낌...

# 확실히 어떤 유형 문제인줄 알고, 규칙을 찾아낼 수 있다면 코드 자체는 매우 간단했다.
# -------------------------------------------------------------------------------- enumerate
# -------------------------------------------------------------------------------- round 함수
# round함수는 반올림해주는데
# 1.5는 2가 나오지만
# 0.5는 1이 아닌 0이 나온다....? 왜지???


# -------------------------------------------------------------------------------- 1. 행렬 테두리 회전하기
# 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의
# 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 
# ------------------------------------------- 내꺼
# 접근법은 같으나 커뮤니티 배울 필요가 있다.
# ------------------------------------------- 커뮤니티
# 여기서 small은 답을 윈한 것이지, 회전에 필요한 것은 아니다.
# def solution(rows, columns, queries):
#     answer = []
#     table = []
#     for r in range(rows):
#         table.append([a for a in range(r*columns+1, (r+1)*columns+1)])

#     for query in queries:
#         query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
#         tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
#         small = tmp

#         # left bottom to top
#         for i in range(query[0]+1, query[2]+1):
#             table[i-1][query[1]] = table[i][query[1]]
#             small = min(small, table[i][query[1]])
#         # bottom right to left
#         for i in range(query[1]+1, query[3]+1):
#             table[query[2]][i-1] = table[query[2]][i]
#             small = min(small, table[query[2]][i])
#         # right
#         for i in range(query[2]-1, query[0]-1, -1):
#             table[i+1][query[3]] = table[i][query[3]]
#             small = min(small, table[i][query[3]])
        
#         # top
#         for i in range(query[3]-1, query[1]-1, -1):
#             table[query[0]][i+1] = table[query[0]][i]
#             small = min(small, table[query[0]][i])
        
#         table[query[0]][query[1]+1] = tmp
#         answer.append(small)

#     return answer


# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100, 97, [[1,1,100,97]]))

# -------------------------------------------------------------------------------- 2. 예상 대진표 성공 but 시간초관
# ------------------------------------------- 내꺼 
# from math import ceil

# def solution(n,a,b):
#   play_count = 1
#   while n >2:
#     n //=2
#     play_count += 1

#   answer = 0
#   for i in range(1,play_count+1):
#     if ceil(a/2) == ceil(b/2):
#       answer = i
#       break
#     a = ceil(a/2)
#     b = ceil(b/2)
#   return answer

# # ------------------------------------------- 커뮤니티 ㅇ_ㅇ....
# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2
#         print(a,b)

#     return answer

# print(solution(16,2,9))
# print(solution(8,4,7))
# print(solution(8,2,3))
# print(solution(4,1,2))
# print(solution(2,1,2))

# -------------------------------------------------------------------------------- 3. N개의 최소공배수 11분 컷!
# ------------------------------------------- 내꺼 lcm 사용
# from math import lcm

# def solution(arr):
#   answer = arr[0]
#   for i in range(1,len(arr)):
#     answer = lcm(answer, arr[i])
#   return answer

# ------------------------------------------- 내꺼 gcd 사용
# from math import gcd

# def solution(arr):
#   answer = arr[0]
#   for i in arr:
#     answer = int((answer * i) / gcd(answer,i))
#   return answer

# print(solution([2,6,8,14]))
# print(solution([1,2,3]))

# -------------------------------------------------------------------------------- 4. 가장 큰 정사각형 찾기
# 동적 프로그래밍 문제인지 알고 푸는 것과
# 모르고 접하는 것은 천지차이...
# ------------------------------------------- 내꺼 전부 통과 그러나 시간초과ㅋㅋㅋㅋ
# def square_ok(board,x,y,count):
#   for i in range(x, x+1+count):
#     for j in range(y, y+1+count):
#       if 0 <= i < len(board) and 0 <= j < len(board[0]):
#         if board[i][j] == 0:
#           return count
#       else:
#         return count
#   return square_ok(board,x,y,count+1)

# def solution(board):
#   count = 0
#   for i in range(len(board)):
#     for j in range(len(board[0])):
#       count = square_ok(board,i,j,count)
#   return count **2

# ------------------------------------------- 커뮤니티 동적프로그래밍 이해가 되긴 한데.....에휴
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-dp
# def solution(board):
#     n = len(board)
#     m = len(board[0])

#     # dp 준비
#     dp = [[0]*m for _ in range(n)]
#     dp[0] = board[0]
#     for i in range(1,n):
#       dp[i][0] = board[i][0]

#     # 2중 포문으로 연산
#     for i in range(1, n):
#       for j in range(1, m):
#         if board[i][j] == 1:
#           dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
#     # # 최대 넓이 구하기
#     answer = 0
#     for i in range(n):
#         temp = max(dp[i])
#         answer = max(answer, temp)
    
#     return answer**2

# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# print(solution([[0,0,1,1],[1,1,1,1]]))

# -------------------------------------------------------------------------------- 5. 점프와 순간이동
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EC%A0%90%ED%94%84%EC%99%80-%EC%88%9C%EA%B0%84-%EC%9D%B4%EB%8F%99
# ------------------------------------------- 내꺼 전부 통과 그러나 시간초과ㅋㅋㅋㅋ
# 동적프로그래밍 인줄 알았는데...
# INF = int(1e9)


# def solution(n):
#   dp = [INF] * (n+1)
#   dp[1] = 1

#   for i in range(2,n+1):
#     if dp[i] == INF:
#       if i%2 == 0 and dp[i//2] != INF:
#         a = 1
#         while True:
#           if i*a > n:
#             break
#           dp[i*a] = dp[i//2]
#           if i*a == n:
#             return dp[i//2]
#           a *= 2
#       else:
#         dp[i] = dp[i-1] + 1
#   print(dp)
#   return dp[n]

# ------------------------------------------- 커뮤니티....ㅅㅂ 이게 머야
# def solution(N):
#     answer = 0
#     while N > 0:
#         answer += N % 2
#         N //= 2
#     return answer

# print(solution(1000000000))
# print(solution(1000000000))
# print(solution(5))
# print(solution(6))
# print(solution(9))
# print(solution(16))
# print(solution(5000))

# -------------------------------------------------------------------------------- 6.
# ------------------------------------------- 내꺼

# -------------------------------------------------------------------------------- 7.
# ------------------------------------------- 내꺼

# -------------------------------------------------------------------------------- 8.
# ------------------------------------------- 내꺼

# -------------------------------------------------------------------------------- 9.
# ------------------------------------------- 내꺼

# -------------------------------------------------------------------------------- 10.
# ------------------------------------------- 내꺼

