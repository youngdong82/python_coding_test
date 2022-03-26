# -------------------------------------------------------------------------------- 1. 11654번 
# ------------------------------------------- 내꺼
# print(ord(str(input())))
# -------------------------------------------------------------------------------- 2. 11720번 
# ------------------------------------------- 내꺼
# n = int(input())
# b = str(input())
# answer = 0
# for i in b:
#     answer += int(i)
# print(answer)
# -------------------------------------------------------------------------------- 3. 10809번 
# ------------------------------------------- 내꺼
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# s = str(input())
# for i in alpha:
#     if i in s:
#         print(s.index(i), end=' ')
#     else:
#         print(-1, end=' ')
# -------------------------------------------------------------------------------- 4. 2675번 
# ------------------------------------------- 내꺼
# n = int(input())
# for _ in range(n):
#     time, s = input().split()
#     time = int(time)
#     s = str(s)
#     tmp = ''
#     for i in s:
#       tmp += (i*time)
#     print(tmp)

# -------------------------------------------------------------------------------- 5. 60437번 
# ------------------------------------------- 내꺼
# s = str(input()).lower()
# dic = {}
# for i in s:
#   if i not in dic.keys():
#     dic[i] = 1
#   else:
#     dic[i] += 1

# max_value = max(dic.values())
# answer = []
# for i,j in dic.items():
#   if j == max_value:
#     answer.append(i)

# if len(answer) > 1:
#   print('?')
# else:
#   print(answer[0].upper())

# -------------------------------------------------------------------------------- 6. 1152번 
# ------------------------------------------- 내꺼
# s = list(map(str,input().split()))
# print(len(s))

# -------------------------------------------------------------------------------- 7. 2908번 
# ------------------------------------------- 내꺼
# a,b = map(str,input().split())
# a = int(a[::-1])
# b = int(b[::-1])

# answer = 0
# if a > b:
#   answer = a
# else:
#   answer = b

# print(answer)
# -------------------------------------------------------------------------------- 8. 5622번 
# ------------------------------------------- 내꺼
# s = str(input())
# answer = 0
# for i in s:
#   num = 0
#   if i in 'ABC':
#     num = 2
#   elif i in 'DEF':
#     num = 3
#   elif i in 'GHI':
#     num = 4
#   elif i in 'JKL':
#     num = 5
#   elif i in 'MNO':
#     num = 6
#   elif i in 'PQRS':
#     num = 7
#   elif i in 'TUV':
#     num = 8
#   elif i in 'WXYZ':
#     num = 9
#   answer += num
# print(answer + len(s))
# -------------------------------------------------------------------------------- 9. 2941번 
# ------------------------------------------- 내꺼
# croati = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# s = str(input())

# for i in croati:
#   if i in s:
#     s = s.replace(i,'X')
# print(len(s))

# -------------------------------------------------------------------------------- 9. 1316번 복습...?
# ------------------------------------------- 내꺼
# n = int(input())
# answer = 0

# for _ in range(n):
#   word = str(input())
#   tmp = ''
#   for i in word:
#     if tmp != '':
#       if tmp[-1] == i:
#         continue
#       else:
#         tmp += i
#     else:
#       tmp += i
#   if len(tmp) == len(set(tmp)):
#     answer += 1

# print(answer)

