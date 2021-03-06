# -------------------------------------------------------------------------------- range
# generater의 한 종류
# a = [n for n in range(1000000)]
# b = range(1000000)

# 이 둘을 출력해보면 같은 값을 지니지만,
# 메모리 차이는 크게 차이난다.

# 전자는 실제로 메모리에 데이터를 할당하는 반면
# range의 경우 생성조건만 보관하고 있기 때문이다.
# 실제로 값이 1억으로 커지더라도 메모리 차이는 나지 않는다.

# -------------------------------------------------------------------------------- enumerate
# generater의 한 종류
# index와 value를 깔끔하게 처리

# 리스트 돌릴 때
# 인덱싱으로 돌릴까, 그냥 value값으로 돌릴까
# 은근 고민하고
# 때로는 잘못해서 되돌아가서 다시 선언하기도 하는데,
# 의외로 잘 사용하면 편할 듯하다!!!

# -------------------------------------------------------------------------------- divmod
# 이건 평소에도 잘 활용한다.
# 몫 구하는 //와
# 나머지 구하는 %를
# 합친 것.

# time,rest = divmod(num,depend)
# 이렇게 요긴하게 쓰는 중이다.

# -------------------------------------------------------------------------------- f-string
# 와 이건 안쓰니까 까먹을 뻔...
# 일반 문자열 앞에 f 넣어주고,
# 문자열 안에 중괄호로 감싼 원하는 변수 넣어주기

# name = 'young dong'
# name2 = 'subin'
# print(f'{name2} is {name}\'s favorite.')

# %를 활용하는 출력도 다시 보자

# -------------------------------------------------------------------------------- is와 ==
# is는 할당된 메모리 id 값을 비교한다.
# 알아만 두자

# a = [1,2,3,4,5]
# a.pop()

# if a is [1,2,3,4]:
#   print('yes')
# else:
#   print('no')


# ------------------------------------------- 