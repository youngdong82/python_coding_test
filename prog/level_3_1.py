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

# -------------------------------------------------------------------------------- 링크드 리스트
# 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조

# 삽입과 삭제가 빈번하다면? LinkedList,
# 데이터 접근,조회가 더 중요하다면? Array
# -------------------------------------------------------------------------------- copy()와 deepcopy()의 차이
# # 1차원 리스트의 경우,
# # copy()로 복사해도,
# # 원 리스트의 값이 변경되어도 복사된 리스트에 영향을 주지 않는다.

# a = [1, 2, 3]
# b = a.copy()
# a[0] = 4

# print(a)
# print(b)

# # 2차원 리스트의 경우,
# # copy()로 복사하면,
# # 원 리스트의 값이 변경되면 복사된 리스트의 값이 변경된다.

# # 이를 방지하기 위해 deepcopy()를 사용한다.

# aa = [[1, 2, 3], [4, 5, 6]]
# bb = a.copy()
# bb[0][0] = 7

# print(aa)
# print(bb) 


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

# -------------------------------------------------------------------------------- 6. 보석 쇼핑
# 집합자료형 + 투포인터??
# 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 
  # left,right으로 만든 list가 gem_reck의 갯수보다 작다면
  # 절대로 모든 종류를 포함할 수 없다. => right += 1로 범위 자체를 늘려
  # left,right으로 만든 list가 gem_reck의 갯수와 같거나 크다면
  # 포함한다면, answer에 기록하고
  # 최소를 찾아야하기 때문에, 전체적으로 오른쪽으로 이동해야하기 때문에 => left += 1
  # 포함하지 않는다면
  # 범위를 늘려야함으로, => right +=1 
  # dic = {}
  # for i in range(len(gems)):
  #   if gems[i] not in dic.keys():
  #     dic[gems[i]] = [i]
  #   else:
  #     dic[gems[i]].append(i)
  # print(dic)
# ------------------------------------------- 내꺼 시간초과!! 효율성을 높여보자
# def solution(gems):
#   gem_reck = list(set(gems))

#   answer_reck = []
#   left = 0
#   right = 1

#   while right <= len(gems):
#     # print(gems[left: right])
#     if right - left < len(gem_reck):
#       right += 1
#     elif right - left >= len(gem_reck):
#       visited = [False] * len(gem_reck)
#       for i in range(len(gem_reck)) :
#         if gem_reck[i] in gems[left: right]:
#           visited[i] = True
#       if visited.count(True) == len(gem_reck):
#         # print('good!')
#         # print()
#         answer_reck.append((right-left, left+1,right))
#         left += 1
#       else:
#         right += 1
#   answer_reck.sort()
#   answer = answer_reck[0]

#   return [answer[1],answer[2]]

# ------------------------------------------- 커뮤니티
# 같은 투포인터인데 이렇게 큰 차이가 나나...?
# 어짜피 visited의 True의 갯수로 확인하니까
# 종류의 갯수로 확인하자. (전부 필요한 것이니까 가능)
# def solution(gems):
#   gem_reck = len(set(gems))

#   shortest = len(gems)+1
#   left = 0
#   right = 0
#   contained = {}
#   answer = []

#   while right < len(gems):
#     if gems[right] not in contained:
#       contained[gems[right]] = 1
#     else:
#       contained[gems[right]] += 1
#     right += 1
#     # 다 포함하고 있는 애들 중에서, 
#     if len(contained) == gem_reck:
#       while left < right:
#         if contained[gems[left]] > 1:
#           contained[gems[left]] -= 1
#           left +=1
#         elif shortest > right - left:
#           shortest = right - left
#           answer = [left+1, right]
#           break
#         else:
#           break
#   return answer


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

# -------------------------------------------------------------------------------- 7. 경주로 건설 시간초과 복습
# bfs느낌 bfs랑 dfs 합치는 것이 아니라 bfs 자체에서 건드릴 수 있나???
# 아냐 아예 애초부터 dfs로 해야하는 느낌
# 0은 빔, 1은 벽
# 직선도로 100, 코너 500

# isVisit에 Cost를 저장하고, 다시 방문했을 때의 Cost가 더 작다면 방문을 허용하는 식으로 작업했습니다.
# ------------------------------------------- 내꺼
# from collections import deque


# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def bfs(graph,x,y,direc,cost,visited,n):
#   q = deque([(x,y,direc,cost)])
#   visited[x][y] = cost
#   while q:
#     now_x, now_y,now_direc,now_cost = q.popleft()
#     for i in range(4):
#       nx = now_x + dx[i]
#       ny = now_y + dy[i]
#       # 범위 안에 있는 경우만 처리
#       if 0<= nx < n and 0 <= ny < n:
#         # 벽이 아니라 갈 수 있는 것만 처리
#         if graph[nx][ny] == 0:
#           new_cost = 0
#           if now_direc != -1 and now_direc != i:
#             new_cost = now_cost + 600
#           elif now_direc == -1 or now_direc == i:
#             new_cost = now_cost + 100
#           # 방문했던 곳이라면
#           if visited[nx][ny] != -1:
#             if new_cost <= visited[nx][ny]:
#               visited[nx][ny] = new_cost
#               q.append((nx,ny,i,new_cost))
#           # 방문하지 않았다면
#           else:
#             visited[nx][ny] = new_cost
#             q.append((nx,ny,i,new_cost))

# def solution(board):
#   n = len(board)
#   visited = [[-1] * n for _ in range(n)]
#   bfs(board,0,0,-1,0,visited,n)
#   for i in visited:
#     print(i)
#   answer = visited[len(board)-1][len(board)-1]
#   return answer

# ------------------------------------------- 커뮤니티 3차원 dp
# from collections import deque

# def solution(board):
#     result = 10000
#     N = len(board)

#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]

#     visited = [[[10000] * N for _ in range(N)] for _ in range(4)]
#     q = deque([(0,0,0,1),(0,0,0,2)])

#     while q:
#       now_x, now_y, now_cost, now_direc = q.popleft()
#       for i in range(4):
#         nx = now_x + dx[i]
#         ny = now_y + dy[i]

#         if 0 <= nx < N and 0 <= ny < N:
#           if board[nx][ny] == 0:
#             new_cost = now_cost + 100
#             if now_direc != i:
#               new_cost += 500
#             if new_cost < visited[i][nx][ny]:
#               visited[i][nx][ny] = new_cost
#               if nx == N-1 and ny == N-1:
#                 continue
#               q.append((nx, ny, new_cost, i))

#     for i in range(4):
#         result = min([result, visited[i][N-1][N-1]])
#     return result


# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))

# -------------------------------------------------------------------------------- 8. 불량 사용자 실패!! 복습
# 당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지
# 1에서 8이하면 완전탐색?
# '*' 문자를 하나 이상 포함
# 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.
# 제재 아이디 목록들을 구했을 때, 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.

# 1. banned_id 별로 일치하는 아이디 list 작성(아이디 자체 이름 필요해)
#   1-1 check 함수로 하나씩 확인한 후 True라면 tmp에 넣기

# ------------------------------------------- 커뮤
# from itertools import permutations


# def check(candidate, banned_id):
#   for i in range(len(banned_id)):
#     if len(banned_id[i]) != len(candidate[i]):
#       return False
#     for j in range(len(candidate[i])):
#       if banned_id[i][j] == "*":
#         continue
#       if banned_id[i][j] != candidate[i][j]:
#         return False
#   return True

# def solution(user_id, banned_id):
#   candidates = list(permutations(user_id,len(banned_id)))
#   answer = []
#   for candidate in candidates:
#     if not check(candidate, banned_id):
#       continue
#     else:
#       candidate = set(candidate)
#       if candidate not in answer:
#         answer.append(candidate)
#   return len(answer)

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))

# -------------------------------------------------------------------------------- 9. 징검다리 건너기 복습
# 뭔가 디테일이 많이 부족하다.
# 풀이법을 알게되어도 계속 틀린다.
# 구현 연습이 필요한 느낌.

# 최대 몇 명까지 징검다리를 건널 수 있는지 
# 친구들의 수는 무제한 
# stones 배열의 크기는 1 이상 200,000 이하
# 각 원소들의 값은 1 이상 200,000,000 이하인 자연수
# k는 1 이상 stones의 길이 이하

# 걍 하나씩 빼면서 세보면 편하겠지만,
# 절대 안되겠지?

# 이분탐색?
# 기준이 뭔데?
# 한명 ~ 스톤의 최대 값
# ------------------------------------------- 내꺼
# k+1개씩 한 세트로 생각하면서 한 칸씩 움직이면서 생각해보자
# 한 세트 안에서 가장 큰 수-1 이 최대 건널 수 있는 수
# 를 모은 세트 중에 가장 작은 값이 정답

