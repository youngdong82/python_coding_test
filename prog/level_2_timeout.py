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

# ------------------------------------------------------------------------------------------------ 220321
# -------------------------------------------------------------------------------- 8. n진수 게임
# 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임
# 뭔가 나쁘진 않다. 진수변환 정도는 아예 외우자!!!
# ------------------------------------------- 내꺼 첫번째 거의 40분...? 두번째 20분 컷!!
# def make(num,depend):
#   deck = '0123456789ABCDEF'
#   answer = ''
#   while num > 0:
#     time, rest = divmod(num, depend)
#     num = time
#     answer += deck[rest]
#   return answer[::-1]

# def solution(n, t, m, p):
#   result = '0'
#   number = 0
#   while number <= m*t:
#     number += 1
#     result += make(number,n)

#   answer = ''
#   for i in range(len(result)):
#     if len(answer) == t:
#       break
#     if i%m == p-1:
#       answer+=(result[i])
#   return answer


# print(solution(2,4,2,1))
# print(solution(16,16,2,1))
# print(solution(16,16,2,2))

# -------------------------------------------------------------------------------- 4. 메뉴 리뉴얼 복습!! 내꺼 시간초과 두번째 시간초과
# dic을 사용하자
# ------------------------------------------- 내꺼 + 커뮤 굉장히 빠르다...!!!
# from itertools import combinations


# def solution(orders, course):
#   answer = []
#   for i in course:
#     candidates = []
#     for order in orders:
#       candidates += combinations(sorted(order),i)

#     dic = {}
#     for candidate in candidates:
#       if candidate not in dic.keys():
#         dic[candidate] = 1
#       else:
#         dic[candidate] += 1

#     for combi, time in dic.items():
#       if time == max(dic.values()) and time >=2 :
#         answer.append(''.join(combi))

#   return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

# -------------------------------------------------------------------------------- 6. [1차] 프렌즈4블록
# 돌려놓고 생각하자
# ------------------------------------------- 내꺼


# -------------------------------------------------------------------------------- 9. 순위 검색 - 시간초과!
# 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구
# info 배열의 크기는 1 이상 50,000 이하
# query 배열의 크기는 1 이상 100,000 이하

# string을 index값으로 바꿔도 큰 차이는 없다. 오히려 string이 빠르다!!
# ------------------------------------------- 내꺼 - 정확도는 ok but 시간초과 두번째 여전히 시간초과
# def solution(infos, querys):
#   answer = []
#   for query in querys:
#     lang, posi, career, pref_score = query.split(' and ')
#     pref, score = pref_score.split(' ')
#     # print(lang, posi, career, pref, score)

#     count = 0
#     for info in infos:
#       i_lang, i_posi, i_career, i_pref, i_score = info.split(' ')

#       if lang == '-' or lang == i_lang:
#         if posi == '-' or posi == i_posi:
#           if career == '-' or career == i_career:
#             if pref == '-' or pref == i_pref:
#               if int(i_score) >= int(score):
#                 # print(lang, posi, career, pref, score)
#                 # print(i_lang, i_posi, i_career, i_pref, i_score)
#                 # print()
#                 count += 1
#             else:
#               continue
#           else:
#             continue
#         else:
#           continue
#       else:
#         continue
#     answer.append(count)
#   return answer

# ------------------------------------------- 내꺼
# from itertools import combinations


# def solution(info, query):
#   answer = []
#   db = {}
#   for i in info:
#     temp = i.split()
#     conditions = temp[:-1]
#     score = int(temp[-1])
#     for n in range(5):
#       combis = list(combinations(range(4), n))
#       for combi in combis:
#         condi_copy = conditions.copy()
#         for index in combi:
#           condi_copy[index] = '-'
#         merged_condi = ''.join(condi_copy)
#         print(merged_condi)
#         if merged_condi in db:
#           db[merged_condi].append(score)
#         else:
#           db[merged_condi] = [score]

#   for value in db.values():
#     value.sort()
#   print(db)

#   for q in query:
#     qry = []
#     for i in q.split():
#       if i != 'and':
#         qry.append(i)

#     q_condi = ''.join(qry[:-1])
#     q_score = int(qry[-1])
#     if q_condi in db:
#       data = db[q_condi]
#       if len(data) > 0:          
#         start, end = 0, len(data)
#         while start != end and start != len(data):
#           mid = (start + end) // 2
#           if data[mid] >= q_score:
#             end = mid
#           else:
#             start = mid + 1
#         answer.append(len(data) - start)      # 해당 인덱스부터 끝까지의 갯수가 정답
#     else:
#       answer.append(0)

#   return answer


# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


