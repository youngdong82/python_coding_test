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
# 완전탐색???
# ------------------------------------------- 커뮤
# from itertools import permutations

# def operation(num1,num2,op):
#     if op == '*':
#         return str(int(num1) * int(num2))
#     if op == '+':
#         return str(int(num1) + int(num2))
#     if op == '-':
#         return str(int(num1) - int(num2))


# def calc(expression, op):
#     string = []
#     tmp = ''
#     for i in expression:
#         if i.isdigit():
#             tmp += i
#         else:
#             string.append(tmp)
#             string.append(i)
#             tmp = ''
#     string.append(tmp)

#     for o in op:
#         stack = []
#         while len(string) != 0:
#             tmp = string.pop(0)
#             if tmp == o:
#                 stack.append(operation(stack.pop(), string.pop(0), o))
#             else:
#                 stack.append(tmp)
#         string = stack

#     return abs(int(string[0]))


# def solution(expression):
#     op = list(permutations(['*','+','-'], 3))
#     result = []
#     for i in op:
#         result.append(calc(expression, i))
#     return max(result)


# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

# -------------------------------------------------------------------------------- 6. 쿼드압축 후 개수 세기
# 재귀함수
# ------------------------------------------- 커뮤 간단해보이는데 굉장히 짜임새 있게 잘 짜여있다...
# def solution(arr):
#     result=[0,0]
#     length=len(arr)
    
#     def compression(a,b,l):
#         # 더이상 나뉠 수 없더라도 start와 해당 값이 비교됨으로써 자체적으로 재귀함수가 종료된다.
#         start = arr[a][b]
#         for i in range(a,a+l):
#             for j in range(b,b+l):
#                 if arr[i][j] != start:
#                     l=l//2
#                     compression(a,b,l)
#                     compression(a,b+l,l)
#                     compression(a+l,b,l)
#                     compression(a+l,b+l,l)
#                     return
#         # 2중 for문이 새로운 함수를 부르지 않고 정상적으로 끝난다면,
#         # = 범위 내 값이 전부 같다면
#         result[start] += 1
        
#     compression(0,0,length)
    
#     return (result)


# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))

# -------------------------------------------------------------------------------- 7. 캐시 17분 컷!!!
#  게시물을 가져오는 부분의 실행시간이 너무 오래 걸린
#  캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황
#  캐시 크기 <= 30
#  최대 도시 수는 100,000
#  도시 이름은 최대 20자
#  "총 실행시간"을 출력
# ------------------------------------------- 내꺼
# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return len(cities) * 5
#     cach = []
#     answer = 0
#     for city in cities:
#         city = city.lower()
#         if city in cach:
#             answer += 1
#             cach.remove(city)
#             cach.append(city)
#         else:
#             answer += 5
#             if len(cach) == cacheSize:
#                 cach.pop(0)
#             cach.append(city)
#     return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# -------------------------------------------------------------------------------- 8. 빛의 경로 실패!! 담에 다시 풀어보자
# ------------------------------------------- 내꺼 루프로 변경해보라고....? 못해 ㅅㅂ...
# dx = [1,0,-1,0]
# dy = [0,-1,0,1]

# def solution(grid):
#     grid = list(map(str,grid))
#     answer = []
#     answer_detail = []

#     x = 0
#     y = 0

#     def dfs(x,y,cicle,index):
#         if (x,y,index) in cicle:
#             return
#         cicle.append((x,y,index))
        
#         nx = x + dx[index]
#         ny = y + dy[index]

#         if nx < 0:
#             nx = (len(grid)-1)
#         elif nx >= len(grid):
#             nx = 0

#         if ny < 0:
#             ny = len(grid[0])-1
#         elif ny >= len(grid[0]):
#             ny = 0

#         if grid[nx][ny] == 'S':
#             dfs(nx,ny,cicle,index)
#         elif grid[nx][ny] == 'R':
#             dfs(nx,ny,cicle,(index +1)%4)
#         elif grid[nx][ny] == 'L':
#             dfs(nx,ny,cicle,(index -1)%4)
    
#     for i in range(4):
#         circle = []
#         index = i
#         dfs(x,y,circle,index)

#         if set(circle) not in answer_detail:
#             answer.append(len(circle))
#             answer_detail.append(set(circle))

#     answer.sort()
#     return answer


# print(solution(["SL","LR"]))
# print(solution(["S"]))
# print(solution(["R","R"]))

