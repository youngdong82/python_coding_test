# -------------------------------------------------------------------------------- bisect
# 9. 순위 검색 참조
# -------------------------------------------------------------------------------- defaultdict
# 문제 2번에서 디폴트딕 뭔가 이상했다.
# 시간만 넣을라고 하니까 전부 쪼개져서 들어갔음
# -------------------------------------------------------------------------------- 2차원 리스트 돌리기
# 이거 개쩐다...!! 문제 6번 커뮤니티
# b = list(map(list,zip(*board)))
# -------------------------------------------------------------------------------- 1. 피보나치 수 10분 컷
# ------------------------------------------- 내꺼
# def solution(n):
#   n = int(n)
#   dp = [0 for _ in range(n+1)]
#   dp[1] = 1
#   dp[2] = 1
#   for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]

#   return dp[n] % 1234567

# print(solution(3))
# print(solution(5))

# -------------------------------------------------------------------------------- 2. 주차 요금 계산 35분 컷!
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림
# ------------------------------------------- 내꺼

# from collections import defaultdict
# from math import ceil


# def solution(fees, records):
#   base_time, base_cost, each_time, each_cost = fees
#   record = defaultdict(list)
#   for i in records:
#     time, car_num, in_out = i.split(' ')
#     print(time, car_num, in_out)
#     record[car_num] += (time, in_out)
  
#   answer = []
#   # 요금 계산한 다음 list에 넣고 sort 한 후 출력하자
#   for i in record.items():
#     # 출차 안한 차량 처리
#     if len(i[1])//2%2 == 1:
#       i[1].append('23:59')
#       i[1].append('OUT')
#     total_time = 0
#     total_cost = 0
#     for j in range(2,len(i[1]),4):
#       o_hour, o_minutes = map(int,i[1][j].split(':'))
#       i_hour, i_minutes = map(int,i[1][j-2].split(':'))
#       total_time += (o_hour-i_hour)*60 + (o_minutes - i_minutes)
#     print(total_time)
#     if total_time <= base_time:
#       total_cost = base_cost
#     else:
#       total_cost = base_cost + ceil((total_time-base_time)/each_time) * each_cost
#     answer.append((i[0], total_cost))
#   answer.sort()
#   real_answer = []
#   for i in answer:
#     real_answer.append(i[1])
#   return real_answer



# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

# -------------------------------------------------------------------------------- 3. [3차] 파일명 정렬 27분 컷!! 기쁘다!!
# 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현
# 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다.
# 파일명은 영문자로 시작, 숫자를 하나 이상 포함

# 1. HEAD 부분을 기준으로 사전 순으로 정렬, 대소문자 구분x
# 2. NUMBER의 숫자 순으로 정렬
# 3. 1,2번 둘 다 같을 경우, 원래 입력에 주어진 순서를 유지
# ------------------------------------------- 내꺼
# def solution(files):
#   answer = []
#   for file in files:
#     head = ''
#     number = ''
#     tail = ''
#     toggle_head = True
#     toggle_number = True
#     for i in file:
#       if i.isdigit() == False and toggle_head:
#         head += i
#       elif i.isdigit() and toggle_number:
#         toggle_head = False
#         number += i
#       else:
#         toggle_number = False
#         tail += i
#     answer.append((head, number, tail))
  
#   answer.sort(key = lambda x: (x[0].lower(), int(x[1])))

#   real_answer = []
#   for i in answer:
#     original = ''.join(i)
#     real_answer.append(original)
#   return real_answer


# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# -------------------------------------------------------------------------------- 4. 메뉴 리뉴얼
# # ------------------------------------------- 내꺼 구현은 괜춘 그러나 시간초과
# # 완전탐색 가능할 것 같다. - 아닌듯...?
# # 아무리 그래도 4중 반복문 좀 심했나...?
# # 접근법은 같았다. 3중과 4중의 차이?? 쓸데없는 게 많나??
# from collections import defaultdict
# from itertools import combinations


