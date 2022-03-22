# 전부 정리했고, 내일은 recap 7문제, timeout 3문제 fail 2문제 풀고 규민이꺼 좀 하자.
# -------------------------------------------------------------------------------- list와 string 처리의 속도차이 봐라...ㄷㄷ
# 짝지어 제거하기
# 문자열
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	통과 (88.60ms, 11.7MB)
# 테스트 3 〉	통과 (1233.56ms, 11.8MB)
# 테스트 4 〉	통과 (1323.38ms, 11.9MB)
# 테스트 5 〉	통과 (1322.84ms, 11.8MB)
# 테스트 6 〉	통과 (1323.41ms, 11.6MB)
# 테스트 7 〉	통과 (1317.05ms, 11.9MB)
# 테스트 8 〉	실패 (시간 초과)

# 리스트
# 테스트 1 〉	통과 (216.92ms, 16.3MB)
# 테스트 2 〉	통과 (151.76ms, 11.8MB)
# 테스트 3 〉	통과 (242.95ms, 12.2MB)
# 테스트 4 〉	통과 (242.51ms, 12.2MB)
# 테스트 5 〉	통과 (242.48ms, 12.2MB)
# 테스트 6 〉	통과 (240.88ms, 12.2MB)
# 테스트 7 〉	통과 (219.21ms, 12.3MB)
# 테스트 8 〉	통과 (258.94ms, 14.7MB)

# 결론
# 문자열 관련 내장함수 써야하는 것 아니면 리스트 변환 후 처리하는 것이 좋다.

# ------------------------------------------------------------------------------------------------ 220317
# -------------------------------------------------------------------------------- 2. 짝지어 제거하기
# ------------------------------------------- 내꺼 시간초과!
# def solution(s):
#   tmp = ''
#   for i in s:
#     if len(tmp) != 0 and tmp[-1] == i:
#       tmp = tmp[:-1]
#       continue
#     tmp += i
#   if tmp == '':
#     return 1
#   else:
#     return 0

# ------------------------------------------- 내꺼 2 문자열과 list의 속도차이...!!!
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
# ------------------------------------------- 내꺼 / 2번째 - 4분 컷!
# def solution(A,B):
#   A.sort()
#   B.sort(reverse=True)
#   answer = 0
#   for i,j in zip(A,B):
#     answer += (i*j)

#   return answer

# ------------------------------------------- 내꺼 / 1번째 이게 평균적으로 더 빠르긴 하다.
# zip과 인덱싱 처리의 차이
# 무조건 내장함수 사용이 좋은 건 아닐 수도 있다!!

# def solution(A,B):
#   n = len(A)
#   answer = 0
#   A.sort()
#   B.sort(reverse=True)

#   for i in range(n):
#     answer += A[i] * B[i]
#   return answer

# print(solution([1,4,2],	[5,4,4]))
# print(solution([1,2], [3,4]))

# -------------------------------------------------------------------------------- 1. 오픈채팅방
# dic으로 시도, 실패
# list 시도, 시간초과 뜸
# ------------------------------------------- 내꺼 
# def solution(records):
#   answer = []
#   for record in records:
#     record = record.split(' ')

#     if record[0] == 'Enter':
#       for i in answer:
#         if i[1] == record[1]:
#           i[2] = record[2]
#           if i[0] == 'Enter':
#             i[3] = f'{record[2]}님이 들어왔습니다.'
#           else:
#             i[3] = f'{record[2]}님이 나갔습니다.'
#       else:
#         answer.append([record[0],record[1],record[2],f'{record[2]}님이 들어왔습니다.'])

#     elif record[0] == 'Leave':
#       for i in answer:
#         if i[1] == record[1]:
#           username = i[2]
#       answer.append([record[0],record[1],username,f'{username}님이 나갔습니다.'])

#     elif record[0] == 'Change':
#       for i in answer:
#         if i[1] == record[1]:
#           i[2] = record[2]
#           if i[0] == 'Enter':
#             i[3] = f'{record[2]}님이 들어왔습니다.'
#           else:
#             i[3] = f'{record[2]}님이 나갔습니다.'
#   real_answer = []
#   for i in answer:
#     real_answer.append(i[-1])
  
#   return real_answer

