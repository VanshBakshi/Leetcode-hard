class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        # Count how many times each word should appear
        target = {}

        for word in words:
            if word in target:
                target[word] += 1
            else:
                target[word] = 1

        result = []

        # Try each possible starting offset
        for offset in range(word_len):
            left = offset
            right = offset
            current = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                # Word is not present in words
                if word not in target:
                    current = {}
                    count = 0
                    left = right
                    continue

                # Add current word
                if word in current:
                    current[word] += 1
                else:
                    current[word] = 1

                count += 1

                # Too many copies of this word
                while current[word] > target[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

                # All words matched
                if count == word_count:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

        return result
