# -------------------------------------------------------------------------------- Counter 와 element
# 4. [1차] 뉴스 클러스터링
  # inter = list((Counter1 & Counter2).elements())
  # union = list((Counter1 | Counter2).elements())

# -------------------------------------------------------------------------------- sort와 string
# strnig은 sort()사용 못함
# 그러나
# sorted는 가능

# -------------------------------------------------------------------------------- 집합연산자
# a = {1,2,3,4,5}
# b = {1,3,5,7,9}
# ------------------------------------- or 합집합
# print(a|b)
# print(set.union(a,b))
# print(a.union(b))

# ------------------------------------- and 교집합
# print(a&b)
# print(set.intersection(a,b))
# print(a.intersection(b))

# ------------------------------------- and 차집합
# print(a-b)
# print(set.difference(a,b) ) 
# print(a.difference(b))

# ------------------------------------- remove 와 discard
# remove()는 실제 존재하는 대상을 지우는 동작
# 대상이 없다면 에러

# discard()는 존재하지 않음을 보장하려고 할때 사용
# 대상이 없어도 에러가 나지 않는다.

# -------------------------------------------------------------------------------- 5. 124나라의 숫자 실패! - 복습!!
# ------------------------------------------- 내꺼
# def solution(n):
#     answer = ''
#     while n:
#         if n % 3:
#             answer += str(n % 3)
#             n //= 3
#         else:
#             answer += "4"
#             n = n//3 - 1
#         print(n)
#         print('answer',answer)
#     return answer[::-1]

# print(solution(2))
# print(solution(4))
# print(solution(7))
# print(solution(11))
# print(solution(37))

# -------------------------------------------------------------------------------- 8. 모음 사전
# 커뮤니티 완전탐색이래 + product 
# ------------------------------------------- 내꺼 알고 푸니까 6분 컷!
# from itertools import product


# def solution(word):
#   words = 'AEIOU'
#   answer = []
#   for i in words:
#     answer.append(i)
#   for i in list(product(words,repeat=2)):
#     answer.append(''.join(i))
#   for i in list(product(words,repeat=3)):
#     answer.append(''.join(i))
#   for i in list(product(words,repeat=4)):
#     answer.append(''.join(i))
#   for i in list(product(words,repeat=5)):
#     answer.append(''.join(i))
#   answer.sort()
#   return answer.index(word)+1

  
# print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
# print(solution("EIO"))

# -------------------------------------------------------------------------------- 5. 큰 수 만들기  - 복습!!
# ------------------------------------------- 내꺼 역시나 시간초과
# 백만짜리 숫자를 combinations...?
# 일단 해보자
# from itertools import combinations

# def solution(number, k):
#   candidate = list(combinations(number,len(number)-k))
#   candidate.sort()
#   tmp = candidate[-1]
#   answer = ''
#   for i in tmp:
#     answer += i

#   return answer

# ------------------------------------------- 커뮤 1 큐와 덱 문제다.
# def solution(number, k):
#   answer = []
#   for num in number:
#     while answer and k > 0 and answer[-1] < num:
#       answer.pop()
#       k -= 1
#     answer.append(num)
#   answer = ''.join(answer[:len(number)-k])

#   return answer

# ------------------------------------------- 커뮤 2 큐와 덱 문제다.
# from collections import deque


# def solution(number, k):
#     q = deque(list(number))
#     stack = deque()

#     while q and k:
#         while stack and stack[-1] < q[0]:
#             stack.pop()
#             k -= 1
#             if not k:
#                 break
#         stack.append(q.popleft())

#     # k를 소진시키지 못했을 수도 있다.
#     while k and stack:
#         stack.pop()
#         k -= 1

#     return "".join(stack + q)


# print(solution("1924",2))
# print(solution("1231234",3))
# print(solution("4177252841",4))
# print(solution("654321",1))
# print(solution("654321",5))

