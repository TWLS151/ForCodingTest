"""
기차의 형태와 방향회전을 시키는 것을 따로 생각해야 한다.
Ex. 4번 선로는 왼쪽, 위쪽이 뚫려있는 타입의 선로이다.
    즉, 4번 선로는 아래쪽이 뚫려있는 선로나, 오른쪽에 뚫려있는 선로와 조합될 수 있다.
    근데 4번 선로의 "기능"은 들어오는 사람의 방향을 회전시켜 주는 것으로,
            오른쪽으로 걸어오면 위쪽으로 회전시키고, 아래로 들어오면 왼쪽으로 회전시켜준다.

"""


def solution(grid):
    answer = 0

    n = len(grid)
    m = len(grid[0])

    # 방향: 0=위, 1=오른쪽, 2=아래, 3=왼쪽
    # rail[선로-1][진입방향] = 출구방향
    rail = [
        [-1, 3, -1, 1],
        [2, -1, 0, -1],
        [2, 3, 0, 1],
        [3, -1, -1, 0],
        [1, 0, -1, -1],
        [-1, 2, 1, -1],
        [-1, -1, 3, 2],
    ]

    def where_to(kind, from_dir):
        return rail[kind - 1][from_dir]

    def candidated(from_dir):
        """
        빈칸에 도달했을 때 어떤 선로를 놓을 수 있는지 구하는 함수
        Ex. 왼쪽(3)에서 진입했는데 빈칸인 경우,
                rail[0][3] = 1 => 가능
                rail[1][3] = -1 => 불가능
                rail[2][3] = 1 => 가능
                ...
        """
        result = []
        for i in range(7):
            out = rail[i][from_dir]
            if out != -1:
                result.append((i + 1, out))

        return result

    def move(row, col, direction):
        # 상우하좌
        dr = (-1, 0, 1, 0)
        dc = (0, 1, 0, -1)
        return row + dr[direction], col + dc[direction]

    def rev(d):
        """
        반대 방향을 구하는 함수
        Ex. 내가 (1, 2)에서 (1, 3)으로 오른쪽으로 들어간 경우,
                (1, 3)칸 입장에서 나는 왼쪽에서 들어온 것이 된다.
        """
        return (d + 2) % 4

    # 원본 격자를 1칸씩 -1(장애물)로 둘러싼다.
    # => 별도의 범위 체크 없이 자동으로 장애물로 처리된다
    g = [[-1] * (m + 2) for _ in range(n + 2)]

    # 전체 선로 수 초기화 (= 앞으로 지나야 할 선로 수)
    # 선로 지날 때 마다 -= 1 / 도착점에서는 res == 1 이어야 성공 (도착점 본인을 차감 하지 않기 때문)
    res = 0
    for i in range(n):
        for j in range(m):
            g[i + 1][j + 1] = grid[i][j]
            if grid[i][j] > 0:
                res += 1

    def dfs(row, col, from_dir, res):
        # 범위 바깥 또는 장애물
        if row < 1 or row > n or col < 1 or col > m:
            return 0
        if g[row][col] == -1:
            return 0

        # 선로가 존재하는 칸의 경우
        if g[row][col] != 0:
            kind = g[row][col]  # 해당 위치의 선로 type을 가져온다.
            out = where_to(kind, from_dir)  # 해당 선로 type의 나가는 방향을 구한다.

            # 내가 지금 가고자 하는 방향으로 위치의 선로를 들어가지 못하는 경우 -1을 반환하기 때문에
            # => 이 경우는 더 이상 갈 수 없음을 의미한다.
            if out == -1:
                return 0

            nrow, ncol = move(row, col, out)  # 이동이 가능한 경우 다음 칸으로 이동
            saved = g[row][col]  # 백트래킹을 위한 이전 값 담아두기

            if kind != 3:
                g[row][col] = -1

            # 3번 선로인 경우
            elif from_dir in (0, 2):
                res += 1
                g[row][col] = 1  # 위아래로 진입한 경우 가로 선로(1번)으로 바꾸어 둔다.
            else:
                res += 1
                g[row][col] = 2  # 좌우로 진입한 경우 세로 선로(2번)으로 바꾸어 둔다.

            # 도착점 체크
            if row == n and col == m:
                result = 1 if res == 1 else 0
                g[row][col] = saved
                return result

            result = dfs(nrow, ncol, rev(out), res - 1)
            g[row][col] = saved
            return result

        # 빈칸인 경우
        ans = 0
        for kind, out in candidated(from_dir):
            nrow, ncol = move(row, col, out)
            saved_res = res

            if kind != 3:
                g[row][col] = -1
            elif from_dir in (0, 2):
                res += 1
                g[row][col] = 1
            else:
                res += 1
                g[row][col] = 2

            ans += dfs(nrow, ncol, rev(out), res)

            # 백트래킹
            res = saved_res
            g[row][col] = 0

        return ans

    g[1][1] = -1
    answer = dfs(1, 2, 3, res - 1)
    g[1][1] = 1

    return answer