# ------------------------------------------- dic을 이렇게 쓰는거구나...ㅋㅋㅋㅋㅋ
# def solution(records):
#   answer = []
#   userdict = {}
#   for record in records:
#     i = record.split(' ')
#     if (i[0] == 'Enter') | (i[0] == 'Change'):
#       userdict[i[1]] = i[2]

#   for record in records: 
#     i = record.split(' ')
#     if i[0] == 'Enter': 
#       answer.append(f"{userdict[i[1]]}님이 들어왔습니다.")
#     elif i[0] == 'Leave': 
#       answer.append(f"{userdict[i[1]]}님이 나갔습니다.")
#     else:
#       pass
#   return answer


# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# -------------------------------------------------------------------------------- 7. 숫자의 표현 얼탱이가 없네;; 오늘 밤에 다시 풀자
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
# -------------------------------------------------------------------------------- 10. 스킬트리 21분 컷!
# ------------------------------------------- 내꺼  뭔가 아무렇게나 막푸는 느낌... 뭐징ㅋㅋㅋ
# def solution(skill, skill_trees):
#   count = len(skill_trees)
#   for skill_tree in skill_trees:
#     tmp_skill = skill
#     for i in skill_tree:
#       if i in tmp_skill and i != tmp_skill[0]:
#         count -= 1
#         break
#       elif i in tmp_skill and i == tmp_skill[0]:
#         tmp_skill= tmp_skill[1:]

#   return count

# ------------------------------------------- 내꺼 + for else
# def solution(skill, skill_trees):
#   count = 0
#   for tree in skill_trees:
#     skill_index = 0
#     for i in range(len(tree)):
#       if tree[i] in skill:
#         if tree[i] == skill[skill_index]:
#           skill_index += 1
#           if skill_index == len(skill):
#             count += 1
#             break
#         else:
#           break
#       if i == len(tree)-1:
#         count += 1

#   return count


# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

# -------------------------------------------------------------------------------- 1. 다음 큰 숫자 3분 컷ㅋㅋㅋㅋㅋ
#  n보다 큰 자연수
#  n은 2진수로 변환했을 때 1의 갯수가 같습니다.
#  다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수
# ------------------------------------------- 내꺼 35분 컷! 너무 수학적으로 풀려고 하지 말자!
# 아 그게 그 뜻이었구나...
# def solution(n):
#   bin_n = bin(n)[2:]
#   many = bin_n.count('1')
#   while True:
#     n += 1
#     if bin(n)[2:].count('1') == many:
#       break
#   return n
  
# print(solution(78))
# print(solution(15))
# print(solution(32))

# ------------------------------------------------------------------------------------------------ 220318
# -------------------------------------------------------------------------------- 2. 피로도
# 던전의 갯수 1 이상 8 이하 완전탐색 쌉가능
# ------------------------------------------- 내꺼 14분 컷!! 두번째 8분 컷!
# from itertools import permutations

# def solution(k, dungeons):
#   max_value = 0
#   candidates = list(permutations(dungeons,len(dungeons)))
#   for candidate in candidates:
#     hp = k
#     count = 0
#     for each in candidate:
#       if hp >= each[0]:
#         hp -= each[1]
#         count += 1
#       else:
#         break
#     max_value = max(max_value, count)

#   return max_value


# print(solution(80, [[80,20],[50,40],[30,10]]))

# -------------------------------------------------------------------------------- 3. 행렬의 곱셈 실패! -- 복습!!
# ------------------------------------------- 커뮤니티 ㅋㅋㅋ이건 끝까지 못 푸네 
# def solution(arr1,arr2):
#   answer = []
#   for i in range(len(arr1)):
#     s_answer = []
#     for j in range(len(arr1[0])):
#       tmp = 0
#       for k in range(len(arr2)):
#         tmp += arr1[i][k] * arr2[k][j]
#       s_answer.append(tmp)
#     answer.append(s_answer)
#   print(answer)


# print(solution([[1,4],[3,2],[4,1]], [[3,3],[3,3]]))
# print(solution([[2,3,2],[4,2,4],[3,1,4]], [[5,4,3],[2,4,1],[3,1,1]]))

# -------------------------------------------------------------------------------- 6. 최댓값과 최솟값
# ------------------------------------------- 내꺼 11분 컷! 두번째 4분 컷!
# def solution(s):
#   s = list(map(int,s.split(' ')))
#   return f'{min(s)} {max(s)}'


