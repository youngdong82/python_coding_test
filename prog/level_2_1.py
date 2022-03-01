# -------------------------------------------------------------------------------- 1. 오픈채팅방
# ------------------------------------------- 내꺼
# dic쓸거 list 써서 개고생했네 진짜....

# ------------------------------------------- 커뮤니티 왐마.... dic쓰자
# def solution(records):
#     answer = []
#     userdict = {}
#     for record in records: 
#         if (record.split(' ')[0] == 'Enter') | (record.split(' ')[0] == 'Change'):
#             userdict[record.split(' ')[1]] = record.split(' ')[2]

#     for record in records: 
#         if record.split(' ')[0] == 'Enter': 
#             answer.append("{}님이 들어왔습니다.".format(userdict[record.split(' ')[1]]))
#         elif record.split(' ')[0] == 'Leave': 
#             answer.append("{}님이 나갔습니다.".format(userdict[record.split(' ')[1]]))
#         else:
#             pass
#     return answer

# print(solution([
#   "Enter uid1234 Muzi", 
#   "Enter uid4567 Prodo",
#   "Leave uid1234",
#   "Enter uid1234 Prodo",
#   "Change uid4567 Ryan"
#   ]))

# -------------------------------------------------------------------------------- 2. 짝지어 제거하기
# ------------------------------------------- 내꺼

def solution(s):
  answer = []
  s = list(s)

  def reduce(s):
    if len(s) == 0:
      answer.append(1)
    for i in range(len(s)-1):
      if s[i] == s[i+1]:
        s.remove(s[i])
        s.remove(s[i])
        reduce(s)
        break

  reduce(s)
  if len(answer) == 0:
    return 0
  else:
    return 1
      
      

print(solution('baabaa'))
print(solution('cdcd'))


# a = [1,2,2,4,5]


# for i in range(len(a)-1):
#   if a[i] == a[i+1]:
#     a.remove(a[i])
#     a.remove(a[i])