# 정확성만
# def solution(stones, k):
#   answer = 0
#   while True:
#     answer += 1
#     for i in range(len(stones)):
#       if stones[i] == 0:
#         continue
#       stones[i] -= 1

#     count = 0
#     for i in stones:
#       if i == 0:
#         count += 1
#         if count == k:
#           return answer
#       else:
#         count = 0

# ------------------------------------------- 커뮤니티
# def solution(stones, k):
#   left = 1
#   right = 200000000
#   while left <= right:
#     copy_stones = stones.copy()
#     mid = (left +right) //2
#     count = 0

#     for i in copy_stones:
#       if i -mid <= 0:
#         count += 1
#       else:
#         count = 0
#       if count >= k:
#         break
#     if count >= k:
#       right = mid -1
#     else:
#       left = mid + 1
#   return left


# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))

# -------------------------------------------------------------------------------- 10. 표 편집
# 모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O,
# 삭제된 행은 X로 표시하여 문자열 형태로 return 

# stack을 이용하는 까다로운 구현문제?
# ------------------------------------------- 내꺼 50분 컷? 시간초과???
# def solution(n, k, cmd):
#   # 첫번째는 index, 두번째는 value
#   ori_table = []
#   for i in range(n):
#     ori_table.append(i)
#   table = ori_table.copy()

#   deleted = []
#   for i in cmd:
#     order_set = i.split(' ')
#     if str(order_set[0]) == 'U':
#       order_set[1] = int(order_set[1])
#       if k >= order_set[1]:
#         k -= order_set[1]
#       else:
#         k = 0
#     elif str(order_set[0]) == 'D':
#       order_set[1] = int(order_set[1])
#       if k+order_set[1] <= n-1:
#         k += order_set[1]
#       else:
#         k = n-1
#     elif str(order_set[0]) == 'C':
#       # 없애고
#       deleted.append((k,table[k]))
#       table.remove(table[k])
#       # k의 위치에 따라 
#       if k == len(table):
#         k -= 1
#     elif str(order_set[0]) == 'Z':
#       index,value = deleted.pop()
#       if index > k:
#         table.insert(index,value)
#       else:
#         table.insert(index,value)
#         k+=1

#     print(order_set)
#     print('k',k)
#     print('table',table)
#     print('deleted', deleted)
#     print()
  
  # sorted_table = [0] * n
  # for i in table:
  #   sorted_table[i] = i

  # answer = ''
  # for i,j in zip(ori_table,sorted_table):
  #   if i == j:
  #     answer += 'O'
  #   else:
  #     answer += 'X'
  # return answer

# ------------------------------------------- 커뮤니티 링크드 리스트
# ref: https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python

# def solution(n, k, cmd):
#   cur = k
#   table = { i:[i - 1, i + 1] for i in range(n) }
#   answer = ['O'] * n
#   table[0] = [None, 1]
#   table[n - 1] = [n - 2, None]
#   stack = []
#   print(table)

  # for c in cmd:
  #   if c == "C":
  #     # 삭제
  #     answer[cur] = 'X'
  #     prev, next = table[cur]
  #     stack.append([prev, cur, next])
  #     if next == None:
  #       cur = table[cur][0]
  #     else:
  #       cur = table[cur][1]
  #     if prev == None:
  #       table[next][0] = None
  #     elif next == None:
  #       table[prev][1] = None
  #     else:
  #       table[prev][1] = next
  #       table[next][0] = prev
  #   elif c == "Z":
  #     # 복구
  #     prev, now, next = stack.pop()
  #     answer[now] = 'O'
  #     if prev == None:
  #       table[next][0] = now
  #     elif next == None:
  #       table[prev][1] = now
  #     else:
  #       table[next][0] = now
  #       table[prev][1] = now

  #   else:
  #     # 커서 이동
  #     c1, c2 = c.split(' ')
  #     c2 = int(c2)
  #     if c1 == 'D':
  #       for _ in range(c2):
  #         cur = table[cur][1]
  #     else:
  #       for _ in range(c2):
  #         cur = table[cur][0]
  # return ''.join(answer)


# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

# -------------------------------------------------------------------------------- 11. 
# ------------------------------------------- 내꺼
# -------------------------------------------------------------------------------- 12. 
# ------------------------------------------- 내꺼
# -------------------------------------------------------------------------------- 13. 
# ------------------------------------------- 내꺼