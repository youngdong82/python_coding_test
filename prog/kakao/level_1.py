# -------------------------------------------------------------------------------- 1. 신고 결과 받기
# ref: https://programmers.co.kr/learn/courses/30/lessons/92334

# 풀이:
# 각 유저는 한 번에 한 명의 유저를 신고
# 신고 횟수에 제한은 없습니다
# 동일한 유저에 대한 신고 횟수는 1회로 처리
# k번 이상 신고된 유저는 게시판 이용이 정지
# 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
# 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지, 정지메일 보냄.
# id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수

# 제한:
# 2 ≤ id_list의 길이 ≤ 1,000
# 1 ≤ report의 길이 ≤ 200,000
# 전부 알파벳 소문자
# 1 ≤ k ≤ 200, k는 자연수

# 풀기 전 생긱:
# 해시 관련 문제로 보인다.
# 신고를 받을 사람을 키 값으로 두고,
# report를 돌면서 신고한 사람을 리스트에 넣는다면,
# 시간복잡도 O(N) = 200,000이기 때문에 1초에 2000만번 연산을 하는 파이썬에겐 충분하다.

# 풀이 계획:
# 1. 리포트 돌면서 신고받은 아이디를 key값으로 하는 해시 테이블 초기화
# 2. 만들어진 해시 테이블 중 value의 길이가 2 이상인 key가 있다면,
#    해당 key 값을 banned_id 리스트에 추가.
# 3. id_list 돌면서 신고한 아이디를 key 값으로 하는 해시 테이블2 초기화
# 4. banned_id 돌면서 reported_dic의 값 리스트 돌면서 report_dic에 +1

# -------------------------------- 내꺼
# def solution(id_list, report, k):
#   report = list(set(report))
#   # 1. 리포트 돌면서 신고받은 아이디를 key값으로 하는 해시 테이블 초기화
#   reported_dic = {}
#   for i in report:
#     ban_to, ban_from = i.split(' ')
#     if ban_from in reported_dic:
#       reported_dic[ban_from].append(ban_to)
#     else:
#       reported_dic[ban_from] = [ban_to]
#   # 2. 만들어진 해시 테이블 중 value의 길이가 2 이상인 key가 있다면,
#   #    해당 key 값을 banned_id 리스트에 추가.
#   banned_id = []
#   for ban_to, ban_list in reported_dic.items():
#     if len(ban_list) >= k:
#       banned_id.append(ban_to)
#   # 3. id_list 돌면서 신고한 아이디를 key 값으로 하는 해시 테이블2 초기화
#   report_dic = {}
#   for i in id_list:
#     report_dic[i] = 0
#   # 4. banned_id 돌면서 reported_dic의 값 리스트 돌면서 report_dic에 +1
#   for i in banned_id:
#     for j in reported_dic[i]:
#       report_dic[j] += 1

#   return list(report_dic.values())


# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"],3))

# -------------------------------------------------------------------------------- 2. 숫자 문자열과 영단어
# ref: https://programmers.co.kr/learn/courses/30/lessons/81301

# 문제 요약:
# 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임
# 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수
# s가 의미하는 원래 숫자를 return

# 제한:
# 1 ≤ s의 길이 ≤ 50
#  "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.

# 풀기 전 생긱:
# 문자열 다루는 문제, 해시테이블 관련 문제
# s의 길이가 50밖에 되지 않기 때문에,
# 1초에 2000만번 연산을 하는 파이썬에겐 충분하다.

# 풀이 계획:
# 1. 숫자의 영어 이름을 key, 해당 숫자를 value로 하는 alpha 사전 자료형 선언.
# 2. tmp 문자열 선언하고,s 돌면서 tmp에 넣어주기
# 3. is.digit()이 True라면 그대로 answer에 넣기
# 3. tmp에 s[i]값 넣을 때마다 alpha에 있는지 확인.
#   있다면, answer에 alpha[tmp]값 넣어주기, tmp 비워주기
#   없다면, tmp 에 넣어주기

# -------------------------------- 내꺼
# def solution(s):
#   alpha =['zero','one','two','three','four','five','six','seven','eight','nine']
#   alpha_dic = {}
#   for i in range(len(alpha)):
#     alpha_dic[alpha[i]] = str(i)
  
#   answer = ''
#   tmp = ''
#   for i in s:
#     if i.isdigit():
#       answer += i
#       continue
#     tmp += i
#     if tmp in alpha_dic:
#       answer += alpha_dic[tmp]
#       tmp = ''

#   return int(answer)

# print(solution("one4seveneight"))
# print(solution("23four5six7"))
# print(solution("2three45sixseven"))
# print(solution("123"))

# -------------------------------------------------------------------------------- 3. 신규 아이디 추천
# ref: https://programmers.co.kr/learn/courses/30/lessons/72410