# def solution(orders, course):
#   order_time = defaultdict(int)
#   for order in orders:
#     for i in order:
#       order_time[i] += 1

#   more_2 = []
#   for i in order_time.items():
#     if i[1] >=2:
#       more_2.append(i[0])
#   more_2.sort()

#   course.sort(reverse = True)
#   answer = []
#   for i in course:
#     candidates = list(combinations(orders,i))
#     temp = []
#     for candidate in candidates:
#       count = 0
#       for order in orders:
#         good = 0
#         # 전부 다 ok일 경우 count += 1
#         for j in candidate:
#           if j in order:
#             good += 1
#         if good == len(candidate):
#           count += 1

#       if count >= 2:
#         temp.append((count, candidate))
#     temp.sort()
#     for each in temp:
#       if each[0] == temp[-1][0]:
#         answer.append(''.join(each[1]))
#   answer.sort()
#   return answer

# ------------------------------------------- 내꺼 2
# 하나하나 선택해서 후보군 만들고 있는 것에서 하나하나 확인하는것이 아니라
# 처음부터 있는 것에서 세는 차이??
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

# ------------------------------------------- 커뮤니티 1
# from itertools import combinations

# def solution(orders, course):
#   answer = []
#   for k in course:
#     candidates = []
#     new_menu = {}
#     for menu in orders:
#       menu_li = list(''.join(menu))
#       for li in combinations(menu_li, k):
#         res = ''.join(sorted(li))
#         if res not in candidates:
#           candidates.append(res)
#         else:
#           if res not in new_menu.keys():
#             new_menu[res] = 2
#           else:
#             new_menu[res] += 1
#     sort_menu = sorted(new_menu.items(), key=lambda x:[len(x[0]), x[1]])

#     if len(sort_menu):
#       now = course[-1]
#       maxi = sort_menu[-1][1]
#     while sort_menu:
#       menu, cnt = sort_menu.pop()
#       if len(menu) == now and cnt >= maxi:
#         answer.append(menu)
#       elif len(menu) != now:
#         now = len(menu)
#         maxi = cnt
#         answer.append(menu)
#   return sorted(answer)

# ------------------------------------------- 커뮤니티 2 Counter 덕분에 굉장히 깔끔하네...
# from collections import Counter
# from itertools import combinations

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += combinations(sorted(order), course_size)

#         most_ordered = Counter(order_combinations).most_common()
#         for k, v in most_ordered:
#           if v > 1 and v == most_ordered[0][1]:
#             result.append(k)

#     return [ ''.join(v) for v in sorted(result) ]

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

# -------------------------------------------------------------------------------- 5. 거리두기 확인하기 실패!
# 똑같은 bfs인데 뭐가 문제였던거여...
# 애초에 q에 들어가는 값을 (x,y,거리)로 설정해서
# nx,ny할 때 nd라는 거리값도 +1 해주니 괜춘하네
# ------------------------------------------- 내꺼
# from collections import deque

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]

# def bfs(place, x,y):
#   if place[x][y] != 'P':
#     return True
#   q = deque([])
#   q.append((x,y))
#   place[x][y] = 0
#   while q:
#     now_x,now_y = q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0<= nx < 5 and 0<= ny < 5:
#         if place[nx][ny] == 'P' and abs(nx-x) + abs(ny-y) <= 2:
#           return False
#         elif place[nx][ny] == 'X':
#           continue
#         elif place[nx][ny] == 'O' or place[nx][ny] == 'P':
#           if place[nx][ny].isdigit() == False:
#             place[nx][ny] = place[now_x][now_y] + 1
#             q.append((nx,ny))
#   return True


# def solution(places):
#   answer = []
#   for place in places:
#     for i in range(5):
#       place[i] = list(place[i])

#     p_list = []
#     for i in range(5):
#       for j in range(5):
#         if place[i][j] == 'P':
#           p_list.append((i,j))

