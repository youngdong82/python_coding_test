# 1로 만들기 22분 컷!!
# n = int(input())

# d = [10001] * (n+1)

# d[0] = 0
# d[1] = 0

# for i in range(2,n+1):
#   d[i] = min(d[i], d[i-1] + 1)
#   if i % 2 == 0:
#     d[i] = min(d[i], d[i//2] +1)
#   if i % 3 == 0:
#     d[i] = min(d[i], d[i//3] +1)
#   if i % 5 == 0:
#     d[i] = min(d[i], d[i//5] +1)

# print(d[n])

# ---------------------------------------------------220129
# 개미전사
# n = int(input())
# stores = list(map(int,input().split()))

# d = [0] * n

# d[0] = stores[0]
# d[1] = max(stores[0],stores[1])

# for i in range(2,n):
#   d[i] = max(d[i-2] + stores[i], d[i-1])

# print(d[n-1])

# 바닥공사
# n = int(input())

# d = [0] * (n+1)

# d[1] = 1
# d[2] = 3

# for i in range(3,n+1):
#   d[i] = d[i-1] + (d[i-2]*2)

# print(d[n])

# 효율적인 화폐구성
# n,m = map(int,input().split())
# coins = []
# for i in range(n):
#   coins.append(int(input()))

# d = [10001] * (m+1)

# d[0] = 0

# for i in coins:
#   for j in range(i,m+1):
#     if d[j-i] != 1001:
#       d[j] = min(d[j], d[j-i] + 1)

# print(d[m])