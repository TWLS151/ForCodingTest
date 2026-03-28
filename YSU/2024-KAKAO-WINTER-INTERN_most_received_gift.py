"""
친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로,
    다음 달에 누가 선물을 많이 받을지 예측하려고 한다.

1) 두 사람 사이에 선물을 주고받은 기록이 있는 경우,
    => 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받는다.
2) 선물을 주고받은 기록이 없거나, 주고받은 수가 같다면
    => 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받는다.
    => 만약 선물 지수도 같다면, 다음 달에 선물을 주고받지 않는다.

선물 지수 = (자신이 이번 달까지 친구들에게 준 선물의 수) - (받은 선물의 수)

선물을 가장 많이 받을 친구를 구한다.
"""

def solution(friends, gifts):
    N = len(friends)

    friends_num = {}
    for i in range(N):
        friends_num[friends[i]] = i

    # 2차원 배열로 선물 기록 관리
    gift_records = [[0] * N for _ in range(N)]

    # 선물 지수 미리 계산
    gift_index = [0] * N

    for gift_str in gifts:
        from_friend, to_friend = gift_str.split()
        i, j = friends_num[from_friend], friends_num[to_friend]

        gift_records[i][j] += 1
        # i가 j에게 선물을 주는 것
        # 선물 지수는 내가 선물을 주면 그만큼 증가하고, 선물을 받으면 그 만큼 감소한다.
        gift_index[i] += 1
        gift_index[j] -= 1

    nxt_month = [0] * N

    # 대칭 관계는 절반만 본다.
    # 단, 절반만 보는 경우 해당 관계는 한 번만 등장하기 때문에,
    #   모든 경우를 고려해야 한다.
    for i in range(N):
        for j in range(i + 1, N):

            if gift_records[i][j] > gift_records[j][i]:
                nxt_month[i] += 1
            elif gift_records[i][j] < gift_records[j][i]:
                nxt_month[j] += 1

            else:

                if gift_index[i] > gift_index[j]:
                    nxt_month[i] += 1
                elif gift_index[i] < gift_index[j]:
                    nxt_month[j] += 1

    return max(nxt_month)

# -------------------------------------------------------------------------------
# def solution(friends, gifts):
#     N = len(friends)
#
#     friends_num = {}
#     for i in range(N):
#         friends_num[friends[i]] = i
#
#     # 2차원 배열로 관리
#     gift_record = [[0] * N for _ in range(N)]
#     for gift_str in gifts:
#         from_friend, to_friend = gift_str.split()
#         gift_record[friends_num[from_friend]][friends_num[to_friend]] += 1
#
#     nxt_gift_cnt = [0] * N
#     for i in range(N):
#         for j in range(i + 1, N):
#             if i == j:
#                 continue
#
#             # i번째 친구가 다음 달에 몇개의 선물을 받을건지 계산한다.
#             # 이를 위해 j번째 친구와의 기록을 확인.
#
#             if gift_record[i][j] > gift_record[j][i]:
#                 # gift_record[i][j] != 0 이면 선물 거래가 존재했다는 것을 의미한다.
#                 # => gift_record[j][i] (= j가 i한테 준 선물 개수) 와 비교한다.
#                 nxt_gift_cnt[i]  += 1
#
#             elif gift_record[i][j] < gift_record[j][i]:
#                 nxt_gift_cnt[j] += 1
#
#             else:
#                 # gift_record[i][j] == 0 이면 두 사람의 선물 거래가 없었다는 것을 의미한다.
#                 # => 선물 지수의 게산이 필요
#
#                 # 먼저 i의 선물 지수 계산
#                 # i가 준 선물의 개수 = i행의 합 / i가 받은 선물의 개수 = i열의 합
#                 i_gave, i_got = sum(gift_record[i]), 0
#                 j_gave, j_got = sum(gift_record[j]), 0
#
#                 for col in (i, j):
#                     got_cnt = 0
#                     for row in range(N):
#                         got_cnt += gift_record[row][col]
#
#                     if col == i:
#                         i_got = got_cnt
#                     else:
#                         j_got = got_cnt
#
#                 # i의 선물 지수가 더 크다면 i는 선물을 하나 받는다.
#                 if (i_gave - i_got) > (j_gave - j_got):
#                     nxt_gift_cnt[i] += 1
#                 elif (i_gave - i_got) < (j_gave - j_got):
#                     nxt_gift_cnt[j]  += 1
#
#     # print(nxt_gift_cnt)
#     return max(nxt_gift_cnt)


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = [
    "muzi frodo",
    "muzi frodo",
    "ryan muzi",
    "ryan muzi",
    "ryan muzi",
    "frodo muzi",
    "frodo ryan",
    "neo muzi",
]
solution(friends, gifts)
