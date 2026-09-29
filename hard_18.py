class Solution:
    def isNumber(self, s):
        s = s.strip()

        if not s:
            return False

        i = 0
        n = len(s)

        # Optional sign
        if s[i] == '+' or s[i] == '-':
            i += 1

        # Digits before decimal point
        digits_before = 0

        while i < n and s[i].isdigit():
            digits_before += 1
            i += 1

        # Decimal point
        digits_after = 0

        if i < n and s[i] == '.':
            i += 1

            while i < n and s[i].isdigit():
                digits_after += 1
                i += 1

        # There must be at least one digit
        if digits_before == 0 and digits_after == 0:
            return False

        # Exponent
        if i < n and (s[i] == 'e' or s[i] == 'E'):
            i += 1

            # Optional exponent sign
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1

            exponent_digits = 0

            while i < n and s[i].isdigit():
                exponent_digits += 1
                i += 1

            # Exponent must contain digits
            if exponent_digits == 0:
                return False

        # Everything must have been consumed
        return i == n
