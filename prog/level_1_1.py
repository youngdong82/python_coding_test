
# -------------------------------------------------------------------------------- strip()
# -------------------------------------------------------------------------------- '구분자'.join()
# -------------------------------------------------------------------------------- 문자열 더하기, 곱하기 등등
# -------------------------------------------------------------------------------- 유클리드 호제법
# https://binaryjourney.tistory.com/93


# -------------------------------------------------------------------------------- 1. 직사각형 별 찍기
# ------------------------------------------- 내꺼 6분 컷
# a, b = map(int, input().strip().split(' '))
# answer = []
# for i in range(b):
#     star = []
#     for j in range(a):
#         star.append('*')
#     answer.append(star)

# for i in answer:
#   for j in i:
#     print(j, end='')
#   print()

# ------------------------------------------- 커뮤니티 넣었다 뺄 필요 없이 바로....
# a, b = map(int, input().strip().split(' '))

# for i in range(b):
#     for j in range(a):
#         print('*', end='')
#     print('')

# -------------------------------------------------------------------------------- 2. x만큼 간격이 있는 n개의 숫자
# ------------------------------------------- 내꺼 4분 컷
# def solution(x, n):
#     answer = [x]
#     summ = x
#     for _ in range(n-1):
#       summ += x
#       answer.append(summ)
#     return answer

# print(solution(2,1))
# print(solution(2,5))
# print(solution(4,3))
# print(solution(-4,2))

# -------------------------------------------------------------------------------- 3. 행렬의 덧셈
# 뭔가 쓸데없이 긴 느낌...?
# 쓸데없지 않다. 확인하는 과정이 있었을 뿐!
# 2,3번째 코드는 testcase 3 작동 안함
# ------------------------------------------- 내꺼 12분 컷 
# def solution(arr1, arr2):
#   arr = []
#   for i in range(len(arr1)):
#     if type(arr1[i]) == list:
#       arr_arr = []
#       for j in range(len(arr1[0])):
#         arr_arr.append(arr1[i][j] + arr2[i][j])
#       arr.append(arr_arr)
#     else:
#       arr.append(arr1[i] + arr2[i])
#   return arr

# ------------------------------------------- zip 사용 5분 컷
# def solution(A, B):
#   answer = []
#   for a,b in zip(A,B):
#     answer_2 = []
#     for c,d in zip(a,b):
#       answer_2.append(c+d)
#     answer.append(answer_2)
#   return answer

# ------------------------------------------- 커뮤니티 
# def solution(A,B):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
#     return answer

# print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
# print(solution([[1],[2]], [[3],[4]]))
# print(solution([1,2], [3,4]))

# -------------------------------------------------------------------------------- 4. 핸드폰 번호 가리기
# ------------------------------------------- 내꺼 12분 컷 
# def solution(phone_number):
#   answer = []
#   for i in range(len(phone_number)-4):
#     answer.append('*')
#   for i in phone_number[len(phone_number)-4:]:
#     answer.append(i)

#   return ''.join(answer)

# ------------------------------------------- 커뮤니티 ㅅㅂ...ㅋㅋㅋㅋㅋㅋ
# def solution(s):
#   return (len(s) - 4) * '*' + s[-4:]

# print(solution("01033334444"))
# print(solution("027778888"))

# -------------------------------------------------------------------------------- 5. 짝수와 홀수
# ------------------------------------------- 내꺼 2분 컷 
# def solution(num):
#   if num%2 == 0:
#     return 'Even'
#   else:
#     return 'Odd'

# ------------------------------------------- 커뮤니티 한줄쓰기 굳이 필요 없다.
# def solution(num):
#     return "Even" if num%2 == 0 else "Odd"

# print(solution(3))
# print(solution(4))

# -------------------------------------------------------------------------------- 6. 제일 작은 수 제거
# ------------------------------------------- 내꺼 1분 컷
# def solution(arr):
#   arr.remove(min(arr))
#   return arr if len(arr) != 0 else [-1]

# print(solution([4,3,2,1]))
# print(solution([10]))

# -------------------------------------------------------------------------------- 7. 하샤드 수
# # ------------------------------------------- 내꺼 6분 컷
# def solution(x):
#   summ = 0
#   for i in str(x):
#     summ += int(i)
#   return x%summ == 0 

# print(solution(10))
# print(solution(12))
# print(solution(11))
# print(solution(13))

# -------------------------------------------------------------------------------- 8. 최대공약수와 최소공배수 실패! - 복습
# ------------------------------------------- 내꺼 왜 안되는건지 모르겠네...
# from math import sqrt


# def solution(n, m):
#   if n == m:
#     return [n, n]
#   n, m = min(n,m), max(n,m)
#   minn = []
#   for i in range(1,int(sqrt(m))+1):
#     if n%i == 0 and m%i == 0:
#       minn.append(i)
#   minnn = 1
#   for i in minn:
#     minnn *= i
#   maxx = minnn * (n//minnn) * (m//minnn)
    
#   return [minnn, maxx]

# ------------------------------------------- 커뮤니티 유클리드 호제법...?
# def gcd(n, m):
#     if n%m == 0: 
#       return m
#     else: 
#       return gcd(m, n%m)

# def lcm(n, m):
#     return n*m//gcd(n, m)

# def solution(n, m):
#     n, m = max(n, m), min(n, m)
#     answer = [gcd(n, m), lcm(n, m)]
#     return answer

# ------------------------------------------- 커뮤니티 2 ...???
# def solution(a, b):
#     for i in range(a):
#         if a%(a-i)+b%(a-i) == 0:
#             return [a-i, a*b//(a-i)]

# print(solution(3,12))
# print(solution(2,5))
# print(solution(4,7))
# print(solution(1,7))
# print(solution(12,3))
# print(solution(2,2))

# -------------------------------------------------------------------------------- 9. 로또의 최고 순위와 최저 순위
# ------------------------------------------- 내꺼 15분 컷ㅋㅋㅋ
def solution(lottos, win_nums):
  n = lottos.count(0)
  count = 0
  for i in lottos:
    for j in win_nums:
      if i == j:
        count += 1

  minn = 7-count
  maxx = 7-(count+n)
  
  if minn == 7:
    minn = 6
  if maxx == 7:
    maxx = 6

  answer = [maxx, minn]
  return answer

# ------------------------------------------- 커뮤니티 오 이건 진짜 놀랍구만...!!
# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

# -------------------------------------------------------------------------------- 10. 문자열 내 마음대로 정렬하기
# ------------------------------------------- 내꺼 7분 컷
# def solution(strings, n):
#   strings.sort(key=lambda x : (x[n], x))

#   return strings

# print(solution(["sun", "bed", "car"], 1))
# print(solution(["abce", "abcd", "cdx"], 2))
