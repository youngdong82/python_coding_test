# -------------------------------------------------------------------------------- 1. 예산
# ------------------------------------------- 내꺼 13분 컷!
# def solution(d, budget):
#   d.sort()
#   count = 0
#   for i in d:
#     budget -= i
#     if budget < 0:
#       return count
#     elif budget == 0:
#       return count + 1
#     else:
#       count += 1
#   return count

# # 전부 가능, 전부 불가
# print(solution([1,1,1,1],9))
# print(solution([10,11,12,13,],9))
# print(solution([1,3,2,5,4], 9))
# print(solution([2,2,3,3], 10))

# -------------------------------------------------------------------------------- 2. 두개 뽑아서 더하기
# 테스트 케이스에 음수가 있었데...노어이
# ------------------------------------------- 내꺼 5분 컷 - set에 대해서!
# from itertools import combinations

# def solution(numbers):
#   candidates = list(combinations(numbers,2))
#   answer = []
#   for candidate in candidates:
#     answer.append(sum(candidate))
#   return sorted(list(set(answer)))

# print(solution([2,1,3,4,-7]))
# print(solution([2,1,3,4,1]))
# print(solution([5,0,2,7]))

# -------------------------------------------------------------------------------- 3. 나누어 떨어지는 배열
# ------------------------------------------- 내꺼 3분 컷!
# def solution(arr, divisor):
#   answer = []
#   for i in arr:
#     if i % divisor == 0:
#       answer.append(i)
#   answer.sort()
#   if len(answer) == 0:
#     answer.append(-1)
#   return answer

# print(solution([5, 9, 7, 10], 5))
# print(solution([2, 36, 1, 3], 1))
# print(solution([3,2,6], 10))
# -------------------------------------------------------------------------------- 4. 음양 더하기
# ------------------------------------------- 내꺼 2분 컷!
# def solution(absolutes, signs):
#   answer = []
#   for i, j in zip(absolutes, signs):
#     if j == True:
#       answer.append(i)
#     else:
#       answer.append(-i)
#   return sum(answer)

# print(solution([4,7,12], [True,False,True]))
# print(solution([1,2,3], [False,False,True]))

# -------------------------------------------------------------------------------- 5. 키패드 누르기 
# ------------------------------------------- 내꺼 32분 컷! 기쁘다!
# def dist(dic, l_hand_posi,r_hand_posi, target, prefer):

#   l_to_traget = abs(dic[target][0] - dic[l_hand_posi][0]) + abs(dic[target][1] - dic[l_hand_posi][1])
#   r_to_target = abs(dic[target][0] - dic[r_hand_posi][0]) + abs(dic[target][1] - dic[r_hand_posi][1])

#   answer = ''
#   if l_to_traget > r_to_target:
#     answer = 'R'
#     r_hand_posi = target
#   elif l_to_traget < r_to_target:
#     answer = 'L'
#     l_hand_posi = target
#   else:
#     if prefer == 'right':
#       answer = 'R'
#       r_hand_posi = target
#     else:
#       answer = 'L'
#       l_hand_posi = target

#   return answer, l_hand_posi, r_hand_posi


# def solution(numbers, hand):
#   dic = {
#     '1':[0,0],
#     '2':[0,1],
#     '3':[0,2],
#     '4':[1,0],
#     '5':[1,1],
#     '6':[1,2],
#     '7':[2,0],
#     '8':[2,1],
#     '9':[2,2],
#     '*':[3,0],
#     '0':[3,1] ,
#     '#':[3,2],
#     }

#   left_n = ['1','4','7']
#   right_n = ['3','6','9']
#   l_hand_posi = '*'
#   r_hand_posi = '#'

#   answer = ''
#   for i in numbers:
#     i = str(i)
#     if i in left_n:
#       answer += 'L'
#       l_hand_posi = i
#     elif i in right_n:
#       answer += 'R'
#       r_hand_posi = i
#     else:
#       answer_s, l_hand_posi, r_hand_posi = dist(dic,l_hand_posi, r_hand_posi, i, hand)
#       answer += answer_s

#   return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))