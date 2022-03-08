# -------------------------------------------------------------------------------- is_integer()
# -------------------------------------------------------------------------------- dic 초기화
  # reports = {x : 0 for x in id_list}

# -------------------------------------------------------------------------------- 중복제거
# arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]
# result1 = dict.fromkeys(arr) # 리스트 값들을 key 로 변경 print(result1) 
# result2 = list(result1) # list(dict.fromkeys(arr)) print(result2)

# -------------------------------------------------------------------------------- 1. 문자열 내림차순으로 배치하기
# ------------------------------------------- 내꺼 6분 컷;; 문제 잘못읽음
# def solution(s):
#   s = list(s)
#   s.sort(reverse=True)
#   answer = ''.join(s)
#   return answer

# print(solution("Zbcdefg"))

# -------------------------------------------------------------------------------- 2.수박수박수박수박수박수?
# ------------------------------------------- 내꺼
# def solution(n):
#   answer = ''
#   for i in range(1,n+1):
#     if i%2 == 0:
#       answer += '박'
#     else:
#       answer += '수'
#   return answer

# print(solution(3))
# print(solution(4))

# -------------------------------------------------------------------------------- 3. 2016년
# ------------------------------------------- 내꺼 13분 컷!
# def solution(a, b):
#   days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
#   months = [31,29,31,30,31,30,31,31,30,31,30,31]

#   total_day = 4
#   for i in range(a-1):
#     if a == 1:
#       break
#     total_day += months[i]
#   total_day += b
#   return days[total_day%7]

# print(solution(5,24))

# -------------------------------------------------------------------------------- 4. 비밀지도
# ------------------------------------------- 내꺼
# def solution(n, arr1, arr2):
#   answer = []
#   for i,j in zip(arr1, arr2):
#     b_1 = str(bin(i)[2:])
#     b_1 = ('0'*(n-len(b_1)))+ b_1

#     b_2 = str(bin(j)[2:])
#     b_2 = ('0'*(n-len(b_2)))+ b_2

#     answer_s = ''
#     for a,b in zip(b_1, b_2):
#       if a == '0' and b == '0':
#         answer_s += ' '
#       else:
#         answer_s += '#'

#     answer.append(answer_s)
#   return answer

# ------------------------------------------- 커뮤니티
# def solution(n, arr1, arr2):
#   answer = []
#   for i,j in zip(arr1,arr2):
#       a12 = str(bin(i|j)[2:])
#       a12=a12.rjust(n,'0')
#       a12=a12.replace('1','#')
#       a12=a12.replace('0',' ')
#       answer.append(a12)
#   return answer

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

# -------------------------------------------------------------------------------- 5. [1차] 다트 게임 실패!
# ------------------------------------------- 커뮤니티
# def solution(dartResult):
#     stack = []
#     dartResult = dartResult.replace("10", "A")
#     bonus = {'S': 1, 'D': 2, 'T': 3}
    
#     for i in dartResult:
#         if i.isdigit() or i=='A':
#             stack.append(10 if i == 'A' else int(i))
#         elif i in ('S', 'D', 'T'):
#             num = stack.pop()
#             stack.append(num ** bonus[i])
#         elif i == '#':
#             stack[-1] *= -1
#         elif i == '*':
#             num = stack.pop()
#             if len(stack):
#                 stack[-1] *= 2
#             stack.append(2 * num)
#         print(stack)
#     return sum(stack)
      

# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))

# -------------------------------------------------------------------------------- 6. 시저암호
# ------------------------------------------- 내꺼
# def solution(s, n):
#   alphabet = "abcdefghijklmnopqrstuvwxyz"
#   # alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#   answer = ''
#   for i in range(len(s)):
#     if s[i] == ' ':
#       answer += s[i]
#     elif s[i].isupper():
#       a = s[i].lower()
#       index = alphabet.index(a)
#       answer_s = (index+n)%26
#       plus = alphabet[answer_s].upper()
#       answer += plus
#     else:
#       index = alphabet.index(s[i])
#       answer_s = (index+n)%26
#       plus = alphabet[answer_s]
#       answer += plus

#   return answer

# ------------------------------------------- 커뮤니티
# def solution(s, n):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

