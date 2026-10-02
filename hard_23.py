class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            if a == b:
                return True

            if len(a) != len(b):
                return False

            # If both strings don't have the same characters,
            # they cannot be scrambled versions of each other.
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            n = len(a)

            # Try every possible split
            for i in range(1, n):
                # Case 1: No swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True

                # Case 2: Swap
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
