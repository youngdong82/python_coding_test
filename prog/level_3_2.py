# -------------------------------------------------------------------------------- deque
# from collections import deque


# deque는 이제껏 popleft()를 위해,
# 큐 자료구조를 구현하기 위해 생각없이 썼지만,
# 정렬도 안되는 것을 보고 어떤 구조를 지니는지 알아보았다.


# 기본적인 구조는 double_linked_list(더블 연결리스트) 구조다.
# 헐 deque가 Double_Ended_Queue의 약자래!!

# 어제 공부한 바에 따르면 list보다 데이터 조회 최악의 경우 O(N)의 시간복잡도를 가져,
# 상대적으로 index 값으로 조회하여 O(1)의 시간복잡도를 지닌 list에 비해 상대적으로 느리지만
# 데이터를 삽입 및 삭제는 O(1)의 시간복잡도로 매우 빠르다.
# 각 노드들이 자신의 옆의 노드를 기억하고 있는 구조이기 때문에, 당연하게도 정렬은 안된다.

# 더해서
# 이중연결 리스트는 양방향이기 때문에,
# 원하는 노드의 순서 값에 따라 일반 연결 리스트보다 더 빠르게 접근할 수 있다.

# 단점
# next필드 뿐만 아니라
# prev필드까지 사용해야하기 때문에 더 많은 메모리가 필요하다.

# 대표적인 매소드
# deque.appendleft()
# deque.popleft()
# deque.rotate(2)
# 뒤에있는 것이 앞으로 온다 (2칸)
# 음수라면 앞에 값이 뒤로 간다.

# -------------------------------------------------------------------------------- heapify
# 기존의 자료구조를 heapq 자료구조로 변환
# import heapq


# h = [4, 1, 7, 3, 8, 5]
# heapq.heapify(h)
# print(h)
# -------------------------------------------------------------------------------- 1. 합승 택시 요금
# 플로이드 워셜 알고리즘 심화
# 다익스트라로 가야해 플로이드 워셜은 최단거리만 나오지 경로를 알 수 없다.
# 경로를 알고 합승여부 따져야함
# 200 **3으로 시간복잡도는 가능
# ------------------------------------------- 내꺼
import heapq


INF = int(1e9)
def solution(n, s, a, b, fares):
  print(fares)
  graph = [[] for i in range(n+1)]
  distance = [INF] * (n+1)

  for fare in fares:
    start,end,cost = fare
    graph[start].append((end,cost))
  
  dijkstra(s)
  
  def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
      cost,now = heapq.heappop(q)
      if distance[now] < cost:
        continue
      for i in graph[now]:
        new_cost = cost + i[1]
        if new_cost < distance[i[0]]:
          distance[i[0]] = new_cost
          heapq.heappush(q,(cost,i[0]))






# print(solution(6,4,6,2,[[4,1,10], [3,5,24], [5,6,2], [3,1,41], [5,1,24], [4,6,50], [2,4,66], [2,3,22], [1,6,25]]))
# print(solution(7,3,4,1,[[5,7,9], [4,6,4], [3,6,1], [3,2,3], [2,1,6]]))
# print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))


# -------------------------------------------------------------------------------- 2. 디스크 컨트롤러 미친 시간초과 복습!!
# 평균이 얼마가 되는지 return 
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
# ------------------------------------------- 내꺼 시간초과
# 마냥 오래걸리는 것 먼저 재배열 하고 구하면 안돼
# from collections import deque
# import heapq


# def solution(jobs):
#   jobs = deque(jobs)
#   time = 0
#   q = []
#   able = True
#   working = 0
#   wait = 0

#   answer = []

#   while True:
#     # 작업이 끝났어?
#     if working > 0:
#       working -= 1
#     else:
#       able = True
#       answer.append(time-wait)
#       if len(jobs) == 0 and len(q) == 0 and working == 0:
#         break

#     if len(jobs) != 0 and time == jobs[0][0]:
#       a,b = jobs.popleft()
#       heapq.heappush(q,(b,a))
      
#     # 작업대기중이 있니? 작업할 수 있어?
#     if len(q) != 0 and able:
#       able = False
#       b,a = heapq.heappop(q)
#       working = b
#       wait = a
#       continue

#     time += 1

#   return sum(answer)//(len(answer)-1)

# ------------------------------------------- 커뮤니티
# 큰 것들은 괜춘한데 디테일 차이가 나네...
# 시간을 1초씩 돌면서 확인하는 것이 아니라
# 처리한 작업의 갯수별로 돌린다.
# 확실히...
# 1작업당 10000초 걸리는 거면,
# 10000번 사이클 돌 동안 1번 사이클이니... 비교할 수가 없긴 하네.

