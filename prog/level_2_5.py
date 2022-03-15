# -------------------------------------------------------------------------------- 나 집합자료형에 대해선 아무것도 모르네...
# 그냥 set 함수가 어떻게 되는지만 알고 있다.
# 순서가 없고 중복이 불가능한 자료형
# 요소들 간 순서가 없어서 indexing이 불가능(Not iterable)
# 가변성(mutable)
# set()에서는 subscriptable이 허용되지 않는다. 즉, set은 각각의 요소에 접근이 불가능

# -------------------------------------------Set에서 사용하는 함수
# add(값) - 집합에 새로운 값을 추가한다. (중복된 값은 무시)

# remove(값) - 전달받은 값을 삭제 (없을 때 에러 메시지를 출력)

# discard(값) - 전달받은 값을 삭제 (없을 때 그냥 무시)

# clear() - 집합에 있는 모든 값을 삭제

# s = {1, 2, 3, 4, 5}
# s.add(6)
# -------------------
# s = {1, 2, 3, 4, 5, 6}	# 결과
# s.remove(7)	# Error
# s.discard(6)
# -------------------
# s = {1, 2, 3, 4, 5}	# 결과
# s.clear()
# -------------------
# s = {}	# 결과

# -------------------------------------------Set에서 사용하는 함수 2
# isdisjoint() - 두 집합이 공통 원소를 갖지 않는가?

# issubset() - 부분집합(subset)인가?

# issuperset() - 확대집합(superset)인가?

# → True or False 출력함

# union() - 합집합을 만들어 리턴

# update() - 합집합을 만들어 원본 데이터를 갱신(수정)

# difference() - 차집합을 만들어 리턴

# intersection() - 교집합을 만들어 리턴



# -------------------------------------------------------------------------------- Counter
# list 넣어주면 하나하나 센 다음에 집합 자료형 리턴
# 리턴된 집합자료형은 그대로 집합연산자 사용 가능하다.

# from collections import Counter


# a = [1,1,2,3,4,4,5]
# b = [1,2,3,4,4,6]
# c = Counter(a)
# d = Counter(b)
# print(c)
# print(d)

# andd = list((c & d).elements())
# orr = list((c | d).elements())
# diff = list((c - d).elements())
# xor = list(((c | d) - (c & d)).elements())
# print(andd)
# print(orr)
# print(diff)
# print(xor)

# -------------------------------------------------------------------------------- extend
# a = [1,2,3]
# a.extend([4,5])

# print(a)
# -------------------------------------------------------------------------------- 1. 후보키 실패!
# ------------------------------------------- 내꺼 접근법은 비슷한 듯 했으나 근처에도 가지 못했다!
# ------------------------------------------- 커뮤니티 뭔가 간단해보이는데 로직 자체도 뭔가 복잡하네... 
# from collections import deque
# from itertools import combinations

# def solution(relation):
#     n_row = len(relation)
#     n_col = len(relation[0])  

#     candidates=[]
#     for i in range(1,n_col+1):
#         candidates.extend(combinations(range(n_col),i))

#     final=[]
#     for keys in candidates:
#         tmp=[tuple([item[key] for key in keys]) for item in relation]
#         if len(set(tmp))==n_row:
#             final.append(keys)

#     answer=set(final[:])
#     for i in range(len(final)):
#         for j in range(i+1,len(final)):
#             if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
#                 answer.discard(final[j])
                
#     return len(answer)
    

# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

# -------------------------------------------------------------------------------- 2. 조이스틱 실패ㅋㅋㅋㅋ 뭐짘ㅋㅋ
# ------------------------------------------- 내꺼
#  아 갔다가 다시 돌아오는 경우가 있을 수 있다.
# def solution(name):
#     alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#     rev_name = name[::-1]
#     move_side_1 = 0
#     for i in range(len(name)):
#         if rev_name[i] != 'A':
#             move_side_1 = len(name)- i -1
#             break

#     move_side_2 = 0
#     for i in range(1,len(name)):
#         if name[i] != 'A':
#             move_side_2 = len(name)-i
#             break

#     move_side = min(move_side_1, move_side_2)

