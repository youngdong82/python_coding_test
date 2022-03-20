# -------------------------------------------------------------------------------- 4. 땅따먹기 - 복습!!!!
# 같은 열을 연속해서 밟을 수 없는 특수 규칙
# 다이나믹
# 개미 곶간 터는 문제랑 비슷해
# 지금 이걸 밟는 것이 다음꺼와 함께 생각했을 때 이득인가?
# 의 반복
# ------------------------------------------- 커뮤
# def solution(land):

#   for i in range(1,len(land)):
#     for j in range(len(land[0])):
#       print(land[i-1][:j])
#       print(land[i-1][j+1:])
#       land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
#   return max(land[len(land)-1])


# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
# print(solution([[1,2,3,5],[5,6,7,8],[1,3,10,2],[]]))


# -------------------------------------------------------------------------------- 6. 게임 맵 최단거리
# ------------------------------------------- 내꺼 시간초과 32분 컷!
# from collections import deque

# def bfs(maps,x,y):
#   dx = [0,1,0,-1]
#   dy = [1,0,-1,0]

#   q = deque([(x,y)])
#   maps[x][y] = 2
#   while q:
#     now_x, now_y =  q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
#         if maps[nx][ny] == 1:
#           maps[nx][ny] = maps[now_x][now_y]+1
#           q.append((nx,ny))

# def solution(maps):
#   n = len(maps)
#   m = len(maps[0])
#   bfs(maps, 0,0)
#   if maps[n-1][m-1] == 1:
#     return -1
#   else:
#     return maps[n-1][m-1]-1


# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

# -------------------------------------------------------------------------------- 9. 구명보트 - 복습!!
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출
# 2명씩이 최대
# 구현도 구현이지만 
# 이걸 보고 투포인터인줄 모르는게 문제다!!!

# ------------------------------------------- 내꺼 이전꺼ㅋㅋㅋㅋ
# def solution(people, limit):
#   people.sort()
#   small_i = 0
#   big_i = len(people)-1
#   count = 0
#   while small_i <= big_i:
#     if people[small_i] + people[big_i] <= limit:
#       big_i -= 1
#       small_i += 1
#       count += 1
#     else:
#       big_i -= 1
#       count += 1

#   return count

# print(solution([20,30,50,70,100], 100))
# print(solution([20,30,70,50,80,50], 100))
# print(solution([70,50,80,50], 100))
# print(solution([70,80,50],	100))
# print(solution([20,30,50],	100))

# -------------------------------------------------------------------------------- 4. 방문길이
# ------------------------------------------- 내꺼 32분 컷!!
# ------------------------------------------- 내꺼 방향이 무방향이다!!!
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def move(x,y,d,visited,answer):
#   nx = x + dx[d]
#   ny = y + dy[d]
#   if 0 <= nx < 11 and 0 <= ny < 11:
#     if (x,y,nx,ny) not in visited:
#       visited.append((x,y,nx,ny))
#       visited.append((nx,ny,x,y))
#       answer += 1
#     return nx,ny,answer
#   return x,y,answer


# def solution(dirs):
#   visited = []
#   x = 5
#   y = 5

#   answer = 0
#   for direc in dirs:
#     if direc == 'U':
#       x,y,answer = move(x,y,0,visited,answer)
#     elif direc == 'R':
#       x,y,answer = move(x,y,1,visited,answer)
#     elif direc == 'D':
#       x,y,answer = move(x,y,2,visited,answer)
#     elif direc == 'L':
#       x,y,answer = move(x,y,3,visited,answer)

#   return answer


# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
# print(solution("L"))

# -------------------------------------------------------------------------------- 8. n^2 배열 자르기 - 실패! 그래도 복습 할 가치가 있다!
# 시키는 대로 따라하는 것이 아니라 규칙을 알아내야해!
# 아니 이걸 어떻게 알아내...?
# 몫과 나머지
# ------------------------------------------- 내꺼 시간초과
# def solution(n, left, right):
#     n = int(n)
#     answer = []
#     for i in range(n*n):
#         a = i//n
#         b = i%n 
#         print(a,b)
#         if a < b: 
#           a,b = b,a
#         answer.append(a)
#     return answer

# print(solution(3,2,5))
# print(solution(4,7,14))


# -------------------------------------------------------------------------------- 2. 예상 대진표 성공 but 시간초관
# 몇 번째 라운드에서 만나는지 return
# n은 2의 20승 이하인 자연수
# 무조건 log로 가야해
# ------------------------------------------- 내꺼 16분 컷!
# a와 b가 못만날 경우는 존재하지 않으니, n값은 따로 처리할 필요가 없다
# def solution(n,a,b):
#   count = 1
#   while n >= 2:
#     n //= 2
#     if a == b:
#       break

