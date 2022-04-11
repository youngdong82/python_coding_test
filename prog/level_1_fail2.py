
# -------------------------------------------------------------------------------- 1. 최대공약수와 최소공배수 12분 컷!
# ------------------------------------------- 내꺼 3번째 5분 컷!
# from math import gcd


# def solution(n, m):
#   gcd_data = gcd(n,m)
#   lcm_data = (n*m) //gcd_data

#   answer = [gcd_data, lcm_data]
#   return answer

# print(solution(3,12))
# print(solution(2,5))

# -------------------------------------------------------------------------------- 2. 같은 숫자는 싫어
# ------------------------------------------- 내꺼 4분 컷! 3번째 6분 컷!
# def solution(arr):
#   tmp = [arr[0]]
#   for i in arr:
#     if i == tmp[-1]:
#       continue
#     else:
#       tmp.append(i)

#   return tmp

# print(solution([1,1,3,3,0,1,1]))
# print(solution([4,4,4,3,3]))

# -------------------------------------------------------------------------------- 3. 문자열 다루기 기본
# ------------------------------------------- 내꺼 4분 컷! 3번째 3분 컷!!
# def solution(s):
#   answer = True
#   if len(s) in [4,6]:
#     if not s.isdigit():
#       answer = False
#   else:
#     answer = False
#   return answer

# print(solution("a234"))
# print(solution('1234'))

# -------------------------------------------------------------------------------- 4. 체육복 11분
# ------------------------------------------- 내꺼
# def solution(n, lost, reserve):
#   students = [1] * n
#   for i in lost:
#     students[i-1] -= 1
#   for i in reserve:
#     students[i-1] += 1
  
#   for i in range(len(students)):
#     if students[i] == 2:
#       if i >= 1:
#         if students[i-1] == 0:
#           students[i-1] += 1
#           students[i] -= 1
#           continue
#       if i+1 < n:
#         if students[i+1] == 0:
#           students[i+1] += 1
#           students[i] -= 1
#   count = 0
#   for i in students:
#     if i >0:
#       count += 1
#   return count


# print(solution(5,[2, 4],[1, 3, 5]))
# print(solution(5,[2, 4],[3]))
# print(solution(3,[3],[1]))

# -------------------------------------------------------------------------------- 5. 3진법 뒤집기 - 진수변환 복습!!!
# ------------------------------------------- 내꺼 3번째 16분 컷!
# def solution(n):
#   answer = make(n,3)
#   answer = answer[::-1]
#   return int(answer,3)

# def make(num, depend):
#   string = '0123456789ABCDEF'
#   answer = ''
#   while num >0:
#     num, rest = divmod(num,depend)
#     answer += str(string[rest])
#   return answer[::-1]

# print(solution(1))
# print(solution(45))
# print(solution(125))

# -------------------------------------------------------------------------------- 6. 약수의 합 11분 컷!
# ------------------------------------------- 내꺼 3번째 
# from math import sqrt


# def solution(n):
#   answer = []
#   for i in range(1, int(sqrt(n))+1):
#     if n%i == 0:
#       if i != n//i:
#         answer.append(n//i)
#       answer.append(i)

#   return sum(answer)

# print(solution(12))
# print(solution(5))
# print(solution(16))

# -------------------------------------------------------------------------------- 7. 키패드 누르기 19분 컷!
# ------------------------------------------- 내꺼 3번째 13분 컷!
# def solution(numbers, hand):
#   dic = {1: (0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)}
#   left = [1,4,7,'*']
#   right = [3,6,9, '#']
#   now_left = '*'
#   now_right = '#'

#   answer = ''
#   for number in numbers:
#     if number in left:
#       answer += 'L'
#       now_left = number
#     elif number in right:
#       answer += 'R'
#       now_right = number
#     else:
#       left_dist = abs(dic[now_left][0] - dic[number][0]) + abs(dic[now_left][1] - dic[number][1])
#       right_dist = abs(dic[now_right][0] - dic[number][0]) + abs(dic[now_right][1] - dic[number][1])
#       if left_dist < right_dist:
#         answer += 'L'
#         now_left = number
#       elif left_dist > right_dist:
#         answer += 'R'
#         now_right = number
#       else:
#         if hand == 'left':
#           answer += 'L'
#           now_left = number
#         else:
#           answer += 'R'
#           now_right = number
#   return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))


