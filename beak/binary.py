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


# -------------------------------------------------------------------------------- LIS 알고리즘 가장 긴 증가하는 부분 수열
# https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 1. 다이나믹 프로그래밍
# 시간복잡도 O(N^2)
# a = [10,20,12,15,30,15,50]
# dp = [1] * len(a)

# for i in range(len(a)):
#   for j in range(i):
#     if a[i] > a[j]:
#       dp[i] = max(dp[i], dp[j]+1)
#   print(dp)


# 2. 이분탐색
# 시간복잡도 O(N log N)
# from bisect import bisect_left

# a = [10,20,12,15,30,15,50]
# dp = [a[0]]

# for i in range(len(a)):
#   if a[i] > dp[-1]:
#     dp.append(a[i])
#   else:
#     index = bisect_left(dp, a[i])
#     dp[index] = a[i]
#   print(dp)
# print(len(dp))


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

# -------------------------------------------------------------------------------- 4. 2805 번 나무 자르기 복습
# 최대값 최소값 구할 때 맞는 mid들을 모은 후 그곳에서 고르는 것이 아닌
# 이진탐색 할때 설정을 바꿔서 start나 end를 출력하자
# 위의 문제도 같다.
# + 무조건 start 0 하지말고 최솟값 확인하자
# ------------------------------------------- 커뮤니티
# n,m = map(int,input().split())
# trees = list(map(int,input().split()))

# start = 1
# end = max(trees)

# while start <= end:
#   mid = (start + end)//2
#   result = 0
#   for i in trees:
#     if mid <= i:
#       result += (i-mid)
#   if result >= m:
#     start = mid+1
#   else:
#     end = mid-1

# print(end)

# -------------------------------------------------------------------------------- 5. 2110 번 공유기 설치 복습
# 한 집에는 공유기를 하나만 설치할 수 있고,
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
# ------------------------------------------- 내꺼
# n,c = map(int, input().split())
# houses = []
# for i in range(n):
#   houses.append(int(input()))
# houses.sort()


# def binary():
#   left = 1
#   right = max(houses) - 1

#   while left <= right:
#     mid = (left + right) // 2
#     count = 1
#     wifi = min(houses) + mid

#     for i in range(1, len(houses)):
#       if wifi <= houses[i]:
#         count += 1
#         wifi = houses[i] + mid
#     print(left,mid,right, 'wifi:',wifi, 'count:', count)

#     if count >= c:
#       left = mid + 1
#     elif count < c:
#       right = mid -1
#   return right

# print(binary())

# -------------------------------------------------------------------------------- 6. 1300 번 k번째 수 복습 이해가 안돼....
# ------------------------------------------- 내꺼 메모리 초과
# n = int(input())
# k = int(input())

# k_list = []
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     k_list.append(i*j)

# k_list.sort()
# print(k_list)
# print(k_list[k-1])

# ------------------------------------------- 커뮤니티
# n = int(input())
# k = int(input())

# def binary_search(target):
#   start = 1
#   end = n*n
#   while start <= end:
#     mid = (start + end) // 2
#     # print(start,mid,end)
#     cnt = 0
#     for i in range(1, n+1):
#       cnt += min(mid//i, n)
#     if cnt >= target:
#       end = mid-1
#     else:
#       start = mid+1
#     # print(cnt)
#   return start


# print(binary_search(k))

# -------------------------------------------------------------------------------- 7. 120115 번 가장 긴 증가하는 부분 수열 2
# ------------------------------------------- 내꺼
# import sys 
# input = sys.stdin.readline 

# n = int(input()) 
# cases = list(map(int, input().split())) 
# lis = [0] 
# for case in cases: 
#   if lis[-1]<case: 
#     lis.append(case) 
#   else:
#     print(lis, case)
#     left = 0 
#     right = len(lis) 

#     while left<right: 
#       mid = (right+left)//2 
#       print(left,mid,right)
#       if lis[mid]<case: 
#         left = mid+1 
#       else: 
#         right = mid 
#     lis[right] = case
#     print(lis, case)
#     print()
# print(lis)
# print(len(lis)-1)


n,m = map(int,input().split())

tmp = []

def back():
  if len(tmp) == m:
    print(' '.join(map(str,tmp)))
    return

  for i in range(1,n+1):
    if i not in tmp:
      tmp.append(i)
      back()
      tmp.pop()

back()