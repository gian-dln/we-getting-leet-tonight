import collections


def numIslands(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0
    visited = [[False]*cols for _ in range(rows)]


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                bfs(grid, visited, r, c)
                count += 1
                
    return count

def bfs(grid ,visited, r, c):
    rows, cols = len(grid), len(grid[0])
    q = collections.deque()
    visited[r][c] = True
    q.append((r,c))

    while q: # (is not empty)
        row, col = q.popleft()
        directions = [[1,0], [-1,0], [0,1], [0,-1]] #

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            # isInBound
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if visited[nr][nc] or grid[nr][nc] == "0":
                continue

            visited[nr][nc] = True
            q.append((nr, nc))



