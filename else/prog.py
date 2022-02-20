#  --------------------------------------------------- hash
#  --------------------------------------------------- zip
#  --------------------------------------------------- startswith
#  --------------------------------------------------- Counter
# 보통 사전자료형에 임의의 값을 넣을 때,
# key값으로 hash화 해서 넣는다.

# hash('문자열')
# 실행할 때마다 문자열에 따른 다른 값이 배정된다.
# int는 hash화 되지 않고 값을 유지
# True는 언제나 1, False는 0

# Example
# hello = True
# hello1 = 123
# hello2 = 'dong1'
# hello3 = 'dong2'
# summ = 0

# summ += hash(hello)
# summ += hash(hello1)
# summ += hash(hello2)
# summ += hash(hello3)
# print(summ)
# summ -= hash(hello)
# summ -= hash(hello1)
# summ -= hash(hello2)
# summ -= hash(hello3)
# print(summ)
# # ---------------------------------------------------  완주하지 못한 선수 - 실패, 정렬 아이디어 얻고 10분 컷!
# # ------------------------- 통과 but 시간초과
# def solution(participant, completion):
#     answer = ''
#     for i in participant:
#         if i in completion:
#             completion.remove(i)
#         else:
#             answer = i
#     return answer

# # ------------------------- 정렬 이용 10분 컷!
# def solution(p, c):
#     p.sort()
#     c.sort()
#     for i in range(len(c)):
#         if p[i] != c[i]:
#             return p[i]
#     return p[-1]

# # ------------------------- 커뮤니티 1 - 나와 가장 비슷, zip 함수 사용
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for p, c in zip(participant, completion):
#         if p != c:
#             return p
#     return participant[-1]

# # ------------------------- 커뮤니티 2 - 해시 함수 사용
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer

# # ------------------------- 커뮤니티 2 - Counter 사용
# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# # ---------------------------------------------------  전화번호 목록 - 실패!
# # -------------------------- startswith 사용 시간초과!
# def solution(phone_book):
#   phone_book.sort()
#   for i in range(len(phone_book)):

#       if phone_book[j].startswith(phone_book[i]):
#         return False
#   return True

# # -------------------------- sort + startswith 사용
# def solution(phone_book):
#   phone_book.sort()
#   for i in range(1,len(phone_book)):
#     if phone_book[i].startswith(phone_book[i-1]):
#       return False
#   return True

# # -------------------------- zip 이게 퍼포먼스 최고
# def solution(phone_book):
#   phone_book.sort()
#   for p1,p2 in zip(phone_book, phone_book[1:]):
#     if p2.startswith(p1):
#       return False
#   return True

# # -------------------------- hash 활용
# def solution(phone_book):
#   hash_map = {}
#   for i in phone_book:
#     hash_map[i] = 1
#   for phone_number in phone_book:
#     jubdoo = ''
#     for number in phone_number[:-1]:
#       jubdoo += number
#       if jubdoo in hash_map:
#         return False
#   return True


# print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))
# print(solution(["12","123","1235","567","88"]))

# # ---------------------------------------------------  위장 실패! 사전자료형 잘 모르겠어.
# # -------------------------- hash 활용
# def solution(clothes):
#   hash_map = {}
#   for cloth,type in clothes:
#     hash_map[type] = hash_map.get(type, 1) + 1
#   answer = 1
#   for type in hash_map:
#     answer *= hash_map[type]
#   return answer-1

# # -------------------------- Counter 활용
# from collections import Counter

# def solution(clothes):
#   counter = (Counter([type for clothe, type in clothes]))
#   answer = 1
#   for i in counter:
#     answer *= (counter[i]+1)
#   print(answer-1)

# # -------------------------- Counter, reduce 활용
# from collections import Counter
# from functools import reduce

# def solution(clothes):
#   counter = (Counter([type for clothe, type in clothes]))
#   answer = reduce(lambda acc, cur: acc*(cur + 1), counter.values(),1)
#   print(answer-1)


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]));
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]));
