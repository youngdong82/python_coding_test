# 특정 거리의 도시 찾기
from collections import deque

INF = int(1e9)
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)

visited = [INF] * (n+1)

def bfs(graph,v,visited):
  q = deque([v])
  count = 0
  visited[v] = count
  while q:
    now = q.popleft()
    count += 1
    for i in graph[now]:
      if visited[i] == INF:
        visited[i] = count
        q.append(i)

bfs(graph,x,visited)

for i in range(1,n+1):
  if visited[i] == k:
    print(i)
if k not in visited:
  print(-1)

# 연구소
n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))
after = [[0] * m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread_dfs(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx <n and 0 <= ny < m:
      if after[nx][ny] == 0:
        after[nx][ny] = 2
        spread_dfs(nx,ny)


def count_safe():
  count = 0
  for i in range(n):
    for j in range(m):
      if after[i][j] == 0:
        count += 1
  return count


result = 0
def dfs(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        after[i][j] = graph[i][j]
    for i in range(n):
      for j in range(m):
        if after[i][j] == 2:
          spread_dfs(i,j)
    result = max(result, count_safe())
    return
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        count += 1
        dfs(count)
        graph[i][j] = 0
        count -= 1

dfs(0)
print(result)

# 경쟁적 전염
INF = int(1e9)
n,k = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))
s,qx,qy = map(int,input().split())

visited = [[INF] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      visited[i][j] = 0


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread(x,y,num,sec):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = num
        visited[nx][ny] = sec

for sec in range(1,s+1):

  for num in range(1,k+1):  
    for i in range(n):
      for j in range(n):
        if graph[i][j] == num and visited[i][j] == (sec-1):
          spread(i,j,num,sec)


if graph[qx-1][qy-1] == 0:
  print(0)
else:
  print(graph[qx-1][qy-1])

# 괄호변환
data = str(input())

def balanced_index(data):
  count = 0
  for i in range (len(data)):
    if data[i] == '(':
      count += 1
    else:
      count -= 1
    if count == 0:
      return i

def is_right(data):
  count = 0
  for i in data:
    if i == '(':
      count += 1
    else:
      if count == 0:
        return False
      count -= 1
  return True

def routin(data):
  answer = ''
  if data == '':
    return answer
  index = balanced_index(data)
  u = data[0:index+1]
  v = data[index+1:]

  if is_right(u) == True:
    answer = u + routin(v)
  else:
    answer = '('
    answer += routin(v)
    answer += ')'
    u = list(u[1:-1])
    for i in range(len(u)):
      if u[i] == '(':
        u[i] = ')'
      else:
        u[i] = '('
    answer += ''.join(u)
  return answer

print(routin(data))

# 연산자 끼워넣기
from itertools import permutations

INF = int(1e9)
n = int(input())
array = list(map(int,input().split()))
oper = list(map(int,input().split()))

after_oper = []

for i in range(4):
  if i == 0:
    for _ in range(oper[i]):
      after_oper.append('+')
  if i == 1:
    for _ in range(oper[i]):
      after_oper.append('-')
  if i == 2:
    for _ in range(oper[i]):
      after_oper.append('*')
  if i == 3:
    for _ in range(oper[i]):
      after_oper.append('%')
  
candidates = list(permutations(after_oper,n-1))
  
max_value = 0
min_value = INF

for candidate in candidates:
  result = array[0]
  index = 1
  for operator in candidate:
    if operator == '+':
      result += array[index]
      index +=1
    elif operator == '-':
      result -= array[index]
      index +=1
    elif operator == '*':
      result *= array[index]
      index +=1
    elif operator == '%':
      if result < 0:
        result_convert = abs(result) // array[index]
        result = -result_convert
        index +=1
      else:
        result //= array[index]
        index +=1
  max_value = max(max_value,result)
  min_value = min(min_value,result)
print(max_value)
print(min_value)
