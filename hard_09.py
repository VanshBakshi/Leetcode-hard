class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            else:
                stack.pop()

                # No valid starting point
                if not stack:
                    stack.append(i)

                else:
                    # Length of current valid substring
                    length = i - stack[-1]
                    max_len = max(max_len, length)

        return max_len
