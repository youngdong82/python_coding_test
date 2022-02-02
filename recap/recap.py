# 복잡도
# 시간 복잡도, 공간 복잡도가 있다. 복잡도에 따라 풀이법이 달라진다!

# 시간 복잡도
# 보통 연산 횟수: C언어 기준 1초에 10억(1,000,000,000)이하
# 보통 연산 횟수: python 기준 1초에 2000만(20,000,000)
# 보통 연산 횟수: pypy3 기준 1초에 2000만(20,000,000) ~ 1억(100,000,000)이하
# 1초일 경우
# N이 500 인 경우: O(N**3)
# N이 2000 인 경우: O(N**)
# N이 100,000 인 경우: O(NlogN)
# N이 10,000,000 인 경우: O(N)

# 공간 복잡도
# 보통 128MB - 512MB로 제한한다.
# a[1000]: 4KB
# a[1000000]: 4MB
# a[2000][2000]: 16MB
# a[100000000]: 400MB

# -------------------------------------------------------------------------- 그리디
# 현재 가장 좋은 것만을 선택했을 때,
# 정확한 답을 찾을 수 있다는 보장이 있을 때 사용.
# 문제 유형을 파악하기 어렵다면,
# 그리디 의심!
# 현재의 선택이 나중에 미칠 영향에 대해 고려하지 않는다.
# 플로이드 워셜
# 다익스트라
# 특히 그리디는 많은 유형 접하고 풀어보는 수 밖에 없다.


# -------------------------------------------------------------------------- 구현
# 완전탐색, 시뮬레이션
# 데이터 처리량이 많을 때는 메모리 제한을 고려하자
# 풀이를 떠올리기는 쉽지만 코드로 옮기기 어려운 문제
# 알고리즘은 간단한데 코드가 매우 길어지는 문제
# 특정 소수점자리까지 출력하는 문제
# 문자열을 한 문자 단위로 끊어서 리스트에 넣어야하는 문제
# 대체로 까다로운 조건들이 많다.
# 감은 잡히는데 막상 코드로 옮기자니 막막 => 각 단계마다 함수화를 시켜서 나눠서 생각하자.


#-------------------------------------------------------------------------- DFS 와 BFS
# 2차원 배열에서 탐색 문제를 만나면, 그래프 형태로 표현한 다음 풀이법 고민!
# 나의 경험으로 일단 맞는 것 같은 알고리즘 써놓고 그곳에다 수정하는 것이 더 효율적이다.
# 아무것도 안 쓰면 아무것도 생각 안남.

#--------------------------------------- DFS
# 인접 리스트
# 스택 자료구조 이용
# 재귀함수
# O(N)

# def dfs(graph,start,visited):
#   visited[start] = True
#   print(start, end=' ')
#   for i in graph[start]:
#     if visited[start] == False:
#       dfs(graph,i,visited)

#---------------------------------------BFS
# 인접 리스트
# 큐 자료구조 이용 deque
# 일반적으로 dfs보다 살짝 더 빠르다.
# O(N)

# from collections import deque

# def bfs(graph,start,visited):
#   q = deque([start])
#   visited[start] = True
#   while q:
#     now = q.popleft()
#     print(now, end=' ')
#     for i in graph[now]:
#       if visited[i] == False:
#         visited[i] = True
#         q.append(i)


#-------------------------------------------------------------------------- 정렬
# array = [6,4,5,9,1,8,2,3,7]
# n = len(array)
# 실제로는 sort()나 sorted 사용
# 최악의 경우에도 O(NlogN)
# 병합정렬, 하이브리드 정렬
# (속도가 비교가 안될 정도로 빠르다)
# sorted()는 기존 값 변경 안함,  return 값이 있다.
# sort()는 기존 값 변경, return 값 없다.
# array.reverse()
# array.sort(reverse=True)
# array.sort(key = lambda x: (-float(x[0]), int(x[1])))
# array.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

