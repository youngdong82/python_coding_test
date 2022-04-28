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

# -------------------------------------------------------------------------------- 4. 
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
def solution(n, arr1, arr2):
  graph1 = []
  for i in arr1:
    binary_value = bin(i)[2:].rjust(n,'0')
    graph1.append(list(binary_value))

  graph2 = []
  for i in arr2:
    binary_value = bin(i)[2:].rjust(n,'0')
    graph2.append(list(binary_value))
  
  for i in range(n):
    for j in range(n):
      graph1[i][j] = int(graph1[i][j]) + int(graph2[i][j])

  answer = []
  for i in graph1:
    tmp = ''
    for j in i:
      if j == 0:
        tmp += ' '
      else:
        tmp += '#'
    answer.append(tmp)

  return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33 ,22, 31, 50], 	[27 ,56, 19, 14, 14, 10]))
