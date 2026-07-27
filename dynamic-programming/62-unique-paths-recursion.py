def uniquePaths(m: int, n: int) -> int:
    # recursion, topdown dp memoization

    memo = {(0,0): 1}

    def paths(i, j):
        if (i,j) in memo:
            return memo(i,j)
        else:
            if i == j == 0:
                return 1
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                val = paths(i, j-1) + paths(i-1, j) # one left, one above
                memo[(i,j)] = val
                return val

        

    return paths(m-1, n-1)

