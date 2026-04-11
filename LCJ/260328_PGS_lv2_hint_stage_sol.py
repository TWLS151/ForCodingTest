min_cost = float('inf') # 최소 비용 갱신을 위한 변수


# 1. DFS 함수 정의

def dfs(idx, hint, cost, chance_lst, purchase_cost):

    global min_cost

    if purchase_cost >= min_cost:                       # [가지치기] 힌트 구매비용으로 이미 최소를 넘겼다면 
        return

    if idx == len(hint):                                # [종료] 모든 힌트 번들을 거쳤다면 비용 계산 후 최소값 갱신

        total = 0                                       # 전체 비용 계산

        for j in range(len(chance_lst)):

            total += cost[j][chance_lst[j]]

        min_cost = min(total + purchase_cost, min_cost)
        return

    dfs(idx + 1, hint, cost, chance_lst, purchase_cost)   # [탐색 1] 힌트 번들을 구매하지 않았을 때

                                                          # [탐색 2] 힌트 번들을 구매했을 때 (상태변화 중요)
    new_lst = chance_lst[:]                               # 1. 새 힌트권 보유 리스트를 선언

    hint_cost = hint[idx][0]                              # 2. 힌트권 비용

    for stage in hint[idx][1:]:                           # 3. 힌트권 보유 리스트 갱신

        if new_lst[stage - 1] < len(cost[stage - 1]) - 1: # <주의> 정해진 힌트 권 사용 수를 넘길 순 없음
            new_lst[stage - 1] += 1

    dfs(idx + 1, hint, cost, new_lst, purchase_cost + hint_cost)    # 탐색


def solution(cost, hint):

    global min_cost

    chance_list = [0]*len(cost)

    dfs(0, hint, cost, chance_list, 0)

    print(min_cost)

    return min_cost