# 문제 요약:
# 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발
# 아이디의 길이는 3자 이상 15자 이하여야
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# 제한:
# new_id는 길이 1 이상 1,000 이하인 문자열
# new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성

# 풀기 전 생각:
# 문자열 다루는 문제, 구현 문제
# new_id는의 길이가 1000 이하 밖에 되지 않기 때문에,
# 1초에 2000만번 연산을 하는 파이썬에겐 충분하다.

# 풀이 계획:
# 1. 소문자로 바꾸기.
# 2. tmp 선언하고 new_id 돌면서
# 3. new_id가 특수문자인데 빼기(-), 밑줄(_), 마침표(.)가 아니라면 continue
# 4.  i가 .인데 tmp[-1]도 .라면 continue
# 5. 이외는 전부 tmp에 넣기
#   한번 끊고
# 6. tmp 양 옆에 . 없애기
# 7. tmp가 비어있다면 a 넣기
# 8. len(tmp) 15이하로 맞추기
#   맞췄는데 마지막이 .이면 없애기
# 9. len(tmp)가 2 이하라면, 3 될 때까지 복사.

# -------------------------------- 내꺼
# def solution(new_id):
#   new_id = new_id.lower()
#   tmp = ''
#   for i in new_id:
#     if i.isdigit() or i.isalpha():
#       tmp += i
#     elif i in ['_', '-', '.']:
#       if i == '.' and tmp and tmp[-1] == '.':
#         continue
#       tmp += i
#     else:
#       continue

#   if tmp and tmp[0] == '.':
#     tmp = tmp[1:]
#   if tmp and tmp[-1] == '.':
#     tmp = tmp[:-1]

#   if len(tmp) == 0:
#     tmp += 'a'

#   if len(tmp) >=16:
#     tmp = tmp[:15]
#     if tmp[-1] == '.':
#       tmp = tmp[:-1]

#   if len(tmp) <= 2:
#     while len(tmp) < 3:
#       tmp += tmp[-1]
  
#   return tmp


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution(	"z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))

# -------------------------------------------------------------------------------- 4. [1차] 비밀지도
# ref: https://programmers.co.kr/learn/courses/30/lessons/72410

# 문제 요약:
# 한 변의 길이가 n인 정사각형 배열 형태
# 각 칸은 "공백"(" ") 또는 "벽"("#")
# 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽
# 모두 공백인 부분은 전체 지도에서도 공백

# 제한:
# 1 ≦ n ≦ 16


# 풀기 전 생각:
# 2진수 변환 내장함수, 2차원 리스트, 집합 연산?
# 리스트가 최대 16**2이기 때문에 시간복잡도 걱정할 필요가 없다.

# 풀이 계획:
# 1. arr1을 돌면서 2진수 변환하고 graph1에 넣기
# 2. arr2을 돌면서 2진수 변환하고 graph2에 넣기
# 3. 인덱스 값으로 2차원 리스트 돌면서 합쳐주기
# 4. answer 선언하고, 더한 2차원 리스트 돌면서
#     0이면 공백, 0이 아니면 #넣기

# -------------------------------- 내꺼
# def solution(n, arr1, arr2):
#   graph1 = []
#   for i in arr1:
#     binary_value = bin(i)[2:].rjust(n,'0')
#     graph1.append(list(binary_value))

#   graph2 = []
#   for i in arr2:
#     binary_value = bin(i)[2:].rjust(n,'0')
#     graph2.append(list(binary_value))
  
#   for i in range(n):
#     for j in range(n):
#       graph1[i][j] = int(graph1[i][j]) + int(graph2[i][j])

#   answer = []
#   for i in graph1:
#     tmp = ''
#     for j in i:
#       if j == 0:
#         tmp += ' '
#       else:
#         tmp += '#'
#     answer.append(tmp)

#   return answer

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33 ,22, 31, 50], 	[27 ,56, 19, 14, 14, 10]))

# -------------------------------------------------------------------------------- 5. [1차] 다트 게임
# ref: https://programmers.co.kr/learn/courses/30/lessons/17682

# 문제 요약:
# 총 3번의 기회
# Single(S) 1제곱 , Double(D) 2제곱, Triple(T) 3제곱
# * 전 점수까지 2배, # 마이너스 됨.

# 제한:
# 총 3번 기회니까 시간 복잡도는 충분하다.

# 풀기 전 생각:
# 스택, 문자열 변환

# 풀이 계획:
# 1. stack, tmp 선언
# 2. dartResult 돌면서,
#   숫자라면 tmp에 넣고
#   S,D,T중 하나라면 tmp에서 해당 연산 후 stack에 넣기
#   *,#라면
#     *라면 stack이 있다면, stack.pop()*2해서 다시 넣은 후, tmp * 2해서 넣기
#     #라면 -tmp stack에 넣기
# 3. sum(stack)리턴

