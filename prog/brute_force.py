# ---------------------------------------------------------- enumerate
# ---------------------------------------------------------- from itertools import cycle
# ---------------------------------------------------------- from itertools import permutations
# ---------------------------------------------------------- join
# ---------------------------------------------------------- |=
# s1 = {"a", "b", "c"}
# s2 = {"d", "e", "f"}

# # OR, | 
# s1 | s2  = {'a', 'b', 'c', 'd', 'e', 'f'}
# s1 = {'a', 'b', 'c'}   # `s1` is unchanged

# # In-place OR, |=
# s1 |= s2
# s1 = {'a', 'b', 'c', 'd', 'e', 'f'}   # `s1` is reassigned



# --------------------------------------------------------------------------------모의고사 22분 컷!
# ------------------------------------------ 내꺼 
# def solution(answers):
#   answer = []
#   a = [1,2,3,4,5]
#   b = [2,1,2,3,2,4,2,5]
#   c = [3,3,1,1,2,2,4,4,5,5]

#   count_a = 0
#   count_b = 0
#   count_c = 0

#   for i in range(len(answers)):
#     if a[i%5] == answers[i]:
#       count_a += 1
#     if b[i%8] == answers[i]:
#       count_b += 1
#     if c[i%10] == answers[i]:
#       count_c += 1

#   counts = [count_a, count_b, count_c]
#   for i in range(3):
#     if counts[i] == max(counts):
#       answer.append(i+1)

#   return answer

# ------------------------------------------ 커뮤니티
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result

# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))
# -------------------------------------------------------------------------------- 소수 찾기 실패!!
# ------------------------------------------ 커뮤니티 permutation, join, |=
# from itertools import permutations
# from math import sqrt

# def check_prime(n):
#   if n == 0 or n == 1:
#     return False
#   for i in range(2, int(sqrt(n))+1):
#     if n%i == 0:
#       return False
#   return True

# def solution(numbers):
#   answers = []
#   prime_set = set()
#   for i in range(len(numbers)):
#     n_permu = permutations(numbers,i+1)
#     prime_set |= set(map(int,map("".join, n_permu)))
#   for i in prime_set:
#     if check_prime(i) == True:
#       answers.append(i)
#   return len(answers)
# ------------------------------------------ 다른 소수 구하기
# ** 0.5는 루트 씌우는 것과 같다.
# ------------------------------------------ 재귀 다시 한번 보자!!
# https://www.youtube.com/watch?v=m3kCKV8oc1g

  # 모든 조합을 만드는 recursive를 수행한다.
  # prime_set의 length를 반환한다.


# print(solution("17"))
# print(solution("011"))

# -------------------------------------------------------------------------------- 카펫 25분 컷!
# 가로가 세로보다 길다
    # 1, 8
    # 1*1, 3*3 -1
    # 2, 10
    # 2*1, 4*3 -2
    # 3, 12
    # 3*1, 5*3 -3
    # 4, 14
    # 4*1, 6*3-4
    # 4, 12
    # 2*2, 4*4-4
    # 24, 24
    # 6*4, 8*6-24
    # 8*3, 10*5-24

    
# import math


# def solution(brown, yellow):
#   # 1. 1부터 옐로 squrt()까지 확인하기
#   candidates = []
#   for i in range(1,int(math.sqrt(yellow))+1):
#     if yellow%i == 0:
#       candidates.append((i, yellow//i))

#   # 2. 각 케이스마다 나오는 몇 *몇 - 몇이 brown과 맞는 지 확인하기
#   for candidate in candidates:
#     a,b = candidate
#     if (a+2) * (b+2) - yellow == brown:
#       answer = [b+2, a+2]
#       print(answer)

# solution(10, 2)
# solution(8, 1)
# solution(24, 24)


