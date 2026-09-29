class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line_words = []
            line_length = 0

            # Pick as many words as possible
            while i < len(words):
                word_length = len(words[i])

                if line_length + word_length + len(line_words) > maxWidth:
                    break

                line_words.append(words[i])
                line_length += word_length
                i += 1

            # Last line or line with only one word
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)
                continue

            # Number of spaces that need to be distributed
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            # Minimum spaces per gap
            spaces = total_spaces // gaps

            # Extra spaces go to the left gaps
            extra = total_spaces % gaps

            line = ""

            for j in range(gaps):
                line += line_words[j]
                line += " " * (spaces + (1 if j < extra else 0))

            line += line_words[-1]

            result.append(line)

        return result
