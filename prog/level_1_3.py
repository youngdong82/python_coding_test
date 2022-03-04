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

# -------------------------------------------------------------------------------- 6. 이상한 문자 만들기 - 시간초과!
# 어렵진 않았는데...테스트케이스 좀 제대로 된 거 좀 주지...
# ------------------------------------------- 내꺼 30분 컷
# def solution(s):
#   split_s = s.split(' ')
#   for i in range(len(split_s)):
#     split_s[i] = list(split_s[i])
#     for j in range(1,len(split_s[i])+1):
#       if j % 2 != 0:
#         split_s[i][j-1] = split_s[i][j-1].upper()
#       elif j % 2 == 0:
#         split_s[i][j-1] = split_s[i][j-1].lower()
#     split_s[i] = ''.join(split_s[i])

#   answer = ' '.join(split_s)
#   return answer

# print(solution("try hello world"))

# -------------------------------------------------------------------------------- 7. 문자열 내 p와 y의 개수
# ------------------------------------------- 내꺼 5분 컷!
# def solution(s):
#   s = s.lower()
#   count = 0
#   for i in s:
#     if i == 'p':
#       count += 1
#     elif i == 'y':
#       count -= 1
#   return True if count == 0 else False 

# ------------------------------------------- 커뮤니티 count 내장함수
# def solution(s):
#   s = s.lower()
#   return s.count('p') == s.count('y')

# print(solution("pPoooyY"))
# print(solution("Pyy"))

# -------------------------------------------------------------------------------- 8. 소수 찾기
# ------------------------------------------- 내꺼 5분 컷!
# from math import sqrt

# def prime(n):
#   for i in range(2,int(sqrt(n))+1):
#     if n%i == 0:
#       return False
#   return True


# def solution(n):
#   count = 0
#   for i in range(2,n+1):
#     if prime(i):
#       count += 1
#   return count

# print(solution(10))
# print(solution(5))

# -------------------------------------------------------------------------------- 9. 최소직사각형
# ------------------------------------------- 내꺼 7분 컷!
# def solution(sizes):
#   max_list = []
#   min_list = []
#   for size in sizes:
#     size[0],size[1] = max(size[0],size[1]), min(size[0],size[1])
#     max_list.append(size[0])
#     min_list.append(size[1])
#   return max(max_list) * max(min_list)

# print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
# -------------------------------------------------------------------------------- 10. 내적
# ------------------------------------------- 내꺼 3분 컷!
# def solution(a, b):
#   summ = 0
#   for i ,j in zip(a,b):
#     summ += (i*j)
#   return summ

# print(solution([1,2,3,4], [-3,-1,0,2]))
# print(solution([-1,0,1], 	[1,0,-1]))
