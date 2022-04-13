# timeout 15, fail 12
# 3일에 걸쳐서
# 2. timeout 4, fail 3
# 금요일부터는 레벨 3 2개씩 풀면서 규민이꺼 하자!!
# -------------------------------------------------------------------------------- 4. 땅따먹기 - 복복습!!!!
# ------------------------------------------- 커뮤 3번째 와....이걸 결국은 못 푸넼ㅋㅋㅋㅋ
# def solution(land):

#   for i in range(1,len(land)):
#     for j in range(len(land[0])):
#       land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
#   return max(land[len(land)-1])

# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
# print(solution([[1,2,3,5]]))
# print(solution([[1,2,3,5],[5,6,7,100],[4,3,2,1]]))


# -------------------------------------------------------------------------------- 6. 게임 맵 최단거리
# ------------------------------------------- 내꺼 시간초과 32분 컷! 3번째 11분 컷!!
# from collections import deque

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
#     bfs(maps,0,0)

#     if maps[n-1][m-1] in [0,1]:
#         return -1
#     else:
#         return maps[n-1][m-1]


# def bfs(maps,x,y):
#     q = deque([(x,y)])
#     maps[x][y] = 1
#     while q:
#         now_x, now_y = q.popleft()
#         for i in range(4):
#             nx = now_x + dx[i]
#             ny = now_y + dy[i]
#             if 0 <= nx < len(maps) and 0<= ny < len(maps[0]):
#                 if maps[nx][ny] == 1:
#                     maps[nx][ny] = maps[now_x][now_y] + 1
#                     q.append((nx,ny))


# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

# -------------------------------------------------------------------------------- 9. 구명보트 - 복복습!!
# ------------------------------------------- 내꺼 3번째 시간초과!! 25분 컷!
# from collections import deque


# def solution(people, limit):
#     people.sort()
#     people = deque(people)
#     # print(people)


#     answer = 0
#     while len(people) > 0:
#         now = people.popleft()
#         if len(people) == 0:
#             answer +=1
#             break

#         left = 0
#         right = len(people)-1

#         while left <= right:
#             mid = (left + right) //2
#             if  (now + people[mid]) <= limit:
#                 left = mid + 1
#             else:
#                 right = mid-1
#         # print('left','right',left,right)
#         if now + people[right] <= limit:
#             people.remove(people[right])
#         answer += 1
#         # print(people,answer)

#     return answer

# ------------------------------------------- 이전의 나 투포인터..와우 어떻게 생각해낸거짘ㅋㅋㅋㅋㅋ 암튼 복습하잨ㅋㅋㅋ
# 뭔가 무기가 많아질수록 머리가 복잡해지는 느낌
# def solution(people, limit):
#   people.sort()
#   small_i = 0
#   big_i = len(people)-1
#   count = 0

#   while small_i <= big_i:
#     if people[small_i] + people[big_i] <= limit:
#       small_i += 1
#     big_i -= 1
#     count += 1

#   return count

# print(solution([20,30,50,70,100], 100))
# print(solution([20,30,70,50,80,50], 80))
# print(solution([70,50,80,50], 100))
# print(solution([70,80,50],	100))
# print(solution([20,30,50],	100))

# -------------------------------------------------------------------------------- 4. 방문길이
# ------------------------------------------- 내꺼 32분 컷!! 3번째 26분 컷!!
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def solution(dirs):
#     visited = []
#     answer = 0
#     x,y = 5,5

#     for direc in dirs:
#         if direc == 'U':
#             i = 0
#         elif direc == 'R':
#             i = 1
#         elif direc == 'D':
#             i = 2
#         elif direc == 'L':
#             i = 3
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<= nx < 11 and 0 <= ny < 11:
#             if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited:
#                 visited.append((x,y,nx,ny))
#                 answer += 1
#             x,y = nx,ny

#     return answer


# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
# print(solution("L"))
# print(solution("LR"))

