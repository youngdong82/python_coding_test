# --------------------------------------------220128
n = int(input())

d = [0] * (n+1)

def pibo_rec(x):
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = pibo_rec(x-1) + pibo_rec(x-2)
  return d[x]

print(pibo_rec(n))

# 반복문
n = int(input())

d = [0] * (n+1)

d[1] = 1
d[2] = 1

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])




