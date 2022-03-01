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

# -------------------------------------------------------------------------------- 단어 변환
# 모든 단어의 길이는 같습니다.
# 변환할 수 없는 경우에는 0을 리턴
# -------------------------------------------- 내꺼 반만 맞음. 잘못된 길로 들어섰을 때 불가능
# 뭔가 dfs느낌
# def dfs(words, start, target, visited, answer):
#     if visited[target] == True:
#         return
#     visited[start] = True
#     answer.append(start)
#     new_words = []
#     for word in words:
#         count = 0
#         for a,b in zip(word, start):
#             if a == b:
#                 count += 1
#         if count == 2 and visited[word] == False:
#             new_words.append(word)

#     if target in new_words:
#         visited[target] = True
#         answer.append(word)
#         return
#     else:
#         for word in new_words:
#             dfs(words, word, target, visited, answer)



# def solution(begin, target, words):
#     if target not in words:
#         return 0
#     visited = {}
#     for i in words:
#         if i not in visited.keys():
#             visited[i] = False
#     answer = []
#     dfs(words, begin, target, visited, answer)
#     return len(answer)-1

# -------------------------------------------- 커뮤니티 
# visited를 하나하나 확인하지 않고 그냥 깊이로 처리하는게 굳이다...
# 여전히 다른 길로 빠진다면 불가능하지 않나??
# def bfs(begin, target, words, visited):
#     q = [(begin, 0)]
#     while q:
#         now, depth = q.pop()
#         if now == target:
#             return depth
        
#         for i in range(len(words)):
#             if visited[i] == True:
#                 continue
#             count = 0
#             for a,b in zip(now, words[i]):
#                 if a!=b:
#                     count += 1
#             if count == 1:
#                 visited[i] = True
#                 print(visited)
#                 q.append((words[i], depth+1))
                
            

# def solution(begin, target, words):
#     answer = 0
#     if target not in words:
#         return 0
#     visited = [False]*(len(words))
#     answer = bfs(begin, target, words, visited)
#     return answer

# print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))


# -------------------------------------------------------------------------------- 여행경로
# -------------------------------------------- 내꺼 반만 맞음 경로가 틀려서  + 커뮤니티 = 완성
# 재귀로 안돌리는 dfs도 있을 수 있구나...

# def dfs(graph, start):
#     stack = [start]
#     path = []
#     while stack:
#         top = stack[-1]
#         if top not in graph or len(graph[top]) == 0:
#             path.append(stack.pop())
#         else:
#             stack.append(graph[top].pop(0))
#     return path[::-1]

# def solution(tickets):
#     graph = {}
#     for i in range(len(tickets)):
#         if tickets[i][0] in graph.keys():
#             graph[tickets[i][0]].append(tickets[i][1])
#         else:
#             graph[tickets[i][0]] = [tickets[i][1]]

#     for i in graph.keys():
#         graph[i].sort()

#     answer = dfs(graph, 'ICN')    

#     return answer


# # -------------------------------------------- 커뮤니티
# from collections import defaultdict


# def solution(tickets):
#     answer = []
#     adj = defaultdict(list)
#     print(adj)
#     for ticket in tickets:
#         adj[ticket[0]].append(ticket[1])
#     print(adj)

#     for key in adj.keys():
#         adj[key].sort(reverse=True)

#     q = ['ICN']
#     while q:
#         tmp = q[-1]

#         if not adj[tmp]:
#             answer.append(q.pop())
#         else:
#             q.append(adj[tmp].pop())
#     answer.reverse()
#     return answer


# print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))