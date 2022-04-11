#-------------------------------------------------------------------------- 파이썬의 큰 수에 대해 
# https://ahracho.github.io/posts/python/2017-05-09-python-integer-overflow/
# 다른 언어는 너무 큰수는 메모리의 한계 때문에 에러가 난다.
# 파이썬은 에러가 나지 않는다.
# 파이썬에는 오버플로우가 없다
# 파이썬 2에서는 정수형 데이터 타입이 int와 long 두 가지가 있었는데, int는 C에서의 그것과 같은 4바이트 데이터형이고, 
# long은 arbitrary precision을 따르는 데이터형이다.
# 그래서 int 타입 변수의 값이 표현 범위를 넘어서게 되면 자동으로 long으로 타입 변경이 되는 형식이었다.

# 파이썬 3에서는 long 타입이 없어지고 int 타입만 남았는데,
# 이 int가 arbitrary precision을 지원하여 오버플로우가 발생하지 않게 되었다.

# arbitrary precision란?
# 사용할 수 있는 메모리양이 정해져 있는 기존의 fixed-precision과 달리,
# 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태

# 기본 28바이트를 사용하다 이를 넘어가면 4바이트씩 증가하면서 수 표현에 사용하는 바이트 수가 탄력적으로 늘어난다.

#-------------------------------------------------------------------------- Counter
# from collections import Counter
# array = [1,2,4,4,4,6,7,8,8,8,8,8,9,10]
# k = 3
# # 각 문자열에 대한 갯수를 사전 집합자료가 담긴 클래스 형태로 출력
# count1 = Counter(array)
# # 각 문자열에 대한 갯수를 많은 순서대로 k개만큼 출력
# # tuple 형태로 담긴 list (a, b) = a가 b개 있다.
# count2 = Counter(array).most_common(k)

# print(count1)
# print(count2)

# -------------------------------------------------------------------------------- list.replace(key, value)
# -------------------------------------------------------------------------------- lower, upper
# upper, lower등은 type만 string이면 굳이 알파벳에 안걸어줘도 에러가 나지 않는다
# -------------------------------------------------------------------------------- str 관련 에러
# 'str' object does not support item assignment

# 문자열 변환은 문자열 변환으로 끝내자. 리스트로 바꿔서 해결하지 말고!!
# 문자열 슬라이싱이랑 replace 등으로 충분히 할 수 있다!!
# replace에 대해서 좀 더 알아보자
# index도 가능한가?? 그럼 인덱스 함수도?? 응 전부 가능
# 안되는 건 지금까지 단 하나 item assignment
# ex) a[3] = 'd'

# -------------------------------------------------------------------------------- replace 적용 안됨 이유는?
# 인덱싱을 사용하지 않는 이상
# 반복문 안에서 변화는 적용되지 않는다.
# 지금에서야 보면 당연한 것.
# def solution(s):
#   words = s.split(' ')
#   print(words)
#   for word in words:
#     for i in range(len(word)):
#       if (i+1)%2 == 0:
#         word.replace(word[i], word[i].upper())
#       else:
#         word.replace(word[i], word[i].lower())
#   print(words)
# solution(a)

# 리스트로 변환해서 해결
# def solution(s):
#   words = list(s)
#   for i in range(len(words)):
#     if (i+1)%2 == 0:
#       words[i] = words[i].upper()
#     else:
#       words[i] = words[i].lower()
#   print(words)
# solution(a)


# 리스트 변환 없이 해결할 수 있는가?
# 없는듯?

# -------------------------------------------------------------------------------- isalpha, isupper, islower
# a = '1aA^?'
# for i in a:
#   if i.isupper():
#     print('im upper', i)
#   if i.islower():
#     print('im lower', i)
#   if i.isalpha():
#     print('im alpha', i)
#   if i.isdigit():
#     print('im digit', i)

# # upper(), lower() 얘네들은 str 타입이기만 하면 알아서 걸르면서 적용됨.
# print(a.upper())
# 하나하나 확인할 필요 없이 문자열 전체 한꺼번에 확인도 가능
# a = 'abwdk'
# b = 'abwdk8'
# print(a.isalpha())
# print(b.isdigit())

# -------------------------------------------------------------------------------- 비트연산자!!!!
# 비밀지도 문제에서 사용하면 매우 좋다.

# -------------------------------------------------------------------------------- array[-1:]
# IndexError: list index out of range
# 리스트에 값이 있거나 없을 수도 있을 경우,
# 마지막 값을 조회할 때 사용

# 기본적인 인덱싱이면 빈 리스트일 경우 에러가 난다.
#그러나 이 방법은 에러 생기지 않음

# array = [1,2,4,6,3,2,6,4]
# # array = []
# print(array[-1:])
# print(array[:1])

# -------------------------------------------------------------------------------- reverse(), reversed()
# 문자열 추가 가능?
# 리턴되는 값은?
# answer = 'hello budddy'
# reversed_answer = "".join(reversed(answer))
# print(reversed_answer)

# -------------------------------------------------------------------------------- 진수 변환
# def make(n):
#     rev_base = ''
#     while n > 0:
#         n, mod = divmod(n, 3)
#         rev_base += str(mod)
#     return rev_base 
