# -------------------------------------------------------------------------------- 1. 오픈채팅방
# ------------------------------------------- 내꺼
# dic쓸거 list 써서 개고생했네 진짜....
# ------------------------------------------- 커뮤니티 왐마.... dic쓰자
# def solution(records):
#     answer = []
#     userdict = {}
#     for record in records: 
#         if (record.split(' ')[0] == 'Enter') | (record.split(' ')[0] == 'Change'):
#             userdict[record.split(' ')[1]] = record.split(' ')[2]

#     for record in records: 
#         if record.split(' ')[0] == 'Enter': 
#             answer.append("{}님이 들어왔습니다.".format(userdict[record.split(' ')[1]]))
#         elif record.split(' ')[0] == 'Leave': 
#             answer.append("{}님이 나갔습니다.".format(userdict[record.split(' ')[1]]))
#         else:
#             pass
#     return answer

# print(solution([
#   "Enter uid1234 Muzi", 
#   "Enter uid4567 Prodo",
#   "Leave uid1234",
#   "Enter uid1234 Prodo",
#   "Change uid4567 Ryan"
#   ]))

# -------------------------------------------------------------------------------- 2. 짝지어 제거하기
# ------------------------------------------- 내꺼 10분 컷!!
# def solution(s):
#   stack = []
#   for i in s:
#     if len(stack) == 0:
#       stack.append(i)
#     elif len(stack) != 0 and stack[-1] == i:
#       stack.pop()
#     elif len(stack) != 0 and stack[-1] != i:
#       stack.append(i)

#   if len(stack) == 0:
#     return 1
#   else:
#     return 0
      

# print(solution('baabaa'))
# print(solution('cdcd'))

# -------------------------------------------------------------------------------- 3. 최솟값 만들기
# ------------------------------------------- 내꺼 시간초과
# def solution(A,B):
#   answer = 0
#   for i in range(len(A)):
#     answer += min(A)*max(B)
#     A.remove(min(A))
#     B.remove(max(B))
#   return answer

# ------------------------------------------- 내꺼 2분컷...근데 뻘짓하느라 20분을 날려먹었다.
# def solution(A,B):
#   n = len(A)
#   answer = 0
#   A.sort()
#   B.sort(reverse=True)

#   for i in range(n):
#     answer += A[i] * B[i]
#   return answer

# print(solution([1, 4, 2], [5, 4, 4]))
# print(solution([1,2], [3,4]))

# -------------------------------------------------------------------------------- 4. 땅따먹기  - 실패! - 복습!!!!
# ------------------------------------------- 내꺼 시간초과
# def max_index(array, ban):
#   max_value = 0
#   index = 0
#   for i in range(4):
#     if ban != None:
#       if array[i] > max_value and i != ban:
#         max_value = array[i]
#         index = i
#     else:
#       if array[i] > max_value:
#         max_value = array[i]
#         index = i
#   return max_value, index


# def solution(array):
#   n = len(array)
#   maxx, index = max_index(array[0], None)
#   answer = maxx

#   for i in range(1,n):
#     maxx, index = max_index(array[i], index)
#     answer += maxx

#   return answer
# ------------------------------------------- 커뮤니티 와 이건 미쳤다 
# def solution(land):
#   for i in range(1,len(land)):
#       for j in range(4):
#           land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
#   return max(land[-1])


# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
# -------------------------------------------------------------------------------- 5. 124나라의 숫자 실패! - 복습!!
# ------------------------------------------- 내꺼
# def solution(n):
#   answer = []
#   a = 1
#   while True:
#     if n < (3**a):
#       break
#     else:
#       a += 1
#   for i in range(a-1,-1,-1):
#     if i == 0:
#       answer.append(n)
#       break
#     answer.append(n // (3**i))
#     n -= (3**i)

#   return answer

# ------------------------------------------- 커뮤니티
# def solution(n):
#     answer = ''
#     while n:
#         if n % 3:
#             answer += str(n % 3)
#             n //= 3
#         else:
#             answer += "4"
#             n = n//3 - 1
#     return answer[::-1]

