# -------------------------------------------------------------------------------- 1. 로또의 최고 순위와 최저 순위 8분 컷!
# ------------------------------------------- 내꺼 3번째 7분 컷!
# def solution(lottos, win_nums):
#   change = lottos.count(0)
#   match = 0
#   for i in lottos:
#     if i in win_nums:
#       match += 1
#   max_match = change + match

#   answer = [get_order(max_match),get_order(match)]
#   return answer

# def get_order(match):
#   if match <1:
#     order = 6
#   else:
#     order = 7- match

#   return order

# print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
# print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
# print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))

# -------------------------------------------------------------------------------- 2. 소수 만들기 8분 컷!
# ------------------------------------------- 내꺼 3번째 7분 컷!
# from math import sqrt
# from itertools import combinations


# def solution(nums):
#   answer = 0
#   combis = list(combinations(nums,3))
#   for combi in combis:
#     if prime_num(sum(combi)):
#       answer += 1
#   return answer


# def prime_num(n):
#   if n in [0,1]:
#     return False
#   for i in range(2,int(sqrt(n))+1):
#     if n % i == 0:
#       return False
#   return True

# print(solution([1,2,3,4]))
# print(solution([1,2,7,6,4]))

# -------------------------------------------------------------------------------- 3. 약수의 개수와 덧셈 4분 컷!
# ------------------------------------------- 내꺼 3번째 2분 컷!
# from math import sqrt


# def solution(left, right):
#   answer = 0
#   for i in range(left,right + 1):
#     if sqrt(i) == int(sqrt(i)):
#       answer -= i
#     else:
#       answer += i

#   return answer

# print(solution(13,17))
# print(solution(24,27))


# -------------------------------------------------------------------------------- 4. 부족한 금액 계산하기 6분 컷!
# ------------------------------------------- 내꺼 3번째 4분 컷!
# def solution(price, money, count):
#   cost = 0
#   for i in range(count+1):
#     cost += price*i
#   if money > cost:
#     answer = 0
#   else:
#     answer = cost-money
#   return answer

# print(solution(3,20,4))

# -------------------------------------------------------------------------------- 5. 이상한 문자 만들기 12분 컷!
# ------------------------------------------- 내꺼 3번째 9분 컷!
# def solution(s):
#   words = s.split(' ')
#   answer = []
#   for word in words:
#     word = list(word)
#     for i in range(len(word)):
#       # 홀수라면
#       if (i+1)%2 == 0:
#         word[i] = word[i].lower()
#       else:
#         word[i] = word[i].upper()
#     answer.append(''.join(word))
#   return ' '.join(answer)

# print(solution("try hello world"))

# -------------------------------------------------------------------------------- 6. 예산 6분 컷!
#  최대한 많은 부서
# ------------------------------------------- 내꺼 3번째 2분 컷!
# def solution(d, budget):
#   d.sort()
#   answer = 0
#   for i in d:
#     if budget-i >= 0:
#       budget -= i
#       answer += 1
#   return answer

# print(solution([1,3,2,5,4],9))
# print(solution([2,2,3,3],10))


# -------------------------------------------------------------------------------- 7. 숫자 문자열과 영단어 8분 컷!
# ------------------------------------------- 내꺼 3번째 7분 컷!
# def solution(s):
#   dic = {'zero': 0, 'one':1, 'two':2, 'three':3, 'four': 4, 'five': 5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
#   answer = ''
#   tmp = ''
#   for i in s:
#     if i.isdigit():
#       answer += i
#     elif i.isalpha():
#       tmp += i
#     if tmp in dic.keys():
#       a = dic[tmp]
#       answer += str(a)
#       tmp = ''

#   return int(answer)

# print(solution("one4seveneight"))
# print(solution("23four5six7"))
# print(solution("2three45sixseven"))
# print(solution("123"))

# -------------------------------------------------------------------------------- 8. 신규 아이디 추천
  # # 이거 왜 안되지??
  # print(answer[:1])
  # if answer[:1] == '.':
  #   answer.pop(0)
  # print(answer)
# ------------------------------------------- 내꺼 3번째 22분 컷!
# def solution(new_id):
#   answer = ''
#   for i in new_id:
#     if i.isupper():
#       answer += i.lower()
#     elif i.isdigit() or i.isalpha() or i in ['_','-','.']:
#       if len(answer) >0 and i == '.' and answer[-1] == '.':
#         continue
#       else:
#         answer += i

#   answer = list(answer)

#   if len(answer) > 0: 
#     if answer[-1] == '.':
#       answer.pop()
#   if len(answer) > 0: 
#     if answer[0] == '.':
#       answer.pop(0)
  
#   if answer == []:
#       answer += 'a'

#   if len(answer) > 15:
#     answer = answer[:15]
#     if answer[-1] != '.':
#       answer.pop()

#   if len(answer) <=2:
#     while len(answer)<3:
#       answer.append(answer[-1])

#   return ''.join(answer)


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))

# -------------------------------------------------------------------------------- 9. 2016년 11분 컷!
# ------------------------------------------- 내꺼 12분 컷!
# def solution(a, b):
#   days = ['SUN','MON','TUE','WED', 'THU','FRI','SAT']
#   month = [31,29,31,30,31,30,31,31,30,31,30,31]
#   count = 4
#   count += sum(month[:a-1])
#   count += b
#   index = count % 7

#   return days[index]

# print(solution(1,1))
# print(solution(5,24))

# -------------------------------------------------------------------------------- 10. [1차] 비밀지도 16분 컷!
# ------------------------------------------- 내꺼 3번째 15분 컷!!
# def solution(n, arr1, arr2):
#   answer = []
#   for i,j in zip(arr1,arr2):
#     merged = bin(i | j)[2:]
#     merged = merged.rjust(n,'0')
#     # print(merged)
#     tmp = ''
#     for i in merged:
#       if i == '1':
#         tmp += '#'
#       else:
#         tmp += ' '
#     answer.append(tmp)
#   return answer

# print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))

# -------------------------------------------------------------------------------- 11. 시저암호 - 시간 초과 
# ------------------------------------------- 내꺼 3번째 14분 컷!
# def solution(s, n):
#   answer = ''
#   for i in s:
#     if i.isalpha():
#       data = ord(i)
#       if 65 <= data <= 90:
#         after = data+n
#         if  after >90:
#           after -=26

#       elif 97 <= data <= 122: 
#         after = data+n
#         if  after >122:
#           after -=26
#       answer += chr(after)
#     else:
#       answer += i
#   return answer

# print(solution("AB",1))
# print(solution("z",1))
# print(solution("a B z",4))

# -------------------------------------------------------------------------------- 12. 폰켓몬 9분 컷!
# ------------------------------------------- 내꺼 3번째 5분 컷!
# def solution(nums):
#   sorted_nums = list(set(nums))
#   return min(len(nums)//2, len(sorted_nums))


# print(solution([3,1,2,3]))
# print(solution([3,3,3,2,2,4]))
# print(solution([3,3,3,2,2,2]))