#     move_updown = 0
#     for i in name:
#         min_value = min(alpha.index(i), 26-alpha.index(i))
#         move_updown += min_value
    
#     return move_side + move_updown

# ------------------------------------------- 커뮤 이 코드가 이해가 안돼....ㅠ 자기 전에 다시 한번 보자!!
# def solution(name):
#     if set(name) == {'A'}:
#         return 0

#     answer = float('inf')
#     for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
#         left_moved = name[-i:]+name[:-i]
#         right_moved = name[i:]+name[:i]
#         for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
#             print(n)
#             while n and n[-1] == 'A':
#                 n = n[:-1]
#             print(n)

#             row_move = i + len(n)-1
#             col_move = 0
#             for c in map(ord, n):
#                 col_move += min(c - 65, 91 - c)

#             answer = min(answer, row_move + col_move)

#     return answer

# print(solution("JEROAA"))
# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("JAZ"))
# print(solution("SAUAVA"))
# print(solution("ZAAAZ"))
# print(solution("Z"))
# print(solution("A"))
# 내꺼는 이거 통과 못함
# print(solution("ABAAAAAAAAAABA"))

# -------------------------------------------------------------------------------- 3. 압축 1시간 컷ㅋㅋㅋ
# ------------------------------------------- 내꺼 뭔가 어거지로 만들긴 했는데 체계적이지 않다.
# 이런건 하다보면 느는건가??
# def solution(msg):
#     alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     dic = {}
#     for i in range(1,len(alpha)+1):
#         dic[alpha[i-1]] = i
    
#     answer = []
#     after = ''
#     i = 0
#     while i <= len(msg)-1:
#         push = msg[i]

#         after = ''
#         if i != len(msg)-1:
#             after = msg[i+1]
#             while push + after in dic.keys():
#                 push += after
#                 if i > len(msg)-3:
#                     after = ''
#                     i += 1
#                     break
#                 else:
#                     after = msg[i+2]
#                 i += 1
#             if push+after not in dic.keys():
#                 dic[push+after] = len(dic)+1
#         answer.append(dic[push])
#         i += 1

#     return answer

# ------------------------------------------- 커뮤니티 개 깔끔쓰...
# def solution(msg):
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     d = {}
#     for i in range(1,len(alpha)+1):
#         d[alpha[i-1]] = i

#     answer = []
#     while True:
#         if msg in d:
#             answer.append(d[msg])
#             break
#         for i in range(1, len(msg)+1):
#             if msg[0:i] not in d:
#                 answer.append(d[msg[0:i-1]])
#                 d[msg[0:i]] = len(d)+1
#                 msg = msg[i-1:]
#                 break

#     return answer
# print(solution('KAKAO'))
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))
# print(solution('ABABABABABABABAB'))

# -------------------------------------------------------------------------------- 4. [1차] 뉴스 클러스터링
# 자카드 유사도
# 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의
# 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
# ------------------------------------------- 내꺼 23분 남음
# from collections import Counter

# def solution(str1, str2):
#     str1_low = str1.lower()
#     str2_low = str2.lower()

#     str1_lst = []
#     str2_lst = []
    
#     for i in range(len(str1_low)-1):
#         if str1_low[i].isalpha() and str1_low[i+1].isalpha():
#             str1_lst.append(str1_low[i] + str1_low[i+1])
#     for j in range(len(str2_low)-1):
#         if str2_low[j].isalpha() and str2_low[j+1].isalpha():
#             str2_lst.append(str2_low[j] + str2_low[j+1])

#     Counter1 = Counter(str1_lst)
#     Counter2 = Counter(str2_lst)

    
#     inter = list((Counter1 & Counter2).elements())
#     union = list((Counter1 | Counter2).elements())

#     if len(union) == 0 and len(inter) == 0:
#         return 65536
#     else:
#         return int(len(inter) / len(union) * 65536)
    
# print(solution('FRANCE', 'french'))
# print(solution('handshake', 'shake hands'))
# print(solution('aa1+aa2', 'AAAA12'))
# print(solution('E=M*C^2', 'e=m*c^2'))

# -------------------------------------------------------------------------------- 5. 수식 최대화
# ------------------------------------------- 내꺼
def solution(expression):
    answer = 0
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))