# 재귀함수 돌릴때 return 여부에 따른 함수 밖 list or global list or 변수의 변화여부 확인!!!!
# 1. 외부 함수 바꾸기, 인자 전달 o 리턴 x
# a = [1,2,3,4,5]
# def recursive(depth,graph):
#   if depth >=3:
#     return
#   graph.append(depth)
#   recursive(depth +1, graph)

# recursive(0,a)
# print(a)

# 2. 외부 함수 바꾸기, 인자 전달 x
# a = [1,2,3,4,5]
# def recursive(depth):
#   if depth >=3:
#     a.pop(0)
#     return 
#   a.append(depth)
#   recursive(depth +1)

# recursive(0)
# print(a)

# 3. 외부 함수 바꾸기, 인자 전달 x 리턴 o
# a = [1,2,3,4,5]
# def recursive(depth,graph):
#   if depth >=3:
#     graph.pop(0)
#     return graph
#   graph.append(depth)
#   return recursive(depth +1, graph)

# b = recursive(0,a)
# print(a,b)

# -------------------------------------------------------------------------------- 5. 큰 수 만들기  - 복복습!!
# permutation쓸 수 있지만 number가 1,000,000이라 사용하면 터진다
# k는 1 이상

# stack을 이용해보자.
# ------------------------------------------- 내꺼 역시나 시간초과 구현 자체도 어려워
# def solution(number, k):
#   answer = []
#   for num in number:
#     while len(answer) > 0 and k > 0 and answer[-1] < num:
#       answer.pop()
#       k-=1
#     answer.append(num)
#   return ''.join(answer[:len(answer)-k])
  

# print(solution("1924",2))
# print(solution("1231234",3))
# print(solution("4177252841",4))

# -------------------------------------------------------------------------------- 5. 거리두기 확인하기
# 맨해튼 거리1가 2 이하
# 파티션 x, 빈자리o, 응시자 p
# ------------------------------------------- 내꺼 두번째 35분 컷!! 3번째 실패!

# -------------------------------------------------------------------------------- 1. 후보키 실패! 복복습 필수!!! 이거 개어려웡... - 졸업
# 컬럼(column)의 길이는 1 이상 8 이하
# 로우(row)의 길이는 1 이상 20 이하
# 모든 문자열의 길이는 1 이상 8 이하

# 유일성과 최소성을 만족해야해

# 컬럼의 길이별로 combinations 돌릴꺼야
# (combi 돌릴때 index값으로 돌리자 (대표성))

# answer를 포함하는 건 빼고,
# 각 combi index를 모아놓은 list 만들고
# set으로 중복여부 확인
# 중복이라면 넘어가
# 중복 아니라면
#   answer에 넣기

# ------------------------------------------- 커뮤니티 뭔가 간단해보이는데 로직 자체도 뭔가 복잡하네... 4번째 23분 컷이다!!! 카카오 놈들아!!!크하핳하하!!
# from itertools import combinations


# def solution(relation):
#   n = len(relation)
#   m = len(relation[0])

#   answer = []
#   for i in range(1,m+1):
#     candidates = list(combinations(range(m),i))
#     for candi in candidates:
#       toggle = True
#       for each_answer in answer:
#         if set(each_answer) & set(candi) == set(each_answer):
#           toggle = False
#       if not toggle:
#         continue
#       # print('candi',candi)
#       tmp_reck = []
#       for k in range(n):
#         tmp = ''
#         for j in candi:
#           tmp += relation[k][j]
#         tmp_reck.append(tmp)
#       # print('tmp_reck', tmp_reck)
#       if len(tmp_reck) == len(set(tmp_reck)):
#         answer.append(candi)
#     # print()

#   return len(answer)



# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))


# -------------------------------------------------------------------------------- 2. 조이스틱 복복습!!! - 졸업
# 1 이상 20 이하
# 위 아래 움직임 + 양옆 움직임
# alpha 선언하고
# 돌면서 updown += 해주기
# max(alpha.index(i), 26-alpha.index(i))

# 양옆 움직임
# A가 아닌 애들 인덱스 전부 받아오기

# 왼 끝에서 오른끝
# 오른끝에서 왼끝
# 한칸씩 갔다가 돌아오는거
# ------------------------------------------- 내꺼 실패!! 두번째 실패 세번째 실패 
# def solution(name):
#   n = len(name)
#   alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#   up_down_move = 0
#   for i in name:
#     if i != 'A':
#       up_down_move += min(alpha.index(i), 26-alpha.index(i))

