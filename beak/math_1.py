# --------------------------------------------------- 손익분기점 12분 컷!
# a,b,c = map(int,input().split())

# def calculate():
#   if c-b <= 0:
#     return -1
#   return a//(c-b)+1

# print(calculate())

# --------------------------------------------------- 벌집 17분 컷!
# n = int(input())

# def bees(n):
#   x = 1
#   i = 1
#   while True:
#     x += ((i-1)*6)
#     if x >= n:
#       return i
#     i += 1

# print(bees(n))

# --------------------------------------------------- 분수찾기 틀림ㅠㅠ - 복습
# n = int(input())

# x = 1
# while n > x:
#   n -= x
#   x += 1
# if x%2 == 0:
#   a = n
#   b = x-n+1
# else:
#   a = x-n+1
#   b = n

# print(a,'/',b, sep='')

# --------------------------------------------------- 달팽이는 올라가고 싶다. 맞추긴 했는데 어거지 느낌 25분컷! - 복습
# import math
# a,b,v = map(int,input().split())

# def up():
#   if a-b < 0:
#     return -1

#   result = (v-a) / (a-b)
#   return  math.ceil(result)+1

# 이걸 더 짧게!!
#   # result = 0
#   # while True:
#   #   if (a-b)*result + a >= v:
#   #     return result +1
#   #   result += 1
# print(up())

# --------------------------------------------------- ACM 호텔 14분 컷! - 복습
# 나누어 떨어질 때도 고려하자 꼭!
# t = int(input())
# for i in range(t):
#   h,w,n = map(int,input().split())
#   num = n//h +1
#   floor =  n%h
#   if floor == 0:
#     num = n//h
#     floor = h
#   print(f'{floor*100 + num}')

# --------------------------------------------------- 부녀회장이 될테야 -복습
# t = int(input())
# for _ in range(t):
#   k = int(input())
#   n = int(input())
#   graph = [[0] * (n) for _ in range(k+1)]

#   for i in range(n):
#     graph[0][i] = i+1
#     if i <= k:
#       graph[i][0] = 1

#   for i in range(1,k+1):
#     for j in range(1,n):
#       graph[i][j] = graph[i-1][j] + graph[i][j-1]


#   print(graph[k][n-1])

# --------------------------------------------------- 설탕 배달 실패! - 복습 while else????
# 힌트 - 5의 배수가 될 때까지 설탕 빼주기
# sugar = int(input())

# bag = 0
# while sugar >= 0:
#   if sugar % 5 == 0:
#     bag += (sugar//5)
#     print(bag)
#     break
#   sugar -= 3
#   bag += 1
# else:
#   print(-1)

# --------------------------------------------------- 큰 수 A+B 이게 뭐여..?../recap/recap.py 한번 읽고 지나가자 - 복습
# a,b = map(int,input().split())

# print(a + b)

# --------------------------------------------------- Fly me to the Alpha Centauri 와 전혀 모르겠어 감도 안잡힘 - 복습
# https://eunhee-programming.tistory.com/99
# 개어렵다ㅠ
# 규칙을 찾아내보도록 하자
# T = int(input())
# for i in range(T):
#   x,y = map(int,input().split())

#   d = y - x
#   n = 0

#   while True:
#     if d <= n*(n+1):
#       break
#     n += 1

#   if d <= n ** 2:
#     print(n*2-1)
#   else:
#     print(n*2)