# ----------------------------------------------------------------------------------------------- list.pop(index)
# 굳이 deque 해서 popleft() 쓸 필요 없는듯?
# a = [1,2,3]
# a.append(a.pop(0))
# print(a)

# ----------------------------------------------------------------------------------------------- enumerate
# enumerate는 열거하다라는 뜻!!
# list, set, tuple, dictionary, string을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
# a = [10,8,6,4]
# # data = list(enumerate(a))
# # print(data)
# data = enumerate(a)
# for index, value in data:
#   print(index, value)

# ----------------------------------------------------------------------------------------------- any


# ---------------------------------------------------  기능개발 실패!! 테스트케이스 좀 더 확인해보자!
# ------------------------- 일단 넘어가자...이게 되는진 알겠는데 내꺼가 왜 안되는진 모르겠다ㅠ
# def solution(progresses, speeds):
#     answer = []
#     time = 0
#     count = 0
    
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100: 
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer


# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# ---------------------------------------------------  프린터
# ------------------------- 내꺼 23분 컷!
# def solution(priorities, location):
#   time = 0
#   while priorities:
#     if priorities[0] == max(priorities):
#       time += 1
#       if location == 0:
#         return time
#       else:
#         priorities.pop(0)
#         location -= 1
#     else:
#       priorities.append(priorities.pop(0))
#       if location == 0:
#         location = len(priorities)-1
#       else:
#         location -= 1

# ------------------------- 커뮤니티 
# enumerate로 인해 index가 values와 박혀있으니까 location값을 움직일 필요가 없이 비교만 해도 된다.
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     print('this one',queue)
#     time = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             time += 1
#             if cur[0] == location:
#                 return time

# print(solution([2, 1, 3, 2], 2 ))
# print(solution([1, 1, 9, 1, 1, 1], 0 ))

# ---------------------------------------------------  다리를 지나는 트럭 
# ------------------------- 내꺼 풀긴 풀었는데 더 빠르게 풀어보자!!
# def solution(bridge_length, weight, t_list):
#   time = 0
#   on_bridge = []

#   while True:
#     if len(t_list) == 0 and len(on_bridge) == 0:
#       break
#     time += 1

#     if on_bridge:
#       for truck in on_bridge:
#         truck[0] += 1
#       if on_bridge[0][0] > bridge_length:
#         on_bridge.pop(0)

#     summ = sum([truck[1] for truck in on_bridge])
#     if t_list and summ + t_list[0] <= weight:
#       on_bridge.append([1,t_list.pop(0)])
#     # print(time, on_bridge, t_list)
#   return time

# ------------------------- 커뮤니티 속도가 굉장히 빠르데
# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     bridge = deque(0 for _ in range(bridge_length))
#     total_weight = 0
#     time = 0
#     # 이건 속도 향상을 위한 것인듯? pop()이후 index 정렬시간이 없어짐.
#     truck_weights.reverse()

#     while truck_weights:
#         total_weight -= bridge.popleft()
#         if total_weight + truck_weights[-1] > weight:
#             bridge.append(0)
#             print(bridge)
#         else:
#             truck = truck_weights.pop()
#             bridge.append(truck)
#             print(bridge)
#             total_weight += truck
#         time += 1

#     time += bridge_length

#     return time


# print(solution( 2, 10, [7,4,5,6]))
# print(solution( 100, 100, [10]))
# print(solution( 100, 100, [10,10,10,10,10,10,10,10,10,10]))
# ---------------------------------------------------  주식 가격 실패라기보다는 좀 문제가 이해하기 힘들어;; 풀긴 풀었다!!
# def solution(prices):
#   answer = []
#   for i in range(len(prices)):
#     count = 0
#     for j in range(i+1, len(prices)):
#       count += 1
#       if prices[i] > prices[j]:
#         break
#     answer.append(count)
#   return answer

# print(solution([1, 2, 3, 2, 3]))