# -------------------------------------------------------------------------------- 1. 행렬 테두리 회전하기
# 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의
# 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 
# ------------------------------------------- 내꺼
# 접근법은 같으나 커뮤니티 배울 필요가 있다.
# ------------------------------------------- 커뮤니티
# 여기서 small은 답을 윈한 것이지, 회전에 필요한 것은 아니다.
# def solution(rows, columns, queries):
#     answer = []
#     table = []
#     for r in range(rows):
#         table.append([a for a in range(r*columns+1, (r+1)*columns+1)])

#     for query in queries:
#         query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
#         tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
#         small = tmp

#         # left bottom to top
#         for i in range(query[0]+1, query[2]+1):
#             table[i-1][query[1]] = table[i][query[1]]
#             small = min(small, table[i][query[1]])
#         # bottom right to left
#         for i in range(query[1]+1, query[3]+1):
#             table[query[2]][i-1] = table[query[2]][i]
#             small = min(small, table[query[2]][i])
#         # right
#         for i in range(query[2]-1, query[0]-1, -1):
#             table[i+1][query[3]] = table[i][query[3]]
#             small = min(small, table[i][query[3]])
        
#         # top
#         for i in range(query[3]-1, query[1]-1, -1):
#             table[query[0]][i+1] = table[query[0]][i]
#             small = min(small, table[query[0]][i])
        
#         table[query[0]][query[1]+1] = tmp
#         answer.append(small)

#     return answer


# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100, 97, [[1,1,100,97]]))

# -------------------------------------------------------------------------------- 2. 예상 대진표 성공 but 시간초관
# ------------------------------------------- 내꺼 
# from math import ceil

# def solution(n,a,b):
#   play_count = 1
#   while n >2:
#     n //=2
#     play_count += 1

#   answer = 0
#   for i in range(1,play_count+1):
#     if ceil(a/2) == ceil(b/2):
#       answer = i
#       break
#     a = ceil(a/2)
#     b = ceil(b/2)
#   return answer

# # ------------------------------------------- 커뮤니티 ㅇ_ㅇ....
# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2
#         print(a,b)

#     return answer

# print(solution(16,2,9))
# print(solution(8,4,7))
# print(solution(8,2,3))
# print(solution(4,1,2))
# print(solution(2,1,2))

# -------------------------------------------------------------------------------- 3. N개의 최소공배수 11분 컷!
# ------------------------------------------- 내꺼 lcm 사용
# from math import lcm

# def solution(arr):
#   answer = arr[0]
#   for i in range(1,len(arr)):
#     answer = lcm(answer, arr[i])
#   return answer

# ------------------------------------------- 내꺼 gcd 사용
# from math import gcd

# def solution(arr):
#   answer = arr[0]
#   for i in arr:
#     answer = int((answer * i) / gcd(answer,i))
#   return answer

# print(solution([2,6,8,14]))
# print(solution([1,2,3]))

# -------------------------------------------------------------------------------- 4. 가장 큰 정사각형 찾기
# 동적 프로그래밍 문제인지 알고 푸는 것과
# 모르고 접하는 것은 천지차이...
# ------------------------------------------- 내꺼 전부 통과 그러나 시간초과ㅋㅋㅋㅋ
# def square_ok(board,x,y,count):
#   for i in range(x, x+1+count):
#     for j in range(y, y+1+count):
#       if 0 <= i < len(board) and 0 <= j < len(board[0]):
#         if board[i][j] == 0:
#           return count
#       else:
#         return count
#   return square_ok(board,x,y,count+1)

# def solution(board):
#   count = 0
#   for i in range(len(board)):
#     for j in range(len(board[0])):
#       count = square_ok(board,i,j,count)
#   return count **2

# ------------------------------------------- 커뮤니티 동적프로그래밍 이해가 되긴 한데.....에휴
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-dp
# def solution(board):
#     n = len(board)
#     m = len(board[0])

#     # dp 준비
#     dp = [[0]*m for _ in range(n)]
#     dp[0] = board[0]
#     for i in range(1,n):
#       dp[i][0] = board[i][0]