# -------------------------------------------------------------------------------- 1. 행렬 테두리 회전하기
# 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의
# 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 
# ------------------------------------------- 내꺼 ㅅㅂ 졸라 오래걸리긴 했지만 풀었다.
# 접근법은 같으나 커뮤니티 배울 필요가 있다.
# def circle(graph, queries):
#   answer = []
#   fx,fy,ex,ey = queries
#   fx = fx-1
#   fy = fy-1
#   ex = ex-1
#   ey = ey-1

#   tmp1 = graph[fx][fy]
#   tmp2 = graph[fx][ey]
#   tmp3 = graph[ex][fy]
#   tmp4 = graph[ex][ey]

#   for i in range(fx,ex):
#     graph[i][fy] = graph[i+1][fy]
#     answer.append(graph[i][fy])

#   for i in range(ey,fy,-1):
#     if i == fy+1:
#       graph[fx][i] = tmp1
#     else:
#       graph[fx][i] = graph[fx][i-1]
#     answer.append(graph[fx][i])

#   for i in range(ex,fx,-1):
#     if i == fx+1:
#       graph[i][ey] = tmp2
#     else:
#       graph[i][ey] = graph[i-1][ey]
#     answer.append(graph[i][ey])

#   for i in range(fy,ey):
#     if i == ey-1:
#       graph[ex][i] = tmp4
#     else:
#       graph[ex][i] = graph[ex][i+1]
#     answer.append(graph[ex][i])

#   return min(answer)


# def solution(rows, columns, queries):
#   graph = [[0] * columns for _ in range(rows)]
#   v = 0
#   result = []
#   for i in range(len(graph)):
#     for j in range(len(graph[0])):
#       v += 1
#       graph[i][j] = v
  
#   for query in queries:
#     result.append(circle(graph, query))

#   return result
  

# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(10,9,[[1,1,10,9]]))

# -------------------------------------------------------------------------------- 7. 삼각 달팽이
# ------------------------------------------- 내꺼 19분 컷!! 기쁘다!!
# 아래,오른,대각선 왼위
# dx = [1,0,-1]
# dy = [0,1,-1]

# def solution(n):
#   graph = [[0] * (i+1) for i in range(n)]
#   max_value = 0
#   if n % 2 == 0:
#     max_value = (n+1) * (n//2)
#   else:
#     max_value = ((n+1) * (n//2)) + (n//2+1)
  
#   d_index = 0
#   x = 0
#   y = 0
#   graph[x][y] = 1
#   if n == 1:
#     return [1]

#   while True:
#     nx = x + dx[d_index]
#     ny = y + dy[d_index]
#     if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
#       graph[nx][ny] = graph[x][y] + 1
#       if graph[nx][ny] == max_value:
#         break
#       x,y = nx,ny
#     else:
#       d_index = (d_index+1)%3

#   answer = []
    
#   for i in graph:
#     for j in i:
#       answer.append(j)

#   return answer

# print(solution(1))
# print(solution(4))
# print(solution(5))
# print(solution(1000))


# -------------------------------------------------------------------------------- 9. 2개 이하로 다른 비트
# https://art-coding3.tistory.com/46
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8-Python
# 100,000개의 길이가 10의 15승 만큼 있다...?
# 오른쪽에서부터 0을 찾은 다음에 
# 그 뒤에 1과 자리 바꿔
# ------------------------------------------- 내꺼 실패 두번째 17분 컷!! 기쁘다!!
# def solution(numbers):
#   answer = []
#   for number in numbers:
#     number = int(number)
#     if number % 2 == 0:
#       answer.append(number + 1)
#     else:
#       a = '0'
#       a += bin(number)[2:]
#       zero_i = a.rfind('0')
#       a = list(a)
#       a[zero_i],a[zero_i+1] = a[zero_i+1],a[zero_i]
#       answer.append(int(''.join(a),2))

#   return answer

# print(solution([2,7,9]))