#--------------------------------------- 선택정렬
# O(N2) - 이중 반복문
# for i in range(n):
#   min_value = i
#   for j in range(i+1, n):
#     if array[min_value] > array[j]:
#       min_value = j
#   array[min_value],array[i] = array[i], array[min_value]


#--------------------------------------- 삽입정렬
# O(N2) - 이중 반복문 
# 최선의 경우 O(N)
# for i in range(1,n):
#   for j in range(i,0,-1):
#     if array[j] < array[j-1]:
#       array[j],array[j-1] = array[j-1],array[j]
#     else:
#       break


#--------------------------------------- 퀵정렬
# 평균 O(NlogN) 연산마다 반퉁나는 것이 2개씩
# def quick_sort(array):
#   if len(array) <= 1:
#     return array

#   pivot = array[0]
#   tail = array[1:]
#   left_side = [x for x in tail if x <= pivot]
#   right_side = [x for x in tail if x > pivot]

#   return quick_sort(left_side) + [pivot] + quick_sort(right_side)


#--------------------------------------- 계수정렬
# O(N+K)
# 데이터 크기가 한정, 중복이 있을 수록 유리함
# 가장 큰 데이터와 작은 데이터의 차이가 1,000,000 을 넘지 않을 때 효과적
# 기수 정렬과 더불어 가장 빠르다.
# 비교기반 알고리즘이 아니다.
# 자꾸 헷갈리는데, 인덱스 값이 아닌 리스트 안의 가장 큰 값을 기준으로 만들어야 한다.
# dp = [0] * (max(array)+1)

# for i in range(n):
#   dp[array[i]] += 1

# for i in range(n):
#   for _ in range(dp[i]):
#     print(i, end=' ')

# 기수정렬이란?

#--------------------------------------------------------------------------이진탐색
# 정렬되지 않은 리스트에서 데이터를 찾을 때, 순차 탐색을 사용한다.
# 순차탐색 시간복잡도: O(N)
# 데이터가 정렬되어있다면 이진탐색 가능!!
# 이진탐색 시간복잡도: O(logN)
# 반퉁한다는 점에서 퀵 정렬과 비슷
# 그리디와 이진탐색이 함께 나오는 고난이도 문제가 나온다!!
# 이진탐색 구현은 껌으로 해야 해!!

# 이진탐색은 효율적이기에
# 입력 데이터가 많거나 탐색 범위가 매우 넓다.
# 따라서 input()을 더 빠른 것으로 바꿔보자
# readline()이후 엔터가 줄 바꿈 기호로 입력되는데,
# 이 공백 문자를 제거하기 위해 rstrip()함수 사용
# import sys
# sys.stdin.readline().rstrip()

# --------------------------------------- 재귀함수
# def binary_re(array, target, start, end):
#   if start>end:
#     return None
#   mid = (start + end) //2
#   if array[mid] == target:
#     return mid
#   elif array[mid] > target:
#     return binary_re(array,target,start,mid-1)
#   else:
#     return binary_re(array,target,mid+1, end)

# --------------------------------------- 반복문
# def binary(array, target, start, end):
#   while start <= end:
#     mid = (start + end)//2
#     if array[mid] == target:
#       return mid
#     elif array[mid] < target:
#       start = mid+1
#     else:
#       end = mid-1
#   return None


# 트리 자료구조
# 부모와 자식 관계
# 최상단 노드를 루트노드
# 최하단 노드를 단말노드
# 일부를 떼어내도 트리구조 유지
# 파일 시스템처럼 계층적이고 정렬된 데이터를 다루기에 적합

# 특징
# 왼쪽 자식 < 부모 < 오른쪽 자식



