# ---------------------------------------------------  기능개발 실패!! 테스트케이스 좀 더 확인해보자!
from collections import deque


def solution(progresses, speeds):
  q = deque(progresses)
  answer = []

  while q:
    # 사이클마다 speed값 더해주면서 돈다.
    for i in range(len(q)):
      q[i] += speeds[i]

    # # 100이 넘었다면 큐에 넣는다.
    count = 0
    for i in range(len(q)):
      if q[i] >= 100:
        count += 1
      else:
        break

    # # 큐에서 나가는 것이 발생했다면, 나간 갯수를 answer에 넣는다.
    if count != 0:
      for i in range(count):
        q.popleft()
      answer.append(count)

  return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))