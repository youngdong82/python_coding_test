# -------------------------------------------------------------------------------- dic의 활용
# list.index(i)는 시간 복잡도가 O(N)이지만,
# dict에서 값을 추출하는 시간은 O(1)의 시간 복잡도를 가져 매우 빠르다.

# 시간 단축이 필요할 경우 적극적으로 사용하자
# 18870번 관련 
# 신기한 단축문과 dic 사용법
# dic = {comp_data[i] : i for i in range(len(comp_data))}

# -------------------------------------------------------------------------------- Counter
# dic 기반으로 만들어진 외장함수인듯
# keys,values,items등 dic 관련 매소드 있고
# most_common(n)은
# 가장 많은 순대로, 갯수가 같을 경우 입력 순대로 n개 만큼 리턴한다.
# (숫자,갯수)형태로 반환 

# from collections import Counter

# a = [2,2,2,1,1,1,3,4,5,5,5,5,6,7,8,8]

# cnt1 = Counter(a).most_common(1)
# cnt2 = Counter(a).most_common(2)
# cnt3 = Counter(a).most_common(3)

# cnt_keys = Counter(a).keys()
# cnt_values = Counter(a).values()
# cnt_items = Counter(a).items()
# print(cnt1)
# print(cnt2)
# print(cnt3)
# print(cnt_keys)
# print(cnt_values)
# print(cnt_items)

# -------------------------------------------------------------------------------- # python3와 pypy3의 차이...?
# 10989번 관련
# 같은 코드인데 python3는 통과하는데 pypy3는 통과못함ㅠ
# Python3의 실행시 시간이 매우 오래 걸린다는 단점이 있어, 
# 이를 개선하고자 JIT컴파일 방식을 도입한 PyPy3의 탄생
# 특정경우에는 메모리, 시간 모두 Python3로 선택하는 것이 우수할 경우가 있었고, 
# 또 다른 경우에는 메모리는 Python3가 우세하지만 시간 상으로는 PyPy3가 우수한 경우도 있었다.

# 기본적으로 python은 c로 구현된 인터프리터 언어임과 동시에 컴파일러
# 작성된 코드를 bytecode로 바꾼 후 인터프리터가 실행된다.

# pypy3의 jit 컴파일의 경우,
# 인터프리트 하면서 자주 쓰이는 코드를 캐싱하기 때문에
# 인터프리터의 느린 실행속도를 개선할 수 있다.

# PyPy3에서는 실행시, 자주 쓰이는 코드를 캐싱하는 기능이 있기 때문에 ,
# 즉  메모리를 조금 더 사용하여 그것들을 저장하고 있어, 실행속도를 개선할 수 있기 때문에
# 간단한 코드상에서는 Python3가 메모리, 속도 측에서 우세할 수 있다
# 복잡한 코드(반복)을 사용하는 경우에서는 PyPy3가 우세할 수 있다.

# -------------------------------------------------------------------------------- 수 정렬하기 1
# ------------------------------------------- 내꺼
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

# -------------------------------------------------------------------------------- 수 정렬하기 2
# ------------------------------------------- 내꺼
# n = int(input())
# data = []
# for i in range(n):
#   data.append(int(input()))

# data.sort()

# for i in data:
#   print(i)

# -------------------------------------------------------------------------------- 3. 10989 복습
# ------------------------------------------- 내꺼
# import sys

# n = int(sys.stdin.readline())

# dp = [0] * 10001

# for _ in range(n):
#   dp[int(sys.stdin.readline())] += 1

# for i in range(10001):
#   if dp[i] != 0:
#     for _ in range(dp[i]):
#       print(i)

# -------------------------------------------------------------------------------- 4. 2108번
# ------------------------------------------- 내꺼
# # n = int(input())
# data = []
# dic = {}

# for i in range(n):
#   a = int(input())
#   data.append(a)
#   if a not in dic.keys():
#     dic[a] = 1
#   else:
#     dic[a] += 1

# data.sort()
# dic_sort = list(dic.items())

# dic_sort.sort(key=lambda x: (-x[1], x[0]))
# max_time = dic_sort[0][1]

# big_dic = []
# for i in dic_sort:
#   if i[1] >= max_time:
#     big_dic.append(i[0])


# aver = int(round(sum(data)/n, 0))
# mid = data[n//2]
# common = 0
# if len(big_dic) > 1:
#   common = big_dic[1]
# else:
#   common = big_dic[0]
# rang = max(data) - min(data)
# print(aver)
# print(mid)
# print(common)
# print(rang)

# -------------------------------------------------------------------------------- 5. 1427번
# ------------------------------------------- 내꺼
# n = list(str(input()))
# n.sort(reverse= True)
# print(''.join(n))

# -------------------------------------------------------------------------------- 6. 11650번
# ------------------------------------------- 내꺼 3분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   x,y = map(int,input().split())
#   data.append((x,y))
# data.sort(key=lambda x: (x[0], x[1]))

# for i in data:
#   a,b = i
#   print(a,b)

# -------------------------------------------------------------------------------- 5. 11651번
# ------------------------------------------- 내꺼 3분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   x,y = map(int,input().split())
#   data.append((x,y))
# data.sort(key=lambda x: (x[1], x[0]))

# for i in data:
#   a,b = i
#   print(a,b)

# -------------------------------------------------------------------------------- 5. 1181번
# ------------------------------------------- 내꺼 3분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   a = str(input())
#   if a not in data:
#     data.append(a)
# data.sort(key=lambda x: (len(x),x))

# for i in data:
#   print(i)

# -------------------------------------------------------------------------------- 5. 10814번
# ------------------------------------------- 내꺼 5분 컷!
# n = int(input())
# data = []
# for i in range(n):
#   age,name = input().split()
#   age = int(age)
#   name = str(name)
#   data.append((age,name))

# data.sort(key=lambda x: (x[0]))

# for i in data:
#   age,name = i
#   print(age, name)

# -------------------------------------------------------------------------------- 5. 18870번 복습!!
# ------------------------------------------- 내꺼 시간초과
# import sys

# input = sys.stdin.readline

# n = int(input())
# data = list(map(int,input().split()))

# comp_data = sorted(list(set(data)))
# dic = {comp_data[i] : i for i in range(len(comp_data))}

# for i in data:
#   print(dic[i], end=' ') 

