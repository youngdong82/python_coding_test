# --------------------------------------------------- 수 정렬하기 1
# n = int(input())
# data = []
# for i in range(n):
#   data.append(int(input()))

# for i in range(n):
#   a = i
#   for j in range(i+1,n):
#     if data[a] > data[j]:
#       a = j
#   data[a],data[i] = data[i],data[a]

# for i in data:
#   print(i)

# --------------------------------------------------- 수 정렬하기 2
# n = int(input())
# data = []
# for i in range(n):
#   data.append(int(input()))

# def quick_sort(array):
#   if len(array) <= 1:
#     return array

#   pivot = array[0]
#   tail = array[1:]
#   left_side = [x for x in tail if x <= pivot]
#   right_side = [x for x in tail if x > pivot]

#   return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# data = quick_sort(data)

# for i in data:
#   print(i)

# ------------------------------------------ 다른 버전

# def quick(data):
#   if len(data)<= 1:
#     return data

#   pivot = data[0]
#   tail = data[1:]

#   left = [x for x in tail if x < pivot]
#   right = [x for x in tail if x > pivot]

#   return quick(left) + [pivot] + quick(right)

# result = quick(data)
# for i in result:
#   print(i)

# --------------------------------------------------- 수 정렬하기 3
# 얕보고 있다가... 어렵다...