#     # 2중 포문으로 연산
#     for i in range(1, n):
#       for j in range(1, m):
#         if board[i][j] == 1:
#           dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
#     # # 최대 넓이 구하기
#     answer = 0
#     for i in range(n):
#         temp = max(dp[i])
#         answer = max(answer, temp)
    
#     return answer**2

# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# print(solution([[0,0,1,1],[1,1,1,1]]))

# -------------------------------------------------------------------------------- 5. 점프와 순간이동
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EC%A0%90%ED%94%84%EC%99%80-%EC%88%9C%EA%B0%84-%EC%9D%B4%EB%8F%99
# ------------------------------------------- 내꺼 전부 통과 그러나 시간초과ㅋㅋㅋㅋ
# 동적프로그래밍 인줄 알았는데...
# INF = int(1e9)


# def solution(n):
#   dp = [INF] * (n+1)
#   dp[1] = 1

#   for i in range(2,n+1):
#     if dp[i] == INF:
#       if i%2 == 0 and dp[i//2] != INF:
#         a = 1
#         while True:
#           if i*a > n:
#             break
#           dp[i*a] = dp[i//2]
#           if i*a == n:
#             return dp[i//2]
#           a *= 2
#       else:
#         dp[i] = dp[i-1] + 1
#   print(dp)
#   return dp[n]

# ------------------------------------------- 커뮤니티....ㅅㅂ 이게 머야
# def solution(N):
#     answer = 0
#     while N > 0:
#         answer += N % 2
#         N //= 2
#     return answer

# print(solution(1000000000))
# print(solution(1000000000))
# print(solution(5))
# print(solution(6))
# print(solution(9))
# print(solution(16))
# print(solution(5000))

# -------------------------------------------------------------------------------- 6. 전력망을 둘로 나누기 30분 컷!
# 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때,
# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return

# 완전탐색으로 차례대로 하나씩 끊었을 때 갯수 차이가 가장 작은 값 리턴
# ------------------------------------------- 내꺼 그래도 기쁘다!!!
# 어거지로 bfs 쓰긴 했지만 find, union 함수로 다시한번 풀어보자
# 연결된 노드가 몇개인지 확인하기
# from collections import deque
# from copy import deepcopy


# def bfs(graph, start, visited):
#   count = 0
#   q = deque([start])
#   visited[start] = True
#   while q:
#     now = q.popleft()
#     count += 1
#     for i in graph[now]:
#       if visited[i] == False:
#         visited[i] = True
#         q.append(i)
#   return count

# def solution(n, wires):
#   graph = [[] for _ in range(n+1)]
#   for i in wires:
#     graph[i[0]].append(i[1])
#     graph[i[1]].append(i[0])

#   answer = 100
#   # 하나씩 빼보기
#   for i in wires:
#     each = deepcopy(graph)
#     visited = [False] * (n+1)
#     each[i[0]].remove(i[1])
#     each[i[1]].remove(i[0])

#     count1 = bfs(each, i[0], visited)
#     count2 = bfs(each, i[1], visited)

#     answer = min(answer, abs(count1-count2))

#   return answer

# ------------------------------------------- 내꺼
# from copy import deepcopy


# def find_root(parent, x):
#   if parent[x] != x:
#     parent[x] = find_root(parent,parent[x])
#   return parent[x]

# def union(parent, x,y):
#   x = find_root(parent,x)
#   y = find_root(parent,y)
#   if x < y:
#     parent[y] = x
#   else:
#     parent[x] = y


# def solution(n, wires):
#   # parent list가 필요해
#   parent = [0] * (n+1)

#   for i in range(1,n+1):
#     parent[i] = i

#   ignore_index = 0
#   for i in range(len(wires)):
#     each_parent = deepcopy(parent)
#     print(each_parent)
#     if i == ignore_index:
#       continue
#     union(each_parent, wires[i][0], wires[i][1])

#     print(each_parent)

# 다시 해봐


# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# print(solution(4, [[1,2],[2,3],[3,4]]))
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))