# -------------------------------- 내꺼
# def solution(dartResult):
#   dartResult = dartResult.replace('10','A')
#   stack = []
#   tmp = 0
#   for i in dartResult:
#     if i.isdigit() or i == 'A':
#       if i.isdigit():
#         tmp = int(i)
#       else:
#         tmp = 10
#     elif i in ['S','D','T']:
#       if i == 'D':
#         tmp **= 2
#       elif i == 'T':
#         tmp **= 3
#       stack.append(tmp)
#       tmp = 0
#     elif i in ['*','#']:
#       if i == '*':
#         if len(stack) >1:
#           pop_1 = stack.pop()
#           pop_2 = stack.pop()
#           stack.append(pop_2 * 2)
#           stack.append(pop_1 * 2)
#         else:
#           stack.append(stack.pop() * 2)
#       elif i == '#':
#         stack.append(-stack.pop())
#   return sum(stack)


# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))


# -------------------------------------------------------------------------------- 5. 크레인 인형뽑기 게임
# ref: https://programmers.co.kr/learn/courses/30/lessons/64061

# 문제 요약:
# N x N 크기의 정사각 격자
# 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다.
# 터트려져 사라진 인형의 개수를 return

# 제한:
# 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하
# 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다. 0은 빈 칸
# moves 배열의 크기는 1 이상 1,000 이하

# 풀기 전 생각:
# 스택, 2차원 리스트, 문자열 다루기
# 각 칸에 담겨있는 숫자의 종류는 시간 복잡도와 무관.
# moves 1000번 이하로 돌면서, stack에 넣고, stack[-1]이랑 확인
# 시간복잡도 = O(N) 1초에 2000만번 연산을 하는 파이썬에겐 충분하다.

# 풀이 계획:
# 1. stack 선언하고
# 2. moves 돌면서,
#   각 moves[i]마다, 
#   x값 i를 더해주면서 반복문
#   0이 아닐때 까지, 아니라면 stack에 넣고 0으로 바꿔주기.
# 3. stack에 넣을 때마다, stack 비어있는지 확인하고,
#   비어있다면, 그냥 넣고
#   비어있지 않다면, stack[-1]이랑 비교 후,
#     같다면 stack.pop()
#     같지 않다면, 추가
#     stack.append()

# -------------------------------- 내꺼
# def solution(board, moves):
#   stack = []
#   answer = 0
#   n = len(board)

#   for each_move in moves:
#     for j in range(n):
#       if board[j][each_move - 1] != 0:
#         now = board[j][each_move - 1]
#         if not stack:
#           stack.append(now)
#         else:
#           if now == stack[-1]:
#             stack.pop()
#             answer += 2
#           else:
#             stack.append(now)
#         board[j][each_move - 1] = 0
#         break
#   return answer


# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

# -------------------------------------------------------------------------------- 7. 키패드 누르기
# ref: https://programmers.co.kr/learn/courses/30/lessons/67256

# 문제 요약:
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때
# 더 가까운 엄지손가락을 사용
# 거리가 같다면, 편한 손가락 사용.
# 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return

# 제한:
# numbers 배열의 크기는 1 이상 1,000 이하

# 풀기 전 생각:
# 구현 문제, 2차원 리스트 이동.
# numbers가 최대 1000이라 해도 시간복잡도 걱정을 할 필요 없다.

# 풀이 계획:
# 1. 각 숫자를 key값, 2차원 리스트 위치 값을 value로 가진 해시 테이블 초기화
# 2. answer 문자열, 현재 오른손가락, 왼손가락 위치 선언.
# 3. numbers 돌면서,
#   numbers[i]가 1,4,7,*라면
#     위치 바꿔주고
#     answer에 'L'추가
#   numbers[i]가 3,6,9,#라면
#     위치 바꿔주고
#     answer에 'R'추가
#   나머지라면,
#     위치 비교, 거리 작은 손 추가.
#     거리 같다면 hand의 값에 따라 answer에 추가

# -------------------------------- 내꺼
def solution(numbers, hand):
  number_x_y = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2),'*':(3,0), 0:(3,1), '#':(3,2)}
  answer = ''
  left_posi = '*'
  right_posi = '#'

  for number in numbers:
    if number in [1,4,7,'*']:
      left_posi = number
      answer += 'L'
    elif number in [3,6,9,'#']:
      right_posi = number
      answer += 'R'
    else:
      left_dist = abs(number_x_y[left_posi][0] - number_x_y[number][0]) + abs(number_x_y[left_posi][1] - number_x_y[number][1])
      right_dist = abs(number_x_y[right_posi][0] - number_x_y[number][0]) + abs(number_x_y[right_posi][1] - number_x_y[number][1])
      if left_dist < right_dist:
        left_posi = number
        answer += 'L'
      elif left_dist > right_dist:
        right_posi = number
        answer += 'R'
      else:
        if hand == 'left':
          left_posi = number
          answer += 'L'
        else:
          right_posi = number
          answer += 'R'
  return answer



# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"	))