# print(solution("1 2 3 4"))
# print(solution("-1 -2 -3 -4"))
# print(solution("-1 -1"))

# -------------------------------------------------------------------------------- 7. JadenCase 문자열 만들기
# ------------------------------------------- 내꺼 11분 컷! 두번째 5분 컷!
# def solution(s):
#   s = s.split(' ')
#   answer = []
#   for word in s:
#     word = list(word)
#     for i in range(len(word)):
#       if i== 0 and word[i].isdigit():
#         continue
#       elif i == 0:
#         word[i] = word[i].upper()
#       else:
#         word[i] = word[i].lower()
#     answer.append(''.join(word))
#   return ' '.join(answer)

# print(solution("3people unFollowed me"))
# print(solution("for the last week"))

# -------------------------------------------------------------------------------- 9. 영어 끝말잇기 
# 가장 먼저 탈락하는 사람의 번호
# 그 사람이 자신의 몇 번째 차례에 탈락하는지
# ------------------------------------------- 내꺼 
# 첫번째는 defaultdict를 이용해서 풀었는데 성능, 깔끔함 전부 두번째가 더 좋다.
# ------------------------------------------- 내꺼 22분 컷! 두번째 10분 컷!
# def solution(n, words):
#   used = []
#   answer = 0
#   for i in range(len(words)):
#     if i != 0 and words[i][0] != words[i-1][-1]:
#       answer = i
#       break
#     if words[i] in used:
#       answer = i
#       break
#     used.append(words[i])
#   if answer == 0:
#     return [0,0]
#   else:
#     time, num = divmod(answer, n)
#     return [num+1,time+1]


# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# -------------------------------------------------------------------------------- 10. 멀쩡한 사각형
# 이건 좀 그렇긴 하다... 너무 수학문제 느낌
# 이걸 어케 알아 ㅅㅂ 일단 패스...
# ------------------------------------------- 내꺼
# def solution(w,h):
#   a = w
#   b = h
#   while(a!=b):
#     if(a>b): 
#       a -= b
#     else: 
#       b -= a
#   return (w*h) - (w+h-a)

# print(solution(8,12))

# -------------------------------------------------------------------------------- 3. N개의 최소공배수 11분 컷!
# ------------------------------------------- 내꺼 lcm 사용
# from math import gcd

# def solution(arr):
#   answer = arr[0]
#   for i in arr:
#     answer = (i * answer) // gcd(answer, i)

#   return answer


# print(solution([2,6,8,14]))
# print(solution([1,2,3]))

# ------------------------------------------------------------------------------------------------ 220320
# -------------------------------------------------------------------------------- 6. 전력망을 둘로 나누기 30분 컷!
# 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때,
# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return

# 완전탐색으로 차례대로 하나씩 끊었을 때 갯수 차이가 가장 작은 값 리턴
# ------------------------------------------- 커뮤 union 으로 풀어보려했는데 실패... 어렵다. 집중도 잘 안돼
parent = []

def find(a):
    global parent
    if parent[a] < 0: 
      return a
    parent[a] = find(parent[a])
    return parent[a]

def merge(a, b):
    global parent
    pa = find(a)
    pb = find(b)
    if pa == pb:
      return
    parent[pa] += parent[pb]
    parent[pb] = pa

def solution(n, wires):
    global parent
    answer = int(1e9)
    k = len(wires)

    for i in range(k):
        parent = []
        for _ in range(n+1):
          parent.append(-1)

        tmp = []
        for x in range(k):
          if x != i:
            tmp.append(wires[x])

        for a, b in tmp:
          merge(a, b)

        v = []
        for x in parent[1:]:
          if x < 0:
            v.append(x)
        answer = min(answer, abs(v[0]-v[1]))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# print(solution(4, [[1,2],[2,3],[3,4]]))
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))

# -------------------------------------------------------------------------------- 10. 배달 
# ------------------------------------------- 내꺼 두번째 25분 컷!!
# import heapq

# INF = int(1e9)

