class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        # dp[i][j] = whether s[i:] matches p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[m][n] = True

        # Fill table from bottom-right
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                # Check if current characters match
                first_match = (
                    i < m and
                    (s[i] == p[j] or p[j] == '.')
                )

                # If next character is '*'
                if j + 1 < n and p[j + 1] == '*':
                    # Option 1: '*' matches zero characters
                    # Option 2: '*' matches current character
                    dp[i][j] = (
                        dp[i][j + 2] or
                        (first_match and dp[i + 1][j])
                    )

                else:
                    # Normal single-character match
                    dp[i][j] = (
                        first_match and dp[i + 1][j + 1]
                    )

        return dp[0][0]