#     return "".join(s)

# print(solution("AB", 1))
# print(solution("z", 1))
# print(solution("a B z", 4))

# -------------------------------------------------------------------------------- 7. 크레인 인형뽑기 게임 - 실패!
# ------------------------------------------- 커뮤니티 와...자괴감 오지네...
# def solution(board, moves):
#     stacklist = []
#     answer = 0

#     for i in moves:
#         for j in range(len(board)):
#             if board[j][i-1] != 0:
#                 stacklist.append(board[j][i-1])
#                 board[j][i-1] = 0
#                 if len(stacklist) > 1:
#                     if stacklist[-1] == stacklist[-2]:
#                         stacklist.pop(-1)
#                         stacklist.pop(-1)
#                         answer += 2     
#                 break
#     return answer

# print(solution(
#   [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],	
#   [1,5,3,5,1,2,1,4]))

# -------------------------------------------------------------------------------- 8. 콜라츠 추측
# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# ------------------------------------------- 내꺼 8분 컷!
# def solution(num):
#   count = 0
#   while True:
#     if num == 1:
#       break
#     if num%2 == 0:
#       num //= 2
#     else:
#       num = (num * 3)+1
#     count += 1
#     if count > 500:
#       count = -1
#       break
#   return count

# print(solution(6))
# print(solution(16))
# print(solution(626331))

# -------------------------------------------------------------------------------- 9. 정수 제곱근 판별
# ------------------------------------------- 내꺼 3분 컷!
# from math import sqrt

# def solution(n):
#   answer = 0
#   if int(sqrt(n)) == sqrt(n):
#     answer = (int(sqrt(n))+1)**2
#   else:
#     answer = -1
#   return answer

# ------------------------------------------- 커뮤니티
# from math import sqrt

# def solution(n):
#   answer = 0
#   if sqrt(n).is_integer():
#     answer = (int(sqrt(n))+1)**2
#   else:
#     answer = -1
#   return answer

# print(solution(121))
# print(solution(3))
# -------------------------------------------------------------------------------- 10. 폰켓몬
# 최대한 다양한 종류의 폰켓몬을 가지길 원하
# 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 
# 그때의 폰켓몬 종류 번호의 개수를 return 
# ------------------------------------------- 내꺼 12분 컷! 오바코딩....
# from collections import defaultdict

# def solution(nums):
#   take_num = len(nums)//2
#   dic = defaultdict(int)
#   for i in nums:
#     dic[i] += 1
#   if len(dic) < take_num:
#     return len(dic) 
#   else:
#     return take_num

# ------------------------------------------- 커뮤니티 깔끔~
# def solution(nums):
#   type_list = set(nums)
#   if type_list < len(nums)//2:
#     return type_list
#   else:
#     return len(nums)//2


# print(solution([3,1,2,3]))
# print(solution([3,3,3,2,2,4]))
# print(solution([3,3,3,2,2,2]))

# -------------------------------------------------------------------------------- 11. 신고 결과 받기
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리
# k번 이상 신고된 유저는 게시판 이용이 정지
# 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
# 모아오다가 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송

# ------------------------------------------- 내꺼 + 커뮤니티
# from collections import defaultdict


# def solution(id_list, report, k):
#   # dic, answer 초기화
#   dic = defaultdict(list)
#   answer = defaultdict(int)
#   for i in id_list:
#     dic[i] = []
#     answer[i] = 0
#   # 신고 결과 입력
#   report = set(report)
#   for i in report:
#     from_id, to_id = i.split(' ')
#     dic[to_id].append(from_id)

#   # # 정지되는 사람 출력
#   for i in dic.items():
#     if len(i[1]) >= k:
#       for j in i[1]:
#         answer[j] += 1

#   return list(answer.values())

# # ------------------------------------------- 커뮤니티 1
# def solution(id_list, report, k):
#   answer = [0] * len(id_list)    
#   report = set(report)
#   dic = {x : 0 for x in id_list}
#   for r in report:
#       dic[r.split()[1]] += 1
#   print(dic)
#   for r in report:
#       if dic[r.split()[1]] >= k:
#           answer[id_list.index(r.split()[0])] += 1
#   return answer


# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))