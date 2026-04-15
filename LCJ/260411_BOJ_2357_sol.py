import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())

# 1. 트리 초기화(크기 구하기)
# 직관적 : while문

size = 1
while 2**size < N:

    size += 1

seg_tree = [0] * (2**size * 2)

# test 1. k(size), 초기화된 트리 확인
# print(size)
# print(seg_tree)
# k == 4 이므로, 총 2**4 * 2 = 32개의 원소를 가진 배열을 생성하게 됨

# 2. 트리 채우기
# leaf -> root (bottom - up 방식)

# (1) 시작 인덱스 지정
start = 2 ** size

# (2) 리프 노드부터 채우기
for idx in range(start, start + N):

    value = int(input())

    seg_tree[idx] = (value, value)

# (3) 리브의 부모노드 -> 루트 노드 순으로 채우기
for idx in range(start - 1, 0, -1):

    # 왼쪽 자식이 비어있다면 -> 빈 트리
    if seg_tree[idx * 2] == 0:
        seg_tree[idx] == 0

    # 오른쪽 자식이 비어있다면 -> 왼쪽 자식값을 그대로
    elif seg_tree[idx * 2 + 1] == 0:
        seg_tree[idx] = seg_tree[idx * 2]

    # 둘 다 차있다면 -> merge
    else:
        seg_tree[idx] = (min(seg_tree[idx*2][0], seg_tree[idx*2 + 1][0]), max(seg_tree[idx*2][1], seg_tree[idx*2 + 1][1]))

    # test 2. segment tree 확인
    # print(seg_tree)

# 3. 질의값 구하기
# 질의값 = (구간 최소, 구간 최대)
# 문제에 맞게 노드의 값을 (최소, 최대)로 정의
for _ in range(M):

    start_idx, end_idx = map(int, input().split())

    # 1. 트리에 맞게 인덱스 변경 (2^k - 1 더하기) -> 시작 인덱스로 이동
    start_idx += (2**size) - 1
    end_idx += (2**size) -1

    selected = []

    # start와 end가 교차되면 종료
    # start : 오른쪽 자식 노드를 독립 선택하는 효과
    # end : 왼쪽 자식 노드를 독립 선택하는 효과
    # 두 경우 모두, 결국 "볼 필요가 없는 부모 노드를 버린다"는 접근 !
    while start_idx <= end_idx:

        if start_idx % 2 == 1:
            selected.append(seg_tree[start_idx])
            start_idx += 1

        if end_idx % 2 == 0:
            selected.append(seg_tree[end_idx])
            end_idx -= 1

        start_idx //= 2
        end_idx //= 2

    # test. 최종 선택된 노드들을 확인
    # print(selected)
    print(min(selected, key= lambda x:x[0])[0], max(selected, key= lambda x:x[1])[1])