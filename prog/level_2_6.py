# -------------------------------------------------------------------------------- 1. k진수에서 소수 개수 구하기 진수변환이랑 소수 확인하기 복습!!
# ------------------------------------------- 내꺼
# from math import sqrt

# def prime(n):
#   if n== 1 or n == 0:
#     return False
#   for i in range(2, int(sqrt(n)+1)):
#     if n%i == 0:
#       return False
#   return True

# def make(num, n):
#   total_string = '0123456789ABCDEF'
#   string = total_string[:n]
#   answer = ''
#   while num > 0:
#       num, mod = divmod(num, n)
#       answer += str(string[mod])
#   return answer[::-1]

# def solution(n, k):
#   result = make(n,k)
#   result = result.split('0')
#   after_re = []
#   for i in result:
#     if len(i)>0:
#         after_re.append(int(i))
#   count = 0
#   for i in after_re:
#     if prime(i):
#       count += 1

#   return count


# print(solution(437674,3))
# print(solution(110011,10))

# -------------------------------------------------------------------------------- 2. 양궁대회
# ------------------------------------------- 내꺼
def solution(n, info):
  a_dic = {}
  info = info[::-1]
  for i in range(11):
    a_dic[i] = info[i]


  print(a_dic)
  r_dic = {}


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))

# -------------------------------------------------------------------------------- 1.
# ------------------------------------------- 내꺼
# -------------------------------------------------------------------------------- 1.
# ------------------------------------------- 내꺼
# -------------------------------------------------------------------------------- 1.
# ------------------------------------------- 내꺼
