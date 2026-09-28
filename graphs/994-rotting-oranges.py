import collections

def orangesRotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    mins = 0
    q = collections.deque()
    # visited = [[False]*cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r,c))
        
    mins = bfs(grid,q,mins)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return -1
    
    return mins
        


def bfs(grid, q, mins):
    rows, cols = len(grid), len(grid[0])

    while q:
        for _ in range(len(q)):
            row,col = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr,dc in directions:
                nr = dr+row
                nc = dc+col
                if nr<0 or nr >= rows or nc<0 or nc >= cols:
                    continue
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr,nc))
        if q:
            mins+=1

    return mins
    


