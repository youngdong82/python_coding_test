# -------------------------------------------------------220127
# 선택 정렬
# 위에서 아래로 5분 컷
# n = int(input())
# data = []
# for i in range(n):
#   data.append(int(input()))
# data.sort(reverse=True)

# print(data)

# 성적이 낮은 순서대로 학생 출력하기 5분 컷
# n = int(input())
# data = []
# for i in range(n):
#   name, score = input().split()
#   name = str(name)
#   score = int(score)
#   data.append((name,score))

# data.sort(key=lambda x: x[1])

# for i in data:
#   print(i[0], end=' ')

# 두 배열의 원소 교체 5분 컷
# n,k = map(int,input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# a.sort()
# b.sort(reverse=True)

# for i in range(k):
#   a[i] = b[i]

# print(sum(a))

# 이진
# 부품 찾기
# n = int(input())
# an = list(map(int,input().split()))
# m = int(input())
# am = list(map(int,input().split()))

# def binary(array, target,start,end):
#   while start <= end:
#     mid = (start + end)//2
#     if array[mid] == target:
#       return True
#     elif array[mid] < target:
#       start = mid +1
#     else:
#       end = mid -1
#   return False

# for i in range(m):
#   if binary(an, am[i], 0, n-1):
#     print('yes')
#   else:
#     print('no')


# 떡볶이 떡 만들기 14분 컷!
# n,m = map(int,input().split())
# dduk = list(map(int,input().split()))

# def cut(array, cut_point):
#   lefts = 0
#   for i in array:
#     if i > cut_point:
#       lefts += i - cut_point
#   return lefts


# def binary(dduk,target,start,end):
#   while start <= end:
#     mid = (start + end) // 2
#     if cut(dduk,mid) == target:
#       return mid
#     elif cut(dduk,mid) < target:
#       end = mid -1
#     else:
#       start = mid + 1
#   return None


# print(binary(dduk,m,0,max(dduk)))

