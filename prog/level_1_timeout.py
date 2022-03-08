# -------------------------------------------------------------------------------- replace 적용 안됨 이유는?
# def solution(s):
#   words = s.split(' ')
#   for word in words:
#     for i in range(len(word)):
#       if (i+1)%2 == 0:
#         word.replace(word[i], word[i].upper())
#         print(word)
#       else:
#         print(word[i])
#         word.replace(word[i], word[i].lower())
#     print(word)

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



# -------------------------------------------------------------------------------- 1. 로또의 최고 순위와 최저 순위 8분 컷!
# ------------------------------------------- 내꺼
# def a(x):
#   if 7-x >= 6:
#     return 6
#   else:
#     return 7-x

# def solution(lottos, win_nums):
#   count_0 = 0
#   count_match = 0
#   for i in lottos:
#     if i == 0:
#       count_0 += 1
#     elif i in win_nums:
#       count_match += 1
#   best = count_0 + count_match
#   return [a(best),a(count_match)]

# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

# -------------------------------------------------------------------------------- 2. 소수 만들기 8분 컷!
# ------------------------------------------- 내꺼
# from itertools import combinations
# from math import sqrt

# def prime_num(n):
#   for i in range(2,int(sqrt(n))+1):
#     if n%i == 0:
#       return False
#   return True

# def solution(num):
#   count = 0
#   candidates = list(combinations(num, 3))
#   for candidate in candidates:
#     summ = sum(candidate)
#     if prime_num(summ):
#       count += 1
#   return count


# print(solution([1,2,3,4]))
# print(solution([1,2,7,6,4]))
# -------------------------------------------------------------------------------- 3. 약수의 개수와 덧셈 4분 컷!
# ------------------------------------------- 내꺼
# from math import sqrt

# def solution(left, right):
#   answer = 0
#   for i in range(left, right+1):
#     if sqrt(i).is_integer():
#       answer -= i
#     else:
#       answer += i
#   return answer

# print(solution(13, 17))
# print(solution(24, 27))

# -------------------------------------------------------------------------------- 4. 부족한 금액 계산하기 6분 컷!
# ------------------------------------------- 내꺼
# def solution(price, money, count):
#   i = 1
#   total_price = 0
#   while i < count+1:
#     total_price += price * i
#     i+= 1
#   if money >= total_price:
#     return 0
#   else:
#     return total_price - money

# print(solution(3,20,4))
# -------------------------------------------------------------------------------- 5. 이상한 문자 만들기 12분 컷!
# ------------------------------------------- 내꺼
# def solution(s):
#   words = s.split(' ')
#   answer = []
#   for word in words:
#     word = list(word)
#     for i in range(len(word)):
#       if (i+1)%2 == 0:
#         word[i] = word[i].lower()
#       else:
#         word[i] = word[i].upper()
#     answer.append(''.join(word)) 
#   return ' '.join(answer)

# print(solution("try hello world"))

# -------------------------------------------------------------------------------- 6. 예산 6분 컷!
#  최대한 많은 부서
# ------------------------------------------- 내꺼
# def solution(d, budget):
#   d.sort()
#   support = 0
#   count = 0
#   for i in d:
#     support += i
#     if support > budget:
#       break
#     count += 1 
#   return count

# print(solution([1,3,2,5,4], 9))
# print(solution([2,2,3,3], 10))

# -------------------------------------------------------------------------------- 7. 숫자 문자열과 영단어 8분 컷!
# ------------------------------------------- 내꺼
# def solution(s):
#   alpha = ["zero", 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#   answer = ''
#   word = ''
#   for i in s:
#     if i.isdigit():
#       answer += i
#     else:
#       word += i
#       if word in alpha:
#         alpha_index = alpha.index(word)
#         answer += str(alpha_index)
#         word = ''
#   return int(answer)


# print(solution("one4seveneight"))
# print(solution("23four5six7"))
# print(solution("2three45sixseven"))
# print(solution("123"))

# -------------------------------------------------------------------------------- 8. 신규 아이디 추천
# ------------------------------------------- 내꺼

# -------------------------------------------------------------------------------- 9. 2016년 11분 컷!
# ------------------------------------------- 내꺼
# def solution(a, b):
#   days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
#   month = [31,29,31,30,31,30,31,31,30,31,30,31]
#   total = b
#   for i in range(a-1):
#     total += month[i]
#   index = (5 + total)%7 -1
#   return days[index]

# print(solution(5,24))

# -------------------------------------------------------------------------------- 10. [1차] 비밀지도 16분 컷!
# ------------------------------------------- 내꺼
# def solution(n, arr1, arr2):
#   graph = []
#   for i,j in zip(arr1, arr2):
#     answer_s = ''
#     for a,b in zip(bin(i)[2:].rjust(n,'0'), bin(j)[2:].rjust(n,'0')):
#       if a == '0' and b == '0':
#         answer_s += ' '
#       else:
#         answer_s += '#'
#     graph.append(answer_s)

#   return graph

# print(solution(5,[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

# -------------------------------------------------------------------------------- 11. 시저암호 - 시간 초과 
# ------------------------------------------- 내꺼 좀 더럽긴 해 그래도 
# def solution(s, n):
#   answer = ''
#   for i in s:
#     if i.isalpha():
#       if i.isupper():
#         ord_i = ord(i) + n
#         if ord_i > 90:
#           ord_i -= 26
#         chr_i = chr(ord_i)
#         answer += chr_i
#       else:
#         ord_i = ord(i) + n
#         if ord_i > 122:
#           ord_i -= 26
#         chr_i = chr(ord_i)
#         answer += chr_i
#     else:
#       answer += i
#   return answer


# print(solution("AB",1))
# print(solution('z', 1))
# print(solution("a B z",	4))
# a = 'z'
# print(ord(a))

# -------------------------------------------------------------------------------- 12. 폰켓몬 9분 컷!
# ------------------------------------------- 내꺼
# def solution(nums):
#   set_num = len(set(nums))
#   take_num = len(nums)//2
#   return min(set_num, take_num)

# print(solution([3,1,2,3]))
# print(solution([3,3,3,2,2,4]))
# print(solution([3,3,3,2,2,2]))