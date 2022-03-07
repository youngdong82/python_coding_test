# -------------------------------------------------------------------------------- 1. 체육복 시간초과 - 복습
# ------------------------------------------- 내꺼 25분 컷! - 시간초과 
# def solution(n, lost, reserve):
#   student = [0 for _ in range(n)]
#   for i in lost:
#     student[i-1] -= 1
#   for i in reserve:
#     student[i-1] += 1

#   print(student)
#   for i in range(n):
#     if i > 0 and student[i] == 1 and student[i-1] == -1:
#       student[i-1] = 0
#       student[i] = 0
#     elif i < n-1 and student[i] == 1 and student[i+1] == -1: 
#       student[i+1] = 0
#       student[i] = 0
#   print(student)

#   answer = 0
#   for i in student:
#     if i >= 0:
#       answer += 1
#   return answer

# print(solution(5, [2,4], [1,3,5]))
# print(solution(5, [2,4], [3]))
# print(solution(5, [2], [3]))
# print(solution(3, [3], [1]))
# print(solution(2, [0], [1]))
# print(solution(2, [1], [1]))

# -------------------------------------------------------------------------------- 2. 없는 숫자 더하기
# ------------------------------------------- 내꺼 3분 컷!
# def solution(numbers):
#   answer = []
#   for i in range(10):
#     if i not in numbers:
#       answer.append(i)
#   return sum(answer)

# print(solution([1,2,3,4,6,7,8,0]))
# print(solution([5,8,4,0,6,7,9]))

# -------------------------------------------------------------------------------- 3. 같은 숫자는 싫어 - 복습!
# ------------------------------------------- 내꺼 2번째 시도에서 5분 컷! 근데 이상하게 헤맸었다!
def solution(a):
  n = len(a)
  answer = [a[0]]
  for i in range(1,n):
    if a[i] != answer[-1]:
      answer.append(a[i])

  return answer


print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
print(solution([4,4,4,4,4]))
print(solution([1,2]))

# -------------------------------------------------------------------------------- 4. 평균 구하기 
# ------------------------------------------- 내꺼 1분 컷!
# def solution(arr):
#   a = sum(arr)/len(arr)
#   return round(a, 2)

# print(solution([1, 4, 5]))
# print(solution([1,2,3,4]))
# print(solution([5,5]))

# -------------------------------------------------------------------------------- 5. 자릿수 더하기
# ------------------------------------------- 내꺼 3분 컷!
# def solution(n):
#   answer = sum(list(map(int,str(n))))
#   return answer

# print(solution(123))
# print(solution(987))

# -------------------------------------------------------------------------------- 6. 문자열 다루기 기본 - 시간초과!! 복습!
# ------------------------------------------- 내꺼 아 어이없게...ㅋㅋㅋㅋㅅㅂ 16분 컷
# def solution(s):
#   if len(s) == 4 or len(s) == 6:
#     for i in s:
#       if i.isdigit() == False:
#         return False
#     return True
#   return False

# ------------------------------------------- 커뮤니티ㅋㅋㅋㅋ
# def solution(s):
#   return len(s) in [4,6] and s.isdigit()

# -------------------------------------------------------------------------------- 7. 문자열을 정수로 바꾸기
# ------------------------------------------- 내꺼 7분 컷!
# def solution(s):
#   answer = 0
#   if s[0] == '+':
#     answer = int(s[1:])
#   elif s[0] == '-' :
#     answer = -int(s[1:])
#   else:
#     answer = int(s)
#   return answer

# ------------------------------------------- 커뮤니티 ㅋㅋㅋㅋㅋㅋㅋㅅㅂ 개쩌네
# def solution(s):
#   return int(s)

# print(solution('+1234'))
# print(solution('1234'))
# print(solution('-1234'))

# -------------------------------------------------------------------------------- 8. 소수 만들기
# ------------------------------------------- 내꺼 11분 컷!
# from math import sqrt
# from itertools import combinations


# def prime_num(n):
#   for i in range(2,int(sqrt(n)) + 1):
#     if n % i == 0:
#       return False
#   return True

# def solution(nums):
#   count = 0
#   num_lists = list(combinations(nums,3))
#   for num in num_lists:
#     if prime_num(sum(num)):
#       count += 1
#   return count


# print(solution([1,2,3,4]))
# print(solution([1,2,7,6,4]))

# -------------------------------------------------------------------------------- 9. 약수의 개수와 덧셈
# ------------------------------------------- 내꺼 11분 컷!
# from math import sqrt

# def solution(left, right):
#   answer = 0
#   for i in range(left, right + 1):
#     if int(sqrt(i)) != sqrt(i):
#       answer += i
#     else:
#       answer -= i
#   return answer

# print(solution(13,17))
# print(solution(24,27))

# -------------------------------------------------------------------------------- 10. 부족한 금액 계산하기
# ------------------------------------------- 내꺼 12분 컷!
# def solution(price, money, count):
#   pay = 0
#   for i in range(1, count+1):
#     pay += (price * i)
#   if money >= pay:
#     return 0
#   else:
#     return pay - money

# print(solution(3,20,4))


