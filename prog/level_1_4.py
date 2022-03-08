# -------------------------------------------------------------------------------- 1. 예산
# ------------------------------------------- 내꺼 13분 컷!
# def solution(d, budget):
#   d.sort()
#   count = 0
#   for i in d:
#     budget -= i
#     if budget < 0:
#       return count
#     elif budget == 0:
#       return count + 1
#     else:
#       count += 1
#   return count

# # 전부 가능, 전부 불가
# print(solution([1,1,1,1],9))
# print(solution([10,11,12,13], 9))
# print(solution([1,3,2,5,4], 9))
# print(solution([2,2,3,3], 10))

# -------------------------------------------------------------------------------- 2. 두개 뽑아서 더하기
# 테스트 케이스에 음수가 있었데...노어이
# ------------------------------------------- 내꺼 5분 컷 - set에 대해서!
# from itertools import combinations

# def solution(numbers):
#   candidates = list(combinations(numbers,2))
#   answer = []
#   for candidate in candidates:
#     answer.append(sum(candidate))
#   return sorted(list(set(answer)))

# print(solution([2,1,3,4,-7]))
# print(solution([2,1,3,4,1]))
# print(solution([5,0,2,7]))

# -------------------------------------------------------------------------------- 3. 나누어 떨어지는 배열
# ------------------------------------------- 내꺼 3분 컷!
# def solution(arr, divisor):
#   answer = []
#   for i in arr:
#     if i % divisor == 0:
#       answer.append(i)
#   answer.sort()
#   if len(answer) == 0:
#     answer.append(-1)
#   return answer

# print(solution([5, 9, 7, 10], 5))
# print(solution([2, 36, 1, 3], 1))
# print(solution([3,2,6], 10))

# -------------------------------------------------------------------------------- 4. 음양 더하기
# ------------------------------------------- 내꺼 2분 컷!
# def solution(absolutes, signs):
#   answer = []
#   for i, j in zip(absolutes, signs):
#     if j == True:
#       answer.append(i)
#     else:
#       answer.append(-i)
#   return sum(answer)

# print(solution([4,7,12], [True,False,True]))
# print(solution([1,2,3], [False,False,True]))

# -------------------------------------------------------------------------------- 5. 키패드 누르기 
# ------------------------------------------- 내꺼 32분 컷! 기쁘다!
# def dist(dic, l_hand_posi,r_hand_posi, target, prefer):

#   l_to_traget = abs(dic[target][0] - dic[l_hand_posi][0]) + abs(dic[target][1] - dic[l_hand_posi][1])
#   r_to_target = abs(dic[target][0] - dic[r_hand_posi][0]) + abs(dic[target][1] - dic[r_hand_posi][1])

#   answer = ''
#   if l_to_traget > r_to_target:
#     answer = 'R'
#     r_hand_posi = target
#   elif l_to_traget < r_to_target:
#     answer = 'L'
#     l_hand_posi = target
#   else:
#     if prefer == 'right':
#       answer = 'R'
#       r_hand_posi = target
#     else:
#       answer = 'L'
#       l_hand_posi = target

#   return answer, l_hand_posi, r_hand_posi


# def solution(numbers, hand):
#   dic = {
#     '1':[0,0],
#     '2':[0,1],
#     '3':[0,2],
#     '4':[1,0],
#     '5':[1,1],
#     '6':[1,2],
#     '7':[2,0],
#     '8':[2,1],
#     '9':[2,2],
#     '*':[3,0],
#     '0':[3,1],
#     '#':[3,2],
#     }

#   left_n = ['1','4','7']
#   right_n = ['3','6','9']
#   l_hand_posi = '*'
#   r_hand_posi = '#'

#   answer = ''
#   for i in numbers:
#     i = str(i)
#     if i in left_n:
#       answer += 'L'
#       l_hand_posi = i
#     elif i in right_n:
#       answer += 'R'
#       r_hand_posi = i
#     else:
#       answer_s, l_hand_posi, r_hand_posi = dist(dic,l_hand_posi, r_hand_posi, i, hand)
#       answer += answer_s

#   return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))

# -------------------------------------------------------------------------------- 6. 나머지가 1이 되는 수 찾기
# ------------------------------------------- 내꺼 5분 컷!
# def solution(n):
#   for i in range(1,n):
#     if n%i == 1:
#       return i

# print(solution(10))
# print(solution(12))

# -------------------------------------------------------------------------------- 7. 자연수 뒤집어 배열로 만들기
# ------------------------------------------- 내꺼 5분 컷!
# def solution(n):
#   a = list(map(int,str(n)))
#   a.reverse()
#   return a

# print(solution(12345))

# -------------------------------------------------------------------------------- 8. 정수 내림차순으로 배치하기
# ------------------------------------------- 내꺼 3분 컷!
# def solution(n):
#   n = list(str(int(n)))
#   n.sort(reverse=True)
#   return int(''.join(n))

# print(solution(10019))
# print(solution(1))
# print(solution(801030501))

# -------------------------------------------------------------------------------- 9. 숫자 문자열과 영단어
# ------------------------------------------- 내꺼
# def solution(s):
#   number = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#   answer = ''
#   word = ''
#   for i in s:
#     if i.isdigit():
#       answer += (word + i)
#       word = ''
#       continue
#     word += i
#     if word in number:
#       num = number.index(word)
#       answer += str(num)
#       word = ''
#   return int(answer)

# ------------------------------------------- 커뮤니티 익숙한 리스트에만 의존하지 말고 dic이나 다른 자료형들을 시도해보자.
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)


# print(solution("one4seveneight"))
# print(solution("23four5six7"))
# print(solution("2three45sixseven"))
# print(solution("123"))

# -------------------------------------------------------------------------------- 10. 신규 아이디 추천
# 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발
# 3자 이상 15자 이하
# 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용
# 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없다.

# ------------------------------------------- 내꺼 성능은 내꺼가 좀 더 좋긴한데 뭔가 너무 지저분해. 그리고 미친듯한 시간초과ㅋㅋ거의 1시간 반 동안 풀었음
# ------------------------------------------- 커뮤니티
# def solution(new_id):
#     answer = ''
#     # 1
#     new_id = new_id.lower()
#     # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
#     # 5
#     if answer == '':
#         answer = 'a'
#     # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7
#     while len(answer) < 3:
#         answer += answer[-1]
#     return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution(	"z-+.^."))
# print(solution(	"=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
# print(solution("..."))
# print(solution(".b."))
