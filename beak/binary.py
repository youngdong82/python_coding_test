# -------------------------------------------------------------------------------- bisect
# from bisect import bisect,bisect_left,bisect_right
# a = [1,4,4,4,5,6]

# print(bisect(a,3))
# 기본 bisect는 bisect_right과 같다.
# 내장함수 index값처럼 쓰려면 bisect_left를 써야한다.
# 기본 bisect는 거의 사용하지 않는다.

# 존재여부 확인을 위해선??
# 갯수 세기 참고



# # ------------------------------------- bisect_left
# # 왼쪽에서 특정 값을 넣는다면 나오는 index 값
# left = bisect_left(a, 4)
# print('left', left)

# # ------------------------------------- bisect_right
# # 오른쪽에서 특정 값을 넣는다면 나오는 index 값
# right = bisect_right(a, 4)
# print('right', right)

# # ------------------------------------- 갯수 구하기

# print('how many', right - left)


# -------------------------------------------------------------------------------- 1. 1920 번 수 찾기
# ------------------------------------------- 내꺼
# n = int(input())
# n_list = list(map(int,input().split()))
# n_list.sort()

# m = int(input())
# m_list = list(map(int,input().split()))

# def binary(data, target):
#   start = 0
#   end = len(data) -1
#   while start <= end:
#     mid = (start + end) //2
#     if data[mid] == target:
#       return mid
#     elif data[mid] < target:
#       start = mid +1
#     else:
#       end = mid -1
#   return None


# for i in m_list:
#   answer = binary(n_list,i)
#   if answer != None:
#     print(1)
#   else:
#     print(0)

# -------------------------------------------------------------------------------- 2. 10816 번 숫자 카드 2
# ------------------------------------------- 내꺼 dic 사용
# n = int(input())
# cards = list(map(int,input().split()))
# dic = {}
# for i in cards:
#   if i not in dic.keys():
#     dic[i] = 1
#   else:
#     dic[i] += 1

# # print(dic)

# m = int(input())
# check = list(map(int,input().split()))

# for i in check:
#   if i not in dic.keys():
#     print(0, end=' ')
#   else:
#     print(dic[i], end=' ')

# ------------------------------------------- 내꺼 이분탐색
# from bisect import bisect_left
# from bisect import bisect_right


# n = int(input())
# cards = list(map(int,input().split()))
# cards.sort()

# m = int(input())
# check = list(map(int,input().split()))
# # print(cards)
# # print(check)

# for i in check:
#   left = bisect_left(cards, i)
#   right = bisect_right(cards, i)
#   print(right- left)

# -------------------------------------------------------------------------------- 3. 1654 번 랜선 자르기 복습
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함!!

# zero division error 발생하는 이유는 m=0인 경우에 발생하는데,
# 랜선 길이의 최소 값은 1입니다. 랜선의 길이는 절대 0일 수 없습니다.
# 그렇다면 탐색 시작 범위인 start의 초기 값은 어때야 할까요? 
# ------------------------------------------- 내꺼
# k,n = map(int,input().split())
# data = []
# for i in range(k):
#   data.append(int(input()))

# def binary(data, target):
#   target_deck = []
#   start = 1
#   end = max(data)
#   while start <= end:
#     mid = (start + end)//2

#     result = 0
#     for i in data:
#       result += i//mid
#     if result >= target:
#       target_deck.append(mid)
#       start = mid+1
#     else:
#       end = mid-1
#   return target_deck


# answer = binary(data, n)
# if len(answer)!= 0:
#   print(max(answer))