#   index_reck = []
#   for i in range(1,len(name)):
#     if name[i] != 'A':
#       index_reck.append(i)
#   if len(index_reck) > 0:
#     left_to_right = index_reck[-1]
#     right_to_left = n - index_reck[0]

#     tmp_reck = [left_to_right, right_to_left]
#     for i in range(len(index_reck)-1):
#       tmp = (index_reck[i] * 2) + (n - index_reck[i+1])
#       tmp_reck.append(tmp)

#     for i in range(len(index_reck)-1):
#       tmp = (index_reck[i]) + ((n - index_reck[i+1]) * 2)
#       tmp_reck.append(tmp)

#     left_right_move =  min(tmp_reck)

#     return up_down_move + left_right_move
#   else:
#     return up_down_move

# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("AD"))
# print(solution("BBABAAAABBBAAAABABB"))
# print(solution("BBAAAAAABBBAAAAAABB"))


# -------------------------------------------------------------------------------- 4. [1차] 뉴스 클러스터링 복복습!! - 졸업
# 자카드 유사도
# 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
# 집합 A와 집합 B가 모두 공집합일 경우에는
# 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의
# 다중집합에도 갯수로 적용가능

# 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다
# 대소문자 같이 취급
# 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력

# 무엇을 묻는 문제?
# 집합연산 묻는 문제, 구현 문제
# 각 문자열의 길이는 2 이상, 1,000 이하

# 1. 각각 한꺼번에 대문자로 만들어주고
# 2. 각 문자열 돌면서 두 개씩 묶은 값 넣어주기(is.alpha로 거르기)
# 3. 각 문자열 집합자료형 선언하고 갯수 세면서 넣어주기

# ------------------------------------------- 내꺼 3번째 50분 컷! 4번째 25분 컷!
# import math


# def solution(str1, str2):
#   # 다중집함으로 만들기
#   str1_list = []
#   for i in range(1,len(str1)):
#     tmp = str1[i-1] + str1[i]
#     if tmp.isalpha():
#       str1_list.append(tmp.upper())

#   str2_list = []
#   for i in range(1,len(str2)):
#     tmp = str2[i-1] + str2[i]
#     if tmp.isalpha():
#       str2_list.append(tmp.upper())
  
#   # 갯수 세기
#   str1_dic = {}
#   for i in str1_list:
#     if i not in str1_dic.keys():
#       str1_dic[i] = 1
#     else:
#       str1_dic[i] += 1

#   str2_dic = {}
#   for i in str2_list:
#     if i not in str2_dic.keys():
#       str2_dic[i] = 1
#     else:
#       str2_dic[i] += 1
#   # print(str1_dic, str2_dic)

#   # 전체집합

#   AND = []
#   OR = []
#   for i,j in str1_dic.items():
#     if i in str2_dic.keys():
#       for _ in range(min(j,str2_dic[i])):
#         AND.append(i)
#       for _ in range(max(j,str2_dic[i])):
#         OR.append(i)
#     else:
#       for _ in range(j):
#         OR.append(i)

#   for i,j in str2_dic.items():
#     if i not in OR:
#       for _ in range(j):
#         OR.append(i)
      
#   # print('AND:',AND)
#   # print('OR:',OR)

#   if len(AND) == len(OR) == 0:
#     return 65536
#   else:
#     return math.floor((len(AND) / len(OR)) * 65536) 


# print(solution('FRANCE',	'french'))
# print(solution('handshake',	'shake hands'))
# print(solution('aa1+aa2',	'AAAA12'))
# print(solution('E=M*C^2',	'e=m*c^2'))

# -------------------------------------------------------------------------------- 5. 수식 최대화 - 애매모시..
# 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출
# 가장 큰 상금 금액을 return 
# 3종류의 연산자의 우선순위를 정하는 것이기 때문에
# 경우의 수는 6이다.

# 최대 길이를 6번 돌려도 시간초과할 일은 없을 듯.
# 한번 사이클마다 3번은 돌기때문에
# 대충잡아
# 50 * 3* 6 이면 만이 넘지 않기 때문에 충분
# expression 3 이상 100 이하인 문자열


# tmp list를 이용해서 숫자와 문자열을 분리시켜서 list에 담고??

# 반복문
# 새로운 tmp stack을 선언하고
# list 돌면서 우선순위에 걸리는 문자열이라면
# tmp_stack.pop()이랑 tmp_list[i]랑 문자열에 따라 계산
# 결과값의 절대값을 answer에 넣고

# max(answer) 리턴

# ------------------------------------------- 내꺼 전에 만든거보단 효율적이긴한데 덱의 활용을 물어보는 문제처럼 잘 풀었다.
# from itertools import permutations

