

# -------------------------------------------------------------------------------- sys.stdin.readline().rstrip()
# ------------------------------------------- 내꺼
# import sys
# input = sys.stdin.readline

# a = input()
# b = input().rstrip()
# print(a, len(a))
# print(b, len(b))

# 스택
# -------------------------------------------------------------------------------- 1. 17298 번 오큰수
# ------------------------------------------- 내꺼
# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int,input().split()))
# answer = []
# for i in range(n):
#   for j in range(i+1, n):
#     if data[j] > data[i]:
#       answer.append(data[j])
#       break
#   else:
#     answer.append(-1)
# for i in answer:
#   print(i, end =' ')

  # 큐 덱
  # -------------------------------------------------------------------------------- 1. 2164 번 카드2
# ------------------------------------------- 내꺼 5분 컷!
# from collections import deque
# n = int(input())
# q = deque([])
# for i in range(1,n+1):
#   q.append(i)

# while len(q) > 1:
#   q.popleft()
#   q.append(q.popleft())

# for i in q:
#   print(i)

# -------------------------------------------------------------------------------- 2. 11866 번 요세푸스 문제 0
# ------------------------------------------- 내꺼
# 인덱스를 옮기면서 값을 빼준다.
# n,k = map(int,input().split())

# data = []
# for i in range(1,n+1):
#   data.append(i)
# index = 0
# answer = []


# while data:
#   index = (index + (k-1))%len(data)
#   answer.append(data[index])
#   data.remove(data[index])

# print('<', end='')
# for i in range(len(answer)):
#   if i == len(answer)-1:
#     print(answer[i], end='')
#   else:
#     print(answer[i],end=', ')
# print('>')

# ------------------------------------------- 이전 풀이
# index를 변경하지 않고 표 전체를 계속 돌린다.
# from collections import deque

# n,k = map(int,input().split())
# queue = deque()
# for i in range(1,n+1):
#     queue.append(i)
    

# print('<', end='')
# while queue:
#     for i in range(k-1):
#         queue.append(queue[0])
#         queue.popleft()
#     print(queue.popleft(), end='')
#     if queue:
#         print(',', end=' ')
# print('>')


# -------------------------------------------------------------------------------- 3. 프린터 큐
# ------------------------------------------- 내꺼 집중 안되서 오래걸렸는데 복습 필요없음
# from collections import deque


# test_case = int(input())
# for _ in range(test_case):
#   n, m = map(int,input().split())
#   q = deque(list(map(int,input().split())))

#   count = 0
#   while q:
#     # 앞에가 우선순위 가장 높다면
#     if q[0] == max(q):
#       q.popleft()
#       count += 1
#       if m == 0:
#         print(count)
#         break
#       else:
#         m -= 1
#     # 안높다면 뒤로 보내
#     else:
#       if m == 0:
#         m = len(q)-1
#       else:
#         m -= 1
#       q.append(q.popleft())


# -------------------------------------------------------------------------------- 4. 10866 번 덱 
# ------------------------------------------- 내꺼
# from collections import deque
# import sys
# input = sys.stdin.readline


# n = int(input())
# q = deque([])
# orders = ['pop_front', 'pop_back', 'front', 'back']

# for _ in range(n):
#   order = list(input().split())
#   order[0] = str(order[0])

#   if order[0] in orders:
#     if len(q) == 0:
#       print(-1)
#     else:
#       if order[0] == 'pop_front':
#         print(q.popleft())
#       elif order[0] == 'pop_back':
#         print(q.pop())
#       elif order[0] == 'front':
#         print(q[0])
#       elif order[0] == 'back':
#         print(q[-1])
#   else:
#     if order[0] == 'push_front':
#       q.appendleft(int(order[1]))
#     elif order[0] == 'push_back':
#       q.append(int(order[1]))
#     elif order[0] == 'size':
#       print(len(q))
#     elif order[0] == 'empty':
#       if len(q) == 0:
#         print(1)
#       else:
#         print(0)

# -------------------------------------------------------------------------------- 5. 1021번 회전하는 큐 
# ------------------------------------------- 내꺼
# from collections import deque


# n,m = map(int,input().split())
# q = deque([])
# for i in range(1,n+1):
#   q.append(i)
# target = list(map(int,input().split()))

# count = 0
# while target:
#   if q[0] == target[0]:
#     q.popleft()
#     target.pop(0)
#   else:
#     if q.index(target[0]) > len(q)-q.index(target[0]):
#       q.appendleft(q.pop())
#     else:
#       q.append(q.popleft())
#     count += 1
# print(count)

# -------------------------------------------------------------------------------- 6. 5430 AC
# ------------------------------------------- 내꺼
# import sys
# input = sys.stdin.readline

# test_case = int(input())
# for _ in range(test_case):
#   order = str(input().rstrip())
#   n = int(input())
#   a = input().rstrip()
#   if a == '[]':
#     data = []
#   else:
#     data = list(map(str,a[1:-1].split(',')))

#   answer = True
#   count_r = 0
#   for i in order:
#     if i == 'R':
#       count_r += 1
#     elif i == 'D':
#       if len(data) == 0:
#         answer = False
#         break
#       else:
#         if count_r%2 ==0:
#           data.pop(0)
#         else:
#           data.pop()
  
#   if not answer:
#     print('error')
#   else:
#     if count_r %2 == 0:
#       print('['+','.join(data) + ']')
#     else:
#       print('['+','.join(data[::-1]) + ']')

# ------------------------------------------- 내꺼 2
# from collections import deque
# import sys
# input = sys.stdin.readline


# test_case = int(input())
# for _ in range(test_case):
#   order = str(input().rstrip())
#   n = int(input())
#   q = deque(input().rstrip()[1:-1].split(','))


#   answer = True
#   count_r = 0
#   if n == 0:
#     q = []

#   for i in order:
#     if i == 'R':
#       count_r += 1
#     elif i == 'D':
#       if len(q) == 0:
#         answer = False
#         break
#       else:
#         if count_r%2 ==0:
#           q.popleft()
#         else:
#           q.pop()
  
#   if not answer:
#     print('error')
#   else:
#     if count_r %2 == 0:
#       print("[" + ",".join(q) + "]")
#     else:
#       q.reverse()
#       print("[" + ",".join(q) + "]")

