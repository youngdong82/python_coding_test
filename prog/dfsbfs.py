# 타겟 넘버
# 더하기 빼기로 타깃 넘버를 만드는 경우의 수 출력
def solution(numbers, target):
    n = len(numbers)
    count = 0
    def dfs(index, result):
        if index == n:
            if result == target:
                nonlocal count
                count += 1
            return
        else:
            dfs(index+1, result+numbers[index])
            dfs(index+1, result-numbers[index])
    dfs(0,0)
    return count

# 아름다운 버전
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 네트워크
# 사이클 확인하는 걸로도 풀 수 있을 것 같다.
# 일단 지금은 dfs,bfs로 풀어보자.
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(computers, start, visited):
      q = deque([start])
      visited[start] = True
      while q:
        now = q.popleft()
        for i in computers[now]:
          if visited[i] == False:
            visited[i] = True
            q.append(i)




    return answer