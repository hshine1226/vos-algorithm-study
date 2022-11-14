import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

board = []
[board.append(list(input())) for _ in range(n)]

direction = [(-1,0), (1,0), (0,1), (0,-1)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by): 
    need_visit = deque()
    need_visit.append((1, rx, ry, bx, by))
    while need_visit:
        cnt, rx, ry, bx, by = need_visit.popleft()
        visited[rx][ry][bx][by] = True

        if cnt > 10: 
            return -1

        for dx, dy in direction:
            next_rx, next_ry, next_rcnt = move(rx, ry, dx, dy)
            next_bx, next_by, next_bcnt = move(bx, by, dx, dy)

            if board[next_bx][next_by] != 'O':
                if board[next_rx][next_ry] == 'O':
                    return cnt
                if next_rx == next_bx and next_ry == next_by:
                    if next_rcnt > next_bcnt:
                        next_rx -= dx
                        next_ry -= dy
                    else:
                        next_bx -= dx
                        next_by -= dy
            
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                need_visit.append((cnt + 1, next_rx, next_ry, next_bx, next_by))
    return -1

rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

print(bfs(rx, ry, bx, by))