# -------------------------------------------------------------------------------- 5. 거리두기 확인하기 실패!
# 맨해튼 거리1가 2 이하
# 애초에 q에 들어가는 값을 (x,y,거리)로 설정해서
# nx,ny할 때 nd라는 거리값도 +1 해주니 괜춘하네
# ------------------------------------------- 내꺼 두번째 35분 컷!!
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

# ------------------------------------------------------------------------------------------------ 220320
# -------------------------------------------------------------------------------- 1. 후보키 실패! 복습 필수!!!
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


# -------------------------------------------------------------------------------- 2. 조이스틱
# ------------------------------------------- 내꺼 실패!! 두번째 45분 컷!
# def solution(name):
#   alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#   name = str(name)
#   up_down = 0
#   for i in name:
#     normal_move = alpha.index(i)
#     up_down += min(normal_move, 26- normal_move)
  
#   left_right = 0
#   not_a = []
#   for i in range(1, len(name)):
#     if name[i] != 'A':
#       not_a.append(i)

#   if len(not_a) == 0:
#     left_right = 0
#   else:
#     left = not_a[-1]
#     right = len(name) - not_a[0]
#     max_index = 0
#     min_index = len(name)
#     mid = len(name)//2
#     for i in not_a:
#       if i <= mid:
#         max_index = max(max_index, i)
#       else:
#         min_index = min(min_index,i)
#     backward_left = (max_index * 2) + (len(name) - min_index)
#     backward_right = max_index + ((len(name) - min_index) * 2)
#     left_right = min(left, right, backward_left, backward_right)

#   return up_down + left_right


# print(solution("AADAAAADADA"))
# print(solution("AADAAAAAADADA"))
# print(solution("AAAAADAAADAA"))
# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("A"))
# print(solution("D"))


# -------------------------------------------------------------------------------- 4. [1차] 뉴스 클러스터링
# 자카드 유사도
# 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의
# 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
# Counter!!!
# ------------------------------------------- 내꺼
# from collections import Counter
# from math import floor


# def solution(str1, str2):
#   dic_1 = []
#   str1 = str1.lower()
#   for i in range(1,len(str1)):
#     frag = str1[i-1] + str1[i]
#     if frag.isalpha():
#       dic_1.append(frag)

#   dic_2 = []
#   str2 = str2.lower()
#   for i in range(1,len(str2)):
#     frag = str2[i-1] + str2[i]
#     if frag.isalpha():
#       dic_2.append(frag)

#   Counter1 = Counter(dic_1)
#   Counter2 = Counter(dic_2)

#   inter = list((Counter1 & Counter2).elements())
#   union = list((Counter1 | Counter2).elements())

#   if len(inter) == 0 and len(union) == 0:
#     answer = 65536
#   else:
#     answer = floor(len(union)/len(union) * 65536)
#   return int(answer)


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
# ------------------------------------------- 커뮤
# from itertools import permutations


# def operation(num1,num2,op):
#   if op == '*':
#     return str(int(num1) * int(num2))
#   if op == '+':
#     return str(int(num1) + int(num2))
#   if op == '-':
#     return str(int(num1) - int(num2))

# def calc(expression, op):
#   string = []
#   tmp = ''
#   for i in expression:
#     if i.isdigit():
#       tmp += i
#     else:
#       string.append(tmp)
#       string.append(i)
#       tmp = ''
#   string.append(tmp)
#   print(string)

#   for o in op:
#     print(o)
#     stack = []
#     while len(string) != 0:
#       tmp = string.pop(0)
#       if tmp == o:
#         stack.append(operation(stack.pop(), string.pop(0), o))
#       else:
#         stack.append(tmp)
#     string = stack

#   return abs(int(string[0]))

# def solution(expression):
#     op = list(permutations(['*','+','-'], 3))
#     result = []
#     for i in op:
#         result.append(calc(expression, i))
#     return max(result)


# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

# -------------------------------------------------------------------------------- 6. 쿼드압축 후 개수 세기
# 재귀함수
# ------------------------------------------- 커뮤 간단해보이는데 굉장히 짜임새 있게 잘 짜여있다...


