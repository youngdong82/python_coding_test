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

# -------------------------------------------------------------------------------- 8. n^2 배열 자르기 - 복복습!!
# 시키는 대로 따라하는 것이 아니라 규칙을 알아내야해!
# 아니 이걸 어떻게 알아내...?
# 몫과 나머지
# ------------------------------------------- 내꺼 시간초과
# def solution(n, left, right):
#     graph = [[0] * n for _ in range(n)]

#     for i in range(len(graph)):
#         for j in range(len(graph[0])):
#             graph[i][j] = max(i,j)+1

#     answer = []
#     for i in range(left,right+1):
#         time,rest = divmod(i,n)
#         answer.append(graph[time][rest])
#     return answer

# ------------------------------------------- 내꺼2 바로 구해버리기?? 오 개쩐다
# 풀이를 생각하고 나서는 3분 컷, 그러나 힌트가 있었기에 가능했었다.ㅠ
# def solution(n, left, right):
#     n = int(n)
#     left = int(left)
#     right = int(right)
#     answer = []
#     for i in range(left,right+1):
#         time,rest = divmod(i,n)
#         if rest > time:
#             answer.append(rest+1)
#         else:
#             answer.append(time+1)
#     return answer


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

# -------------------------------------------------------------------------------- 4. 가장 큰 정사각형 찾기
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

# -------------------------------------------------------------------------------- 4. 메뉴 리뉴얼 복복습!!
# ------------------------------------------- 내꺼 시간초과 두번째 시간초과 3번째 시간초과
# 쓰여진 모든 메뉴들 정리하고
# 그것을 만들수 있는 모든 케이스 렉 만든 후
# 계속 안으로 들어감
# 하나하나확인
# from itertools import combinations


# def solution(orders, course):
#     orders.sort(key=lambda x:(len(x)))
#     reck = []
#     for i in orders:
#         for j in i:
#             if j not in reck:
#                 reck.append(j)
#     answer = []
#     for i in course:
#         candidates = list(combinations(reck,i))
#         answer_reck = []
#         for candi in candidates:
#             count = 0
#             for order in orders:
#                 toggle = True
#                 for each in candi:
#                     if each not in order:
#                         toggle = False
#                 if toggle:
#                     count += 1
#             if count >=2:
#                 answer_reck.append((count,''.join(sorted(candi))))
#         answer_reck.sort(reverse=True)
#         for count,menu in answer_reck:
#             if count == answer_reck[0][0]:
#                 answer.append(menu)
#     answer.sort()
#     return answer

# ------------------------------------------- 내꺼 2
# 쓰여진 모든 메뉴들 정리하고
# 그것을 만들수 있는 모든 케이스 렉 만든 후
# 한번 빠져나온 후에 - 의미없는듯??
# 집합연산으로 확인
# from itertools import combinations


# def solution(orders, course):
#     orders.sort(key=lambda x:(len(x)))
#     reck = []
#     for i in orders:
#         for j in i:
#             if j not in reck:
#                 reck.append(j)
#     candi_reck = []
#     for i in course:
#         candidates = list(combinations(reck,i))
#         for candi in candidates:
#             candi_reck.append(candi)

#     answer_reck = {}
#     for candi in candi_reck:
#         count = 0
#         for order in orders:
#             toggle = True
#             for each in candi:
#                 if each not in order:
#                     toggle = False
#             if toggle:
#                 count += 1
#         if count >=2:
#             if len(candi) not in answer_reck.keys():
#                 answer_reck[len(candi)] = [(count,''.join(sorted(candi)))]
#             else:
#                 answer_reck[len(candi)].append((count,''.join(sorted(candi))))

#     answer = []
#     for i in answer_reck.values():
#         i.sort(reverse = True)
#         for j in i:
#             if j[0] == i[0][0]:
#                 answer.append(j[1])
#     answer.sort()
#     return answer

# ------------------------------------------- 내꺼
# 이거 크게 다른 것 없이 순서의 차이였던걸로 기억하는데...꾸준히 못 푸네
# 집합연산 사용해보자
# from itertools import combinations


# def solution(orders, course):
#     orders.sort(key=lambda x:(len(x)))
#     reck = []
#     # 정렬 된 orders를 돌면서 order별로 만들 수 있는 조합들 reck에 넣기
#     for order in orders:
#         for i in range(2,len(order)+1):
#             candidates = list(combinations(order,i))
#             for candi in candidates:
#                 reck.append(''.join(sorted(candi)))

#     # 중복되는 값 제거 후 정렬
#     reck = list(set(reck))
#     reck.sort()

#     dic = {}
#     for i in reck:
#         count = 0
#         for order in orders:
#             if set(i) & set(order) == set(i):
#                 count += 1
#         if count >= 2:
#             if len(i) not in dic.keys():
#                 dic[len(i)] = [(count,i)]
#             else:
#                 dic[len(i)].append((count,i))

#     answer = []
#     for i in dic.values():
#         i.sort(reverse = True)
#         for each in i:
#             if each[0] == i[0][0]:
#                 answer.append(each[1])
#     answer.sort()
#     return answer

# ------------------------------------------- 커뮤 놀랍다 놀라워...!!!!
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

# -------------------------------------------------------------------------------- 6. [1차] 프렌즈4블록 복복습!!
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

# print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))



# -------------------------------------------------------------------------------- 9. 순위 검색 - 복복습!!
# 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구
# info 배열의 크기는 1 이상 50,000 이하
# query 배열의 크기는 1 이상 100,000 이하
# ------------------------------------------- 커뮤
# from itertools import combinations


# def solution(info, query):
#     dic = {}
#     for i in info:
#         temp = i.split(' ')
#         conditions = temp[:-1]
#         score = int(temp[-1])
#         for n in range(5):
#             combis = list(combinations(range(4), n))
#             # print(combis)
#             for combi in combis:
#                 condi_copy = conditions.copy()
#                 for index in combi:
#                     condi_copy[index] = '-'
#                 merged_condi = ''.join(condi_copy)
#                 if merged_condi in dic:
#                     dic[merged_condi].append(score)
#                 else:
#                     dic[merged_condi] = [score]

#     for value in dic.values():
#         value.sort()

#     answer = []
#     for q in query:
#         qry = []
#         for i in q.split():
#             if i != 'and':
#                 qry.append(i)

#         q_condi = ''.join(qry[:-1])
#         q_score = int(qry[-1])

#         if q_condi in dic:
#             data = dic[q_condi]
#             if len(data) > 0:          
#                 start, end = 0, len(data)
#                 while start != end and start != len(data):
#                     mid = (start + end) // 2
#                     if data[mid] >= q_score:
#                         end = mid
#                     else:
#                         start = mid + 1
#                 answer.append(len(data) - start)      # 해당 인덱스부터 끝까지의 갯수가 정답
#         else:
#             answer.append(0)

#     return answer


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

# -------------------------------------------------------------------------------- 1. k진수에서 소수 개수 구하기
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