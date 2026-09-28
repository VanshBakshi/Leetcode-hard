class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        result = []

        # Factorials
        factorial = 1
        for i in range(1, n):
            factorial *= i

        # Convert k to 0-based index
        k -= 1

        while numbers:
            index = k // factorial
            result.append(str(numbers[index]))
            numbers.pop(index)

            if not numbers:
                break

            k %= factorial
            factorial //= len(numbers)

        return "".join(result)
