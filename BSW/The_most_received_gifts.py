# 선물을 주고받았다면, 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 받는다.
# 주고받은 선물이 같거나, 주고받지 않았다면, 선물 지수가 더 작은 사람에게 선물 하나 받기
# 선물 지수 : 이번달까지 자신이 준 선물의 수에서 받은 선물의 수를 뺀 값
# 선물 지수도 같으면 주고받지 않음.
# 다음 달에 가장 많은 선물을 받을 친구가 받을 선물의 수
# 이름이 주어지고, 이름이 같은 친구는 없음
# "A B"에서 A는 선물을 준 친구, B는 선물을 받은 친구

# 받은 선물 개수와 준 선물 개수 양을 나누어 볼까

def solution(friends, gifts):
    n = len(friends)
    friend_lst = {friend: idx for idx, friend in enumerate(friends)}
    
    # 주고받은 선물 표 작성 
    info = [[0] * n for _ in range(n)] 
    for gift in gifts:
        giver, receiver = gift.split() # 나누어 주는 사람과 받는 사람 구분
        info[friend_lst[giver]][friend_lst[receiver]] += 1
        
    # 선물 지수 계산 
    # 가로 줄과 세로 줄 동시 검사를 위해 zip 사용
    rotated_info = list(zip(*info))
    gift_idx = [0] * n 
    
    for i in range(n):
        # 준 선물 받은 선물을 기록
        give_gifts = sum(info[i])
        receive_gifts = sum(rotated_info[i])
        gift_idx[i] = give_gifts - receive_gifts
        
    # 다음 달 받을 선물 계산 
    next_month_gift = [0] * n
    
    # i와 j의 조합으로 중복 방지 (i는 j보다 항상 작음)
    for i in range(n):
        for j in range(i + 1, n):
            i_gave = info[i][j]
            j_gave = info[j][i]
            
            # 주고받은 기록이 있고 수가 다른 경우
            if i_gave > j_gave:
                next_month_gift[i] += 1
            elif j_gave > i_gave:
                next_month_gift[j] += 1
            # 주고받은 수가 같거나, 아예 주고받지 않은(둘 다 0) 경우
            else:
                if gift_idx[i] > gift_idx[j]:
                    next_month_gift[i] += 1
                elif gift_idx[j] > gift_idx[i]:
                    next_month_gift[j] += 1
                # 선물 지수까지 같다면 아무도 받지 않으므로 pass

    # 가장 많이 받는 사람의 선물 개수 반환
    return max(next_month_gift) if next_month_gift else 0
                            
                            
                    
                    
                    
    return gift_idx