
# -------------------------------------------------------------------------------- 5. 124나라의 숫자 실패! - 복습!!
# ------------------------------------------- 내꺼 3번째 24분 컷!!!!!!
# def solution(num):
#   tmp = ''
#   while num > 0:
#     num,rest = divmod(num,3)
#     if rest == 0:
#       rest = '4'
#       num -= 1
#     tmp += str(rest)
#   return tmp[::-1]

# print(solution(2))
# print(solution(4))
# print(solution(12))
# print(solution(11))
# print(solution(37))

# -------------------------------------------------------------------------------- 8. 모음 사전
# ------------------------------------------- 내꺼 알고 푸니까 6분 컷! 3번째 6분 컷!!
# from itertools import product


# def solution(word):
#   alpha = 'AEIOU'
#   answer = []
#   for i in range(1,6):
#     candidates = list(product(alpha,repeat=i))
#     for i in candidates:
#       answer.append(''.join(i))
#   answer.sort()
#   return answer.index(word)+1

# print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
# print(solution("EIO"))

# -------------------------------------------------------------------------------- 5. 큰 수 만들기  - 복복습!!
# permutation쓸 수 있지만 number가 1,000,000이라 사용하면 터진다
# ------------------------------------------- 내꺼 역시나 시간초과 구현 자체도 어려워
# def solution(number, k):
#   answer = []
#   for num in number:
#     while answer and k > 0 and answer[-1] < num:
#       answer.pop()
#       k -= 1
#     answer.append(num)
#     print(answer)
#   answer = ''.join(answer[:len(number)-k])

#   return answer

# print(solution("1924",2))
# print(solution("1294",2))
# print(solution("1941",2))
# print(solution("1231234",3))
# print(solution("4177252841",4))
# print(solution("654321",1))
# print(solution("654321",5))

# -------------------------------------------------------------------------------- 1. 행렬 테두리 회전하기
# 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의
# 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 
# ------------------------------------------- 내꺼 ㅅㅂ 졸라 오래걸리긴 했지만 풀었다.
# 접근법은 같으나 커뮤니티 배울 필요가 있다.

# def solution(rows, columns, queries):

# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(10,9,[[1,1,10,9]]))

# -------------------------------------------------------------------------------- 7. 삼각 달팽이
# ------------------------------------------- 내꺼 19분 컷!! 기쁘다!!
# 아래,오른,대각선 왼위
# def solution(n):

# print(solution(1))
# print(solution(4))
# print(solution(5))
# print(solution(1000))


# -------------------------------------------------------------------------------- 9. 2개 이하로 다른 비트
# https://art-coding3.tistory.com/46
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8-Python
# 100,000개의 길이가 10의 15승 만큼 있다...?
# 오른쪽에서부터 0을 찾은 다음에 
# 그 뒤에 1과 자리 바꿔
# ------------------------------------------- 내꺼 실패 두번째 17분 컷!! 기쁘다!!
# def solution(numbers):

# print(solution([2,7,9]))

# -------------------------------------------------------------------------------- 5. 거리두기 확인하기 실패!
# 맨해튼 거리1가 2 이하
# 애초에 q에 들어가는 값을 (x,y,거리)로 설정해서
# nx,ny할 때 nd라는 거리값도 +1 해주니 괜춘하네
# ------------------------------------------- 내꺼 두번째 35분 컷!!
# def solution(places):

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# ------------------------------------------------------------------------------------------------ 220320
# -------------------------------------------------------------------------------- 1. 후보키 실패! 복습 필수!!!
# ------------------------------------------- 커뮤니티 뭔가 간단해보이는데 로직 자체도 뭔가 복잡하네... 
# def solution(relation):

# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))


# -------------------------------------------------------------------------------- 2. 조이스틱 복복습!!!
# ------------------------------------------- 내꺼 실패!! 두번째 45분 컷! 
# 3번째 푼 결과
# 2번째도 운 좋게 통과했을 뿐이었다.
# -------------------------------------------  커뮤니티 배우자...간결하다
# 연속되는 A가 있을 때, 그것의 왼쪽이나 오른쪽부터 시작하며 알파벳을 변경하는 것이 가장 효율적
# ref: https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy

# def solution(name):
#   answer = 0
#   min_move = len(name) - 1
#   for i, char in enumerate(name):
#     answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
#     # 해당 알파벳 다음부터 연속된 A 문자열 찾기
#     next = i + 1
#     while next < len(name) and name[next] == 'A':
#       next += 1
#     print('next', next)
#     # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
#     min_move = min([min_move,  2 *i + len(name) - next,  i + 2 * (len(name) -next)])
#     print(min_move)
#   answer += min_move
#   return answer


# print(solution("BBABAAAABBBAAAABABB"))
# print(solution("BBAAAAAABBBAAAAAABB"))
# print(solution("AAAAADAAAAA"))
# print(solution("AABAAABAAAA"))
# print(solution("AADAAAADADA"))
# print(solution("AADAAAAAADADA"))
# print(solution("AAAAADAAADAA"))
# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("A"))
# print(solution("D"))

# -------------------------------------------------------------------------------- 4. [1차] 뉴스 클러스터링
# 자카드 유사도
# 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의
# 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
# Counter!!!
# ------------------------------------------- 내꺼
# def solution(str1, str2):


# print(solution('FRANCE','french'))
# print(solution('handshake','shake hands'))
# print(solution('aa1+aa2','AAAA12'))
# print(solution('E=M*C^2','e=m*c^2'))
# print(solution('abcde','fghij'))

# print(solution('abc','abbb'))
# print(solution('aa1+aa2','AA12'))
# print(solution('aaabb','aabbb'))
# print(solution('aabbb','aaabb'))

# -------------------------------------------------------------------------------- 5. 수식 최대화
# 완전탐색???
# ------------------------------------------- 내꺼
# from itertools import permutations


# def solution(expression):
#   data = []
#   tmp = ''
#   for i in range(len(expression)):
#     if expression[i] in ['-','+','*']:
#       data.append(int(tmp))
#       data.append(expression[i])
#       tmp = ''
#     else:
#       tmp += expression[i]
#     if i == len(expression)-1:
#       data.append(int(tmp))
  
#   answer = []
#   prefers = list(permutations(['-','+','*'], 3))
#   for prefer in prefers:
#     stack = []
#     for i in prefer:
#       for j in range(len(data)):
#         if i == data[j]:
#           tmp = stack.pop()
#           stack.append(calculate(tmp,i,data[j+1]))
#         else:
#           # stack이 있을 경우
#           if len(stack):
#             if data[j] in ['-','+','*']:
#               stack.append(data[j])
#             else:
#               # stack[-1]이 문자일경우 무조건 넣어
#               if stack[-1] in ['-','+','*']:
#                 stack.append(data[j])
#           # stack이 비었을 경우
#           else:
#             stack.append(data[j])
#     data = stack
#     stack = []

          
#     answer.append(stack[0])
#   return answer

# def calculate(a,oper,b):
#   if oper == '+':
#     return a+b
#   elif oper == '-':
#     return a-b
#   elif oper == '*':
#     return a*b
      


# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

# -------------------------------------------------------------------------------- 6. 쿼드압축 후 개수 세기
# 재귀함수
# ------------------------------------------- 커뮤 간단해보이는데 굉장히 짜임새 있게 잘 짜여있다...