# def dijkstra(graph,start,distance,k):
#   q = []
#   heapq.heappush(q,(0,start))
#   distance[start] = 0
#   while q:
#     dist, now = heapq.heappop(q)
#     if distance[now] < dist:
#       continue
#     for i in graph[now]:
#       cost = dist + i[1]
#       if cost < distance[i[0]]:
#         distance[i[0]] = cost
#         heapq.heappush(q,(cost,i[0]))


# def solution(n, roads, k):
#   graph = [[] for _ in range(n+1)]
#   distance = [INF] * (n+1)
#   for road in roads:
#     start, end,dist = road
#     graph[start].append((end,dist))
#     graph[end].append((start,dist))

#   dijkstra(graph,1,distance,k)

#   count = 0
#   for i in distance:
#     if i <= k:
#       count += 1
#   return count


# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
# print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))

# -------------------------------------------------------------------------------- 1. 피보나치 수 
# ------------------------------------------- 내꺼 10분 컷! 두번째 4분 컷!!
# def solution(n):
#   dp = [0]*(n+1)
#   dp[1] = 1
#   for i in range(2,n+1):
#     dp[i] = dp[i-1] + dp[i-2]

#   return dp[n] % 1234567


# print(solution(3))
# print(solution(5))

# -------------------------------------------------------------------------------- 2. 주차 요금 계산 
# ------------------------------------------- 내꺼 35분 컷!! 두번째 30분 컷!ㅋㅋㅋㅋ
# from math import ceil

# def solution(fees, records):
#   dic = {}
#   for record in records:
#     time, car_n, act = record.split(' ')
#     if car_n not in dic.keys():
#       dic[car_n] = [time]
#     else:
#       dic[car_n].append(time)
    
#   answer = []
#   for i in dic.items():
#     if len(i[1])%2 != 0:
#       dic[i[0]].append('23:59')

#     total_time = 0
#     for j in range(1,len(i[1]),2):
#       out_hour, out_minutes = map(int,i[1][j].split(':'))
#       in_hour, in_minutes = map(int,i[1][j-1].split(':'))
#       total_time += (out_hour-in_hour) * 60 + out_minutes - in_minutes

#     if total_time <= fees[0]:
#       answer.append((i[0],fees[1]))
#     else:
#       else_cost = ceil((total_time - fees[0])/fees[2]) * fees[3]
#       total_cost = fees[1] + else_cost
#       answer.append((i[0], total_cost))

#   answer.sort()
#   real_answer = []
#   for i in answer:
#     real_answer.append(i[1])

#   return real_answer


# print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# print(solution([1, 461, 1, 10],["00:00 1234 IN"]))


# -------------------------------------------------------------------------------- 3. [3차] 파일명 정렬 기쁘다!!
# 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현
# 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다.
# 파일명은 영문자로 시작, 숫자를 하나 이상 포함

# 1. HEAD 부분을 기준으로 사전 순으로 정렬, 대소문자 구분x
# 2. NUMBER의 숫자 순으로 정렬
# 3. 1,2번 둘 다 같을 경우, 원래 입력에 주어진 순서를 유지
# ------------------------------------------- 내꺼  27분 컷!! 두번째 35분 컷ㅋㅋㅋ 중간에 뭔가 꼬였다.
# def solution(files):
#   answer = []
#   for file in files:
#     head = ''
#     number = ''
#     tail = ''
#     head_toggle = True
#     num_toggle = True

#     for i in file:
#       if i.isdigit() == False and head_toggle:
#         head += i
#       elif i.isdigit() and num_toggle:
#         head_toggle = False
#         number += i
#       else:
#         num_toggle = False
#         tail += i
    
#     answer.append((head,number,tail))

#   answer.sort(key=lambda x:(x[0].lower(), int(x[1])))
#   real_answer = []
#   for i in answer:
#     real_answer.append(''.join(i))
#   return real_answer


# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# -------------------------------------------------------------------------------- 7. 이진 변환 반복하기 
# ------------------------------------------- 내꺼 11분 컷! 두번째 6분 컷!!
# def solution(s):
#   count = 0
#   removed_zero = 0
#   while True:
#     if s == '1':
#       break
#     zero_count = s.count('0')
#     removed_zero += zero_count
#     s = bin(len(s)-zero_count)[2:]
#     count += 1
#   return [count,removed_zero]
    


# print(solution("110010101001"))
# print(solution("01110"))
# print(solution("1111111"))