# -------------------------------------------------------------------------------- 8. n^2 배열 자르기 - 실패! 그래도 복습 할 가치가 있다!
# 시키는 대로 따라하는 것이 아니라 규칙을 알아내야해!
# 아니 이걸 어떻게 알아내...?
# 몫과 나머지
# ------------------------------------------- 내꺼 시간초과
# def solution(n, left, right):

# print(solution(3,2,5))
# print(solution(4,7,14))


# -------------------------------------------------------------------------------- 2. 예상 대진표 성공 but 시간초관
# 몇 번째 라운드에서 만나는지 return
# n은 2의 20승 이하인 자연수
# 무조건 log로 가야해
# ------------------------------------------- 내꺼 16분 컷! 3번째 6분 컷!!
# def solution(n,a,b):
#   count = 0
#   while True:
#     if a == b:
#       break
#     if a%2 ==0:
#       a //=2
#     else:
#       a = a//2 + 1

#     if b%2 ==0:
#       b //=2
#     else:
#       b = b//2 + 1
#     count += 1
#   return count

# print(solution(8,4,7))

# -------------------------------------------------------------------------------- 4. 가장 큰 정사각형 찾기 - 복습!!!
# 동적 프로그래밍 문제인지 알고 푸는 것과
# 모르고 접하는 것은 천지차이...
# 1000*1000 이하의 2차원 배열
# 1000000
# ------------------------------------------- 내꺼 전부 통과 그러나 시간초과ㅋㅋㅋㅋ  두번째도 전부통과 but 시간초과 3번째 12분 컷!!!
# def solution(board):
#   max_value = 0
#   for i in range(1,len(board)):
#     for j in range(1,len(board[0])):
#       if board[i][j] != 0:
#         board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
#   for i in board:
#     for j in i:
#       max_value = max(max_value,j)
#   return max_value **2
  

# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# print(solution([[0,0,1,1],[1,1,1,1]]))
# print(solution([[1,1],[1,0]]))
# print(solution([[0,0],[0,0]]))

# -------------------------------------------------------------------------------- 5. 점프와 순간이동
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EC%A0%90%ED%94%84%EC%99%80-%EC%88%9C%EA%B0%84-%EC%9D%B4%EB%8F%99
# ------------------------------------------- 내꺼 전부 통과 그러나 시간초과ㅋㅋㅋㅋ 두번째 6분 컷! 3번째 3분 컷!!
# 동적프로그래밍 인줄 알았는데...
# 10억 이하의 자연수
# def solution(n):
#     count = 0
#     while n >0:
#         if n %2 == 0:
#             n //= 2
#         else:
#             n -= 1
#             count += 1
#     return count


# print(solution(5))
# print(solution(6))
# print(solution(5000))
# print(solution(999999999))

# ------------------------------------------------------------------------------------------------ 220321
# -------------------------------------------------------------------------------- 8. n진수 게임
# 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임
# 뭔가 나쁘진 않다. 진수변환 정도는 아예 외우자!!!
# ------------------------------------------- 내꺼 첫번째 거의 40분...? 두번째 20분 컷!! 3번째 16분 컷!!
# def solution(n, t, m, p):
#     seequence = ''
#     for i in range(t*m):
#         seequence += convert(i,n)
#     answer = ''
#     for i in range(len(seequence)):
#         if len(answer) == t:
#             break
#         if i % m == (p-1):
#             answer += seequence[i]
#     return answer

# def convert(num,depend):
#     string = '0123456789ABCDEF'
#     if num == 0:
#         return '0'
#     answer = ''
#     while num > 0:
#         num,rest = divmod(num,depend)
#         answer += string[rest]
#     return answer[::-1]


# print(solution(2,4,2,1))
# print(solution(16,16,2,1))
# print(solution(16,16,2,2))

# -------------------------------------------------------------------------------- 4. 메뉴 리뉴얼 복습!! 내꺼 시간초과 두번째 시간초과
# dic을 사용하자
# ------------------------------------------- 내꺼 + 커뮤 굉장히 빠르다...!!!
# def solution(orders, course):


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

