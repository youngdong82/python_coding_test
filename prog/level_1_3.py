# -------------------------------------------------------------------------------- 진법 변환
# https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95
# -------------------------------------------------------------------------------- array.index()
# a = [1,2,3,'kim', 63]
# print(a.index('kim'))
# -------------------------------------------------------------------------------- 1.서울에서 김서방 찾기 
# ------------------------------------------- 내꺼 3분 컷!
# "김서방은 1에 있다"
# def solution(seoul):
#   a = 0
#   for i in range(len(seoul)):
#     if seoul[i] == 'Kim':
#       a = i
#   return f'김서방은 {a}에 있다'

# print(solution(["Jane", "Kim"]))

# ------------------------------------------- 커뮤니티 index 내장함수!!
# def solution(seoul):
#   a = seoul.index('Kim')
#   return f'김서방은 {a}에 있다'

# print(solution(["Jane", "Kim"]))

# -------------------------------------------------------------------------------- 2. 가운데 글자 가져오기
# ------------------------------------------- 내꺼 5분 컷!
# def solution(s):
#   n = len(s)
#   if n%2 == 0:
#     answer = s[n//2 -1:n//2+1]
#   else:
#     answer = s[n//2]
#   return answer

# print(solution("abcde"))
# print(solution("qwer"))

# -------------------------------------------------------------------------------- 3. 정수의 합
# ------------------------------------------- 내꺼 5분 컷!
# def solution(a, b):
#   if a == b:
#     answer = a
#   else:
#     answer = 0
#     a,b = min(a,b),max(a,b)
#     for i in range(a,b+1):
#       answer += i

#   return answer
# ------------------------------------------- 커뮤니티 range함수는 장식이 아니다! 기하급수적으로 빨라짐
# def solution(a, b):
#   if a == b:
#     answer = a
#   else:
#     a,b = min(a,b),max(a,b)
#     answer = sum(range(a,b+1))
#   return answer

# print(solution(3,5))
# print(solution(3,3))
# print(solution(5,3))
# -------------------------------------------------------------------------------- 4. 3진법 뒤집기 복습!!!
# ------------------------------------------- 커뮤니티 배워라 영동아...!!
# def make(n):
#     rev_base = ''
#     while n > 0:
#         n, mod = divmod(n, 3)
#         rev_base += str(mod)
#     return rev_base 
    
# def solution(n):
#   a = make(n)
#   return (int(a,3))

# print(solution(45))
# print(solution(125))

# -------------------------------------------------------------------------------- 5. 약수의 합 - 복습!(바쁘면 패스)
# ------------------------------------------- 내꺼 12분 컷! 선능이 내꺼가 훨 낫다!!
# from math import sqrt

# def solution(n):
#   if n == 0:
#     return 0
#   answer = []
#   for i in range(1,int(sqrt(n))+1):
#     if n%i == 0:
#       if sqrt(n) == i:
#         answer.append(i)
#       else:
#         answer.append(i)
#         answer.append(n//i)
#   return sum(answer)

# ------------------------------------------- 커뮤니티
# def solution(num):
#   a = []
#   for i in range(1, (num // 2) + 1):
#     if num % i == 0:
#       a.append(i)
  
#   return num + sum(a)

# print(solution(12))
# print(solution(5))