# -------------------------------------------------------------------------------- 8. [1차] 다트 게임 실패! - 복복습
# ------------------------------------------- 내꺼 27분 컷!!
# def solution(dartResult):

#   dartResult = dartResult.replace('10','A')
  
#   tmp = dartResult[0]
#   reck = []

#   for i in range(1,len(dartResult)):
#     if dartResult[i].isdigit() or dartResult[i] == 'A':
#       data = tmp
#       tmp = ''
#       reck.append(data)
#     tmp += dartResult[i]
#     if i == len(dartResult)-1:
#       reck.append(tmp)

#   answer = []
#   tmp_answer = 0
#   for i in reck:
#     digit = 0
#     if i[0] == 'A':
#       digit = 10
#     else:
#       digit = int(i[0])
#     if i[1] == 'S':
#       tmp_answer = digit** 1
#     elif i[1] == 'D':
#       tmp_answer = digit** 2
#     elif i[1] == 'T':
#       tmp_answer = digit** 3

#     if i[-1] in ['*','#']:
#       if i[-1] == '*':
#         tmp_answer *= 2
#         if len(answer) != 0:
#           a = answer.pop()
#           a *= 2
#           answer.append(a)
#         answer.append(tmp_answer)
#       else:
#         answer.append(-tmp_answer) 
#     else:
#       answer.append(tmp_answer)
#   return sum(answer)


# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))

# -------------------------------------------------------------------------------- 9. 크레인 인형뽑기 게임 15분 컷!! 복습!!!
# 2차원 리스트 돌리는거 쓰지 말고 풀어봐
# ------------------------------------------- 내꺼 3번쩨 22분 컷!!
# def solution(board, moves):
#   board = rotate_right(board)
#   for i in range(len(board)):
#     while True:
#       if board[i][-1] == 0:
#         board[i].pop()
#       else:
#         break

#   stack = []
#   answer = 0
#   for i in moves:
#     if len(board[i-1]):
#       tmp = board[i-1].pop()
#       if len(stack):
#         if stack[-1] == tmp:
#           stack.pop()
#           answer += 2
#         else:
#           stack.append(tmp)
#       else:
#         stack.append(tmp)
#   return answer


# def rotate_right(a):
#   row = len(a)
#   column = len(a[0])

#   res = [[0] * row for _ in range(column)]
#   for i in range(row):
#     for j in range(column):
#       res[j][row-1-i] = a[i][j]
#   return res

# ------------------------------------------- 내꺼 3번쩨 22분 컷!!
# def solution(board, moves):
#     bucket = []
#     answer = []
#     for move in moves:
#         for i in range(len(board)):
#             if board[i][move-1] > 0:
#                 bucket.append(board[i][move-1])
#                 board[i][move-1] = 0
#                 if bucket[-1:] == bucket[-2:-1]:
#                     answer += bucket[-1:]
#                     bucket = bucket[:-2]
#                 break
#     return len(answer)*2


# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

# -------------------------------------------------------------------------------- 10. 신고 결과 받기 14분 컷!
# ------------------------------------------- 내꺼 16분 컷!!
# def solution(id_list, report, k):
#   ban_dic = {}
#   from_dic={}
#   for id in id_list:
#     ban_dic[id] = 0
#     from_dic[id] = []

#   report = set(report)
#   for i in report:
#     from_id,ban_id = i.split(' ')
#     ban_dic[ban_id] += 1
#     from_dic[from_id].append(ban_id)
  
#   banned = []
#   for i in ban_dic.keys():
#     if ban_dic[i] >= k:
#       banned.append(i)

#   answer = []
#   for i in from_dic.values():
#     count = 0
#     for ban in banned:
#       if ban in i:
#         count += 1
#     answer.append(count)
#   return answer

# print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
# print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
