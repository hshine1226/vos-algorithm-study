import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

# 빨간 구슬을 구멍으로 나오면 통과
# 파란구슬이 구멍에 빠지면 실패
# 구슬은 사방탐색 가능 (구슬은 동시에 움직임)
# 빨간 구슬과 파란 구슬은 같은 칸에 있을 수 없음
# 움직인 횟수가 10회를 초과하면 실패
# #(공이 이동할 수 없는 장애물) / 0(구멍의 위치)

n, m = map(int, input().split())

board = []
[board.append(list(input())) for _ in range(n)]

direction = [(-1,0), (1,0), (0,1), (0,-1)]

def move(x, y, dx, dy):
    cnt = 0
    # 한 방향으로 움직일 수 있는 만큼 움직이기
    # 벽에 마주치거나 원래 위치가 구멍이라면 종료
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by): 
    need_visit = deque()
    need_visit.append((1, rx, ry, bx, by))
    # [rx][ry][bx][by]
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    while need_visit:
        cnt, rx, ry, bx, by = need_visit.popleft()
        visited[rx][ry][bx][by] = True

        if cnt > 10: 
            return -1

        for dx, dy in direction:
            rx_next, ry_next, rcnt_next = move(rx, ry, dx, dy)
            bx_next, by_next, bcnt_next = move(bx, by, dx, dy)

            if board[bx_next][by_next] != 'O':
                if board[rx_next][ry_next] == 'O':
                    return cnt 
                if rx_next == bx_next and ry_next == by_next:
                    if rcnt_next > bcnt_next:
                        rx_next -= dx
                        ry_next -= dy
                    else:
                        bx_next -= dx
                        by_next -= dy
            
            if not visited[rx_next][ry_next][bx_next][by_next]:
                visited[rx_next][ry_next][bx_next][by_next] = True
                need_visit.append((cnt + 1, rx_next, ry_next, bx_next, by_next))
    return -1

rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

print(bfs(rx, ry, bx, by))