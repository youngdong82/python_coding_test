# -------------------------------------------------------------------------------- level 3의 느낌
# level 1는 특정 내장함수나 자료구조의 개념 및 사용, 기본적인 알고리즘 사용을 물어보는 느낌
# level 2는 특정 알고리즘을 능숙하게 쓸 수 있는지 물어보는 느낌
# level 3는 특정 알고리즘 사용에 뭔가 다른 요소 하나가 추가된다. bfs + 최소 힙 = 다익스트라 이런 느낌
# -------------------------------------------------------------------------------- 재귀함수 return None
# ref: https://velog.io/@munang/%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-Python-None-%EB%A6%AC%ED%84%B4%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98-None-%EB%A6%AC%ED%84%B4#3-%EA%B7%B8%EB%9E%98%EC%84%9C-%EA%B2%B0%EB%A1%A0%EC%9D%80

# 재귀적으로 함수를 호출하다가 if문에 걸리면 그 값을 리턴하려 할 때,
# 계속 None이 리턴되는 경우가 있다.
# 이는 재귀함수를 리턴 값으로 주지 않기 때문에 생긴다.
# return문이 없으면 자동으로 return None 을 한다.
# 함수에 global변수를 사용하는 것은 좋지 않으나, 코딩테스트에서는 사용해도 무관한 것 같다.

# 1) return을 사용할때
# early return의 경우 많이 사용한다.
# 맥락 상 break와 유사한 효과를 내기 때문에,
# 무언가를 리턴하기 보다는 실행 중단의 의미가 더 크다.

# 2) return을 사용하지 않을 때
# 함수가 무언가를 반환하는게 목적이 아닌, 단순 연산의 목적일 경우이다.
# 연산이 끝난 후 연산 성공이나 실패를 반환해야 한다면 달라지겠지만,
# 그게 아니라 단순히 글로벌 변수 연산이 목적이라면, 사용하지 않는 경우가 있다.

# -------------------------------------------------------------------------------- 이분탐색 구조
# 탐색의 범위는 무엇으로 할지
# 탐색의 기준을 무엇으로 할지

# 기준
# 범위(start,mid,end)

# -------------------------------------------------------------------------------- 1. 네트워크
# 전에는 bfs 원툴이라 좀 억지스럽게 bfs로 푼 것 같은데 이번엔 dfs로 풀었다! 기쁘다!!!
# ------------------------------------------- 내꺼 19분 컷!!!
# def dfs(graph,start,visited):
#   visited[start] = True
#   for i in graph[start]:
#     if visited[i] == False:
#       dfs(graph,i,visited)

# def solution(n, computers):
#   graph = [[] for _ in range(n)]
#   for i in range(n):
#     for j in range(n):
#       if i != j and computers[i][j] == 1:
#         graph[i].append(j)
#   visited = [False] * n

#   count = 0
#   for i in range(n):
#     if visited[i] == False:
#       dfs(graph,i,visited)
#       count += 1

#   return count


# print(solution(3,[[1,1,0], [1,1,0], [0,0,1]]))
# print(solution(3,[[1,1,0], [1,1,1], [0,1,1]]))

# -------------------------------------------------------------------------------- 2. 단어변환
# begin에서 target으로 변환하는 가장 짧은 변환 과정
# ------------------------------------------- 내꺼 40분 컷!
# answer = []
# def dfs(begin,target,words,visited):
#   if begin == target:
#     count = 0
#     for i in visited.values():
#       if i == True:
#         count += 1
#     answer.append(count)
#   # 문자 1개만 다른 list tmp 만들기
#   tmp = []
#   for word in words:
#     count = 0
#     for i,j in zip(begin,word):
#       if i != j:
#         count += 1
#     if count == 1:
#       tmp.append(word)

#   # 하나씩 들어가자
#   for word in tmp:
#     if visited[word] == False:
#       visited[word] = True
#       dfs(word,target,words,visited)
#       visited[word] = False

# def solution(begin, target, words):
#   visited = {}
#   for  i in words:
#     visited[i] = False
#   dfs(begin, target, words,visited)
#   if len(answer) == 0:
#     return 0
#   else:
#     return min(answer)


# print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"]))

# -------------------------------------------------------------------------------- 3. 여행경로
# ------------------------------------------- 내꺼 내일 다시 해보자


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# -------------------------------------------------------------------------------- 4. 입국심사 복습
# 시간을 기준으로 그 시간에 받을 수 있는 사람의 수가 원하는 값인가? 작은가? 큰가?
# ------------------------------------------- 내꺼
# def solution(n, times):
#   answer = 0

#   # 이건 시간이다 시간
#   start = 1
#   end = max(times) * n

#   while start <= end:
#     # mid란 가장 적게걸리는 시간과 많이 걸릴 때의 중간
#     mid = (start + end)//2
#     people = 0
#     for time in times:
#       people += mid // time
#       if people >= n:
#           break
#     print(mid,people)
#     if people >= n:
#       answer = mid
#       end = mid - 1
#     elif people < n:
#         start = mid + 1

#   return answer


# print(solution(6,[7,10]))
# -------------------------------------------------------------------------------- 5. 베스트앨범
# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
# 고유 번호로 구분
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다. 장르 별 총 재생시간 필요
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다. 곡 별 재싱시간 필요 => 다 더하면 되니까 위에꺼 해결
# 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

# ------------------------------------------- 내꺼
# def solution(genres, plays):
#   dic = {}
#   total={}
#   index = 0
#   for genre,play in zip(genres,plays):
#     if genre in dic.keys():
#       dic[genre].append((play,index))
#       total[genre] += play
#     else:
#       dic[genre] = [(play,index)]
#       total[genre] = play
#     index += 1


#   genre_sort = sorted(total.items(), key=lambda x: (-x[1]))

#   for genre in dic.keys():
#     dic[genre].sort(key=lambda x: (-x[0],x[1]))
  
#   # 다 해놓고 뭐여 이게!!!
#   answer = []
#   for genre in genre_sort:
#     if len(dic[genre[0]]) == 1:
#       answer.append(dic[genre[0]][0][1])
#     else:
#       for i in range(2):
#         answer.append(dic[genre[0]][i][1])
#   return answer


# print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))

