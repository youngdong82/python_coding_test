# --------------------------------------------------------------------------------  defaultdict
# https://www.daleseo.com/python-collections-defaultdict/

# -------------------------------------------------------------------------------- 타겟 넘버
# 더하기 빼기로 타깃 넘버를 만드는 경우의 수 출력
# def solution(numbers, target):
#     n = len(numbers)
#     count = 0
#     def dfs(index, result):
#         if index == n:
#             if result == target:
#                 nonlocal count
#                 count += 1
#             return
#         else:
#             dfs(index+1, result+numbers[index])
#             dfs(index+1, result-numbers[index])
#     dfs(0,0)
#     return count

# # 아름다운 버전
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# -------------------------------------------------------------------------------- 네트워크
# -------------------------------------------- 내꺼 30분 컷 풀긴 풀었는데....
# 뭔가 쓸데없는게 많은 느낌
# from collections import deque


# def bfs(graph, start, visited):
#     answer = 0
#     q = deque([start])
#     visited[start] = True
#     while q:
#         now = q.popleft()
#         answer += 1
#         for i in range(len(visited)):
#             if i != now and graph[now][i] == 1:
#                 if visited[i] == False:
#                     visited[i] = True
#                     q.append(i)
#     return answer
        

# def solution(n, computers):
#     count = 0
#     visited = [False] * n
#     for i in range(n):
#         if visited[i] == True:
#             continue
#         hello = bfs(computers, i, visited)
#         if hello >= 1:
#             count += 1
#     return count

# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# -------------------------------------------- 다 풀고 사이클 판별로 한번 해보자
# -------------------------------------------------------------------------------- 여행경로
# -------------------------------------------- 내꺼 반만 맞음 경로가 틀려서 
from collections import deque


def bfs(graph, start):
    answer = []
    q = deque([start])
    while q:
        now = q.popleft()
        answer.append(now)
        if now not in graph.keys():
            break
        for i in graph[now]:
            q.append(i)
            graph[now].remove(i)
    return answer


def solution(tickets):
    graph = {}
    for i in range(len(tickets)):
        if tickets[i][0] in graph.keys():
            graph[tickets[i][0]].append(tickets[i][1])
        else:
            graph[tickets[i][0]] = [tickets[i][1]]
    
    for i in graph.keys():
        graph[i].sort()
    
    answer = bfs(graph, 'ICN')    

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# -------------------------------------------- 커뮤니티 이거 보고 공부하자.
from collections import defaultdict


def solution(tickets):
    answer = []
    adj = defaultdict(list)

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    for key in adj.keys():
        adj[key].sort(reverse=True)

    q = ['ICN']
    while q:
        tmp = q[-1]

        if not adj[tmp]:
            answer.append(q.pop())
        else:
            q.append(adj[tmp].pop())
    answer.reverse()
    return answer
