# -------------------------------------------------------------------------------- level 2 느끼는 점
# level 1의 대부분이 너 이거 사용할 줄 알아? 였다면
# level 2는 너 이거 어떤 유형 문제인줄 알아? + 규칙을 찾아낼 수 있어? 느낌...
# 의외로 카카오 문제가 구현에서 시간은 많이 잡아먹어도 깔끔한 듯?

# 확실히 어떤 유형 문제인줄 알고, 규칙을 찾아낼 수 있다면 코드 자체는 매우 간단했다.

# -------------------------------------------------------------------------------- enumerate
# index와 value 값을 튜플로 묶어서 보내준다.
# 당연하지만 index는 int
# value는 원래 타입
# a = ['a','b','c','d']
# b = 'abcd'
# c = '1234'
# d = [1,2,3,4]
# for i, value in enumerate(d):
#   print(i,value)
#   print(type(i),type(value))

# for i in enumerate(b):
#   print(i)
#   print(type(i))

# -------------------------------------------------------------------------------- round 함수
# round함수는 반올림해주는데
# print(round(0.5))
# print(round(1.5))
# print(round(2.5))
# 1.5는 2가 나오지만
# 0.5는 1이 아닌 0이 나온다....? 왜지???
# 2.5도 3이 아닌 2가 나온다.

# 파이썬의 round 함수는 똑같이 가깝다면 짝수를 반환하게 설계되어있기 때문에 0 을 반환하는 것
# 음수인 경우도 마찬가지
# print(round(-0.5))
# print(round(-1.5))
# print(round(-2.5))

# 이유는? 부동소수점 때문.

# 해결책은??
# 조심하는 것 외에 딱히 없는 듯;;

# -------------------------------------------------------------------------------- for else
# 10번 스킬트리 문제
# for문이 중간에 break 등으로 끊기지 않고,
# 끝까지 수행 되었을 때 수행하는 코드

# a = [1,2,3,4,5]
# for i in a:
#   if i > 5:
#     break
#   print('hello')
# else:
#   print('5보다 큰 수 없음')
# -------------------------------------------------------------------------------- product, permutations, combinatioins
# a = [1,2,3,4,5,6,7]
# #-------------------------------------------- permutations 순서
# # # 요소 간 순서가 다르면 다르다고 인식하는가? o
# # # 인스턴스 내에서 반복을 허용하는 가? x

# from itertools import permutations,combinations,product, combinations_with_replacement
# candi_permu = list(permutations(a,3))
# print(len(candi_permu))
# print(candi_permu)

# #-------------------------------------------- combinations 조합
# # # 요소 간 순서가 다르면 다르다고 인식하는가? x
# # # 인스턴스 내에서 반복을 허용하는 가? x
# candi_combi = list(combinations(a,3))
# print(len(candi_combi))
# print(candi_combi)

# #-------------------------------------------- product
# # # 요소 간 순서가 다르면 다르다고 인식하는가? o
# # # 인스턴스 내에서 반복을 허용하는 가? o

# candi_product = list(product(a,repeat=3))
# print(len(candi_product))
# print(len(a) ** 3)
# print(candi_product)

# candi_product = list(product(a,repeat=2))
# print(len(candi_product))
# print(len(a) ** 2)
# print(candi_product)

# #-------------------------------------------- combinations_with_replacement
# # # 요소 간 순서가 다르면 다르다고 인식하는가? x
# # # 인스턴스 내에서 반복을 허용하는 가? o

# candi_combi_repl = list(combinations_with_replacement(a,3))
# print(len(candi_combi_repl))
# print(candi_combi_repl)

# -------------------------------------------------------------------------------- 문자열 뒤짚기
# 문자열 [::-1]
# -------------------------------------------------------------------------------- from math import gcd, lcm
# from math import gcd, lcm
# print(gcd(4,9))
# print(gcd(3,9))
# print(gcd(4,6))

# print(lcm(4,9))
# print(int(4*9/gcd(4,9)))
# print(lcm(3,9))
# print(int(3*9/gcd(3,9)))
# print(lcm(4,6))
# print(int(4*6/gcd(4,6)))

# -------------------------------------------------------------------------------- 진수 변환
# def make(num, depend):
#   total_string = '0123456789ABCDEF'
#   string = total_string[:depend]
#   answer = ''
#   while num >0:
#     num, rest = divmod(num,depend)
#     print(num, rest)
#     answer += str(string[rest])
#   return answer[::-1]

# print(make(38, 8))

# -------------------------------------------------------------------------------- 2차원 배열 확실하게!!
# a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# print(a[1][2])
# print(len(a))
# print(len(a[0]))
# list[세로값][가로값]



# -------------------------------------------------------------------------------- bisect
# 9. 순위 검색 참조
# -------------------------------------------------------------------------------- defaultdict
# 문제 2번에서 디폴트딕 뭔가 이상했다.
# 시간만 넣을라고 하니까 전부 쪼개져서 들어갔음
# -------------------------------------------------------------------------------- 2차원 리스트 돌리기
# 이거 개쩐다...!! 문제 6번 커뮤니티
# b = list(map(list,zip(*board)))