
# -------------------------------------------------------------------------- 소수점 관련 
#--------------------------------------- round 함수
# n = 0.5555555555
# m = 0.4444444444
# # 3번째에서 반올림해서 2번째까지 출력
# result = round(n,2)
# print(result)

#--------------------------------------- 올림,내림, 버림
# import math

# 올림
# math.ceil()
# 내림
# math.floor()
# 버림
# math.trunc()
# -------------------------------------------------------------------------- 사전 자료형
a = ['young','subin', 'kyumin', 'sangmin','ubin']
b = [1,2,3,4,5]
dic = {}
for i in range(len(a)):
  dic[a[i]] = b[i]
print(dic)

#--------------------------------------- key, value 리스트 만들기
print('-----------------------')
key_list = list(dic.keys())
value_list = list(dic.values())
key_value = list(dic.items())

print(key_list)
print(value_list)
print(key_value)

#--------------------------------------- key로  value 값 얻기
print('-----------------------')
print(dic['young'])
print(dic.get('sangmin'))
print(dic.get('ssssss', 'There is no sssss'))

#--------------------------------------- value에 특정 값 더하기
print('-----------------------')
dic['susu'] = 100
if 'susu' in dic:
  dic['susu'] += 100
else:
  dic['susu'] = 100

if 'young' in dic:
  dic['young'] += 99
else:
  dic['young'] = 100

print(dic)
#--------------------------------------- value에 특정 값 추가하기
print('-----------------------')

dic['friends'] = ['young']
dic['friends'].append('yesss')
dic['friends'].append(1)
dic['friends'].append(True)
print(dic)
  

