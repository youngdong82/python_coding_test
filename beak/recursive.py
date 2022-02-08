# --------------------------------------------------- 팩토리얼 - 5분 컷!
# import math
# n = int(input())

# math.factorial(n)
# print(math.factorial(n))
# -------------------------------다른 버전
# n = int(input())
# result = 1
# for i in range(1,n+1):
#   result *= i

# print(result)
# --------------------------------------------------- 피보나치 4분컷인데  왜 대체 런타임 에러가..?
# n = int(input())

# dp = [0]*(n+1)

# dp[1] = 1
# dp[2] = 1

# for i in range(3,n+1):
#   dp[i] = dp[i-1] + dp[i-2]

# print(dp[n])
# -------------------------------다른 버전
# n = int(input())

# dp = [0]*(n+1)

# def fibo(n):
#   if n == 2 or n == 1:
#     return 1
#   if dp[n] != 0:
#     return dp[n]
#   dp[n] = fibo(n-1) + fibo(n-2)
#   return dp[n]

# print(fibo(n))
# -------------------------------다른 버전 이건 답으로 되는데 뭐징
# n = int(input())

# fibonacci = [0, 1]
# for i in range(2, n+1):
#     num = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(num)
# print(fibonacci[n])
# --------------------------------------------------- 별찍기




# --------------------------------------------------- 하노이 탑 실패! -복습 - 암기
# n = int(input())
# # a에서 시작해서, b를 이용해서,  c로 이동,
# def hanoi(n, a, b, c):
#   if n == 1:
#     print(a, c)
#   else:
#     hanoi(n - 1, a, c, b)
#     print(a, c)
#     hanoi(n - 1, b, a, c)

# sum = 1
# for _ in range(n - 1):
#     sum = sum * 2 + 1

# print(sum)
# hanoi(n, 1, 2, 3)