# -------------------------------------------------------------------------------- 5. 큰 수 만들기  - 복복습!!
# permutation쓸 수 있지만 number가 1,000,000이라 사용하면 터진다
# ------------------------------------------- 내꺼 역시나 시간초과 구현 자체도 어려워

# -------------------------------------------------------------------------------- 5. 거리두기 확인하기
# 맨해튼 거리1가 2 이하
# 파티션 x, 빈자리o, 응시자 p
# ------------------------------------------- 내꺼 두번째 35분 컷!! 3번째 실패!

# -------------------------------------------------------------------------------- 1. 후보키 실패! 복복습 필수!!!
# 컬럼(column)의 길이는 1 이상 8 이하
# 로우(row)의 길이는 1 이상 20 이하
# 모든 문자열의 길이는 1 이상 8 이하
# ------------------------------------------- 커뮤니티 뭔가 간단해보이는데 로직 자체도 뭔가 복잡하네... 

# -------------------------------------------------------------------------------- 2. 조이스틱 복복습!!!
# ------------------------------------------- 내꺼 실패!! 두번째 45분 컷! 
# 3번째 푼 결과
# 2번째도 운 좋게 통과했을 뿐이었다.
# -------------------------------------------  커뮤니티 배우자...간결하다

# -------------------------------------------------------------------------------- 4. [1차] 뉴스 클러스터링 복복습!!
# ------------------------------------------- 내꺼 3번째 50분 컷!

# -------------------------------------------------------------------------------- 5. 수식 최대화
# 완전탐색???
# ------------------------------------------- 내꺼





# -------------------------------------------------------------------------------- 4. 땅따먹기 - 복복습!!!!
# ------------------------------------------- 커뮤 3번째 와....이걸 결국은 못 푸넼ㅋㅋㅋㅋ

# -------------------------------------------------------------------------------- 9. 구명보트 - 복복습!!
# ------------------------------------------- 내꺼 3번째 시간초과!! 25분 컷!
# ------------------------------------------- 이전의 나 투포인터..와우 어떻게 생각해낸거짘ㅋㅋㅋㅋㅋ 암튼 복습하잨ㅋㅋㅋ

# -------------------------------------------------------------------------------- 8. n^2 배열 자르기 - 복복습!!
# ------------------------------------------- 내꺼 시간초과

# -------------------------------------------------------------------------------- 4. 메뉴 리뉴얼 복복습!!
# ------------------------------------------- 내꺼 시간초과 두번째 시간초과 3번째 시간초과 4번째 시간초괔ㅋㅋㅋㅋㅋㅋ 학습 안하냨ㅋㅋ
# from itertools import combinations


# def solution(orders, course):
#   answer = []
#   for i in course:
#     candidates = []
#     for order in orders:
#       candidates += combinations(sorted(order),i)

#     dic = {}
#     for candidate in candidates:
#       if candidate not in dic.keys():
#         dic[candidate] = 1
#       else:
#         dic[candidate] += 1
#     print(dic)

#     for combi, time in dic.items():
#       if time == max(dic.values()) and time >=2 :
#         answer.append(''.join(combi))

#   return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

# -------------------------------------------------------------------------------- 6. [1차] 프렌즈4블록 복복습!!
# 지워지는 블록은 모두 몇 개
# ------------------------------------------- 커뮤...

# -------------------------------------------------------------------------------- 9. 순위 검색 - 복복습!!
# 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구
# info 배열의 크기는 1 이상 50,000 이하
# query 배열의 크기는 1 이상 100,000 이하
# ------------------------------------------- 커뮤