# 그리고 작은 차이같은데 이런건 배워야 해
# import heapq


# def solution(jobs):
#   answer,now,i = 0,0,0
#   start = -1
#   heap = []

#   while i < len(jobs):
#     # 오...!
#     for j in jobs:
#       if start < j[0] <= now:
#         heapq.heappush(heap, [j[1],j[0]])
#     if len(heap) > 0:
#       take_time,wait = heapq.heappop(heap)
#       # 그냥 time 1씩 더하는 건데? 아님
#       start = now
#       now += take_time
#       answer += (now - wait)
#       i += 1
#     # 작업할 것이 없다면 시간 1씩 추가하면서 사이클돌기
#     else:
#       now += 1
    
#   return int(answer/len(jobs))


# print(solution([[0,3], [1,9], [2,6]]))

# -------------------------------------------------------------------------------- 3. 이중우선순위 큐 
# 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return
# ------------------------------------------- 내꺼 + 커뮤
# import heapq


# def solution(operations):
#   # 최소힙
#   min_h = []
#   # 최대힙
#   max_h = []

#   for operation in operations:
#     order, digit = operation.split(' ')
#     digit = int(digit)
#     if order == 'D':
#       if len(min_h) > 0 and len(max_h) > 0:
#         if digit == 1:
#           heapq.heappop(max_h)
#           if max_h == [] or -max_h[0] < min_h[0]:
#             min_h = []
#             max_h = []

#         else:
#           heapq.heappop(min_h)
#           if min_h == [] or -max_h[0] < min_h[0]:
#             min_h = []
#             max_h = []
#     else:
#       heapq.heappush(min_h,digit)
#       heapq.heappush(max_h,-digit)
  
#   if min_h == []:
#       return [0, 0]
#   return [-heapq.heappop(max_h), heapq.heappop(min_h)]

# ------------------------------------------- 내꺼 이게 왜 되지??ㅋㅋㅋㅋ
# import heapq


# def solution(operations):
#   # 최소힙
#   h = []

#   for operation in operations:
#     order, digit = operation.split(' ')
#     digit = int(digit)
#     if order == 'D':
#       if len(h) > 0:
#         if digit == 1:
#           h.remove(max(h))
#         else:
#           heapq.heappop(h)
#     else:
#       heapq.heappush(h,digit)

#   if h == []:
#     return [0,0]
#   else:
#     return [max(h), min(h)]


# print(solution(["I 16","D 1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
# print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
# print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

# -------------------------------------------------------------------------------- 4. 단속카메라 복습
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 
# 차는 10,000대 이하
# 이런건 어떻게 생각해내는 거지...?
# ------------------------------------------- 커뮤니티
# def solution(routes):
#   answer = 0
#   routes.sort(key=lambda x:x[1])
#   n = len(routes)
#   checked = [0] * n

#   for i in range(n):
#     if checked[i] == 0:
#       camera = routes[i][1] # 진출 지점에 카메라를 갱신
#       answer += 1
#     for j in range(i+1, n):
#       if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
#         checked[j] = 1
#   return answer

# ------------------------------------------- 커뮤니티 2
# def solution(routes):
#   answer = 0
#   routes.sort(key=lambda x: x[1])
#   camera = -30001

#   for route in routes:
#     if camera < route[0]:
#       answer += 1
#       camera = route[1]
#   return answer


# print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

# -------------------------------------------------------------------------------- 5. 섬 연결하기
# 크루스칼 알고리즘
# 오... 동빈나가 의미가 있다!!굳굳
# ------------------------------------------- 내꺼
# def find_parent(parent,x):
#   if parent[x] != x:
#     parent[x] = find_parent(parent,parent[x])
#   return parent[x]

# def check_cycle(parent,a,b):
#   a = find_parent(parent,a)
#   b = find_parent(parent,b)
#   if a<b:
#     parent[b] = a
#   else:
#     parent[a] = b

# def solution(n, costs):
#   costs.sort(key= lambda x: (x[2]))
#   parent = [0] * (n+1)
#   for i in range(1,n+1):
#     parent[i] = i
  
#   answer = 0
#   for i in costs:
#     start,end,cost = i
#     if find_parent(parent,start) != find_parent(parent,end):
#       check_cycle(parent,start,end)
#       answer += cost

#   return answer


# print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))