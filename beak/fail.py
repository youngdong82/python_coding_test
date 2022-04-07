# -------------------------------------------------------------------------------- 음수를 양수로 나눌 때는 C++14의 기준
# 음수를 양수로 나눌 때는
# 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
# a = -7
# ab = 7
# b = 3
# print(a//b)
# print(ab//b)

# -------------------------------------------------------------------------------- 백트래킹
# -------------------------------------------------------------------------------- 5. 9663 번 N-Queen 복습
# 2차원 배열을 사용하지 않고
# row[x] = i 형태로 사용하는거
# ------------------------------------------- 내꺼 포기
# n = int(input())

# answer = 0
# row = [0] * n

# def check(depth):
#   for i in range(depth):
#     # 가로는 체크 할 필요 없고
#     # or 전이 세로 체크
#     # or 이후가 양쪽 대각선 체크 같은데... 이해 졸라 안되네...
#     if row[depth] == row[i] or abs(row[depth] - row[i]) == abs(depth - i):
#       return False
#   return True

# def n_queens(depth):
#   global answer
#   if depth == n:
#     answer += 1
#     return
#   else:
#     for i in range(n):
#       row[depth] = i
#       if check(depth):
#         n_queens(depth+1)

# n_queens(0)
# print(answer)

# -------------------------------------------------------------------------------- 7. 14888 번 연산자 끼워넣기 복습
# ------------------------------------------- 내꺼 두번째 27분 컷!! 재귀로 잘 풀었어!! 잘했다 영동아!!
# n = int(input())
# data = list(map(int,input().split()))
# oper = list(map(int,input().split()))

# max_value = int(-1e9)
# min_value = int(1e9)

# def dfs(depth, plus,minus,multiple, divide,summ_value):
#   global max_value, min_value
#   if depth == n:
#     max_value = max(max_value,summ_value)
#     min_value = min(min_value,summ_value)
#     return
#   if plus > 0:
#     dfs(depth+1, plus-1,minus,multiple, divide, summ_value + data[depth])
#   if minus > 0:
#     dfs(depth+1, plus,minus-1,multiple, divide, summ_value - data[depth])
#   if multiple > 0:
#     dfs(depth+1, plus,minus,multiple-1, divide, summ_value * data[depth])
#   if divide > 0:
#     if summ_value < 0:
#       summ_value = -(-summ_value // data[depth])
#     else:
#       summ_value //= data[depth]
#     dfs(depth+1, plus,minus,multiple, divide-1, summ_value)
  
# dfs(1,oper[0],oper[1],oper[2],oper[3], data[0])

# print(max_value)
# print(min_value)

# -------------------------------------------------------------------------------- 8. 14889 번 스타트와 링크 복습
# ------------------------------------------- 내꺼 두번째 21분 컷!! 시간초과 그래도 재귀 약간 늘은 것 같긴 하다.
# ------------------------------------------- 실전에선 라이브러리 사용하자
# n = int(input())
# graph = []
# for _ in range(n):
#   graph.append(list(map(int,input().split())))
# # for i in graph:
# #   print(i)

# def calculate(group):
#   sum_value = 0
#   for i in range(len(group)):
#     for j in range(i+1, len(group)):
#       if i != j:
#         sum_value += graph[group[i]-1][group[j]-1] + graph[group[j]-1][group[i]-1]
#   return sum_value

# answer = int(1e9)
# start = []
# def dfs():
#   global answer
#   if len(start) == n//2:
#     link = []
#     for i in range(1,n+1):
#       if i not in start:
#         link.append(i)
#     answer = min(answer,abs(calculate(start)-calculate(link)))
#     return
#   for i in range(1,n+1):
#     if i not in start:
#       start.append(i)
#       dfs()
#       start.pop()
# dfs()
# print(answer)

# -------------------------------------------------------------------------------- 이진탐색
# -------------------------------------------------------------------------------- 3. 1654 번 랜선 자르기 복습
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함
# binary 무조건 while 문에서 start <= end
# start랑 end가 같은 순간을 포함해야한다.
# ------------------------------------------- 내꺼 두번째 13분 컷!!
# k,n = map(int,input().split())
# lens = []
# for i in range(k):
#   lens.append(int(input()))

# start = 1
# end = max(lens)
# answer = 0
# while start <= end:
#   mid = (start + end)//2
#   tmp = 0
#   for i in lens:
#     tmp += i//mid
#   if tmp >= n:
#     answer = max(answer,mid)
#     start = mid +1
#   else:
#     end = mid -1

# print(answer)

