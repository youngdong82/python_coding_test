# -------------------------------------------------------------------------------- 1. 15649 번 N과 M (1)
# ------------------------------------------- 내꺼 맞긴 한데 백트래킹으로 풀지 않았다.
# from itertools import permutations


# n,m = map(int,input().split())
# answer = list(permutations(range(1,n+1), m))

# for i in answer:
#   for j in i:
#     print(j, end=' ')
#   print()

# ------------------------------------------- 커뮤니티 백트래킹
# n,m = map(int,input().split())
# tmp = []
# def back():
#   if len(tmp) == m:
#     print(' '.join(map(str,tmp)))
#     return
#   for i in range(1,n+1):
#     if i not in tmp:
#       tmp.append(i)
#       back()
#       tmp.pop()

# back()

# -------------------------------------------------------------------------------- 2. 15650 번 N과 M (2)
# ------------------------------------------- 내꺼
# n,m = map(int,input().split())

# tmp = []
# def back():
#   for i in range(1,n+1):
#     if len(tmp) == m:
#       if tmp == sorted(tmp):
#         print(' '.join(map(str,tmp)))
#       return
#     if i not in tmp:
#       tmp.append(i)
#       back()
#       tmp.pop()
# back()

# -------------------------------------------------------------------------------- 3. 15651 번 N과 M (3)
# ------------------------------------------- 내꺼 1 product
# from itertools import product


# n,m = map(int,input().split())
# answer = list(product(range(1,n+1), repeat=m))
# for i in answer:
#   print(' '.join(map(str,i)))

# ------------------------------------------- 내꺼 2 백트래킹
# n,m = map(int,input().split())

# tmp = []
# def back():
#   if len(tmp) == m:
#     print(' '.join(map(str,tmp)))
#     return
#   for i in range(1,n+1):
#     tmp.append(i)
#     back()
#     tmp.pop()

# back()


# -------------------------------------------------------------------------------- 4. 15652 번 N과 M (4)
# 비 내림차순 뭐여 올림차순이라 하면 되는거 아니냐
# 각 원소가 앞의 원소보다 크거나 같을 경우
# ------------------------------------------- 내꺼
# n,m = map(int,input().split())

# tmp = []
# def back():
#   if len(tmp) == m:
#     if tmp == sorted(tmp):
#       print(' '.join(map(str,tmp)))
#     return
#   for i in range(1,n+1):
#     tmp.append(i)
#     back()
#     tmp.pop()
# back()

# -------------------------------------------------------------------------------- 5. 9663 번 N-Queen 복습
# 어려운데...ㅠ
# ------------------------------------------- 커뮤니티
# n = int(input())

# answer = 0
# row = [0] * n

# def is_promising(x):
#   for i in range(x):
#     if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#       return False
  
#   return True

# def n_queens(x):
#   global answer
#   if x == n:
#     answer += 1
#     return
#   else:
#     for i in range(n):
#       # [x, i]에 퀸을 놓겠다.
#       row[x] = i
#       if is_promising(x):
#         n_queens(x+1)

# n_queens(0)
# print(answer)

# -------------------------------------------------------------------------------- 6. 2580 번 스도쿠 아 졸ㄹㄹㄹ라 어렵네...
# ------------------------------------------- 커뮤니티
# graph = []
# for i in range(9):
#   graph.append(list(map(int,input().split())))

# blank = []
# for i in range(9):
#   for j in range(9):
#       if graph[i][j] == 0:
#           blank.append((i, j))

# def checkRow(x, a):
#   for i in range(9):
#     if a == graph[x][i]:
#       return False
#   return True

# def checkCol(y, a):
#   for i in range(9):
#     if a == graph[i][y]:
#       return False
#   return True

# def checkRect(x, y, a):
#   nx = x // 3 * 3
#   ny = y // 3 * 3
#   for i in range(3):
#     for j in range(3):
#       if a == graph[nx+i][ny+j]:
#         return False
#   return True


# def dfs(idx):
#   if idx == len(blank):
#     for i in range(9):
#       print(*graph[i])
#     return

#   for i in range(1, 10):
#     x = blank[idx][0]
#     y = blank[idx][1]

#     if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
#       graph[x][y] = i
#       dfs(idx+1)
#       graph[x][y] = 0

# dfs(0)