# ------------------------------------------- 커뮤니티 2 이게 더 깔끔 이걸 어떻게 알아내냐...
# def change124(n):
#     num = ['1','2','4']
#     answer = ""
#     while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3

#     return answer
# print(solution(11))
# print(solution(12))
# print(solution(13))
# print(solution(14))
# print(solution(15))

# -------------------------------------------------------------------------------- 6. 게임 맵 최단거리
# ------------------------------------------- 내꺼 시간초과 32분 컷!
# from collections import deque

# def solution(maps):
#   n = len(maps)
#   m = len(maps[0])
#   dx = [0,1,0,-1]
#   dy = [-1,0,1,0]

#   def bfs(graph, x,y):
#     q = deque([(x,y)])
#     graph[y][x] = 2
#     while q:
#       now = q.popleft()
#       now_x, now_y = now
#       for i in range(4):
#         nx = now_x + dx[i]
#         ny = now_y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n:
#           if graph[ny][nx] == 1:
#             graph[ny][nx] = graph[now_y][now_x] + 1
#             q.append((nx,ny))

#   bfs(maps, 0,0)
#   if maps[n-1][m-1] in [0,1]:
#     return -1
#   else:
#     return maps[n-1][m-1] -1

# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

# -------------------------------------------------------------------------------- 7. 숫자의 표현
# ------------------------------------------- 내꺼 20분 컷!
# def solution(n):
#   summ = 0
#   count = 0
#   index1 = 1
#   index2 = 1
#   while index1 <= n//2 + 1 or index2 <= n//2 + 1:
#     if summ < n:
#       summ += index2
#       index2 += 1
#     elif summ > n:
#       summ -= index1
#       index1 += 1
#     else:
#       count += 1
#       summ += index2
#       index2 += 1
#   return count + 1


# print(solution(15))

# -------------------------------------------------------------------------------- 8. 모음 사전 - 실패! 복습!!
# ------------------------------------------- 커뮤니티 완전탐색이래 + product
# from itertools import product

# def solution(word):
#     list1 = ['A','E','I','O','U']
#     list2 = list(product('AEIOU',repeat=2))
#     list3 = list(product('AEIOU',repeat=3))
#     list4 = list(product('AEIOU',repeat=4))
#     list5 = list(product('AEIOU',repeat=5))
#     data_list = list1 + list2 + list3 + list4 + list5

#     for i in range(len(data_list)):
#         data_list[i] = ''.join(data_list[i])
#     data_list.sort()
#     return data_list.index(word) + 1

# print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
# print(solution("EIO"))

# -------------------------------------------------------------------------------- 9. 구명보트 - 28분 컷 - 시간초과
# 다음엔 deque로 풀어보자
# ------------------------------------------- 내꺼 - 시간초과
# def solution(people, limit):
#   people.sort()
#   count = 0
#   while people:
#     if len(people) >= 2 and people[0] + people[-1] <= limit:
#       people.pop()
#       people.pop(0)
#       count += 1
#     else:
#       people.pop()
#       count += 1

#   return count

# # ------------------------------------------- 내꺼 성공~
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

# print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))

# -------------------------------------------------------------------------------- 10. 스킬트리 21분 컷!
# ------------------------------------------- 내꺼 + for else
# def solution(skill, skill_trees):
#   count = 0
#   for tree in skill_trees:
#     skill_index = 0
#     for i in tree:
#       if i in skill:
#         if i == skill[skill_index]:
#           skill_index += 1
#           if skill_index == len(skill):
#             count += 1
#             break
#         else:
#           break
#     else:
#       count += 1

#   return count

# # ------------------------------------------- 커뮤니티 훨씬 깔끔하다.
# def solution(skill, skill_trees):
#   count = 0
#   for skills in skill_trees:
#       skill_list = list(skill)
#       for s in skills:
#           if s in skill:
#               if s != skill_list.pop(0):
#                   break
#       else:
#           count += 1
#   return count


# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))