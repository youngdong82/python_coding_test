# -------------------------------------------------------------------------------- 1. 네트워크
# 네트워크의 개수를 return 
# ------------------------------------------- 내꺼
# def dfs(graph,start,visited):
#   visited[start] = True
#   for i in graph[start]:
#     if visited[i] == False:
#       dfs(graph,i,visited)

# def solution(n, computers):
#   for i in computers:
#     print(i)
#   print()
#   graph = [[] for _ in range(n)]
#   for i in range(n):
#     for j in range(n):
#       if i != j and computers[i][j] == 1:
#         graph[i].append(j)
#   visited = [False] * n

#   print(graph)
#   print(visited)

#   count = 0
#   for i in range(n):
#     if visited[i] == False:
#       dfs(graph,i,visited)
#       count += 1

#   return count


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# -------------------------------------------------------------------------------- 2. 단어변환
# 누가봐도 dfs
# 각 사이클마다,
#   words에서 1개만 다른거 리스트업, 
#   그 중 한개로 바뀐다.


# 최소 몇 단계의 과정?
# 변환할 수 없는 경우에는 0를 return

# ------------------------------------------- 내꺼
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
#   for i in words:
#     visited[i] = False
#   dfs(begin, target, words,visited)
#   if len(answer) == 0:
#     return 0
#   else:
#     return min(answer)



# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

# -------------------------------------------------------------------------------- 4. 입국심사 복습
# 시간을 기준으로
# 몇명 통과할 수 있는지,
# 통과할 수 있는 숫자가 n이 될때까지 이분탐색
# ------------------------------------------- 내꺼
# def solution(n, times):
#   times.sort()
#   left = 1
#   right = times[-1] * n
#   while left <= right:
#     mid = (left + right)//2
#     passed =0
#     for i in times:
#       passed += mid//i
#     if passed < n:
#       left = mid+1
#     else:
#       right = mid-1
#   return left

# print(solution(6,[7, 10]))

# -------------------------------------------------------------------------------- 9. 징검다리 건너기 복습
# 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return

# 감사하게도 난 지금 이 문제가
# 이분탐색 문제라는 것을 인지하고 있다.

# 이분탐색 할때 중요한 것은
# 정렬여부,
# 거리를 기준으로

# ------------------------------------------- 내꺼
# def solution(distance, rocks, n):
#   answer = 0
#   start, end = 0, distance
  
#   rocks.sort()

#   while start<=end:
#     mid = (start+end)//2
#     delete_count = 0
#     anchor = 0
#     for rock in rocks:
#       if rock - anchor < mid:
#         delete_count += 1
#       else:
#         anchor = rock
#       if delete_count >n:
#         break

#     if delete_count >n:
#       end = mid-1
#     else:
#       answer = mid
#       start = mid+1

#   return answer

# print(solution(25,[2, 14, 11, 21, 17],2))

# -------------------------------------------------------------------------------- 5. 더 맵게
# ------------------------------------------- 내꺼
# import heapq


# def solution(scov, k):
#   answer = 0
#   heapq.heapify(scov)

#   while True:
#     now = heapq.heappop(scov)
#     if now < k and len(scov) >= 1:
#       mix = heapq.heappop(scov)
#       heapq.heappush(scov,now + (mix*2))
#       answer += 1
#     else:
#       scov.append(now)
#       break
  
#   if len(scov) == 1 and scov[0] < k:
#     return -1
#   return answer


# print(solution([1, 2, 3, 9, 10, 12],7))

# --------------------------------------------------------------------------------5. 베스트앨범
# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
# 속한 노래가 많이 재생된 장르를 먼저 수록 => 장르별 총 재생횟수 알아야해
# 장르 내에서 많이 재생된 노래를 먼저 수록 => 각 노래별 
# 고유 번호가 낮은 노래

# ------------------------------------------- 내꺼
# def solution(genres, plays):
#   genres_dic = {}
#   for i in range(len(genres)):
#     if genres[i] in genres_dic:
#       genres_dic[genres[i]].append([plays[i],i]);
#     else:
#       genres_dic[genres[i]] = [[plays[i],i]];

#   tmp = []
#   for play_reck in genres_dic.values():
#     play_reck.sort(key=lambda x: (-x[0], x[1]))
#     total = 0
#     for each in play_reck:
#       total += each[0]
    
#     tmp.append([total, play_reck[0][0], play_reck[0][1]])
#     if len(play_reck) >= 2:
#       tmp.append([total, play_reck[1][0], play_reck[1][1]])

#   tmp.sort(key=lambda x:(-x[0]))
#   answer = []
#   for i in tmp:
#     answer.append(i[2])
#   return answer



# print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))

# --------------------------------------------------------------------------------6. 보석 쇼핑
# ------------------------------------------- 내꺼
def solution(gems):
  gem_reck = len(set(gems))

  shortest = len(gems)+1
  left = 0
  right = 0
  contained = {}
  answer = []

  while right < len(gems):
    if gems[right] not in contained:
      contained[gems[right]] = 1
    else:
      contained[gems[right]] += 1
    right += 1
    # 다 포함하고 있는 애들 중에서, 
    if len(contained) == gem_reck:
      while left < right:
        if contained[gems[left]] > 1:
          contained[gems[left]] -= 1
          left +=1
        elif shortest > right - left:
          shortest = right - left
          answer = [left+1, right]
          break
        else:
          break
  return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

print(solution(["A","A","A","B","B"]))
print(solution(["A"]))
print(solution(["A","B","B","B","B","B","B","C","B","A"] ))
print(solution(["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"] ))

print(solution(["A", "B", "C", "B", "A"] ))
print(solution(['A','B','B','C','B','A','B','B','B','C']))
