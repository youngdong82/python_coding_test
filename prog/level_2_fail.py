# -------------------------------------------------------------------------------- sort와 string
# strnig은 sort()사용 못함
# 그러나
# sorted는 가능
# -------------------------------------------------------------------------------- 5. 124나라의 숫자 실패! - 복습!!
# ------------------------------------------- 내꺼
# def solution(n):
#     answer = ''
#     while n:
#         if n % 3:
#             answer += str(n % 3)
#             n //= 3
#         else:
#             answer += "4"
#             n = n//3 - 1
#         print(n)
#         print('answer',answer)
#     return answer[::-1]

# print(solution(2))
# print(solution(4))
# print(solution(7))
# print(solution(11))
# print(solution(37))

# -------------------------------------------------------------------------------- 8. 모음 사전
# 커뮤니티 완전탐색이래 + product 
# ------------------------------------------- 내꺼 알고 푸니까 6분 컷!
# from itertools import product


# def solution(word):
#   words = 'AEIOU'
#   answer = []
#   for i in words:
#     answer.append(i)
#   for i in list(product(words,repeat=2)):
#     answer.append(''.join(i))
#   for i in list(product(words,repeat=3)):
#     answer.append(''.join(i))
#   for i in list(product(words,repeat=4)):
#     answer.append(''.join(i))
#   for i in list(product(words,repeat=5)):
#     answer.append(''.join(i))
#   answer.sort()
#   return answer.index(word)+1

  
# print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
# print(solution("EIO"))

# -------------------------------------------------------------------------------- 5. 큰 수 만들기  - 복습!!
# ------------------------------------------- 내꺼 역시나 시간초과
# 백만짜리 숫자를 combinations...?
# 일단 해보자
# from itertools import combinations

# def solution(number, k):
#   candidate = list(combinations(number,len(number)-k))
#   candidate.sort()
#   tmp = candidate[-1]
#   answer = ''
#   for i in tmp:
#     answer += i

#   return answer

# ------------------------------------------- 커뮤 1 큐와 덱 문제다.
# def solution(number, k):
#   answer = []
#   for num in number:
#     while answer and k > 0 and answer[-1] < num:
#       answer.pop()
#       k -= 1
#     answer.append(num)
#   answer = ''.join(answer[:len(number)-k])

#   return answer

# ------------------------------------------- 커뮤 2 큐와 덱 문제다.
# from collections import deque


# def solution(number, k):
#     q = deque(list(number))
#     stack = deque()

#     while q and k:
#         while stack and stack[-1] < q[0]:
#             stack.pop()
#             k -= 1
#             if not k:
#                 break
#         stack.append(q.popleft())

#     # k를 소진시키지 못했을 수도 있다.
#     while k and stack:
#         stack.pop()
#         k -= 1

#     return "".join(stack + q)


# print(solution("1924",2))
# print(solution("1231234",3))
# print(solution("4177252841",4))
# print(solution("654321",1))
# print(solution("654321",5))

# -------------------------------------------------------------------------------- 1. 행렬 테두리 회전하기
# 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의
# 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 
# ------------------------------------------- 내꺼 ㅅㅂ 졸라 오래걸리긴 했지만 풀었다.
# 접근법은 같으나 커뮤니티 배울 필요가 있다.
# def circle(graph, queries):
#   answer = []
#   fx,fy,ex,ey = queries
#   fx = fx-1
#   fy = fy-1
#   ex = ex-1
#   ey = ey-1

#   tmp1 = graph[fx][fy]
#   tmp2 = graph[fx][ey]
#   tmp3 = graph[ex][fy]
#   tmp4 = graph[ex][ey]

#   for i in range(fx,ex):
#     graph[i][fy] = graph[i+1][fy]
#     answer.append(graph[i][fy])

#   for i in range(ey,fy,-1):
#     if i == fy+1:
#       graph[fx][i] = tmp1
#     else:
#       graph[fx][i] = graph[fx][i-1]
#     answer.append(graph[fx][i])

#   for i in range(ex,fx,-1):
#     if i == fx+1:
#       graph[i][ey] = tmp2
#     else:
#       graph[i][ey] = graph[i-1][ey]
#     answer.append(graph[i][ey])

#   for i in range(fy,ey):
#     if i == ey-1:
#       graph[ex][i] = tmp4
#     else:
#       graph[ex][i] = graph[ex][i+1]
#     answer.append(graph[ex][i])

#   return min(answer)


# def solution(rows, columns, queries):
#   graph = [[0] * columns for _ in range(rows)]
#   v = 0
#   result = []
#   for i in range(len(graph)):
#     for j in range(len(graph[0])):
#       v += 1
#       graph[i][j] = v
  
#   for query in queries:
#     result.append(circle(graph, query))

#   return result
  

# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(10,9,[[1,1,10,9]]))

# -------------------------------------------------------------------------------- 7. 삼각 달팽이
# ------------------------------------------- 내꺼 무의미
# ------------------------------------------- 커뮤니티 훌륭하다! 그래프 있는 것은 왠만하면 dx,dy 적용해보자


# -------------------------------------------------------------------------------- 9. 2개 이하로 다른 비트 - 실패! 복습
# https://art-coding3.tistory.com/46
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8-Python
# ------------------------------------------- 내꺼 + 커뮤 - 런타임에러, 시간초과 10분만 더 고민해보자!! 
# -------------------------------------------------------------------------------- 5. 거리두기 확인하기 실패!
# 똑같은 bfs인데 뭐가 문제였던거여...
# 애초에 q에 들어가는 값을 (x,y,거리)로 설정해서
# nx,ny할 때 nd라는 거리값도 +1 해주니 괜춘하네
# ------------------------------------------- 내꺼
