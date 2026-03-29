# 힌트를 사용하는 리스트를 따로 만들고, 그 인덱스에다가 힌트 개수를 추가 ㄱㄱ
# 1번 스테이지부터 풀기 시작하므로 힌트 내역에 따른 합과, 힌트를 추가로 구매하는 조건을 따로 생성하고, 따로 재귀 부여
# 힌트 구매하는 코드를 아래에 작성
min_cost = float('inf')

def solution(cost, hint):
    n = len(cost)
    
    def dfs(idx, cur_cost, hint_use):
        global min_cost
        
        # 가지 치기
        if cur_cost >= min_cost:
            return
        
        # 마지막 스테이지 해결
        if idx == n - 1:
            
            # 힌트 사용 개수(최대 사용 개수가 n - 1)
            used_hint = min(hint_use[idx], n - 1)
            
            min_cost = min(min_cost, cur_cost + cost[idx][used_hint])
            return
        
        # 2. 힌트 구매 내역에 따른 계산
        used_hint = min(hint_use[idx], n - 1)
        next_cost = cur_cost + cost[idx][used_hint]
        dfs(idx + 1, cur_cost + cost[idx][used_hint], hint_use)
        
        # 3. 힌트 구매하는 경우
        price = hint[idx][0]
        new_hint_use = list(hint_use)
        
        # 힌트 사용 가능한 번호 지정
        for target_stage in hint[idx][1:]:
            
            # 인덱스 조절위해 target_stage -= 1
            new_hint_use[target_stage - 1] += 1
            
        # 힌트 가격만큼 추가, 새로운 힌트 사용 내역
        dfs(idx + 1, next_cost + price, new_hint_use)
        
    dfs(0, 0, [0] * n)
    return min_cost