# -------------------------------------------------------------------------------- 9. 올바른 괄호 3분 컷!
# ------------------------------------------- 내꺼
# def solution(s):
#     result = 0
#     for i in s:
#         if result < 0:
#             return False
#         if i == '(':
#             result += 1
#         else:
#             result -= 1
#     if result == 0:
#         return True
#     else:
#         return False

# print(solution("()()"))
# print(solution("(())()"))
# print(solution(")()("))
# print(solution("(()("))

# -------------------------------------------------------------------------------- 10. [3차] 방금그곡
# 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다.
# 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다.
# 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교

# 재생된 시간이 제일 긴 음악 제목을 반환
# 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
# ------------------------------------------- 내꺼
# def solution(m, musicinfos):
#     change = {'C#': 'c', 'D#': 'd', 'E#': 'e', 'F#': 'f', 'G#': 'g', 'A#': 'a', 'B#': 'b'}

#     for rm in change.keys():
#         m = m.replace(rm, change[rm])

#     splited = []
#     for i in musicinfos:
#         splited_s = i.split(',')
#         for rm in change.keys():
#             splited_s[-1] = splited_s[-1].replace(rm, change[rm])

#         big_hour, big_min = map(int,splited_s[1].split(':'))
#         small_hour, small_min = map(int,splited_s[0].split(':'))
#         total_time = (big_hour-small_hour)*60 + (big_min-small_min)


#         time, rest = divmod(total_time,len(splited_s[-1]))
#         splited.append((splited_s[2], splited_s[-1]*time + splited_s[-1][:rest]))

#     # answer = []
#     # for i in splited:
#     #     if m in i[1]:
#     #         answer.append((i[0],len(i[1])))
    
#     # if answer == []:
#     #     return '(None)'
#     # else:
#     #     if len(answer) >1:
#     #         answer.sort(key=lambda x: (-len(x[1])))
#     #     return answer[0][0]

# ------------------------------------------- 내꺼 + 커뮤
# def solution(m, musicinfos):
#     change = {'C#': 'c', 'D#': 'd', 'E#': 'e', 'F#': 'f', 'G#': 'g', 'A#': 'a', 'B#': 'b'}

#     for rm in change.keys():
#         m = m.replace(rm, change[rm])


#     candidate = "(None)"
#     prev_du = 0
#     for i in musicinfos:
#         splited_s = i.split(',')
#         for rm in change.keys():
#             splited_s[-1] = splited_s[-1].replace(rm, change[rm])

#         big_hour, big_min = map(int,splited_s[1].split(':'))
#         small_hour, small_min = map(int,splited_s[0].split(':'))
#         total_time = (big_hour-small_hour)*60 + (big_min-small_min)
#         print(total_time)


#         time, rest = divmod(total_time,len(splited_s[-1]))
#         hello = splited_s[2], splited_s[-1]*time + splited_s[-1][:rest]

#         if m in hello:
#             if prev_du >= total_time:
#                 pass
#             else:
#                 candidate = splited_s[2]
#                 prev_du = total_time

#     return candidate

# # ------------------------------------------- 커뮤니티
# from datetime import datetime
# def solution(m, musicinfos):
#     rmv = {"C#":"c","D#":"d","E#":"e","F#":"f","G#":"g","A#":"a","B#":"b"}
#     candidate = "(None)"
#     prev_du = 0
#     for rm in rmv.keys():
#         m = m.replace(rm, rmv[rm])

#     for info in musicinfos:
#         split_info = info.split(',')
#         for rm in rmv.keys():
#             split_info[-1] = split_info[-1].replace(rm,rmv[rm])

#         st = datetime.strptime(split_info[0], "%H:%M")
#         et = datetime.strptime(split_info[1], "%H:%M")
#         duration = (((et-st).seconds)//60)
#         print(duration)

    #     if len(split_info[-1]) < duration:
    #         cir = duration // len(split_info[-1])
    #         more = duration % len(split_info[-1])
    #         split_info[-1] *= cir
    #         split_info[-1] += split_info[-1][:more]

    #     elif len(split_info[-1]) > duration:   
    #         split_info[-1] = split_info[-1][:duration]


    #     if m in split_info[-1]:
    #         if prev_du >= duration:
    #             pass
    #         else:
    #             candidate = split_info[2]
    #             prev_du = duration

    # return candidate

# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))