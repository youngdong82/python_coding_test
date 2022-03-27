# -------------------------------------------------------------------------------- 2e+9+1...
# a = 2e+9+1
# b = int(1e9)
# print(a)
# print(b)


# -------------------------------------------------------------------------------- 1. 3273번 복습...?
# ------------------------------------------- 내꺼 17분 컷!
# n = int(input())
# data = list(map(int,input().split()))
# data.sort()
# target = int(input())
# min_index = 0
# max_index = n-1
# count = 0
# while min_index <max_index:
#   summ = data[min_index] + data[max_index]
#   if summ == target:
#     count += 1
#     min_index += 1
#   elif summ > target:
#     max_index -= 1
#   else:
#     min_index += 1
# print(count)

# -------------------------------------------------------------------------------- 2. 2470번 복습ㅋㅋㅋㅋ
# ------------------------------------------- 내꺼
# n = int(input())
# data = list(map(int,input().split(' ')))
# data.sort()

# min_index = 0
# max_index = n-1

# min_value = 2e+9+1
# final = []

# while min_index < max_index:
#   data_min = data[min_index]
#   data_max = data[max_index]
#   summ =  data_min + data_max

#   if summ == 0:
#     final = [data_min, data_max]
#     break

#   if abs(summ) < min_value:
#     min_value = abs(summ)
#     final = [data_min, data_max]

#   if summ > 0:
#     max_index -= 1
#   elif summ < 0:
#     min_index += 1

# print(final[0], final[1])

# -------------------------------------------------------------------------------- 3. 1806번 복습!!!
# ------------------------------------------- 내꺼 아 이거 동빈나랑 같이 공부했던건데...ㅠㅠㅠ
# n,target = map(int,input().split())
# data = list(map(int,input().split()))

# sum_data = [0] * (n+1)
# for i in range(1,n+1):
#   sum_data[i] = sum_data[i-1] + data[i-1]

# left = 0
# right = 1
# answer = int(1e9)


# while left != n:
#     if sum_data[right] - sum_data[left] >= target:
#         if right - left< answer:
#             answer = right - left
#         left += 1
        
#     else:
#         if right != n:
#             right += 1
#         else:
#             left += 1

# if answer != int(1e9):
#   print(answer)
# else:
#   print(0)

# -------------------------------------------------------------------------------- 4. 1644번  복습!!
# 1. n보다 작은 소수들 전부 구해서 prime_deck에 넣기
# 2. 부분합 적용해서 (자기자신 포함 가능) 가능할 때마다 count += 1
# 3. count 출력
# ------------------------------------------- 내꺼
from math import sqrt

n = int(input())
# 에라토네스의 체를 이용한 소수 list 구하기
array = [True for i in range(n+1)]

for i in range(2,int(sqrt(n))+1):
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i*j] = False
      j += 1

prime_deck = []
for i in range(len(array)):
  if array[i] == True:
    prime_deck.append(i)

prime_deck = prime_deck[2:]

# 부분 합
sum_reck = [0 for _ in range(len(prime_deck)+1)]

for i in range(len(prime_deck)):
  sum_reck[i+1] = sum(prime_deck[:i+1])

left = 0
right = 0

count = 0
while left < len(sum_reck) and right < len(sum_reck):
  summ = sum_reck[right] - sum_reck[left]
  if summ == n:
    count += 1
    left += 1
  elif summ > n:
    left += 1
  else:
    right += 1

print(count)









# -------------------------------------------------------------------------------- 5. 1450번
# 시키는대로 하면 안끝남
# ------------------------------------------- 내꺼
# from itertools import combinations


# n,c = map(int,input().split())
# deck = list(map(int,input().split()))


# count = 0
# for i in range(1,n+1):
#   candidates = list(combinations(deck,i))
#   for candidate in candidates:
#     if sum(candidate) <= c:
#       count += 1
# print(count+1)
