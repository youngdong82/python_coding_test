
# -------------------------------------------------------------------------------- array[-1:]
# IndexError: list index out of range
# 에러 생기지 않음

# -------------------------------------------------------------------------------- reverse(), reversed()
# 문자열 추가 가능?
# 리턴되는 값은?
  # reversed_answer = "".join(reversed(answer))
  # print(reversed_answer)


# -------------------------------------------------------------------------------- 진수 변환
# def make(n):
#     rev_base = ''
#     while n > 0:
#         n, mod = divmod(n, 3)
#         rev_base += str(mod)
#     return rev_base 


# -------------------------------------------------------------------------------- 1. 최대공약수와 최소공배수 12분 컷!
# ------------------------------------------- 내꺼
# from math import sqrt

# def a(x):
#   x_list = []
#   for i in range(1, int(sqrt(x))+1):
#     if x%i == 0:
#       if i**2 == x:
#         x_list.append(i)
#       else:
#         x_list.append(i)
#         x_list.append(x//i)
#   return sorted(x_list)

# def solution(n, m):
#   max_value = 0
#   for i in a(n):
#     for j in a(m):
#       if i == j:
#         max_value = max(max_value, i)
#   min_value = (n//max_value)*(m//max_value)*max_value
#   return [max_value, min_value]

# print(solution(3, 12))
# print(solution(2,5))

# -------------------------------------------------------------------------------- 2. 같은 숫자는 싫어
# ------------------------------------------- 내꺼 4분 컷!
# def solution(arr):
#   answer = [arr[0]]
#   for i in range(1,len(arr)):
#     if arr[i] != answer[-1]:
#       answer.append(arr[i])
#   return answer

# print(solution([1,1,3,3,0,1,1]))
# print(solution([4,4,4,3,3]))

# -------------------------------------------------------------------------------- 3. 문자열 다루기 기본
# ------------------------------------------- 내꺼 4분 컷!
# def solution(s):
#   answer = False
#   if (len(s) == 4 or len(s) == 6) and s.isdigit():
#     answer = True
#   return answer

# print(solution("a234"))
# print(solution("1234"))

# -------------------------------------------------------------------------------- 4. 체육복 11분
# ------------------------------------------- 내꺼
# def solution(n, lost, reserve):
#   student = [0] * (n+1)
#   for i in lost:
#     student[i] -= 1
#   for i in reserve:
#     student[i] += 1

#   for i in range(n+1):
#     if (student[i-1] == 1 and student[i] == -1) or (student[i-1] == -1 and student[i] == 1):
#       student[i-1] = 0
#       student[i] = 0

#   count = 0
#   for i in student:
#     if i >= 0:
#       count += 1
#   return count - 1

# print(solution(5, [2,4], [1,3,5]))
# print(solution(5, [2,4], [3]))
# print(solution(3, [3], [1]))

# -------------------------------------------------------------------------------- 5. 3진법 뒤집기 - 복습
# ------------------------------------------- 내꺼
# 내꺼 전혀 의미 없고, 진수 변환하는 함수는 어느정도 외우자.
# ------------------------------------------- 커뮤
# def make(n):
#     rev_base = ''
#     while n > 0:
#         n, mod = divmod(n, 3)
#         print(n,mod)
#         rev_base += str(mod)
#     return rev_base 

# def solution(n):
#   a = make(n)
#   return (int(a,3))


# print(solution(45))
# print(solution(125))

# -------------------------------------------------------------------------------- 6. 약수의 합 11분 컷!
# ------------------------------------------- 내꺼 
# from math import sqrt


# def solution(n):
#   array = []
#   for i in range(1,int(sqrt(n))+1):
#     if n%i == 0:
#       if (n//i)**2 == n:
#         array.append(i)
#       else:
#         array.append(i)
#         array.append(n//i)
#   return sum(array)

# print(solution(12))
# print(solution(5))
# print(solution(16))
# print(solution(2))

# -------------------------------------------------------------------------------- 7. 키패드 누르기 19분 컷!
# ------------------------------------------- 내꺼
# def solution(numbers, hand):
#   answer = ''
#   matrix = {1:(0,0),2:(1,0),3:(2,0),4:(0,1),5:(1,1),6:(2,1),7:(0,2),8:(1,2),9:(2,2),'*':(0,3),0:(1,3),'#':(2,3)}

#   left_list = [1,4,7]
#   right_list = [3,6,9]
#   now_left = '*'
#   now_right = '#'
#   for i in numbers:
#     if i in left_list:
#       answer += 'L'
#       now_left = i
#     elif i in right_list:
#       answer += 'R'
#       now_right = i
#     else:
#       sub_left = abs(matrix[i][0] - matrix[now_left][0]) + abs(matrix[i][1] - matrix[now_left][1])
#       sub_right = abs(matrix[i][0] - matrix[now_right][0]) + abs(matrix[i][1] - matrix[now_right][1])
#       if sub_left > sub_right:
#         now_right = i
#         answer += 'R'
#       elif sub_left < sub_right:
#         now_left = i
#         answer += 'L'
#       else:
#         if hand == 'right':
#           now_right = i
#           answer += 'R'
#         else:
#           now_left = i
#           answer += 'L'
#   return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))

# -------------------------------------------------------------------------------- 8. 1차] 다트 게임 실패! - 복복습
# ------------------------------------------- 커뮤니티,
# 10처럼 이것만 없으면 규칙을 적용할 수 있다면 치환하는 것도 아주 좋다.
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
#     return sum(stack)

# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))

# -------------------------------------------------------------------------------- 9. 크레인 인형뽑기 게임 15분 컷!!
# ------------------------------------------- 내꺼
# def solution(board, moves):
#   n = len(board)
#   stack = []
#   count = 0

#   for i in moves:
#     for j in range(n):
#       if board[j][i-1] != 0:
#         if len(stack) != 0:
#           if board[j][i-1] == stack[-1]:
#             stack.pop()
#             count += 2
#           else:
#             stack.append(board[j][i-1])
#         else:
#           stack.append(board[j][i-1])
#         board[j][i-1] = 0
#         break
#   return count

# # ------------------------------------------- 내꺼 + 커뮤
# # 더 깔금하긴 한데 성능은 비슷함. 근데 이건 구력차이지 모르는게 아니라 굳이 복습은 필요 없을 듯
# def solution(board, moves):
#   n = len(board)
#   stack = []
#   count = 0

#   for i in moves:
#     for j in range(n):
#       if board[j][i-1] != 0:
#         stack.append(board[j][i-1])
#         board[j][i-1] = 0
#         if stack[-1:] == stack[-2:-1]:
#           stack = stack[:-2]
#           count += 2
#         break

#   return count


# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

# -------------------------------------------------------------------------------- 10. 신고 결과 받기 14분 컷!
# ------------------------------------------- 내꺼
# from collections import defaultdict


# def solution(id_list, report, k):
#   report = set(report)
#   collect = defaultdict(list)
#   answer_dic = defaultdict(int)

#   for i in id_list:
#     collect[i] = []
#     answer_dic[i] = 0
#   for i in report:
#     do, to = i.split(' ')
#     collect[to].append(do)
  
#   for i in collect.items():
#     if len(i[1]) >= k:
#       for j in i[1]:
#         answer_dic[j] += 1

#   return list(answer_dic.values())

# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))