
# -------------------------------------------------------------------------- 소수점 관련 
#--------------------------------------- round 함수
# n = 0.5555555555
# m = 0.4444444444
# # 3번째에서 반올림해서 2번째까지 출력
# result = round(n,2)
# print(result)

# #--------------------------------------- 올림, 내림, 버림
# import math

# ceil = math.ceil(n)
# floor = math.floor(n)
# trunc = math.trunc(n)
# print(ceil)
# print(floor)
# print(trunc)
# -------------------------------------------------------------------------- 사전 자료형
# a = ['young','subin', 'kyumin', 'sangmin','ubin']
# b = [1,2,3,4,5]
# dic = {}
# for i in range(len(a)):
#   dic[a[i]] = b[i]
# print(dic)

# #--------------------------------------- key, value 리스트 만들기
# print('-----------------------')
# key_list = list(dic.keys())
# value_list = list(dic.values())
# key_value = list(dic.items())

# print(key_list)
# print(value_list)
# print(key_value)

# #--------------------------------------- key로 value 값 얻기  dic.get 함수
# print('-----------------------')
# print(dic['young'])
# print(dic.get('sangmin'))
# print(dic.get('ssssss', 'There is no sssss'))

# #--------------------------------------- value에 특정 값 더하기
# print('-----------------------')
# dic['susu'] = 100
# if 'susu' in dic:
#   dic['susu'] += 100
# else:
#   dic['susu'] = 100

# if 'young' in dic:
#   dic['young'] += 99
# else:
#   dic['young'] = 100

# print(dic)
#--------------------------------------- value에 특정 값 추가, 삭제하기
# print('-----------------------')
# dic = {}
# dic['friends'] = ['young']
# dic['friends'].append('yesss')
# dic['friends'].append(1)
# dic['friends'].append(True)
# print(dic)
# dic['friends'].pop(0)
# print(dic)
# dic['friends'].pop(2)
# print(dic)
# --------------------------------------- value에 여러 값 있다면 정렬하기
# 당연하게 서로 타입이 다르면 불가능
# print('-----------------------')
# dic = {}
# dic['friends'] = ['aaa']
# dic['friends'].append('abc')
# dic['friends'].append('acd')
# dic['friends'].append('b')
# print(dic)
# dic['friends'].sort(reverse=True)
# print(dic)

# -------------------------------------------------------------------------------- collections.defaultdict
# https://www.daleseo.com/python-collections-defaultdict/
# from collections import defaultdict

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# a = defaultdict(list)
# for ticket in tickets:
#     a[ticket[0]].append(ticket[1])

# # defaultdict 안썼을 때
# b = {}
# for i in range(len(tickets)):
#     if tickets[i][0] in b.keys():
#         b[tickets[i][0]].append(tickets[i][1])
#     else:
#         b[tickets[i][0]] = [tickets[i][1]]

# print(a)
# print(a["ICN"].pop(0))
# print(a)

# print(b)
# print(b["ICN"].pop(1))
# print(b)

# # 숫자 넣을 때
# word = 'abcda'
# def countLetters(word):
#     counter = defaultdict(int)
#     for letter in word:
#         counter[letter] += 1
#     return counter

# print(countLetters(word))

# -------------------------------------------------------------------------------- divmod
# 몫과 나머지를 튜플로 묶어서 return
# a = 6
# b = 3
# c,d = divmod(a, b)
# -------------------------------------------------------------------------------- array[::-1]
# 거꾸로 만들기
# a = [1,2,3,4,5]
# print(a[::-1])
# -------------------------------------------------------------------------------- 문자열.rjust(전체 자리 숫자, 공백을 채울 텍스트)
# a = 'young dong'
# b = 'su bin'
# c = 'sang min'
# print(a.rjust(12,'0'))
# print(a.rjust(10,'0'))
# print(b.rjust(10,'0'))
# print(c.rjust(10,'0'))

# 문자열.ljust(전체 자리 숫자, 공백을 채울 텍스트)
# print(a.ljust(10,'0'))
# print(b.ljust(10,'0'))
# print(c.ljust(10,'0'))

# -------------------------------------------------------------------------------- 문자열.replace("찾을값", "바꿀값", [바꿀횟수])
# a = "abcdabcda"
# print(a.replace('a', '0'))
# print(a.replace('a', '0', 1))
# print(a.replace('a', '0', 2))

# 거꾸로 쌉가능
# b = a[::-1].replace('a', '0', 2)
# print(b[::-1])

# -------------------------------------------------------------------------------- 진수와 비트연산자
# # 10진수를 2진수로
# a = 38
# b_a = bin(a)
# # print(f'type is {type(b_a)}')
# # 2진수 문자열을 10진수로
# # print(int(b_a,2))

# b = 13
# a_and_b = bin(a&b)
# a_or_b = bin(a|b)
# a_xor_b = bin(a^b)
# a_not_b = bin(~a)

# print(b_a)
# print(a_and_b)
# print(a_or_b)
# print(a_xor_b)
# print(a_not_b)
# print(int(a_and_b, 2))
# print(int(a_or_b, 2))
# print(int(a_xor_b, 2))
# print(int(a_not_b, 2))

# -------------------------------------------------------------------------------- chr(), ord()
# a = 'a'
# A = 'A'
# ord_a = ord(a)
# ord_A = ord(A)
# print(ord_a)
# print(ord_A)
# chr_a = chr(ord_a)
# chr_A = chr(ord_A)
# print(chr_a)
# print(chr_A)

# -------------------------------------------------------------------------------- 문자열 슬라이싱 뭐든 가능!
# a = 'asdfasdf'
# for i in a:
#   print(i)
# for i in range(len(a)):
#   print(a[i])
# print(a[1:-1])
# print(a[::-1])

# -------------------------------------------------------------------------------- set에 대해
# set은 중복된 값을 없애주고 오름차순 정렬을 해주지만, 음수는 정렬이 적용되지 않는다.

# -------------------------------------------------------------------------------- 대문자 만들기
# string.upper()
# string.capitalize()
# string.title()
# -------------------------------------------------------------------------------- 진법 변환
# https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95
# -------------------------------------------------------------------------------- array.index()
# a = [1,2,3,'kim', 63]
# print(a.index('kim'))

# -------------------------------------------------------------------------------- strip()
# -------------------------------------------------------------------------------- '구분자'.join()
# -------------------------------------------------------------------------------- 문자열 더하기, 곱하기 등등
# -------------------------------------------------------------------------------- 유클리드 호제법
# https://binaryjourney.tistory.com/93

# -------------------------------------------------------------------------------- list.title()
# def solution(s):
#   return s.title()

# print(solution("3people unFollowed me"))
# print(solution("for the last week"))
# -------------------------------------------------------------------------------- ''.join(array)
# a = ['1','2','3','4']
# print(' '.join(a))
# print('!'.join(a))
# -------------------------------------------------------------------------------- 백트랙킹
# https://chanhuiseok.github.io/posts/algo-23/