# 이게 뭐하는거여..
# a = [[1,2,3,4,5] for _ in range(5)]
# for i in range(len(a)):
#   print(*a[i])


# -------------------------------------------------------------------------------- 7. 14888 번 연산자 끼워넣기
# 수와 수 사이에 연산자를 하나씩 넣어서
# 수식을 하나 만들 수 있다.
# 주어진 수의 순서를 바꾸면 안 된다.
# ------------------------------------------- 내꺼 어찌되었건 풀긴 풀었다ㅋㅋㅋ
# from itertools import permutations


# n = int(input())
# data = list(map(int,input().split()))
# oper = []
# p,m,t,d = map(int,input().split())

# for i in range(p):
#   oper.append('+')
# for i in range(m):
#   oper.append('-')
# for i in range(t):
#   oper.append('*')
# for i in range(d):
#   oper.append('//')


# def calculate(oper,x,y):
#   if oper == '+':
#     return x + y
#   elif oper == '-':
#     return x-y
#   elif oper == '*':
#     return x*y
#   elif oper == '//':
#     if x <0:
#       return -(-x//y)
#     else:
#       return x//y
  
# answer = []
# candidates = list(permutations(oper, len(oper)))
# for candidate in candidates:
#   stack = [data[0]]
#   for i in range(len(data)-1):
#     x = stack.pop()
#     y = data[i+1]
#     oper = candidate[i]
#     stack.append(calculate(oper, x,y)) 
#   answer.append(stack[0])
      

# print(max(answer))
# print(min(answer))

# ------------------------------------------- 재귀로 풀어보자
# n = int(input())
# data = list(map(int,input().split()))
# op = list(map(int,input().split()))

# max_value = int(-1e9)
# min_value = int(1e9)


# def dfs(depth, total, p,m,t,d):
#   global max_value, min_value
#   if depth == n:
#     max_value = max(total,max_value)
#     min_value = min(total,min_value)
#     return

#   if p:
#     dfs(depth +1,total + data[depth], p-1,m,t,d)
#   if m:
#     dfs(depth +1,total - data[depth], p,m-1,t,d)
#   if t:
#     dfs(depth +1,total * data[depth], p,m,t-1,d)
#   if d:
#     dfs(depth +1, int(total / data[depth]), p,m,t,d-1)

# dfs(1,data[0], op[0],op[1],op[2],op[3])

# print(max_value)
# print(min_value)

# -------------------------------------------------------------------------------- 8. 14889 번 스타트와 링크 복습
# ------------------------------------------- 내꺼
# from itertools import combinations


# n = int(input())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input().split())))

# candidates = list(combinations(range(n),n//2))

# def calculate(array):
#   answer = 0
#   for i in array:
#     for j in array:
#       if i != j:
#         answer += graph[i][j]
#   return answer

# answer = int(1e9)
# for start in candidates:
#   start = list(start)
#   link = []
#   for i in range(n):
#     if i not in start:
#       link.append(i)
#   answer = min(answer, abs(calculate(start) - calculate(link)))
# print(answer)


# ------------------------------------------- 커뮤
# import sys
# sys.setrecursionlimit(100001)

# n = int(input())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input().split())))
# visited = [0 for _ in range(n)]
# min_value = int(1e9)

# def dfs(index, count):
#   global min_value
#   if count == n//2:
#     start, link = 0,0
#     for i in range(n):
#       for j in range(n):
#         if visited[i] == True and visited[j] == True:
#           start += graph[i][j]
#         elif visited[i] == False and visited[j] == False:
#           link += graph[i][j]
#     min_value = min(min_value, abs(start - link))

#   for i in range(index, n):
#     if visited[i] == True:
#       continue
#     visited[i] = 1
#     dfs(i+1, count + 1)
#     visited[i] = 0
  
# dfs(0,0)
# print(min_value)

# -------------------------------------------------------------------------------- 9. 15654 번 n과 m (5)
# ------------------------------------------- 내꺼
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# tmp = []
# def dfs():
#   if len(tmp) == m:
#     print(' '.join(map(str,tmp)))

#   for i in range(n):
#     if data[i] not in tmp:
#       tmp.append(data[i])
#       dfs()
#       tmp.pop()

# dfs()