#     count = 0
#     for i in p_list:
#       result = bfs(place, i[0], i[1])
#       if result:
#         count += 1
#     for i in place:
#       print(i)
#     print()
#     if count == len(p_list):
#       answer.append(1)
#     else:
#       answer.append(0)
    
#   return answer


# ------------------------------------------- 커뮤니티
# from collections import deque

# def bfs(p, index):
#   q = deque([index])
#   visited = [[False]*5 for _ in range(5)]
#   dic = {0: [0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}

#   while q:
#     x, y, d = q.popleft()
#     visited[x][y] = True
#     for i in range(4):
#       nx = x + dic[i][0]
#       ny = y + dic[i][1]
#       nd = d + 1
#       if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
#         visited[nx][ny] = True
#         if p[nx][ny] == 'P':
#           if nd <= 2:
#             return False
#         elif p[nx][ny] == 'O':
#           if nd == 1:
#             q.append([nx, ny, nd])
#   return True

# def solution(places):
#   answer = []
#   for p in places:
#     flag = 1
#     for i in range(5):
#       for j in range(5):
#         if p[i][j] == 'P':
#           result = bfs(p, [i, j, 0])
#           if not result:
#             flag = 0
#     answer.append(flag)
    
#   return answer


# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# -------------------------------------------------------------------------------- 6. [1차] 프렌즈4블록
# 돌려놓고 생각하자
# ------------------------------------------- 내꺼
# dx = [1,0,1]
# dy = [0,1,1]

# def check(board, x,y, remove_list):
#   for k in range(3):
#     nx = x + dx[k]
#     ny = y + dy[k]
#     if 0<= nx < len(board) and 0<= ny < len(board[0]):
#       if board[x][y] != board[nx][ny]:
#         return
#     else:
#       return
#   remove_list.append((x,y))
#   remove_list.append((x+1,y))
#   remove_list.append((x,y+1))
#   remove_list.append((x+1,y+1))
#   check(board, x+1,y, remove_list)
#   check(board, x,y+1, remove_list)
#   check(board, x+1,y+1, remove_list)
  


# def solution(m, n, board):
#   for i in board:
#     print(i)

#   remove_list = []
#   for x in range(len(board)):
#     for y in range(len(board[0])):
#       check(board, x,y, remove_list)
#   print(set(remove_list))
  
# ------------------------------------------- 커뮤
# def pop_num(b, m, n):
#     pop_set = set()
#     # search
#     for i in range(1, n):
#         for j in range(1, m):
#             if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] and b[i][j] != '_':
#                 pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
#     print(pop_set)
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
#     while True:
#         pop = pop_num(b, m, n)
#         if pop == 0:
#           return count
#         count += pop


# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

# -------------------------------------------------------------------------------- 7. 이진 변환 반복하기 11분 컷!
# ------------------------------------------- 내꺼
# def solution(s):
#   a = s
#   count = 0
#   removed = 0
#   while len(a) > 1:
#     temp = ''
#     remove = 0
#     for i in a:
#       if i == '1':
#         temp += i
#       else:
#         remove += 1
#     a = bin(len(temp))[2:]
#     count += 1
#     removed += remove
#   return [count, removed]
  

# print(solution("110010101001"))
# print(solution("01110"))
# print(solution("1111111"))

# -------------------------------------------------------------------------------- 8. 괄호 회전하기 26분 컷!
# ------------------------------------------- 내꺼 6분
# from collections import deque

# def check(string):
#   right = [']', '}', ')']
#   big_c = 0
#   mid_c = 0
#   small_c = 0
#   for i in string:
#     if big_c < 0 or mid_c < 0 or small_c < 0:
#       return False
#     if i in right:
#       if i == ']':
#         big_c -= 1
#       elif i == '}':
#         mid_c -= 1
#       else:
#         small_c -= 1
#     else:
#       if i == '[':
#         big_c += 1
#       elif i == '{':
#         mid_c += 1
#       else:
#         small_c += 1

