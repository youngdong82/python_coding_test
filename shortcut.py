
# 미래도시
# 다익스트라 2번 돌리면 되나
# 다익스트라 2번 돌릴 거면 플로이드 돌리는 것이 더 낫다?
# 아닌데...
# 플로이드는 125 다익스 두 번은 50
# import heapq

# INF = int(1e9)
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# distance_1 = [INF] * (n + 1)
# distance_2 = [INF] * (n + 1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# x, k = map(int, input().split())


# def dijkstra(start, distance):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + 1
#             if cost < distance[i]:
#                 distance[i] = cost
#                 heapq.heappush(q, (cost, i))


# dijkstra(1, distance_1)

# first = 0
# if distance_1[k] == INF:
#     first = -1
# else:
#     first = distance_1[k]

# dijkstra(k, distance_2)

# second = 0
# if distance_2[x] == INF:
#     second = -1
# else:
#     second = distance_2[x]


# print(distance_1)
# print(distance_2)
# if first == -1 or second == -1:
#     print(-1)
# else:
#     print(first, second)

# 플로이드로 풀기
# INF = int(1e9)
# n, m = map(int, input().split())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1


# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# x, k = map(int, input().split())

# print(graph[1][k] + graph[k][x])

# 전보
# import heapq

# INF = int(1e9)
# n, m, c = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)

# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z))


# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))


# dijkstra(c)

# count = n
# max_time = 0
# for i in distance:
#     if i == INF:
#         count -= 1
#     else:
#         max_time = max(max_time, i)

# print(count, max_time)


# 플로이드
# INF = int(1e9)
# n = int(input())
# m = int(input())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]


# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = min(graph[a][b], c)

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         print(graph[a][b], end=" ")
#     print()

# 정확한 순위
# 플로이드
# INF = int(1e9)
# n, m = map(int, input().split())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1


# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# result = 0

# for a in range(1, n + 1):
#     count = 0
#     for b in range(1, n + 1):
#         if graph[a][b] != INF or graph[b][a] != INF:
#             count += 1
#     if count == n:
#         result += 1

# print(result)

# 화성탐사
# 다시한번 느끼는 것 - 일단 적어놓고 시작해라
# import heapq

# INF = int(1e9)
# # t = int(input())
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))

# distance = [[INF] * n for _ in range(n)]

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# x, y = 0, 0
# q = []
# heapq.heappush(q, (graph[x][y], x, y))
# distance[x][y] = graph[x][y]
# while q:
#     dist, x, y = heapq.heappop(q)
#     if distance[x][y] < dist:
#         continue
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#             continue
#         cost = dist + graph[nx][ny]
#         if cost < distance[nx][ny]:
#             distance[nx][ny] = cost
#             heapq.heappush(q, (cost, nx, ny))

# print(distance[n - 1][n - 1])

# 숨바꼭질
# 기본적인 다익스
import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)

index = 0
max_value = 0
for i in range(1, n + 1):
    if max_value < distance[i]:
        max_value = distance[i]
        index = i


count = distance.count(max_value)
# for i in range(1, n + 1):
#     if distance[i] == max_value:
#         count += 1

print(index, max_value, count)
