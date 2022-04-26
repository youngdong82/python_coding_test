
# -------------------------------------------------------------------------------- 5. 124나라의 숫자
# ------------------------------------------- 내꺼 3번째 24분 컷!!!!!!
# def solution(num):
#   tmp = ''
#   while num > 0:
#     num,rest = divmod(num,3)
#     if rest == 0:
#       rest = '4'
#       num -= 1
#     tmp += str(rest)
#   return tmp[::-1]

# print(solution(2))
# print(solution(4))
# print(solution(12))
# print(solution(11))
# print(solution(37))

# -------------------------------------------------------------------------------- 8. 모음 사전
# ------------------------------------------- 내꺼 알고 푸니까 6분 컷! 3번째 6분 컷!!
# from itertools import product


# def solution(word):
#   alpha = 'AEIOU'
#   answer = []
#   for i in range(1,6):
#     candidates = list(product(alpha,repeat=i))
#     for i in candidates:
#       answer.append(''.join(i))
#   answer.sort()
#   return answer.index(word)+1

# print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
# print(solution("EIO"))

# -------------------------------------------------------------------------------- 5. 큰 수 만들기  - 복복습!!
# permutation쓸 수 있지만 number가 1,000,000이라 사용하면 터진다
# ------------------------------------------- 내꺼 역시나 시간초과 구현 자체도 어려워
# def solution(number, k):
#   answer = []
#   for num in number:
#     while answer and k > 0 and answer[-1] < num:
#       answer.pop()
#       k -= 1
#     answer.append(num)
#     print(answer)
#   answer = ''.join(answer[:len(number)-k])

#   return answer

# print(solution("1924",2))
# print(solution("1294",2))
# print(solution("1941",2))
# print(solution("1231234",3))
# print(solution("4177252841",4))
# print(solution("654321",1))
# print(solution("654321",5))

# -------------------------------------------------------------------------------- 1. 행렬 테두리 회전하기
# 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의
# 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 
# ------------------------------------------- 내꺼 ㅅㅂ 졸라 오래걸리긴 했지만 풀었다. 3번째 40분 컷!!!
# 접근법은 같으나 커뮤니티 배울 필요가 있다.

# def solution(rows, columns, queries):
#   graph = []
#   index = 0
#   for i in range(rows):
#     tmp = []
#     for j in range(columns):
#       index += 1
#       tmp.append(index)
#     graph.append(tmp)

#   answer = []
#   for query in queries:
#     sx,sy,ex,ey = query
#     sx -= 1
#     sy -= 1
#     ex -= 1
#     ey -= 1
#     max_value = rotate(graph,sx,sy,ex,ey)
#     answer.append(max_value)

#   return answer

# def rotate(graph,sx,sy,ex,ey):
#   reck = []
#   # 왼쪽에서 오른쪽
#   tmp = 0
#   for i in range(ey,sy,-1):
#     if i == ey:
#       tmp = graph[sx][i]
#     graph[sx][i] = graph[sx][i-1]
#     reck.append(graph[sx][i])

#   # 위에서 아래
#   tmp2 = 0
#   for i in range(ex,sx,-1):
#     if i == ex:
#       tmp2 = graph[i][ey]
#     if i == sx+1:
#       graph[i][ey] = tmp
#     else:
#       graph[i][ey] = graph[i-1][ey]
#     reck.append(graph[i][ey])

#   # 오른쪽에서 왼쪽
#   tmp3 = 0
#   for i in range(sy,ey):
#     if i == sy:
#       tmp3 = graph[ex][i]
#     if i == ey-1:
#       graph[ex][i] = tmp2
#     else:
#       graph[ex][i] = graph[ex][i+1]
#     reck.append(graph[ex][i])

#   # 아래에서 위
#   for i in range(sx,ex):
#     if i == ex-1:
#       graph[i][sy] = tmp3
#     else:
#       graph[i][sy] = graph[i+1][sy]
#     reck.append(graph[i][sy])

#   return min(reck)

      

# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(10,9,[[1,1,10,9]]))

# -------------------------------------------------------------------------------- 7. 삼각 달팽이
# ------------------------------------------- 내꺼 19분 컷!! 기쁘다!! 재귀로 구현하니까 recursive maximum뜬다??
# import sys

# sys.setrecursionlimit(10001)
# dx = [1,0,-1]
# dy = [0,1,-1]

# def solution(n):
#   n = int(n)
#   graph = [[0] * n for _ in range(n)]

#   x,y = -1,0
#   graph[x][y] = 0
#   i = 0
#   dfs(graph,x,y,i,n)
#   asnwer = []
#   for i in graph:
#     for j in i:
#       if j != 0:
#         asnwer.append(j)
#   return asnwer

# def dfs(graph,x,y,i,n):
#   if n == 0:
#     return
#   for _ in range(n):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     graph[nx][ny] = graph[x][y] + 1
#     x,y = nx,ny
#   i = (i+1)%3
#   dfs(graph,x,y,i,n-1)

# print(solution(1))
# print(solution(4))
# print(solution(5))
# print(solution(100))
# print(solution(1000))


# -------------------------------------------------------------------------------- 9. 2개 이하로 다른 비트
# https://art-coding3.tistory.com/46
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8-Python
# 100,000개의 길이가 10의 15승 만큼 있다...?
# ------------------------------------------- 내꺼 실패 두번째 17분 컷!! 기쁘다!! 3번째 18분 컷!!
# def solution(numbers):
#   answer = []
#   for i in numbers:
#     i = int(i)
#     bit = bin(i)[2:]
#     rjust_bit = bit.rjust(len(bit)+1,'0')
#     bit_list = list(rjust_bit)

#     a = rjust_bit.rfind('0')
#     if a == len(rjust_bit)-1:
#       bit_list[a] = '1'
#     else:
#       bit_list[a],bit_list[a+1] = bit_list[a+1],bit_list[a]

#     answer.append(int(''.join(bit_list),2))
#   return answer


# print(solution([2,7,9]))

# -------------------------------------------------------------------------------- 5. 거리두기 확인하기
# 맨해튼 거리1가 2 이하
# 파티션 x, 빈자리o, 응시자 p
# ------------------------------------------- 내꺼 두번째 35분 컷!! 3번째 실패!
# from collections import deque
# from copy import deepcopy

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# def dfs(graph,x,y,dist):
#   if graph[x][y] != 'P':
#     return True
#   graph[x][y] = dist
#   q = deque([(x,y,dist)])
#   while q:
#     now_x, now_y, now_dist = q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0<= nx < 5 and 0<= ny < 5:
#         if graph[nx][ny] == 'P':
#           if now_dist+1 > 2:
#             graph[nx][ny] = now_dist+1
#             q.append((nx,ny,now_dist+1))
#           else:
#             return False
#         elif graph[nx][ny] == 'O':
#           graph[nx][ny] = now_dist+1
#           q.append((nx,ny,now_dist+1))
#   return True

# def solution(places):
#   result = []
#   for place in places:
#     for i in range(len(place)):
#       place[i] = list(place[i])

#     p_list = []
#     for i in range(5):
#       for j in range(5):
#         if place[i][j] == 'P':
#           p_list.append((i,j))
    
#     answer = 1
#     for i in p_list:
#       if answer == 0:
#         break
#       copy_place = deepcopy(place)
#       if dfs(copy_place,i[0],i[1],0) == False:
#         answer = 0

#     result.append(answer)
#   return result


# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# -------------------------------------------------------------------------------- 1. 후보키 실패! 복복습 필수!!!
# 컬럼(column)의 길이는 1 이상 8 이하
# 로우(row)의 길이는 1 이상 20 이하
# 모든 문자열의 길이는 1 이상 8 이하
# ------------------------------------------- 커뮤니티 뭔가 간단해보이는데 로직 자체도 뭔가 복잡하네... 
# from itertools import combinations

