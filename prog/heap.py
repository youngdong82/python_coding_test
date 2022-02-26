
# -------------------------------------------------------------------------------- 더 맵게
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# k가 10억 이고 scov가 100만
# q = []
# heapq.heappush(q,(0,start))
# dist, now = heapq.heappop(q)
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

# ------------------------------------------- 내꺼 시간초과 실패! heapq은 비교안될정도로 빠르다!
def solution(scov, k):
  step = 0
  scov.sort(reverse=True)
  while scov[-1] < k and len(scov) >= 2:
    scov.append(scov.pop() + (scov.pop()*2))
    step += 1
    scov.sort(reverse=True)

  if scov[-1] >=k:
    return step
  else:
    return -1

# ------------------------------------------- 커뮤니티 개빠름
# from heapq import *

# def solution(scov, K):
#     count = 0
#     heapify(scov)
#     while scov[0] < K and len(scov) > 1:
#         num1 = heappop(scov)
#         num2 = heappop(scov)
#         heappush(scov, num1 + num2 * 2)
#         count += 1
#     if scov[0] >=K:
#       return count
#     else:
#       return -1

print(solution([1, 2, 3, 9, 10, 12], 7))
