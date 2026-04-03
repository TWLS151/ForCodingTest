'''
DFS 백트래킹 완전탐색

DP..? 는 아닌 것 같은데

인자 둘 다 2차원 리스트

cost[스테이지 넘버][힌트권 사용시 가격], hint[스테이지 넘버][0= 가격, 1: 힌트권 번호]

[1] 1번 스테이지는 힌트권이 없다.
[2] 현재 스테이지에 쓸 수 있는 힌트권이 있으면 사용한다.
[3] constraint = 힌트권을 살지 말지
[4] pruning = 비용 커지면 cut
[5] status = cur_stage, cur_cost, ticket: list
'''

def solution(cost, hint):
    answer = 0
    
    # ====== #
    def dfs(cur_stage: int, cur_cost: int, ticket: list) -> None:
        nonlocal min_cost, cost, hint, N

        # base_case: cur_stage == n
        if cur_stage == N:
            min_cost = min(min_cost, cur_cost)
            return

        # pruning: cur_cost > min_cost
        if cur_cost >= min_cost:
            return
        
        # 이 부분에서 시간을 좀 많이 썼는데
        # cost의 내부 리스트의 길이가 정해져있지 않아서 num 을 구해줘야했습니다.
        # 2차원 리스트의 내부 길이가 무조건 N-1 인 줄 알았지만 그렇지 않아서 길이를 구해줘야했다.
        # 또 힌트권의 개수가 문제에서 제시된 사용 가능 수보다 많은 경우도 있어서 그 부분도 if 문으로 해결했습니다.
        cur_hint = ticket[cur_stage]
        num = len(cost[cur_stage])
        if cur_hint >= num:
            cur_hint = num - 1
        next_cost = cur_cost + cost[cur_stage][cur_hint]

        # dont buy
        # 힌트권 구매하지 않는 경우
        dfs(cur_stage + 1, next_cost, ticket)

        # buy
        # 구매하는 경우
        # 마지막 스테이지는 힌트권이 없어서 인덱스 에러가 발생합니다.
        if cur_stage < N-1:
            next_cost += hint[cur_stage][0]
            
            for i in hint[cur_stage][1:]:
                ticket[i] += 1
                
            dfs(cur_stage + 1, next_cost, ticket) 
            
            for i in hint[cur_stage][1:]:
                ticket[i] -= 1
                
    # 더미 추가
    cost = [[0]] + cost
    hint = [[0]] + hint
    
    N = len(cost)
    min_cost = float('inf')
    
    # 힌트권 현황 확인용 리스트
    ticket = [0] * (N + 1)
    dfs(1, 0, ticket)
    
    answer = min_cost
    # ====== #
    
    return answer