# -------------------------------------------------------------------------------- 4. 2805 번 나무 자르기 복습
# 최대값 최소값 구할 때 맞는 mid들을 모은 후 그곳에서 고르는 것이 아닌
# 이진탐색 할때 설정을 바꿔서 start나 end를 출력하자
# 위의 문제도 같다.
# + 무조건 start 0 하지말고 최솟값 확인하자
# ------------------------------------------- 내꺼 두번째 8분 컷!
# n,m = map(int,input().split())
# trees = list(map(int,input().split()))

# answer = 0
# start = 1
# end = max(trees)
# while start <= end:
#   mid = (start + end)//2
#   tmp = 0
#   for i in trees:
#     if mid < i:
#       tmp += (i-mid)
#   if tmp >= m:
#     answer = max(answer,mid)
#     start = mid + 1
#   elif tmp <m:
#     end = mid-1
# print(answer)

# -------------------------------------------------------------------------------- 5. 2110 번 공유기 설치 복습
# 한 집에는 공유기를 하나만 설치할 수 있고,
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
# 모르겠다... 그만... 나중에 다시 도전하자..
# ------------------------------------------- 내꺼
# n,c = map(int,input().split())
# house = []
# for _ in range(n):
#   house.append(int(input()))
# house.sort()
# print(house)

# # 거리를 기준으로 이분탐색
# left = house[0]
# right = house[-1] - house[0]
# answer = 0

# while left <= right:
#   mid = (left + right) // 2
#   current = house[0]
#   count = 1
  
#   for i in range(1,len(house)):
#     if house[i] >= current + mid:
#       count += 1
#       current = house[i]

#   if count >= c:
#     left = mid +1
#     answer = mid
#   else:
#     right = mid-1

# print(answer)


# -------------------------------------------------------------------------------- 6. 1300 번 k번째 수 복습 이해가 안돼....
# 그냥 풀면 쉽다.그러나 n이 10의 5제곱이라 
# 10만 곱하기 10만 총 10억
# b를 만들기만 해도 메모리 초과

# k가 10의 9제곱이기 때문에 메모리 초과된다.
# 리스트를 안만들고 구해야해.
# 어떻게...?
# 모르겠어....ㅋㅋㅋㅋㅋㅋㅅㅂㅅㅂㅅㅂㅅㅂㅅㅂㅅㅂㅅㅂㅅㅂㅅ

# ------------------------------------------- 내꺼
# n = int(input())
# k = int(input())

# b = []
# for i in range(n):
#   for j in range(n):
#     b.append((i+1)*(j+1))

# b.sort()
# print(b[k-1])

# ------------------------------------------- 커뮤니티
# n = int(input())
# k = int(input())

# a = [[0] * n for _ in range(n)]
# b = []
# for i in range(n):
#   for j in range(n):
#     a[i][j] = (i+1)*(j+1)

# for i in a:
#   print(i)

# start, end = 1, k
# while start <= end:
#     mid = (start + end) // 2
    
#     temp = 0
#     for i in range(1, n+1):
#         temp += min(mid//i, n) #mid 이하의 i의 배수 or 최대 N
    
#     if temp >= k: #이분탐색 실행
#         answer = mid
#         end = mid - 1
#     else:
#         start = mid + 1
# print(answer)


# -------------------------------------------------------------------------------- 완전탐색
# --------------------------------------------------- 체스판 다시 칠하기 와우 너무 기뻐!!! 33분 컷!!! 대견하다!!!영동!!
#  지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
#  당연히 8*8 크기는 아무데서나 골라도 된다.
#  지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
# ------------------------------------------- 내꺼 두번째 19분 컷!! 크하하핳하하하!!!나는 성장하는 천재인가!!
# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(str,input())))

# # 짝수가 W
# # 홀수가 B
# def check(x,y):
#   count = 0
#   for i in range(8):
#     for j in range(8):
#       if (x+i+y+j) %2 == 0 and graph[x+i][y+j] == 'B':
#         count += 1
#       elif (x+i+y+j) %2 == 1 and graph[x+i][y+j] == 'W':
#         count += 1
#   if count > 64-count:
#     count = 64-count
#   return count

# min_value = int(1e9)
# for i in range(n):
#   for j in range(m):
#     if i+8 <= n and j+8 <=m:
#       min_value = min(min_value, check(i,j))
# print(min_value)

# -------------------------------------------------------------------------------- dfs/bfs
# -------------------------------------------------------------------------------- 9. 2206 번 복습필수
# 완전탐색은 불가능해
# bottleneck을 찾고 개선점을 찾자.
# 굳이 벽을 하나하나 다 부숴봐야하는가?

# 두번째
# 배웠던대로 3차원으로 만들려했지만 실패했다.
# 그래서 꾸역꾸역 만들긴 했는데
# 내가 봤을땐 로직에 문제가 없어보이지만 틀린다.
# 가르쳐줬던 사람이 3차원으로 안하면 어떻게든 빵꾸나는 부분이 생긴다고 했는데
# 딱 그 상황인가 싶다.
# ------------------------------------------- 내꺼
# from collections import deque


# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,str(input()))))

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def bfs(x,y,toggle):
#   q = deque([(x,y,toggle)])
#   graph[x][y] = 1
#   while q:
#     now_x, now_y,now_toggle = q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0<= nx < n and 0<= ny < m:
#         # 벽인데 부술 수 있을 경우
#         if graph[nx][ny] == 1 and now_toggle == 0:
#           if 
#           graph[nx][ny] = graph[now_x][now_y] + 1
#           q.append((nx,ny,1))
#         # 아무도 밟지 않은 땅
#         elif graph[nx][ny] == 0:
#           graph[nx][ny] = graph[now_x][now_y] + 1
#           q.append((nx,ny,now_toggle))
#         # 전에 밟았던 땅
#         elif graph[nx][ny] > 1:
#           if graph[nx][ny] > graph[now_x][now_y] + 1:
#             graph[nx][ny] = graph[now_x][now_y] + 1
#             q.append((nx,ny,now_toggle))

# bfs(0,0,0)

# for i in graph:
#   print(i)
# if graph[n-1][m-1] == 0:
#   print(-1)
# else:
#   print(graph[n-1][m-1])

# ------------------------------------------- 3차원 visited 함수 사용 *** 다시 한번 복습!!
# 원 함수 graph는 안건드리고, visited 함수만 건드린다.
# 가장 안쪽 차원에서 [0]은 벽을 안부수고 도달할 때, [1]은 벽을 한번 부수도 도달했을 때
# 벽을 부순 후에는 [0]의 값이 [1]로 간다.
# 밑의 코드는 나중의 값이 더 크더라도 덮어쓴다.(최소 값을 보장하진 않는다?) 그럴리가 있나..?
# from collections import deque


# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,str(input()))))
# visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def bfs(x, y, iscrash, visited, graph):
#   #crash 0: 벽안부시고 가는경우, 1: 부신 경우
#   q = deque()
#   q.append((x, y, iscrash))
#   visited[x][y][iscrash] = 1

#   while q:
#     now_x, now_y, iscrash = q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       if 0<= nx < n and 0<= ny < m:
#         # 벽 안부수고 이동
#         if graph[nx][ny] == 0 and visited[nx][ny][iscrash] == 0:
#             q.append((nx, ny, iscrash))
#             visited[nx][ny][iscrash] = visited[now_x][now_y][iscrash] + 1
#         # 벽 부수고 이동
#         if graph[nx][ny] == 1 and iscrash == 0:
#             q.append((nx, ny, iscrash + 1))
#             visited[nx][ny][iscrash + 1] = visited[now_x][now_y][iscrash] + 1

# bfs(0, 0, 0, visited, graph)

# for i in visited:
#   print(i)


# -------------------------------------------------------------------------------- 9. 1707 번 복습 다시 복습
# 음수를 이용해서 무방향 그래프에서 그룹을 확인한다.
# 같은 길로 왔다 가는 것은 -1 => 1 => -1 이기 때문에 문제가 되지 않는다.
# 다른 길로 특정 노드에 도착했는데, 이미 도착해 있으며, -1 => -1이거나 1 => 1이라면
# visited를 처음엔 False로 놓았다가 1과 -1로 사이클 확인
# ------------------------------------------- 내꺼
# from collections import deque


# def bfs(start, group):
#   q = deque([start])
#   visited[start] = group
#   while q:
#     now = q.popleft()
#     for i in graph[now]:
#       if visited[i] == False:
#         visited[i] = - visited[now]
#         q.append(i)
#       elif visited[i] == visited[now]:
#         return False
#   return True

# n = int(input())
# for _ in range(n):
#   v,e = map(int,input().split())
#   graph = [[] for _ in range(v+1)]
#   visited = [False] * (v+1)

#   for i in range(e):
#     start,end = map(int,input().split())
#     graph[start].append(end)
#     graph[end].append(start)
  
#   for i in range(1,v+1):
#     if visited[i] == False:
#       result = bfs(i,1)
#       if result == False:
#         break

#   if result:
#     print('YES')
#   else:
#     print('NO')

# -------------------------------------------------------------------------------- 정렬
# -------------------------------------------------------------------------------- 3. 10989 수 정렬하기 3 복습
# ------------------------------------------- 내꺼 두번째 10분 컷!!
# import sys
# input = sys.stdin.readline
# n = int(input())

# data = [0] * 10001
# for i in range(n):
#   data[int(input())] += 1

# for i in range(len(data)):
#   if data[i] != 0:
#     for j in range(data[i]):
#       print(i)

