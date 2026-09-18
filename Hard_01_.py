class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid interval for each character
        for c in range(26):
            if first[c] == n:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                idx = ord(s[i]) - ord('a')

                # This character appears before l,
                # so this interval cannot be valid
                if first[idx] < l:
                    valid = False
                    break

                # Expand interval to include all occurrences
                r = max(r, last[idx])
                i += 1

            if valid:
                intervals.append((l, r))

        # Select maximum number of non-overlapping intervals.
        # Sorting by ending position gives the optimal greedy solution.
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result