# -------------------------------------------------------------------------------- 9. 15655 번 n과 m (6)
# ------------------------------------------- 내꺼
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# tmp = []
# def dfs():
#   if len(tmp) == m:
#     if tmp == sorted(tmp):
#       print(' '.join(map(str,tmp)))
#   return
  
#   for i in data:
#     if i not in tmp:
#       tmp.append(i)
#       dfs()
#       tmp.pop()
# dfs()

# -------------------------------------------------------------------------------- 9. 15656 번 n과 m (7)
# ------------------------------------------- 내꺼
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# tmp = []
# def dfs():
#   if len(tmp) == m:
#     print(' '.join(map(str,tmp)))
#     return
  
#   for i in data:
#     tmp.append(i)
#     dfs()
#     tmp.pop()
# dfs()
# -------------------------------------------------------------------------------- 9. 15657 번 n과 m (8)
# ------------------------------------------- 내꺼
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# tmp = []
# def dfs():
#   if len(tmp) == m:
#     if tmp == sorted(tmp):
#       print(' '.join(map(str,tmp)))
#     return
  
#   for i in data:
#     tmp.append(i)
#     dfs()
#     tmp.pop()
# dfs()

# -------------------------------------------------------------------------------- 9. 15654 번 n과 m (9)
# ------------------------------------------- 내꺼 시간초과
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()
# visited = [False] * n

# tmp = []
# answer = []
# def dfs():
#   if len(tmp) == m:
#     print(' '.join(map(str,tmp)))
#     return
#   overlap = 0
#   for i in range(n):
#     if not visited[i] and overlap != data[i]:
#       tmp.append(data[i])
#       visited[i] = True
#       overlap = data[i]
#       dfs()
#       tmp.pop()
#       visited[i] = False
# dfs()

# ------------------------------------------- 내꺼 2
# from itertools import permutations


# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# candidates = list(permutations(data,m))

# candidates = list(set(candidates))
# candidates.sort()

# for i in candidates:
#   print(' '.join(map(str,i)))

# -------------------------------------------------------------------------------- 9. 15654 번 n과 m (10)
# ------------------------------------------- 내꺼
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()
# visited = [False] * n

# tmp = []
# def dfs():
#   if len(tmp) == m:
#     if tmp == sorted(tmp):
#       print(' '.join(map(str,tmp)))
#     return
  
#   overlap = 0
#   for i in range(n):
#     if visited[i] == False and overlap != data[i]:
#       visited[i] = True
#       tmp.append(data[i])
#       overlap = data[i]
#       dfs()
#       visited[i] = False
#       tmp.pop()
# dfs()

# ------------------------------------------- 내꺼 2
# from itertools import combinations


# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# candidates = list(combinations(data,m))

# candidates = list(set(candidates))
# candidates.sort()

# for i in candidates:
#   print(' '.join(map(str,i)))

# -------------------------------------------------------------------------------- 9. 15654 번 n과 m (11)
# ------------------------------------------- 내꺼 1
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()
# visited = [False] * n

# tmp = []
# def dfs():
#   if len(tmp) == m:
#     print(' '.join(map(str,tmp)))
#     return
  
#   overlap = 0
#   for i in range(n):
#     if overlap != data[i]:
#       visited[i] = True
#       tmp.append(data[i])
#       overlap = data[i]
#       dfs()
#       visited[i] = False
#       tmp.pop()
# dfs()

# ------------------------------------------- 내꺼 2
# from itertools import product

# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# candidates = list(product(data,repeat=m))

# candidates = list(set(candidates))
# candidates.sort()

# for i in candidates:
#   print(' '.join(map(str,i)))

# -------------------------------------------------------------------------------- 9. 15654 번 n과 m (12)
# ------------------------------------------- 내꺼 1
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# tmp = []
# def dfs():
#   if len(tmp) == m:
#     if tmp == sorted(tmp):
#       print(' '.join(map(str,tmp)))
#     return
  
#   overlap = 0
#   for i in range(n):
#     if overlap != data[i]:
#       tmp.append(data[i])
#       overlap = data[i]
#       dfs()
#       tmp.pop()

# dfs()

# ------------------------------------------- 내꺼 2
# from itertools import combinations_with_replacement

# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()

# candidates = list(combinations_with_replacement(data,m))

# candidates = list(set(candidates))
# candidates.sort()

# for i in candidates:
#   print(' '.join(map(str,i)))