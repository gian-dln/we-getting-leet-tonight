def maxAreaOfIsland(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    rows,cols = len(grid), len(grid[0])
    area = 0
    maxArea = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                area = dfs(grid, r, c)
                maxArea = max(maxArea, area)
    
    return maxArea


def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
        return 0
    
    grid[i][j] = 0
    area = 1

    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    for dr,dc in directions:
        area += dfs(grid, i+dr, j+dc)


    return area



