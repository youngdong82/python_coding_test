# 1로 만들기 22분 컷!!
n = int(input())

d = [10001] * (n+1)

d[0] = 0
d[1] = 0

for i in range(2,n+1):
  d[i] = min(d[i], d[i-1] + 1)
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2] +1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3] +1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5] +1)

print(d[n])


# 개미전사
n = int(input())
stores = list(map(int,input().split()))

d = [0] * n

d[0] = stores[0]
d[1] = max(stores[0],stores[1])

for i in range(2,n):
  d[i] = max(d[i-1], d[i-2] + stores[i])

print(d)


# 바닥공사