# def calculate(x,y,oper):
#   x = int(x)
#   y = int(y)
#   if oper == '+':
#     return str(x + y)
#   elif oper == '-':
#     return str(x - y)
#   elif oper == '*':
#     return str(x * y)

# def solution(expression):
#   oper = ['-','+','*']
#   data_list = []
#   tmp = ''
#   for i in expression:
#     if i in oper:
#       data_list.append(tmp)
#       data_list.append(i)
#       tmp = ''
#     else:
#       tmp += i
#   data_list.append(tmp)

#   candidates = list(permutations(oper,3))
#   answer = []
#   for candi in candidates:
#     data_list_copy = data_list.copy()
#     toggle = True
#     tmp = []
#     for oper in candi:
#       for i in range(len(data_list_copy)):
#         if data_list_copy[i] == oper:
#           after_cal = calculate(tmp.pop(),data_list_copy[i+1], data_list_copy[i])
#           tmp.append(after_cal)
#           toggle = False
#         else:
#           if toggle:
#             tmp.append(data_list_copy[i])
#           else:
#             toggle = True
#             continue
#       data_list_copy = tmp
#       tmp = []
#     answer.append(abs(int(data_list_copy[0])))
#   return max(answer)
      
      
# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))


# -------------------------------------------------------------------------------- 4. 땅따먹기 - 복복습!!!! - 졸업
# ------------------------------------------- 커뮤 3번째 와....이걸 결국은 못 푸넼ㅋㅋㅋㅋ
# def solution(land):
#   for i in range(1,len(land)):
#     for j in range(len(land[0])):
#       new_list = land[i-1][:j] + land[i-1][j+1:]
#       land[i][j] = land[i][j] + max(new_list)
#   return max(land[-1])

# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# -------------------------------------------------------------------------------- 9. 구명보트 - 복복습!! - 졸업
# ------------------------------------------- 내꺼 3번째 시간초과!! 25분 컷!
# [50, 50, 70, 80]
# 1명 이상 50,000명 이하

# 이분탐색
# 1.people을 정렬
# 왼쪽부터 시작
# can_load_weight 는 최대가능무게 - 현재 무게
# can_load_weight이 현재무게보다 작으면,
#   브레이크 - 이후 전부 한명씩 밖에 못탐.
# can_load_weight이 현재무게보다 크면,
#   일단 ok
#   이분탐색으로 돌려서(can_load_weight보다 작은사람 중에 가장 무거운사람 찾기)
#   두명 빼기
#   못찾으면 한명빼기

# 투포인터
# 1.people을 정렬
# 왼쪽과 오른쪽 선언
# 왼,오 더해서 최대가능무게보다 크다?
#   answer += 1
#   오 -=1
# 왼,오 더해서 최대가능무게보다 작다?
# answer+=1하고

# def solution(people, limit):
#   people.sort()
#   # print(people)
#   left = 0
#   right = len(people)-1
#   answer = 0
#   while left <= right:
#     if people[left] + people[right] >limit:
#       right -= 1
#       answer += 1
#     else:
#       left += 1
#       right -= 1
#       answer += 1

#   return answer

# print(solution([70, 50, 80, 50],100))
# print(solution([70, 80, 50],100))

# -------------------------------------------------------------------------------- 8. n^2 배열 자르기 - 복복습!! - 졸업
# ------------------------------------------- 내꺼 시간초과 14분 컷!!
# n이 10의 7제곱이라
# 2차원 배열 만들고 
# 하나하나 계산하면서 값 넣는 것에서 이미 끝남 10의 14제곱

# 규칙을 찾아서
# range(left,right+1)돌면서
# 바로바로 answer list에 넣어야해.

# 규칙:
# a로 나뉘어진다면
# 인덱스 a까지는 a+1
# 나머지는 나머지 값

# def solution(n, left, right):
#   answer = []
#   for i in range(left,right+1):
#     time,rest = divmod(i,n)
#     if rest <= time:
#       answer.append(time+1)
#     else:
#       answer.append(rest+1)
#   return answer

# print(solution(3,2,5))
# print(solution(4,7,14))


# -------------------------------------------------------------------------------- 4. 메뉴 리뉴얼 복복습!!
# ------------------------------------------- 내꺼 시간초과 두번째 시간초과 3번째 시간초과 4번째 시간초괔ㅋㅋㅋㅋㅋㅋ 학습 안하냨ㅋㅋ
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
#     print(dic)

#     for combi, time in dic.items():
#       if time == max(dic.values()) and time >=2 :
#         answer.append(''.join(combi))

