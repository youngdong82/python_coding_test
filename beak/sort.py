# -------------------------------------------------------------------------------- 수 정렬하기 1
# ------------------------------------------- 내꺼
# n = int(input())
# data = []
# for i in range(n):
#   data.append(int(input()))

# for i in range(n):
#   a = i
#   for j in range(i+1,n):
#     if data[a] > data[j]:
#       a = j
#   data[a],data[i] = data[i],data[a]

# for i in data:
#   print(i)

# -------------------------------------------------------------------------------- 수 정렬하기 2
# ------------------------------------------- 내꺼
# n = int(input())
# data = []
# for i in range(n):
#   data.append(int(input()))

# data.sort()

# for i in data:
#   print(i)

# -------------------------------------------------------------------------------- 3. 10989 복습
# ------------------------------------------- 내꺼
# import sys

# n = int(sys.stdin.readline())

# dp = [0] * 10001

# for _ in range(n):
#   dp[int(sys.stdin.readline())] += 1

# for i in range(10001):
#   if dp[i] != 0:
#     for _ in range(dp[i]):
#       print(i)

# -------------------------------------------------------------------------------- 4. 2108번
# ------------------------------------------- 내꺼
# # n = int(input())
# data = []
# dic = {}

# for i in range(n):
#   a = int(input())
#   data.append(a)
#   if a not in dic.keys():
#     dic[a] = 1
#   else:
#     dic[a] += 1

# data.sort()
# dic_sort = list(dic.items())

# dic_sort.sort(key=lambda x: (-x[1], x[0]))
# max_time = dic_sort[0][1]

# big_dic = []
# for i in dic_sort:
#   if i[1] >= max_time:
#     big_dic.append(i[0])


# aver = int(round(sum(data)/n, 0))
# mid = data[n//2]
# common = 0
# if len(big_dic) > 1:
#   common = big_dic[1]
# else:
#   common = big_dic[0]
# rang = max(data) - min(data)
# print(aver)
# print(mid)
# print(common)
# print(rang)

# -------------------------------------------------------------------------------- 5. 1427번
# ------------------------------------------- 내꺼
# n = list(str(input()))
# n.sort(reverse= True)
# print(''.join(n))

# -------------------------------------------------------------------------------- 6. 11650번
# ------------------------------------------- 내꺼 3분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   x,y = map(int,input().split())
#   data.append((x,y))
# data.sort(key=lambda x: (x[0], x[1]))

# for i in data:
#   a,b = i
#   print(a,b)

# -------------------------------------------------------------------------------- 5. 11651번
# ------------------------------------------- 내꺼 3분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   x,y = map(int,input().split())
#   data.append((x,y))
# data.sort(key=lambda x: (x[1], x[0]))

# for i in data:
#   a,b = i
#   print(a,b)

# -------------------------------------------------------------------------------- 5. 1181번
# ------------------------------------------- 내꺼 3분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   a = str(input())
#   if a not in data:
#     data.append(a)
# data.sort(key=lambda x: (len(x),x))

# for i in data:
#   print(i)

# -------------------------------------------------------------------------------- 5. 10814번
# ------------------------------------------- 내꺼 5분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   age,name = input().split()
#   age = int(age)
#   name = str(name)
#   data.append((age,name))

# data.sort(key=lambda x: (x[0]))

# for i in data:
#   age,name = i
#   print(age, name)

# -------------------------------------------------------------------------------- 5. 18870번 복습!!
# ------------------------------------------- 내꺼 시간초과
# import sys

# input = sys.stdin.readline

# n = int(input())
# data = list(map(int,input().split()))

# comp_data = sorted(list(set(data)))
# dic = {comp_data[i] : i for i in range(len(comp_data))}

# for i in data:
#   print(dic[i], end=' ') 

