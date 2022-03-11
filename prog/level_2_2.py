# -------------------------------------------------------------------------------- 인덱스 슬라이싱 좀 더 적재적소에 사용하면 매우 유용하다.
# 9번 문제에서 used를 없앨 수 있다.
# 문자열 뒤짚기
# 문자열 [::-1]
# -------------------------------------------------------------------------------- from math import gcd, lcm
# -------------------------------------------------------------------------------- 진수 변환
# def make(num, n):
#   total_string = '0123456789ABCDEF'
#   string = total_string[:n]
#   answer = ''
#   while num > 0:
#       num, mod = divmod(num, n)
#       answer += str(string[mod])
#   return answer[::-1]


# -------------------------------------------------------------------------------- 1. 다음 큰 숫자 - 복습!
# ------------------------------------------- 내꺼 35분 컷! 너무 수학적으로 풀려고 하지 말자!
# def solution(n):
#   b_n = bin(n)[2:]
#   n1 = b_n.count('1')
#   next = 0
#   while True:
#     n += 1
#     aa = bin(n)[2:]
#     if aa.count('1') == n1:
#       next = n
#       break
#   return next

# print(solution(78))
# print(solution(15))

# -------------------------------------------------------------------------------- 2. 피로도
# ------------------------------------------- 내꺼 14분 컷!!
# from itertools import combinations, permutations

# def solution(k, dungeons):
#   candidates = list(permutations(dungeons, len(dungeons)))
  
#   max_count = 0
#   for candidate in candidates:
#     fatigue = k
#     count = 0
#     for dun in candidate:
#       if fatigue < dun[0]:
#         break
#       else:
#         fatigue -= dun[1]
#         count += 1
#     max_count = max(max_count, count)
      
#   return max_count

# ------------------------------------------- 커뮤니티 뭔가 재귀 dfs하면서 최대값 설정하는 것이 좋아보임.
# answer = 0
# N = 0
# visited = []

# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt
#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0

# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer

# print(solution(80, [[80,20],[50,40],[30,10]]))

# -------------------------------------------------------------------------------- 3. 행렬의 곱셈 실패! -- 복습!!
# ------------------------------------------- 커뮤니티
# def solution(arr1, arr2):
#   answer = []
  
#   for i in range(len(arr1)):
#     print(i)
#     temp_lst = []
#     for j in range(len(arr2[0])):
#       temp = 0
#       for k in range(len(arr2)):
#         temp += arr1[i][k] * arr2[k][j]
#       temp_lst.append(temp)
#     answer.append(temp_lst) 
    
#   for i in answer:
#     print(i)

# print(solution([[1,4], [3,2], [4,1]],  [[3,3], [3,3]]))
# print(solution([[2,3,2], [4,2,4], [3,1,4]],  [[5,4,3], [2,4,1], [3,1,1]]))

# -------------------------------------------------------------------------------- 4. 방문길이
# ------------------------------------------- 내꺼 32분 컷!!
# def solution(dirs):
#   dx = [0,1,0,-1]
#   dy = [-1,0,1,0]
#   now = (5,5)
#   count = 0
#   visited = []

#   def move(x, y, direc, visited,count):
#     nx = x + dx[direc]
#     ny = y + dy[direc]
#     if 0 <= nx < 11 and 0 <= ny < 11:
#       if (x,y,nx,ny) not in visited:
#         count += 1
#         visited.append((x,y,nx,ny))
#         visited.append((nx,ny,x,y))
#       now = (nx,ny)
#     else:
#       now = (x,y)
#     return now, count

#   dirs = list(dirs)

#   while dirs:
#     order = dirs.pop(0)
#     if order == 'U':
#       now,count = move(now[0], now[1], 0, visited, count)
#     elif order == 'R':
#       now,count = move(now[0], now[1], 1, visited, count)
#     elif order == 'D':
#       now,count = move(now[0], now[1], 2, visited, count)
#     else:
#       now,count = move(now[0], now[1], 3, visited, count)
  
#   return count
  
# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))

# ------------------------------------------- 커뮤니티 굉장히 깔끔하긴 하다...! 훌륭하다!!
# def solution(dirs):
#     s = set()
#     d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#     x, y = 0, 0
#     for i in dirs:
#         nx, ny = x + d[i][0], y + d[i][1]
#         if -5 <= nx <= 5 and -5 <= ny <= 5:
#             s.add((x,y,nx,ny))
#             s.add((nx,ny,x,y))
#             x, y = nx, ny
#     return len(s)//2
# -------------------------------------------------------------------------------- 5. 큰 수 만들기  - 복습!!
# ------------------------------------------- 내꺼 그냥 접근 방법자체가 문제였음(이게 가장 큰 문제지...)
# def solution(number, k):
#   def sub_ok(max_digit, number,k):
#     count = 0
#     ok = False
#     for digit in number:
#       if digit == max_digit:
#         ok = True
#         break
#       count += 1
#       if count > k:
#         break
#     return ok, count
#   # 1. 구성하고 있는 숫자 구하기, 정렬
#   consist = list(set(number))
#   consist.sort(reverse=True)

