def uniquePaths(m: int, n: int) -> int:
        dp = []
        # building grid row by row
        # dp is a list of m rows, each containing n zeros — i.e. an m x n grid, all initialized to 0.
        for _ in range(m):
            dp.append([0]*n)

        #starting position
        dp[0][0] = 1

        #iterate through list
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue #ignore base case

                # count dp to the left or above, if there it exists
                val = 0
                if i > 0:
                      val += dp[i-1][j]
                if j > 0:
                      val += dp [i][j-1]

                dp[i][j] = val

        return dp[m-1][n-1]