#   return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

# -------------------------------------------------------------------------------- 6. [1차] 프렌즈4블록 복복습!!
# 지워지는 블록은 모두 몇 개

# 1. 그래프 오른쪽으로 돌려주고
# 2. while로 전체 돌면서 확인
#   x,y가 
#   0이면 다음,
#   x+1,y/ x,y+1/ x+1,y+1 확인해보고
#   2-1 확인되면
#     tmp에 넣고
#     사이클 한번 끝나면 set(tmp)한 후 전부 없애고
    # len(tmp)가 0이라면
    # 종료
#   2-2 없어진거 0으로 채워주기 (rjust)

# ------------------------------------------- 내꺼 이게 왜 안되는지 모르겠네 완전탐색인데...
# def rotate_right(graph):
#   row = len(graph)
#   column = len(graph[0])

#   result = [[0] * row for _ in range(column)]
#   for i in range(row):
#     for j in range(column):
#       result[j][row-1-i] = graph[i][j]
#   return result


# def solution(m, n, board):
#   new_board = rotate_right(board)
#   answer = 0

#   while True:
#     # for i in new_board:
#     #   print(i)
#     # print()
#     tmp = []
#     for i in range(n-1):
#       for j in range(m-1):
#         if new_board[i][j] != '0':
#           if new_board[i][j] == new_board[i][j+1] == new_board[i+1][j] == new_board[i+1][j+1]:
#             tmp.append((i,j))
#             tmp.append((i,j+1))
#             tmp.append((i+1,j))
#             tmp.append((i+1,j+1))
    
#     if len(tmp) == 0:
#       break
#     tmp = list(set(tmp))
#     tmp.sort(reverse=True)

#     answer += len(tmp)
#     for i,j in tmp:
#       new_board[i].remove(new_board[i][j])
    
#     # for i in new_board:
#     #   print(i)
#     # print()

#     for i in range(len(new_board)):
#       a = m-len(new_board[i])
#       if a > 0:
#         for _ in range(a):
#           new_board[i].append('0')

#   return answer

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
#     while True:
#         pop = pop_num(b, m, n)
#         if pop == 0: return count
#         count += pop

# print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
# print(solution(3,8,['AAAAAAAA','BBAAAACC','BBAAAACC']))
# print(solution(2,2,["CZ","CC"]))
# print(solution(6,5,["CCZXZ","CCZXZ","XXZXZ","AAZAA","AAAAA","ZAAXX"]))

# -------------------------------------------------------------------------------- 9. 순위 검색 - 복복습!! - 졸업
# 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구
# info 배열의 크기는 1 이상 50,000 이하
# query 배열의 크기는 1 이상 100,000 이하
# 해당하는 사람들의 숫자


# 1. 공백을 기준으로 나눈다음 condition과 score로 나눈다
# 2. 집합자료형 선언하고
#    모든 info 돌면서
#    condition을 하나씩 _으로 바꾼 후 score 값으로 넣어준다.

# 3. and를 기준으로 나누고 condition과 score로 나눈다.
# 4. 집합자료형에 condi로 조회하고
#    정렬한 후
#    score 인덱스를 통해 일치하는 사람 수 찾아 answer에 넣기

# 시간초과 포인트는 중간에 sort 시키는 것.
# 이해는 안됨... 애초에 연산 수가 다른데 왜 이게 더 빠른거지...
# ------------------------------------------- 내꺼 시간초과 드디어 실패에서 시간초과로 옮겨졌다
# from bisect import bisect_left
# from collections import defaultdict
# from itertools import combinations


# def solution(info, query):
#   candidates = []
#   for i in range(5):
#     candidates += combinations(range(4),i)
  
#   data_dic = defaultdict(list)
#   for i in info:
#     condi = i.split(' ')
#     score = int(condi.pop())

#     for each_candi in candidates:
#       condi_copy = condi.copy()
#       for i in each_candi:
#         condi_copy[i] = '-'
#       made_candi = ''.join(condi_copy)
#       data_dic[made_candi].append(score)

#   for value in data_dic.values():
#     value.sort()

#   answera = []
#   for i in query:
#     lang,posi,career,prefer_score = i.split(' and ')
#     prefer,score = prefer_score.split(' ')
#     score_q = int(score)
#     condi_q = lang+posi+career+prefer

#     if condi_q in data_dic:
#       left_index = bisect_left(data_dic[condi_q],score_q)
#       answera.append(len(data_dic[condi_q]) - left_index)
#     else:
#       answera.append(0)

#   return answera


# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


