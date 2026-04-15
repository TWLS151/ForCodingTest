import sys
input = sys.stdin.readline

def find_val(start: int, end: int, size: int, seg: list) -> list[int, int]:

    # 포인터 설정
    start += size
    end += size

    # 최소 최대값 설정
    min_val = seg[start][0]
    max_val = seg[end][1]

    # 두 가지 동시에 계산
    # 두 포인터가 교차되면 종료
    while start <= end:

        # 스타트가 고립되어 있다면 [오른쪽 자식 노드] 값 갱신
        if start % 2 == 1:
            min_val = min(min_val, seg[start][0])
            max_val = max(max_val, seg[start][1])
            start += 1
        
        # 엔드가 고립되어 있다면 [왼쪽 자식 노드] 값 갱신
        if end % 2 == 0:
            min_val = min(min_val, seg[end][0])
            max_val = max(max_val, seg[end][1])
            end -= 1

        # 위 층으로 이동
        start //= 2
        end //= 2

    # 값 반환
    return min_val, max_val


N, M = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]

INF = 10**18

# ===== 트리 구현 ===== #
size = 1
while size < N:
    size *= 2

# 최댓값 최솟값을 동시에 계산하기 위해 2차원으로 만듭니다.
seg = [[INF, 0] for _ in range(2*size)]

# 리프 노드를 다 채우고 [같은 값으로 2차원 모두]
for i in range(N):
    seg[size + i][0] = nums[i]
    seg[size + i][1] = nums[i]

# 최댓값 트리, 최솟값 트리를 구분해서 구현합니다.
for i in range(size-1, 0, -1):
    seg[i][0] = min(seg[i*2][0], seg[i*2+1][0])
    seg[i][1] = max(seg[i*2][1], seg[i*2+1][1])
# ===== 구현 종료 ===== #

for _ in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    print(*find_val(start, end, size, seg))
   