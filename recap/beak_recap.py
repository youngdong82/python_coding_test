# -------------------------------------------------------------------------------- 2e+9+1...
# a = 2e+9+1
# b = int(1e9)
# print(a)
# print(b)

# -------------------------------------------------------------------------------- meet in the middle 알고리즘
# 완전탐색 + 이분탐색
# Brutefroce 알고리즘을 사용해야하지만 경우의 수가 Bruteforce를 사용하기에 조금 클 때 사용
# Bruteforce를 사용하되 이를 분할해서 연산의 수를 최소화하는 것

# N 크기 배열 원소의 모든 조합을 고려할 때
# N이 40이라면 경우의 수가 2^40으로 (약 1조)로 시간 내에 연산 불가
# 이때 MITM 사용

# 1450 번 참고
# 기본구조
# n을 2로 나눈다.
# 나눈 2에서 끼리 완전탐색으로 인스턴스를 넣은 두 리스트 만들기
# (이때 combinations 사용하면 안됨.)
# (사용하면 이 짓하는 의미가 없다.)
# dfs(백트래킹)으로 고고
# 백트래킹으로 하기 때문에 애초에 평균적으론 n^2도 안걸림 (최악의 경우 n^2)

# 두 리스트가 나왔다면
# 이중반복 쓰면 의미없다.
# 반복문 + 이분탐색으로 찾아야해
# 이분탐색은 반퉁씩 하면서 합보다 큰 값을 지니는 인덱스의 왼쪽을 가져가는 것.

# -------------------------------------------------------------------------------- sys.stdin.readline().rstrip()
# ------------------------------------------- 내꺼
# 문자열일 경우 rstrip 필수!!
# import sys
# input = sys.stdin.readline

# a = input()
# b = input().rstrip()
# print(a, len(a))
# print(b, len(b))

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

# -------------------------------------------------------------------------------- dfs,재귀,백트래킹
# 자주하는 실수
# 1. 가지치기를 하지 않아서 시간초과 발생
# 2. 한 단계 더 들어갈 때 가능한 값인지 불가능한 값인지 비효율적으로 판단(visited 같은 함수를 이용하자)
# 3. 재귀를 들어갔다가 탈출할 때 값을 원래대로 바꿔놓지 않는다. 넣었으면 빼라.

# 기본적인 구조

# 방문처리를 위한 visited리스트 (중복이 가능하다면 필요없다.)

# 깊이를 담을 임의의 리스트
# def dfs():
#   원하는 깊이에 도달했다면 or 더이상 갈 수 없다면, 
#   출력을 하던 answer 값을 지정을 하던 탈출

#   (리스트 내 같은 원소 때문에 중복 출력이 싫다면 overlap 변수 사용)
#   포문을 돌면서
#   방문처리한 후
#   dfs()
#   빠져나온 후 다른 길로 가는데 방문처리되어있으면 안되니까.
#   방문처리 취소