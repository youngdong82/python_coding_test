# # -------------------------------------------------------220127
# # 국영수 8분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   name, a,b,c = input().split()
#   a = int(a)
#   b = int(b)
#   c = int(c)
#   data.append((name,a,b,c))

# data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

# for i in data:
#   print(i[0])


# # 안테나 15분 컷! 
# # 이것보다 훨씬 간단한 방법이 있긴 하다.
# # 그것을 간파하는 것은 다음 단계인 듯 하다.
# # 일단 무식하게 풀어보고 이후 간단한 방법을 찾아보자

# n = int(input())
# data = list(map(int,input().split()))
# data.sort()

# def dist_is(array,point):
#   summ = 0
#   for i in array:
#     summ += abs(i-point)
#   return summ

# min_value = int(1e9)
# result = 0
# for i in data:
#   if dist_is(data,i) < min_value:
#     min_value = dist_is(data,i)
#     result = i

# print(result)

# # 실패율 23분 컷!
# n = int(input())
# stages = list(map(int, input().split()))

# graph = [0] * (n + 2)

# for i in range(len(stages)):
#     graph[stages[i]] += 1


# fail = []

# for i in range(1, (len(graph)) - 1):
#     stage_man = 0
#     for j in range(i, len(graph)):
#         stage_man += graph[j]
#     rate = graph[i] / stage_man
#     fail.append((rate, i))


# fail.sort(key=lambda x: (-float(x[0]), int(x[1])))

# for rate, index in fail:
#     print(index, end=" ")


# # 카드 정렬하기 풀었지만 시간초과ㅠ
# n = int(input())
# cards = []
# for i in range(n):
#   cards.append(int(input()))

# cards.sort(reverse=True)
# array = []

# while len(cards) > 1:
#   a = cards.pop()
#   b = cards.pop()
#   cards.append(a+b)
#   array.append(a+b)

# print(sum(array))


# # 정렬된 배열에서 특정 수의 개수 구하기
# n,x = map(int,input().split())
# data = list(map(int,input().split()))

# result = data.count(x)

# if result == 0:
#   print(-1)
# else:
#   print(result)
# # count 함수는 시간복잡도 O(N)이라 부적합
# n, x = map(int, input().split())
# data = list(map(int, input().split()))


# def binary_first(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target and (mid == 0 or array[mid - 1] < target):
#             return mid
#         elif array[mid] >= target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None


# def binary_last(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target and (mid == n - 1 or array[mid + 1] > target):
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None


# a = binary_first(data, x, 0, n - 1)
# if a == None:
#     print(-1)
# else:
#     b = binary_last(data, x, 0, n - 1)
#     print(b - a + 1)

# # 고정점 찾기 20분 컷!
# n = int(input())
# array = list(map(int, input().split()))

# def binary(array,start,end):
#   while start <= end:
#     mid = (start + end) // 2
#     if array[mid] == mid:
#       return mid
#     elif array[mid] < mid:
#       start = mid +1
#     else:
#       end = mid -1
#   return None



# # 공유기 설치
# from itertools import combinations

# n,c = map(int,input().split())
# homes = []
# for i in range(n):
#   homes.append(int(input()))
# homes.sort()

# candidates = list(combinations(homes,c))

# result = -1e9
# for home in candidates:
#   min_value = 1e9
#   for i in range(c-1):
#     min_value = min(min_value, home[i+1] - home[i])
#   result = max(result,min_value)

# print(result)

# # 설명이 이해가 안되면 코드를 봐 은근 이해된다. 아주 은근
# n,c = map(int,input().split())
# homes = []
# for i in range(n):
#   homes.append(int(input()))
# homes.sort()

# start = 1
# end = homes[-1] - homes[0]
# result = 0

# while start <= end:
#   mid = (start + end) // 2
#   value = homes[0]
#   count = 1
#   for i in range(1,n):
#     if homes[i] >= value +mid:
#       count += 1
#       value = homes[i]

#   if count >= c:
#     start = mid + 1
#     result = mid
#   else:
#     end = mid -1

# print(result)

# 가사 검색
# 완전탐색 40분컷
words = list(input().split())
quer = list(input().split())
result = [0]* len(quer)


def isit(stand,word):
  for k in range(len(stand)):
    if stand[k] == '?':
      continue
    else:
      if stand[k] == word[k]:
        continue
      else:
        return False
  return True


for stand in quer:
  leng = len(stand)
  count = 0
  for word in words:
    if len(word) == leng:
      if isit(stand,word):
        count += 1
  print(count)

# 모르겠어ㅠ
# 가까스로 이해는 되는 듯...?
# from bisect import bisect_left, bisect_right

# words = list(input().split())
# queries = list(input().split())


# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index


# array = [[] for _ in range(10001)]
# reversed_array = [[] for _ in range(10001)]


# def solution(words, queries):
#     answer = []
#     for word in words:
#         array[len(word)].append(word)
#         reversed_array[len(word)].append(word[::-1])
#     for i in range(10001):
#         array[i].sort()
#         reversed_array[i].sort()
#     for q in queries:
#         if q[0] != "?":
#             res = count_by_range(
#                 array[len(q)], q.replace("?", "a"), q.replace("?", "z")
#             )
#         else:
#             res = count_by_range(
#                 reversed_array[len(q)],
#                 q[::-1].replace("?", "a"),
#                 q[::-1].replace("?", "z"),
#             )
#         answer.append(res)
#     return answer


# result = solution(words, queries)
# print(result)
