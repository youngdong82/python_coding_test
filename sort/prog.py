# ------------------------------------------------------- k번째 수 11분 컷!
array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

#-------------------------- 내꺼
def solution(array, commands):
    answer = []
    for command in commands:
        split_list = array[command[0]-1: (command[1])]
        split_list.sort()
        answer.append(split_list[command[2]-1])
        print(answer)
    return answer

print(solution(array, commands))

# #-------------------------- 커뮤니티 좋은거
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer


# ------------------------------------------------------- 가장 큰 수 실패!

# #-------------------------- 커뮤니티 좋은거 람다 공부 하자.
# numbers = [3,300,34,5,9]

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))

# print(solution(numbers))

# ------------------------------------------------------- H-index 12분 컷!
# #-------------------------- 내꺼
# def solution(citations):
#     citations.sort()
#     max_c = 0
#     for i in range(max(citations)):
#         count = 0
#         for j in citations:
#             if j >= i:
#                 count += 1
#         if count >= i and i > max_c:
#             max_c = i
#     return max_c



# #-------------------------- 커뮤니티 좋은거
# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0