#     if a % 2 == 0:
#       a = a // 2
#     else:
#       a = (a+1) //2
      
#     if b % 2 == 0:
#       b = b // 2
#     else:
#       b = (b+1) //2

#     count += 1
#   return count -1

# print(solution(8,4,7))

# -------------------------------------------------------------------------------- 4. 가장 큰 정사각형 찾기 - 복습!!!
# 동적 프로그래밍 문제인지 알고 푸는 것과
# 모르고 접하는 것은 천지차이...
# 1000*1000 이하의 2차원 배열
# 1000000
# ------------------------------------------- 내꺼 전부 통과 그러나 시간초과ㅋㅋㅋㅋ  두번째도 전부통과 but 시간초과
# 작은거부터 확인.
# 네모가 나오자마자 멈추고 그 다음 확인
# 작은게 안되는데 큰게 되는 법은 없다.
# def check(board,x,y,count):
#   for i in range(x,x+count):
#     for j in range(y,y+count):
#       if i < len(board) and j < len(board[0]):
#         if board[i][j] != 1:
#           return False
#       else:
#         return False
#   return True

# def solution(board):
#   count = 1
#   for i in range(len(board)):
#     for j in range(len(board[0])):
#       while True:
#         if check(board,i,j,count):
#           count += 1
#         else:
#           break
#   return (count -1) **2

# ------------------------------------------- 커뮤 다이내믹, 이런건 어떻게 생각해내는걸까...?
# def solution(board):
#   n = len(board)
#   m = len(board[0])

#   # dp 준비
#   dp = [[0]*m for _ in range(n)]
#   dp[0] = board[0]
#   for i in range(1,n):
#     dp[i][0] = board[i][0]

#   # 2중 포문으로 연산
#   for i in range(1, n):
#     for j in range(1, m):
#       if board[i][j] == 1:
#         dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

#   # # 최대 넓이 구하기
#   answer = 0
#   for i in range(n):
#       temp = max(dp[i])
#       answer = max(answer, temp)
#   return answer**2
        

# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# print(solution([[0,0,1,1],[1,1,1,1]]))

# -------------------------------------------------------------------------------- 5. 점프와 순간이동
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EC%A0%90%ED%94%84%EC%99%80-%EC%88%9C%EA%B0%84-%EC%9D%B4%EB%8F%99
# ------------------------------------------- 내꺼 전부 통과 그러나 시간초과ㅋㅋㅋㅋ 두번째 6분 컷!
# 동적프로그래밍 인줄 알았는데...
# def solution(n):
#   move_c = 0
#   while n > 0:
#     if n % 2 == 1:
#       n -= 1
#       move_c += 1
#     else:
#       n //= 2
#   return move_c

# print(solution(5))
# print(solution(6))
# print(solution(999999999))

# -------------------------------------------------------------------------------- 8. n진수 게임 거의 40분...? 시간초과!
# 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임
# ------------------------------------------- 내꺼 뭔가 나쁘진 않다. 진수변환 정도는 아예 외우자!!!
# -------------------------------------------------------------------------------- 4. 메뉴 리뉴얼
# # ------------------------------------------- 내꺼 구현은 괜춘 그러나 시간초과
# -------------------------------------------------------------------------------- 6. [1차] 프렌즈4블록
# 돌려놓고 생각하자
# ------------------------------------------- 내꺼
# -------------------------------------------------------------------------------- 9. 순위 검색 - 시간초과!
# 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구
# info 배열의 크기는 1 이상 50,000 이하
# query 배열의 크기는 1 이상 100,000 이하
# 나눈 다음 정렬을 좀 해놓을까...?
# 그 후 이진탐색..? 맞추긴 했다ㅋㅋㅋㅋㅋㅋㅋ
# string을 index값으로 바꿔도 큰 차이는 없다. 오히려 string이 빠르다!!
# ------------------------------------------- 내꺼 - 정확도는 ok but 시간초과 
# -------------------------------------------------------------------------------- 3. 압축 1시간 컷ㅋㅋㅋ
# ------------------------------------------- 내꺼 뭔가 어거지로 만들긴 했는데 체계적이지 않다.
# -------------------------------------------------------------------------------- 8. 빛의 경로 실패!! 담에 다시 풀어보자
# ------------------------------------------- 내꺼 루프로 변경해보라고....? 못해 ㅅㅂ...



# -------------------------------------------------------------------------------- 1. k진수에서 소수 개수 구하기 진수변환이랑 소수 확인하기 복습!!
# ------------------------------------------- 내꺼