# -------------------------------------------------------------------------------- 5. 18870번 복습!!
# ------------------------------------------- 내꺼 시간초과 두번째 11분 컷!
# n = int(input())
# data = list(map(int,input().split()))
# dic = {}
# sort_data = sorted(set(data))

# for i in range(len(sort_data)):
#   if sort_data[i] not in dic.keys():
#     dic[sort_data[i]] = i

# for i in range(len(data)):
#   data[i] = dic[data[i]]

# for i in data:
#   print(i, end=' ')

# -------------------------------------------------------------------------------- 덱 큐
# -------------------------------------------------------------------------------- 6. 5430 AC
# ------------------------------------------- 내꺼 20분 컷!
# from collections import deque


# test_case = int(input())
# for _ in range(test_case):
#   order = str(input())
#   n = int(input())
#   a = input()

#   if a == '[]':
#     q = deque([])
#   else:
#     q = deque(list(map(str,a[1:-1].split(','))))

#   answer = True
#   r_count = 0
#   for i in order:
#     if i == 'R':
#       r_count += 1
#     elif i == 'D':
#       if len(q) == 0:
#         answer = False
#         break
#       if r_count %2 == 0:
#         q.popleft()
#       else:
#         q.pop()

#   q = list(q)
#   if not answer:
#     print('error')
#   else:
#     if r_count %2 == 0:
#       print('['+','.join(q) + ']')
#     else:
#       print('['+','.join(q[::-1]) + ']')

# -------------------------------------------------------------------------------- string
# -------------------------------------------------------------------------------- 9. 1316번 그룹단어 체커 복습...?
# 여기서 중요한 것은 문자열 하나하나 비교하는 문제가 나올 때,
# 임의의 리스트 tmp를 이용해서 문제를 풀어나간다는 것!
# ------------------------------------------- 내꺼 이전꺼 이것도 깔끔하긴 하다!!
# n = int(input())
# answer = 0

# for _ in range(n):
#   word = str(input())
#   tmp = ''
#   for i in word:
#     if tmp != '':
#       if tmp[-1] == i:
#         continue
#       else:
#         tmp += i
#     else:
#       tmp += i
#   if len(tmp) == len(set(tmp)):
#     answer += 1
#   else:
#     print(tmp, set(tmp))

# print(answer)
# ------------------------------------------- 내꺼 두번째 14분 컷!!
# n = int(input())
# count = 0
# for i in range(n):
#   answer = True
#   word = str(input())
#   dic = {}
#   tmp = []
#   for i in range(len(word)):
#     if word[i] in dic.keys():
#       if tmp[-1] != word[i]:
#         answer = False
#         break
#       dic[word[i]] += 1
#     elif word[i] not in dic.keys():
#       dic[word[i]] = 1
#       tmp.append(word[i])
#   if answer == True:
#     count += 1
# print(count)

# -------------------------------------------------------------------------------- 투 포인터
# -------------------------------------------------------------------------------- 2. 2470번 복습ㅋㅋㅋㅋ
#  두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램
# ------------------------------------------- 내꺼
# n = int(input())
# data = list(map(int,input().split()))
# data.sort()

# left = 0
# right = n-1
# answer = 2e+9+1

# while left < right:
#   sum_value = data[left] + data[right]
#   if sum_value == 0:
#     answer_left = data[left]
#     answer_right = data[right]
#     break

#   if abs(sum_value) < answer:
#     answer = abs(sum_value)
#     answer_left = data[left]
#     answer_right = data[right]
#   # 별 의미없이 경우의 수를 위해 이동시키는 것,
#   # left와 right이 중앙으로 온다고 해서 sum_value가 0에 가까워지는 것은 아니다.
#   # 이 부분 때문에 헤맸다.
#   if sum_value > 0:
#     right -= 1
#   elif sum_value < 0:
#     left += 1

# print(answer_left, answer_right)


# -------------------------------------------------------------------------------- 3. 1806번 복습!!! 문제 제대로 좀 읽자
# left와 right이 에러나지 않고 마지막 인덱스까지 도달하는 방법이 중요하다!!
# 은근히 까다로움
# ------------------------------------------- 내꺼 아 이거 동빈나랑 같이 공부했던건데...ㅠㅠㅠ
# n,s = map(int,input().split())
# data = list(map(int,input().split()))
# dp = [0]
# for i in range(len(data)):
#   dp.append(dp[-1] + data[i])


# left = 0
# right = 1
# answer = int(1e9)

# while left != n:
#   sum_value = dp[right] - dp[left]
#   print(left,right,sum_value)

#   if sum_value >= s:
#     answer = min(answer, right-left)
#     left += 1
#   else:
#     if right == n:
#       left += 1
#     else:
#       right += 1

# if answer == int(1e9):
#   print(0)
# else:
#   print(answer)