#   exclusive = ['[]', '{}', '()']
#   if big_c + mid_c + small_c != 0:
#     return False
#   else:
#     for i in exclusive:
#       if i in ''.join(string):
#         return True


# def solution(s):
#   s = deque(list(s))
#   answer = 0
#   for i in range(len(s)):
#     s.append(s.popleft()) 
#     if check(s):
#       answer += 1
#   return answer


# print(solution("([{)}]"))
# print(solution("{{}"))
# print(solution("[](){}"))
# print(solution("}]()[{"))
# print(solution("[)(]"))
# print(solution("}}}"))
# -------------------------------------------------------------------------------- 9. 순위 검색 - 시간초과!
# 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구
# info 배열의 크기는 1 이상 50,000 이하
# query 배열의 크기는 1 이상 100,000 이하
# 나눈 다음 정렬을 좀 해놓을까...?
# 그 후 이진탐색..? 맞추긴 했다ㅋㅋㅋㅋㅋㅋㅋ
# string을 index값으로 바꿔도 큰 차이는 없다. 오히려 string이 빠르다!!
# ------------------------------------------- 내꺼 - 정확도는 ok but 시간초과 
# def solution(info, query):
#   sorted_info = []
#   for i in range(len(info)):
#     lang, posi, expir, pref, score = info[i].split(' ')
#     sorted_info.append((lang, posi, expir, pref, score))
#   sorted_info.sort(key=lambda x:(x[0], x[1] ,x[2], x[3], x[4]))
  

#   answer = []
#   for i in range(len(query)):
#     splited = []
#     a = query[i].split(' ')
#     for i in a:
#       if i == 'and':
#         continue
#       else:
#         splited.append(i)
#     lang, posi, expir, pref, score = splited

#     index_list = []
#     for i in range(len(sorted_info)):
#       if sorted_info[i][0] == lang or lang == '-':
#         index_list.append(i)

#     index_list_2 = []
#     for i in index_list:
#       if sorted_info[i][1] == posi or posi == '-':
#         index_list_2.append(i)

#     index_list_3 = []
#     for i in index_list_2:
#       if sorted_info[i][2] == expir or expir == '-':
#         index_list_3.append(i)

#     index_list_4 = []
#     for i in index_list_3:
#       if sorted_info[i][3] == pref or pref == '-':
#         index_list_4.append(i)

#     index_list_5 = []
#     for i in index_list_4:
#       if int(sorted_info[i][4]) >= int(score):
#         index_list_5.append(i)
#     answer.append(len(index_list_5))
#   return answer

# ------------------------------------------- 커뮤니티 이진탐색 의외로 dic의 힘이지, 이진은 아닌듯??
# from itertools import combinations
# from collections import defaultdict
# from bisect import bisect_left

# def solution(information, queries):
#     answer = []
#     dic = defaultdict(list)
#     for info in information:
#         info = info.split()
#         condition = info[:-1]  
#         score = int(info[-1])
#         print(info)
#         print(condition, score)
#         for i in range(5):
#             case = list(combinations([0,1,2,3], i))
#             for c in case:
#                 tmp = condition.copy()
#                 for idx in c:
#                     tmp[idx] = "-"
#                 key = ''.join(tmp)
#                 dic[key].append(score) 
#     # value의 숫자 오름차순으로
#     for value in dic.values():
#         value.sort()
#     print(dic)
      

#     for query in queries:
#         query = query.replace("and ", "")
#         query = query.split()
#         target_key = ''.join(query[:-1])
#         target_score = int(query[-1])
#         # print(target_key, target_score)
#         count = 0
#         if target_key in dic:
#             target_list = dic[target_key]
#             idx = bisect_left(target_list, target_score)
#             print(target_list, idx)
#             count = len(target_list) - idx
#         answer.append(count)      
#     return answer


# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# -------------------------------------------------------------------------------- 10. 튜플
# ------------------------------------------- 내꺼
def solution(s):
    answer = []
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))