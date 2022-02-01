# 소수 판별
import math

n = int(input())

def prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True

print(prime(n))

# 에라스토네스의 체
import math

n = int(input())
array = [True for _ in range(n+1)]

for i in range(2,int(math.sqrt(n)+1)):
  if array[i] == True:
    j = 2
    while i * j <=n:
      array[i * j] = False
      j += 1


for i in range(1,n+1):
  if array[i] == True:
    print(i, end=' ')


# 투 포인터
n = 5
m = 5

array = [1,2,3,2,5]

end = 0
inter_sum = 0
count = 0

for start in range(n):
  while inter_sum < m and end < n:
    inter_sum += array[end]
    end += 1
  if inter_sum == m:
    count += 1
  inter_sum -= array[start]

print(count)


# # 합집합
a = [1, 3, 5]
b = [2, 4, 6, 8]

i = 0
j = 0
k = 0

result = [0] * (len(a) + len(b))

while i < len(a) or j < len(b):
  if j >=len(b) or (i < len(a) and a[i] <= b[j]):
    result[k] = a[i]
    i += 1
  else:
    result[k] = b[j]
    j += 1
  k += 1

print(result)


# 구간합
left, right = 3, 4
data = [10, 20, 30, 40, 50]


prefix = [0]
summ = 0
for i in range(len(data)):
  summ += data[i]
  prefix.append(summ)

print(prefix[right] - prefix[left-1])