# -------------------------------------------------------------------------------- 7. 삼각 달팽이
# ------------------------------------------- 내꺼 무의미
# ------------------------------------------- 커뮤니티 훌륭하다! 그래프 있는 것은 왠만하면 dx,dy 적용해보자
# def solution(n):
#     dx = [0,1,-1]
#     dy = [1,0,-1]

#     graph = [[0]*i for i in range(1,n+1)]
#     x,y = 0,0
#     num = 1
#     direc = 0

#     while num<=(n+1)*n//2:
#         graph[y][x] = num
#         for i in graph:
#           print(i)
#         ny = y + dy[direc]
#         nx = x + dx[direc]
#         num += 1
#         if 0<=ny<n and 0<=nx<=ny and graph[ny][nx]==0:
#           y,x = ny,nx
#         else:
#           direc = (direc+1)%3
#           y += dy[direc]
#           x += dx[direc]
#     return sum(graph,[])


# print(solution(4))
# print(solution(6))
# print(solution(6))

# -------------------------------------------------------------------------------- 8. n진수 게임 거의 40분...? 시간초과!
# 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임
# ------------------------------------------- 내꺼 뭔가 나쁘진 않다. 진수변환 정도는 아예 외우자!!!
# def make(num, n):
#   total_string = '0123456789ABCDEF'
#   string = total_string[:n]
#   answer = ''
#   while num > 0:
#       num, mod = divmod(num, n)
#       answer += str(string[mod])
#   return answer[::-1]


# def solution(n, t, m, p):
#   merged = ''
#   answer = []

#   for i in range(m*t):
#     each_value = make(i,n)
#     if each_value == '':
#       merged += '0'
#     else:
#       merged += each_value

#   for i in range(len(merged)):
#     if len(answer) == t:
#       break
#     if i%m == p-1:
#       answer.append(merged[i])

#   return ''.join(answer)
      

# print(solution(2,4,2,1))
# print(solution(16,16,2,1))
# print(solution(16,16,2,2))


# -------------------------------------------------------------------------------- 9. 2개 이하로 다른 비트 - 실패! 복습
# https://art-coding3.tistory.com/46
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8-Python
# ------------------------------------------- 내꺼 + 커뮤 - 런타임에러, 시간초과 10분만 더 고민해보자!! 
# 비트연산자 사용하자 XOR - 같은 것은 0 다른 것은 1로 표시된다.
# def f(i):
#   x = i+1
#   while True:
#     if bin(i ^ x).count('1') <= 2:
#       break
#     else:
#       x += 1
#   return x


# def solution(numbers):
#   answer = []
#   for i in numbers:
#     answer.append(f(i))
#   return answer

# # ------------------------------------------- 커뮤니티 홀짝일 경우 규칙을 눈치챘어야 했다!!
# def f(x):
#   if x % 2 == 0:
#     return x+1
    
#   else:
#     y = '0' + bin(x)[2:]
#     # 오른쪽에서 '0'의 인덱스
#     idx = y.rfind('0')
#     y = list(y)
#     print(y, idx)
#     y[idx] = '1'
#     y[idx+1] = '0'
            
#     return int(''.join(y), 2)

# def solution(numbers):
#   answer = [f(i) for i in numbers]
#   return answer


# print(solution([7,15]))
# print(solution([2,7]))
# print(solution([2,7,4,5,8,20]))
# -------------------------------------------------------------------------------- 10. 배달 
# 양방향 통행
# N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다
# ------------------------------------------- 내꺼
# 최소힙..?
# 다익스트라!!!
# INF = int(1e9)
# import heapq

# def solution(n, road, k):
#   distance = [INF] * (n+1)
#   graph = [[] for _ in range(n+1)]
#   for i in road:
#     a,b,c = i
#     graph[a].append((b,c))
#     graph[b].append((a,c))
  
#   def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#       time,now = heapq.heappop(q)
#       if distance[now] < time:
#         continue
#       for i in graph[now]:
#         total_time = time + i[1]
#         if total_time < distance[i[0]]:
#           distance[i[0]] = total_time
#           heapq.heappush(q,(total_time, i[0]))
  
#   dijkstra(1)
#   answer = 0
#   for i in distance:
#     if i <= k:
#       answer += 1
#   return answer


# print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))


