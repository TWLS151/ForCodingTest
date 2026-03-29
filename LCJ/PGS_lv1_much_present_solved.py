'''
# 문제 조건
선물을 더 준 사람이 다음엔 받는다
거래 내역이 없거나 같은 수를 받았다면, 선물 지수(give - accept)가 높은 사람이 받는다.

# 구현

1. 선물 교환 내역 정리
2. 선물 지수 계산
3. 교환 내역에 따른 다음 달 선물 정산

교훈 : 문제를 꼼꼼히 읽자... 교환 내역이 없는 경우도 고려해라
'''
from collections import defaultdict

# test case 3. (모두의 선물 지수가 같은 경우)

friends = ["a", "b", "c"]

gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]

def solution(friends, gifts):

    # 1. 선물 교환 내역을 정리
    gift_history = dict()

    # 2. 인원 별 선물 지수를 계산
    gift_index = defaultdict(int)

    # 3. 다음 달에 받을 선물 수를 정리
    next_month = dict()

    # 1-1. 가능한 모든 선물 교환 시나리오를 key에 입력
    for i in range(len(friends)):

        next_month[friends[i]] = 0      # 3-1. 다음 달 선물 수에 인원을 모두 추가

        for j in range(len(friends)):

            if i != j and (friends[j], friends[i]) not in gift_history:

                gift_history[(friends[i], friends[j])] = 0

    # test 1. print(gift_history) - nC2 만큼의 내역이 출력됨

    for give_take in gifts:                     # 2-1. 선물 내역 로드

        give, take = give_take.split()          # give -> take 내역 분리

        gift_index[give] += 1                   # 준 경우 +1
        gift_index[take] -= 1                   # 받은 경우 -1

        if (give, take) in gift_history:        # 1-2. give -> take 내역이 있다면

            gift_history[(give, take)] += 1     # 해당 내역에 1을 추가

        else:                                   # <중요> 내역에 없다면 -> take -> give 내역이 존재
            gift_history[(take, give)] -= 1     # 교환 수를 하나 차감
                                                # 결과가 음수 == 앞 사람이 뒷 사람에게 더 받은 것

    # test 2. 선물 지수 및 교환 내역 확인
    # print(f"선물 지수 : {gift_index}")
    # print(f"선물 교환 내역 정리 : {gift_history}")

    for history, amount in gift_history.items():   # 3-1. 교환 기록과 양을 로드

        give_person, take_person = history

        if amount > 0:                              # (1) giver가 더 많이 줬다면
            next_month[give_person] += 1            # 다음 달엔 give가 받음

        elif amount < 0:                            # (2) giver가 더 많이 받았다면
            next_month[take_person] += 1            # 다음 달엔 take가 받음

        else:                                       # (3) 주고받은 횟수가 같거나 없다면 -> 선물 지수가 높은 사람이 다음 달에 받게됨
                                                    # -> 만약 선물 지수도 같다면 -> 교환하지 않음 (카운트 X)

            if gift_index[give_person] > gift_index[take_person]:
                next_month[give_person] += 1

            elif gift_index[give_person] < gift_index[take_person]:
                next_month[take_person] += 1

    # test 3. 다음달 받을 선물 수 확인 print(next_month)

    answer = max(next_month.values())

    return answer

# test 4. 최종 결과 확인
# result = solution(friends, gifts)
# print(result)