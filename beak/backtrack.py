# -------------------------------------------------------------------------------- 1. 15649 번 N과 M (1)
# 자주하는 실수
# 1. 가지치기를 하지 않아서 시간초과 발생
# 2. 한 단계 더 들어갈 때 가능한 값인지 불가능한 값인지 비효율적으로 판단(visited 같은 함수를 이용하자)
# 3. 재귀를 들어갔다가 탈출할 때 값을 원래대로 바꿔놓지 않는다. 넣었으면 빼라.

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

# -------------------------------------------------------------------------------- 5. 9663 번 N-Queen
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

