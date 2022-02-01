
# # 소수 구하기
# import math

# m,n = map(int,input().split())
# array = [True for _ in range(n+1)]

# for i in range(2, int(math.sqrt(n))+1):
#   if array[i] == True:
#     j = 2
#     while j*i <= n:
#       array[j * i] = False
#       j+=1

# for i in range(m,n+1):
#   if array[i] == True:
#     print(i, end=' ')

# 암호 만들기


from itertools import combinations
from unittest import result


l,c = map(int,input().split())
words = input().split()
mo = ['a','e','i','o','u']
words.sort()


candidates = list(combinations(words, 4))
result = []

for candidate in candidates:
  count = 0
  for i in candidate:
    if i in mo:
      count += 1
  if count >= 1 and l- 2 >=count:
    result.append(candidate)

for i in result:
  for j in i:
    print(j, end='')
  print()







# mo = ['a','e','i','o','u']
# moo = []
# jaa = []

# for i in words:
#   if i in mo:
#     moo.append(i)
#   else:
#     jaa.append(i)



  


# print(words)














# import math

# m, n = map(int, input().split())

# result = [True for _ in range(n + 1)]

# for i in range(2, int(math.sqrt(n)) + 1):
#     if result[i] == True:
#         j = 2
#         while i * j <= n:
#             result[i * j] = False
#             j += 1

# for i in range(m, len(result)):
#     if result[i] == True:
#         print(i)

# 암호 만들기
# from itertools import combinations

# l, c = map(int, input().split())
# data = list(input().split())
# data.sort()

# alpha_mo = ["a", "e", "i", "o", "u"]

# combination = list(combinations(data, l))
# result = []

# for i in combination:
#     ja = 0
#     mo = 0
#     for j in i:
#         if j in alpha_mo:
#             mo += 1
#         else:
#             ja += 1
#     if ja >= 2 and mo >= 1:
#         print("".join(i))