# def solution(relation):
#   n_row = len(relation)
#   n_col = len(relation[0])

#   candidates=[]
#   for i in range(1,n_col+1):
#     candidates.extend(combinations(range(n_col),i))
  
#   final=[]
#   for keys in candidates:
#     tmp=[]
#     for item in relation:
#       ttuple = ''
#       for key in keys:
#         ttuple += item[key]
#       tmp.append(ttuple)
#     if len(set(tmp)) == n_row:
#       final.append(keys)

#   answer = set(final[:])

#   for i in range(len(final)):
#     for j in range(i+1,len(final)):
#       if len(final[i]) == len(set(final[i]) & set(final[j])):
#         print(final[i], final[j])
#         answer.discard(final[j])

#   return answer


# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))


# -------------------------------------------------------------------------------- 2. 조이스틱 복복습!!!
# ------------------------------------------- 내꺼 실패!! 두번째 45분 컷! 
# 3번째 푼 결과
# 2번째도 운 좋게 통과했을 뿐이었다.
# -------------------------------------------  커뮤니티 배우자...간결하다
# 연속되는 A가 있을 때, 그것의 왼쪽이나 오른쪽부터 시작하며 알파벳을 변경하는 것이 가장 효율적
# ref: https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy

# def solution(name):
#   answer = 0
#   min_move = len(name) - 1
#   for i, char in enumerate(name):
#     answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
#     # 해당 알파벳 다음부터 연속된 A 문자열 찾기
#     next = i + 1
#     while next < len(name) and name[next] == 'A':
#       next += 1
#     print('next', next)
#     # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
#     min_move = min([min_move,  2 *i + len(name) - next,  i + 2 * (len(name) -next)])
#     print(min_move)
#   answer += min_move
#   return answer


# print(solution("BBABAAAABBBAAAABABB"))
# print(solution("BBAAAAAABBBAAAAAABB"))
# print(solution("AAAAADAAAAA"))
# print(solution("AABAAABAAAA"))
# print(solution("AADAAAADADA"))
# print(solution("AADAAAAAADADA"))
# print(solution("AAAAADAAADAA"))
# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("A"))
# print(solution("D"))

# -------------------------------------------------------------------------------- 4. [1차] 뉴스 클러스터링 복복습!!
# ------------------------------------------- 내꺼 3번째 50분 컷!
# def solution2(str1, str2):
#   str_1_reck = []
#   str1 = str1.upper()
#   for i in range(len(str1)-1):
#     tmp = str1[i]+str1[i+1]
#     if tmp.isalpha():
#       str_1_reck.append(tmp)

#   str_2_reck = []
#   str2 = str2.upper()
#   for i in range(len(str2)-1):
#     tmp = str2[i]+str2[i+1]
#     if tmp.isalpha():
#       str_2_reck.append(tmp)

#   # dic에 몇개씩 들어갔는지 세자.
#   dic_1 = {}
#   for i in str_1_reck:
#     if i not in dic_1.keys():
#       dic_1[i] = 1
#     else:
#       dic_1[i] += 1

#   dic_2 = {}
#   for i in str_2_reck:
#     if i not in dic_2.keys():
#       dic_2[i] = 1
#     else:
#       dic_2[i] += 1

#   AND = {}
#   OR = {}
#   for key1,value1 in dic_1.items():
#     OR[key1] = value1

#     for key2,value2 in dic_2.items():
#       if key1 == key2:
#         AND[key1] = min(value1,value2)
#         OR[key2] = max(OR[key2],value2)
#       else:
#         if key2 in OR.keys():
#           OR[key2] = max(OR[key2],value2)
#         else:
#           OR[key2] = value2

#   len_and = 0
#   len_or = 0
#   for i in AND.values():
#     len_and += i
#   for i in OR.values():
#     len_or += i

#   if len_and == 0 and len_or == 0:
#     return 65536
#   else:
#     return int(len_and / len_or * 65536)

# ------------------------------------------- 커뮤
# from collections import Counter

