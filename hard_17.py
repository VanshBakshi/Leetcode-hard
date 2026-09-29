class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # First character must be '('
        if grid[0][0] == ')':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Balance after starting cell
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # From top
                if i > 0:
                    for balance in dp[i - 1][j]:

                        if grid[i][j] == '(':
                            new_balance = balance + 1
                        else:
                            new_balance = balance - 1

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

                # From left
                if j > 0:
                    for balance in dp[i][j - 1]:

                        if grid[i][j] == '(':
                            new_balance = balance + 1
                        else:
                            new_balance = balance - 1

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

        # Valid path must finish with balance 0
        return 0 in dp[m - 1][n - 1]