# -------------------------------------------------------------------------------- 8. 괄호 회전하기
# ------------------------------------------- 내꺼  26분 컷! 두번째 18분 컷!!
# pop(0)을 deque의 popleft()로 바꾸니까 빨라지긴 했지만 결국엔 중간에서 짤라줘야 빨라진다.
# from collections import deque

# def check(string):
#   stack = []
#   for i in string:
#     if stack == []:
#       stack.append(i)
#     elif (stack[-1] =='[' and  i==']') or (stack[-1] =='{' and  i=='}') or (stack[-1] =='(' and  i==')'):
#       stack.pop()
#     else:
#       stack.append(i)

#   if stack == []:
#     return True
#   else:
#     return False

# def solution(s):
#   count = 0
#   q = deque(list(s))
#   for i in s:
#     q.append(q.popleft())
#     if check(q):
#       count += 1
#   return count

# ------------------------------------------- 내꺼 이전꺼 틀림 테스트 케이스 6번 통과 못함

# print(solution("[](){}"))
# print(solution("}]()[{"))
# print(solution("[)(]"))
# print(solution("}}}"))
# print(solution("[({]})"))
# print(solution("[({}])"))

# ------------------------------------------------------------------------------------------------ 220321
# -------------------------------------------------------------------------------- 10. 튜플 
# ------------------------------------------- 내꺼 28분 컷! 두번째 18분 컷!
# def solution(s):
#   result = s[2:-2].split('},{')
#   result.sort(key=lambda x:(len(x)))
#   answer = []
#   for i in result:
#     split_i = list(map(int,i.split(',')))
#     for j in split_i:
#       if j not in answer:
#         answer.append(j)

#   return answer


# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# print(solution("{{20,111},{111}}"))
# print(solution("{{123}}"))
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

# -------------------------------------------------------------------------------- 7. [1차] 캐시 
# 캐시 크기에 따른 실행시간 측정 프로그램을 작성
#  캐시 크기 <= 30
#  최대 도시 수는 100,000
#  도시 이름은 최대 20자
#  "총 실행시간"을 출력
# ------------------------------------------- 내꺼 17분 컷 두번째 11분 컷!!
# from collections import deque


# def solution(cacheSize, cities):
#   total_time = 0
#   stack = deque([])
#   if cacheSize == 0:
#     return 5 * len(cities)
#   for city in cities:
#     city = city.lower()
#     if city in stack:
#       total_time += 1
#       stack.remove(city)
#       stack.append(city)
#     else:
#       total_time += 5
#       if len(stack) >= cacheSize:
#         stack.popleft()
#       stack.append(city)
#   return total_time


# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))



# -------------------------------------------------------------------------------- 9. 올바른 괄호 
# ------------------------------------------- 내꺼 3분 컷! 두번 째 3분 컷!
# def solution(s):
#   summ = 0
#   for i in s:
#     if summ < 0:
#       return False
#     if i == ')':
#       summ -= 1
#     elif i == '(':
#       summ += 1
#   if summ == 0:
#     return True
#   else:
#     return False

# print(solution("()()"))
# print(solution("(())()"	))
# print(solution(")()("))
# print(solution("(()("))

# -------------------------------------------------------------------------------- 10. [3차] 방금그곡
# ------------------------------------------- 내꺼 실패 두번째 32분 컷!!
# def solution(m, musicinfos):
#   convert = {'C#':'c','D#':'d', 'E#':'e', 'F#':'f', 'G#':'g', 'A#':'a'}
#   for i in convert.keys():
#     m = m.replace(i, convert[i])

#   answer = []
#   for i in musicinfos:
#     s,e,title,order = i.split(',')
#     for i in convert.keys():
#       order = order.replace(i, convert[i])

#     s_hour,s_minutes = list(map(int,s.split(':')))
#     e_hour,e_minutes = list(map(int,e.split(':')))
#     total_time = (e_hour - s_hour) * 60 + (e_minutes - s_minutes)

#     seequence = ''
#     time = total_time // len(order)
#     left = total_time % len(order)
#     seequence += (order*time)
#     seequence += order[:left]
    
#     if m in seequence:
#       answer.append((total_time, title))

#   answer.sort(key=lambda x: -x[0])

#   if len(answer) == 0:
#     return '(None)'
#   else:
#     return answer[0][1]


# print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))