# def solution(str1, str2):
#     str1_low = str1.lower()
#     str2_low = str2.lower()

#     str1_lst = []
#     str2_lst = []

#     for i in range(len(str1_low)-1):
#         if str1_low[i].isalpha() and str1_low[i+1].isalpha():
#             str1_lst.append(str1_low[i] + str1_low[i+1])
#     for j in range(len(str2_low)-1):
#         if str2_low[j].isalpha() and str2_low[j+1].isalpha():
#             str2_lst.append(str2_low[j] + str2_low[j+1])

#     Counter1 = Counter(str1_lst)
#     Counter2 = Counter(str2_lst)

#     inter = list((Counter1 & Counter2).elements())
#     union = list((Counter1 | Counter2).elements())

#     if len(union) == 0 and len(inter) == 0:
#         return 65536
#     else:
#         return int(len(inter) / len(union) * 65536)

# print(solution('FRANCE','french'))
# print(solution('handshake','shake hands'))
# print(solution('aa1+aa2','AAAA12'))
# print(solution('E=M*C^2','e=m*c^2'))

# print(solution('abcde','fghij'))
# print(solution('abc','abbb'))
# print(solution('aa1+aa2','AA12'))
# print(solution('aaabb','aabbb'))
# print(solution('aabbb','aaabb'))

# -------------------------------------------------------------------------------- 5. 수식 최대화
# 완전탐색???
# ------------------------------------------- 내꺼
# from itertools import permutations


# def solution(expression):
#   data = []
#   tmp = ''
#   for i in range(len(expression)):
#     if expression[i] in ['-','+','*']:
#       data.append(int(tmp))
#       data.append(expression[i])
#       tmp = ''
#     else:
#       tmp += expression[i]
#     if i == len(expression)-1:
#       data.append(int(tmp))
  
#   answer = []
#   prefers = list(permutations(['-','+','*'], 3))
#   for prefer in prefers:
#     stack = []
#     for i in prefer:
#       for j in range(len(data)):
#         if i == data[j]:
#           tmp = stack.pop()
#           stack.append(calculate(tmp,i,data[j+1]))
#         else:
#           # stack이 있을 경우
#           if len(stack):
#             if data[j] in ['-','+','*']:
#               stack.append(data[j])
#             else:
#               # stack[-1]이 문자일경우 무조건 넣어
#               if stack[-1] in ['-','+','*']:
#                 stack.append(data[j])
#           # stack이 비었을 경우
#           else:
#             stack.append(data[j])
#     data = stack
#     stack = []

          
#     answer.append(stack[0])
#   return answer

# def calculate(a,oper,b):
#   if oper == '+':
#     return a+b
#   elif oper == '-':
#     return a-b
#   elif oper == '*':
#     return a*b
      


# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

# -------------------------------------------------------------------------------- 6. 쿼드압축 후 개수 세기
# 재귀함수
# ------------------------------------------- 커뮤 간단해보이는데 굉장히 짜임새 있게 잘 짜여있다...
# def solution(arr):
#   constant_n = len(arr)
#   n = constant_n
#   answer = [0,0]
#   while n > 0:
#     # 시작포인트
#     for i in range(0,constant_n,n):
#       for j in range(0,constant_n,n):
#         if arr[i][j] in [0,1]:
#           toggle = True
#           for i2 in range(n):
#             if not toggle:
#               break
#             for j2 in range(n):
#               if arr[i][j] != arr[i+i2][j+j2]:
#                 toggle = False
#                 break
#           # 전부 같다면
#           if toggle:
#             if arr[i][j] == 0:
#               answer[0] += 1
#             else:
#               answer[1] += 1
#             # 전부 다 바꾸고
#             for i2 in range(n):
#               for j2 in range(n):
#                 arr[i+i2][j+j2] = 'X'
#           # 전부 안같다면
#           else:
#             continue
#           # for each in arr:
#           #   print(each)
#           # print()
#     n //= 2
#   return answer


# print(solution([[1]]))
# print(solution([[1,0],[1,1]]))
# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))