#-------------------------------------------------------------------------- 다이나믹 프로그래밍
# 그리디 알고리즘
# 분할 정복 알고리즘
# 메모이제이션: 때에 따라 사전 자료형을 사용할 수도 있데!
# 점화식!!!
# 두 가지 조건
# 큰 문제를 작은 문제로 나눌 수 있다.
# 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
# 완전탐색이 너무 오래 걸리면 다이나믹을 의심해보자!
# 비효율적으로 구현한 후 메모이제이션으로 코드 개선하는 것도 좋은 방법!!
# O(N)
# ---------------------------------------재귀함수 버전
# 탑다운 방식: 오버헤드가 발생할 수 있다.
# 오천번째 이상 recursive 되면 recursive depth 관련 오류가 발생할 수 있다.
# setrecursionlimit()을 이용해서 완화할 수는 있다.
# dp = [0]*(x+1)

# def fibo_re(x):
#   if x == 1 or x == 2:
#     return 1
#   if dp[x] != 0:
#     return dp[x]
#   dp[x] = fibo_re(x-1) + fibo_re(x-2)
#   return dp[x]

#--------------------------------------- 반복문 버전 추천!
# 보텀업 방식
# d = [0] * (n+1)

# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3,n+1):
#   d[i] = d[i-1] + d[i-2]


#-------------------------------------------------------------------------- 최단 경로
#-------------------------------------------------------------------------- 그래프 이론
#-------------------------------------------------------------------------- 소수 판별, 에라토스테네스의 체
# --------------------------------------- 소수 판별
# 그냥 구현한다면 O(X)이지만
# 해당 알고리즘을 사용하면
# O(X1/2) X의 제곱근
# 약수의 대칭성을 이용한 제곱근 사용
# import math

# def prime_number(x):
#   for i in range(2,int(math.sqrt(x)) + 1):
#     if x%i == 0:
#       return False
#   return True

#--------------------------------------- 에라토스테네스의 체
# O(NloglogN)
# 선형시간에 가깝게 빠르다.
# 그러나
# 메모리가 많이 필요하다.
# data = [True for _ in range(n+1)]

# for i in range(2, int(math.sqrt(x))+1):
#   if array[i] == True:
#     j = 2
#     while i*j <=n:
#       array[i*j] = False
#       j += 1

#-------------------------------------------------------------------------- 투 포인터, 합집합, 구간 합
#--------------------------------------- 투 포인터
# 음수 데이터 있을 경우 해결 불가

# n = 5
# m = 7
# array = [1,2,3,2,5]

# count = 0
# end = 0
# inter_sum = 0

# for start in range(n):
#   while inter_sum < m and end<n:
#     inter_sum += array[end]
#     end += 1
#   if inter_sum == m:
#     count += 1
#   inter_sum -= array[start]
  

#--------------------------------------- 합집합
# a = [1,4,5,8]
# b = [2,3,6,7,9]
# d = [0] * (len(a) + len(b))

# i = 0
# j = 0
# k = 0

# while i < len(a) or j < len(b):
#   if j >= len(b) or (i < len(a) and a[i] <= b[j] ):
#     d[k] = a[i]
#     i += 1
#   else:
#     d[k]= b[i]
#     j+=1
#   k += 1

#--------------------------------------- 구간 합
# n = 5
# data = [10,20,30,40,50]

# right = 4
# left = 2

# prefix_sum = [0]
# inter_sum = 0

# for i in data :
#   inter_sum += i
#   prefix_sum.append(inter_sum)

# print(prefix_sum[right] - prefix_sum[left-1])


#-------------------------------------------------------------------------- 순열과 조합









#-------------------------------------------------------------------------- 2차원 리스트 90도 회전
# a = [[1,2,3], [4,5,6], [7,8,9]]

# def rotate_right(a):
#   row = len(a)
#   column = len(a[0])

#   res = [[0] * row for _ in range(column)]
#   for i in range(row):
#     for j in range(column):
#       res[j][row-1-i] = a[i][j]
#   return res

# def rotate_left(a):
#   row = len(a)
#   column = len(a[0])

#   res = [[0] * row for _ in range(column)]
#   for i in range(row):
#     for j in range(column):
#       res[column-1-j][i] = a[i][j]
#   return res


