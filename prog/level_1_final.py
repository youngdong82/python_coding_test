# -------------------------------------------------------------------------------- isdecimal(), isnumeric()
# isdigit() 함수는 단일 글자가 '숫자' 모양으로 생겼으면 무조건 True를 반환
# isdecimal() 함수는 주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수이기 때문에 특수문자 중 숫자모양을 숫자로 치지않는다.

# a = '12345'
# print(a.isdecimal()) 
# print(a.isdigit()) 
# print(a.isnumeric()) 
# b = '3²'
# print(b.isdecimal()) 
# print(b.isdigit()) 
# print(b.isnumeric()) 
# -------------------------------------------------------------------------------- 8. [1차] 다트 게임 실패! - 복복습
# ------------------------------------------- 내꺼 27분 컷!!
# def solution(dartResult):
#   dartResult = dartResult.replace('10','A')
#   multiple = {'S': 1, 'D': 2, 'T': 3}
#   bonus = ['*','#']
#   stack = []
#   for i in dartResult:
#     if i.isdigit():
#       stack.append(int(i))
#     elif i == 'A':
#       stack.append(10)
#     elif i in multiple:
#       stack[-1] = stack[-1] ** multiple[i]
#     elif i in bonus:
#       if i == '*':
#         if len(stack) >= 2:
#           stack[-1] = stack[-1] * 2
#           stack[-2] = stack[-2] * 2
#         else:
#           stack[-1] = stack[-1] * 2
#       else:
#         stack[-1] = -stack[-1]

#   return sum(stack)

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
#   stack = []
#   answer = 0
#   for i in moves:
#     for j in range(len(board)):
#       if board[j][i-1] != 0:
#         stack.append(board[j][i-1])
#         board[j][i-1] = 0
#         if len(stack) > 1:
#           if stack[-1] == stack[-2]:
#             stack.pop()
#             stack.pop()
#             answer += 2
#         break

#   return answer

# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))