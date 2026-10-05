def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(grid, r ,c)
                count += 1
    
    return count

def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    
    grid[i][j] = '#' #visited
    # self.dfs(grid, i+1, j)
    # self.dfs(grid, i-1, j)
    # self.dfs(grid, i, j+1)
    # self.dfs(grid, i, j-1)

    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    for dr,dc in directions:
        dfs(grid,i+dr,j+dc)
       