# -------------------------------------------------------------------------------- 6. [1차] 프렌즈4블록
# 지워지는 블록은 모두 몇 개
# ------------------------------------------- 커뮤...
# def pop_num(b, m, n):
#     pop_set = set()
#     # search
#     for i in range(1, n):
#         for j in range(1, m):
#             if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '_':
#                 pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
#     # set_board
#     for i, j in pop_set:
#         b[i][j] = 0        
#     for i, row in enumerate(b):
#         empty = ['_'] * row.count(0)
#         b[i] = empty + [block for block in row if block != 0]
#     return len(pop_set)

# def solution(m, n, board):
#     count = 0
#     b = list(map(list,zip(*board)))
#     for i in b:
#       print(i)
    # while True:
    #     pop = pop_num(b, m, n)
    #     if pop == 0: return count
    #     count += pop


# ------------------------------------------- 내꺼
# def rotate_right(board):
#   new_board = []
#   for j in range(len(board[0])):
#     tmp = []
#     for i in range(len(board)):
#       tmp.append(board[i][j])
#     tmp.reverse()
#     new_board.append(tmp)
#   return new_board

# print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))



# -------------------------------------------------------------------------------- 9. 순위 검색 - 시간초과!
# 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구
# info 배열의 크기는 1 이상 50,000 이하
# query 배열의 크기는 1 이상 100,000 이하

# string을 index값으로 바꿔도 큰 차이는 없다. 오히려 string이 빠르다!!
# ------------------------------------------- 내꺼 - 정확도는 ok but 시간초과 두번째 여전히 시간초과
# ------------------------------------------- 내꺼
# def solution(info, query):



# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


# -------------------------------------------------------------------------------- 3. 압축 
# ------------------------------------------- 내꺼 1시간 컷ㅋㅋㅋ 두번째 20분 컷!! 3번째 19분 컷!!!
# def solution(msg):
#   alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#   dic = {}
#   index = 0
#   for i in alpha:
#     index += 1
#     dic[i] = index

#   answer = []
#   tmp = ''
#   for i in range(len(msg)+1):
#     if i == len(msg):
#       answer.append(dic[tmp])
#       break
#     tmp += msg[i]
#     if tmp in dic.keys():
#       continue
#     else:
#       answer.append(dic[tmp[:-1]])
#       index += 1
#       dic[tmp] = index
#       tmp = tmp[-1]

#   return answer

# print(solution('KAKAO'))
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))
# print(solution('ABABABABABABABAB'))


# -------------------------------------------------------------------------------- 8. 빛의 경로 실패!!
# ------------------------------------------- 내꺼 두번째 변경!! 야호!!
# def solution(grid):


# print(solution(["SL","LR"]))
# print(solution(["S"]))
# print(solution(["R","R"]))

# -------------------------------------------------------------------------------- 1. k진수에서 소수 개수 구하기 진수변환이랑 소수 확인하기 복습!!
# ------------------------------------------- 내꺼 두번째 24분 컷!! 3번째 20분 컷!!
# from math import sqrt


# def solution(n, k):
#   converted_num = convert(int(n),int(k))
#   answer = 0
#   tmp = ''
#   for i in range(len(converted_num)):
#     if converted_num[i] != '0':
#       tmp += converted_num[i]
#     else:
#       if len(tmp) and prime(int(tmp)):
#         answer += 1
#       tmp = ''
#     if i == len(converted_num)-1:
#       if len(tmp) and prime(int(tmp)):
#         answer += 1

#   return answer

# def prime(num):
#   if num == 0 or num == 1:
#     return False
#   if num == 2:
#     return True
#   for i in range(2,int(sqrt(num))+1):
#     if num % i == 0:
#       return False
#   return True

# def convert(num,depend):
#   string = '0123456789ABCDEF'
#   answer = ''
#   while num > 0:
#     num,rest = divmod(num,depend)
#     answer += string[rest]

#   return answer[::-1]

# print(solution(437674, 3))
# print(solution(110011, 10))