#   number = list(number)
#   for max_digit in consist:
#     ok, count = sub_ok(max_digit, number,k)
#     if ok:
#       for _ in range(count):
#         index = 0
#         while True:
#           if number[index] > max_digit:
#             index += 1
#             continue
#           number.remove(number[index])
#           print(number)
#           break
#       k -= count
#   answer = ''.join(number)
#   return answer

# ------------------------------------------- 커뮤니티 ㅅㅂ 이거 뭐여.... 오...훌륭하다!!
# answer는 number의 길이 - k만큼 슬라이싱 해준다.
# -> 슬라이싱은 index 바깥으로 나가도 괜찮음! 
# 일반적으로 k는 0일텐데 ex) k = 3 number = 1000000 이런 경우엔 k는 처음 인풋받은 그대로 유지됨
# 이럴 때 답은 뒷 숫자를 k개만큼 없애준 1000 이므로 슬라이싱을 len(number) - k로 해주는 것
# def solution(number, k):
#   answer = []
#   for num in number:
#     while answer and k > 0 and answer[-1] < num:
#       answer.pop()
#       k -= 1
#     answer.append(num)
#   # answer = ''.join(answer)
#   answer = ''.join(answer[:len(number)-k])
  
#   return answer

# print(solution("1924", 2))
# print(solution("1231234", 3))
# print(solution("4177252841", 4))
# -------------------------------------------------------------------------------- 6. 최댓값과 최솟값
# ------------------------------------------- 내꺼 11분 컷!
# def solution(s):
#   s_list = list(map(int,s.split(' ')))
#   s_list.sort()

#   answer = []
#   answer.append(str(min(s_list)))
#   answer.append(' ')
#   answer.append(str(max(s_list)))
#   return ''.join(answer)


# def solution(s):
#   s_list = list(map(int,s.split(' ')))
#   s_list.sort()

#   return str(min(s_list)) + ' ' + str(max(s_list))

# print(solution("1 2 3 4"))
# print(solution("-1 -2 -3 -4"))
# print(solution("-1 -1"))

# -------------------------------------------------------------------------------- 7. JadenCase 문자열 만들기
# ------------------------------------------- 내꺼 11분 컷!
# def solution(s):
#   s_split = list(map(list,s.split(' ')))
#   for word in s_split:
#     for i in range(len(word)):
#       if i == 0 and word[i].isalpha():
#         a = word[0].upper()
#         word[i] = a
#       elif i != 0:
#         b = word[i].lower()
#         word[i] = b
#   answer = []
#   for word in s_split:
#     answer.append(''.join(word))

#   return ' '.join(answer)

# print(solution("3people unFollowed me"))
# print(solution("for the last week"))
# -------------------------------------------------------------------------------- 8. n^2 배열 자르기 - 실패! 그래도 복습 할 가치가 있다!
# ------------------------------------------- 내꺼 시간초과
# def solution(n, left, right):
#   empty = [[1] * n for _ in range(n)]
#   for i in range(n):
#     for j in range(i):
#       empty[i][j] = i+1
#       empty[i][i] = i+1
#       empty[j][i] = i+1

#   answer = []
#   for i in empty:
#     for j in i:
#       answer.append(j)

#   return answer[left:right+1]
# ------------------------------------------- 내꺼 + 커뮤 시간초과
# def solution(n, left, right):
#   answer = []
#   for i in range(n*n):
#       a = i//n
#       b = i%n
#       if a<b: a,b =b,a
#       answer.append(a+1)
#   print(answer)
#   return answer[left:right+1]

# ------------------------------------------- 커뮤 와 미쳤다리부리...
# def solution(n, left, right):
#     answer = []
#     for i in range(left,right+1):
#         a = i//n
#         b = i%n 
#         if a<b: a,b =b,a
#         answer.append(a+1)
#     return answer

# print(solution(3,0,0))
# print(solution(4,7,14))

# -------------------------------------------------------------------------------- 9. 영어 끝말잇기  - 22분 컷!
# ------------------------------------------- 내꺼 
# from collections import defaultdict


# def solution(n, words):
#   used = []
#   player = defaultdict(int)
#   for i in range(n):
#     player[i] = 0

#   for i in range(len(words)):
#     if i>0 and words[i][0] != words[i-1][-1]:
#       return [i%n + 1, player[i%n]+1]
#     if words[i] in used:
#       return [i%n + 1, player[i%n]+1]
#     else:
#       player[i%n] += 1
#       used.append(words[i])
#   return [0,0]

# ------------------------------------------- 내꺼 + 커뮤니티
# def solution(n, words):
#   for i in range(1, len(words)):
#     if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
#       return [i%n + 1, i//n + 1]
#   else:
#     return [0,0]


# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# -------------------------------------------------------------------------------- 10. 멀쩡한 사각형 - 복습! gcd, lcm
# 이건 좀 그렇긴 하다... 너무 수학문제 느낌
# ------------------------------------------- 내꺼
# from math import gcd, lcm


# def solution(w,h):
#   a = gcd(w,h)
#   b = lcm(w,h)

#   print(a,b)


# print(solution(8,12))