'''
[Constraint]

1. 더 많이 준 사람이 다음 달에 하나 받는다.
2. 기록이 없거나 수가 같으면 '선물 지수' 가 더 큰 사람이 더 작은 사람에게 하나 받는다.
    - 선물 지수: '이번 달까지' 자신이 친구들에게 준 선물 수 - 받은 선물의 수
3. 이 선물 지수도 같다면 주고받지 않는다.

이 때 선물을 가장 많이 받을 친구가 받을 선물의 수

---

[Thinking Process w. numbering]

[1] -----------------
우선 리스트 형태로 정리
info = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
ex_idx = 받은 사람
in_idx = 누구에게

edge 를 받으며 전부 다 기록
edge = ["준사람 받은사람", "준사람 받은사람", "준사람 받은사람"]
-> gift를 for문 순회하면서 split 으로 찢고 언패킹
for log in gift:
    give, recieve = log.split()
    
맵핑 딕셔너리가 필요. friends 들어오면 먼저 처리
MAP = {}
for idx in range(len(friends)):
    name = friends[idx]
    MAP[name] = idx

이러면 위에서 순회할 때
info[recieve][give] += 1 : 기록


[2] ---------------

리스트가 완성되면 계산 시작

[3] ----------------

1. 더 많이 준 사람이 하나 받는다.
cur_status = [0, 0, 0]
idx = name

for ex_idx in range(N):
    for in_idx in range(N):
        if info[ex_idx][in_idx] < info[in_idx][ex_idx]:
            이 때는 in_idx 가 ex_idx 한테 반대보다 더 적게 받았으니 in_idx 가 ex_idx 에 하나 준다
            cur_status[ex_idx] += 1
        elif info[ex_idx][in_idx] > info[in_idx][ex_idx]:
            반대의 경우는 in 가 하나 받는다.
            cur_status[in_idx] += 1

            
[4] -----------------

2. 기록이 없거나(양쪽 다 0 이라 수가 같은 것과 같다.) 수가 같다면 선물 지수가 더 큰 사람이 작은 사람에게 하나 받는다
선물 지수 계산은 gifts 받을 때 진행

# edge 를 받으며 전부 다 기록
# edge = ["준사람 받은사람", "준사람 받은사람", "준사람 받은사람"]
# -> gift를 for문 순회하면서 split 으로 찢고 언패킹
# for log in gift:
#     give, recieve = log.split()

순회 이전에 지수 리스트를 만들고 지수 반영
give_exp[give] += 1
recieve_exp[recieve] += 1
exp = []
for e in range(N):
    exp.append(
        give_exp[e] - recieve_exp[e] 
    )

이 리스트를 데이터로 위 if 문에 else 추가
            else:
                if exp[ex_idx] < exp[in_idx]:
                    cur_state[in_idx] += 1
                elif exp[ex_idx] > exp[in_idx]:
                    cur_state[ex_idx] += 1

선물 지수마저 같다면 (바로 위 else 안 if 문의 else) 그냥 넘긴다. (정의하지 않음)

[5] ------------

이 때 cur_state 안의 가장 높은 값을 출력
answer = max(cur_state)
        
'''

'''
[Trouble-Log]

위에까지 하고 제출하니 테케 한 개 통과
보니까 두 배가 나온다.

똑같은 걸 두 번 본다는건데 아까 생각해봤을 때는 두 번 보는게 아니었는데
이중 for문 둘 다 봐야하는거 아닌가?
[받은사람][준사람]

반으로 나누니까 통과되긴 하는데
왜지?

두 방향 다 봐야하는거 아닌가?

그럼 start 인덱스를 제한해야하나?
맞네

아 내가 elif 문을 달아놔서 한 번에 처리가 끝나는구나
해결 완료
'''


def solution(friends, gifts):
    answer = 0
    
    # [1] ============= #
    N = len(friends)
    info = [[0] * N for _ in range(N)]
    
    MAP = {}
    for idx in range(N):
        name = friends[idx]
        MAP[name] = idx
    
    give_exp = [0] * N
    receive_exp = [0] * N
    
    for log in gifts:
        give, receive = log.split()
        give, receive = MAP[give], MAP[receive]
        
        info[receive][give] += 1
        
        give_exp[give] += 1
        receive_exp[receive] += 1
    
    exp = []
    for e in range(N):
        exp.append(
            give_exp[e] - receive_exp[e]
        )
        
    # [2] ============== #
    cur_state = [0] * N
    
    # [3] ============== #
    for ex_idx in range(N):
        for in_idx in range(ex_idx + 1, N):
            if info[ex_idx][in_idx] < info[in_idx][ex_idx]:
                cur_state[ex_idx] += 1
            elif info[ex_idx][in_idx] > info[in_idx][ex_idx]:
                cur_state[in_idx] += 1
                
            # [4] ============== #
            else:
                if exp[ex_idx] < exp[in_idx]:
                    cur_state[in_idx] += 1
                elif exp[ex_idx] > exp[in_idx]:
                    cur_state[ex_idx] += 1
    
    # [5] ============== #
    answer = max(cur_state)
    
    return answer