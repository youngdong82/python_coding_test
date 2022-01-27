
# a = [4, 3, 6, 4, 1, 6, 8, 5, 3]
# 선택
# for i in range(len(a)):
#   min_index = i
#   for j in range(i+1,len(a)):
#     if a[j] < a[min_index]:
#       min_index = j
#   a[i],a[min_index] = a[min_index],a[i] 


# 삽입
# for i in range(1,len(a)):
#   for j in a[i,0,-1]:
#     if a[j] < a[j-1]:
#       a[j], a[j-1] = a[j-1],a[j]
#     else:
#       break


# 퀵
# def quick(a):
#   if len(a) <= 1:
#     return a
#   pivot = a[0]
#   tail = a[1:]

#   left = [x for x in tail if x < pivot]
#   right = [x for x in tail if x > pivot]

#   return quick(left) + [pivot] + quick(right)


# 계수
# 전부 양의 정수일 때
# 가장 작은 수와 큰 수의 차이가 1000000을 넘지 않을 때
# array = [0] * (max(a) + 1)

# for i in range(len(a)):
#   array[a[i]] += 1

# for i in range(len(array)):
#   for _ in range(array[i]):
#     print(i, end=' ')



# 이진탐색
# 재귀
# def binary_recur(array, target, start,end):
#   if start > end:
#     return None
#   mid = (start + end)//2

#   if array[mid] == target:
#     return mid
#   elif array[mid] > target:
#     return binary_recur(array,target,start,mid-1)
#   else:
#     return binary_recur(array,target, mid + 1, end)

# 반복
# def binary(array,target,start,end):
#   while start <= end:
#     mid = (start + end)//2
#     if array[mid] == target:
#       return mid
#     elif array[mid] > target:
#       end = mid-1
#     else:
#       start = mid + 1
#   return None