# -------------------------------------------------------------------------------- 3. 압축 
# ------------------------------------------- 내꺼 1시간 컷ㅋㅋㅋ 두번째 20분 컷!!
# def solution(msg):
#   alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#   dic = {}
#   index = 0
#   for i in range(len(alpha)):
#     index += 1
#     dic[alpha[i]] = index

#   answer = []
#   tmp = ''
#   msg = list(msg)
#   while len(msg) > 0:
#     # print(tmp)
#     a = msg.pop(0)
#     if tmp+a not in dic.keys():
#       index += 1
#       dic[tmp+a] = index
#       # print(dic)
#       answer.append(dic[tmp])
#       tmp = a
#     else:
#       tmp += a

#   answer.append(dic[tmp])

#   return answer


# print(solution('KAKAO'))
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))
# print(solution('ABABABABABABABAB'))


# -------------------------------------------------------------------------------- 8. 빛의 경로 실패!!
# ------------------------------------------- 내꺼 두번째 변경!! 야호!!
dx = [0,-1,0,1]
dy = [1,0,-1,0]

def move(grid, x,y,d_index):
  nx = x + dx[d_index]
  ny = y + dy[d_index]
  if 0 <= nx < len(grid) and 0<= ny < len(grid[0]):
    return nx,ny,(x,y,nx,ny,d_index,'O')
  else:
    if nx < 0:
      nx = len(grid)-1
    elif nx == len(grid):
      nx = 0

    if ny < 0:
      ny = len(grid[0])-1
    elif ny == len(grid[0]):
      ny = 0
    return nx,ny,(x,y,nx,ny,d_index,'C')

def solution(grid):
  answer = []
  for i in range(4):
    x = 0
    y = 0
    history = []
    d_index = i
    while True:
      x,y,hist = move(grid,x,y,d_index)

      if hist in history:
        break
      else:
        history.append(hist)

      if grid[x][y] == 'L':
        d_index = (d_index-1)%4
      elif grid[x][y] == 'R':
        d_index = (d_index+1)%4

    if set(history) not in answer:
      answer.append(set(history))

  real_answer = []
  for i in answer:
    real_answer.append(len(i))
  real_answer.sort()
  return real_answer

# ------------------------------------------- 커뮤 내껀 뭐가 문제일까??
def solution(grid):
  # 이동 방향용 리스트 d
  d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
  # 격자의 값에 따른 방향 이동 방법
  right = {0: 3, 1: 2, 2: 0, 3: 1}
  left = {0: 2, 1:3, 2: 1, 3: 0}
  
  answer = []
  w, h = len(grid[0]), len(grid)
  # 각 격자에서의 모든 방향을 이동하였는지 판단하는 리스트 case
  cases = [[[1]*4 for _ in range(w)] for _ in range(h)]
  for y in range(h):
      for x in range(w):
          for i in range(4):
              # 이미 이동한 적 있는 방향은 판단 X
              if not cases[y][x][i]:
                  continue
              cnt = 0 # 길이 판단을 위한 변수
              ty, tx, ti = y, x, i # 위치 ty, tx, 방향 ti
              while True:
                  cases[ty][tx][ti] -= 1
                  cnt += 1
                  now = grid[ty][tx]
                  # 현재 격자의 값을 확인하여 방향 결정
                  if now == 'L':
                      ti = left[ti]
                  elif now == 'R' :
                      ti = right[ti]
                  tx, ty = (tx+d[ti][1])%w, (ty+d[ti][0])%h
                  # 처음 출발점에 도착하면 완료
                  if tx == x and ty == y and ti == i:
                      break
              answer.append(cnt)
  # 값을 정렬 후 리턴
  answer.sort()
  return answer


print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))

# -------------------------------------------------------------------------------- 1. k진수에서 소수 개수 구하기 진수변환이랑 소수 확인하기 복습!!
# ------------------------------------------- 내꺼 두번째 24분 컷!!
# from math import sqrt


# def convert(n,k):
#   digits = '0123456789ABCDEF'
#   answer = ''
#   while True:
#     time, rest = divmod(n,k)
#     n = time
#     answer += digits[rest]
#     if time == 0:
#       break
#   return answer[::-1]

# def prime(n):
#   if n == 0 or n == 1:
#     return False
#   for i in range(2,int(sqrt(n))+1):
#     if n%i == 0:
#       return False
#   return True

# def solution(n, k):
#   converted = convert(n,k)
#   tmp = ''
#   count = 0
#   for i in converted:
#     if i == '0' and tmp != '':
#       if prime(int(tmp)) == True:
#         count += 1
#       tmp = ''
#     else:
#       tmp += i
#   if tmp != '':
#     if prime(int(tmp)) == True:
#       count += 1

#   return count

# print(solution(437674, 3))
# print(solution(110011, 10))