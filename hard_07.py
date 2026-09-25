class Solution:
    def braceExpansionII(self, expression):
        self.s = expression
        self.i = 0

        result = self.parse_expression()

        return sorted(result)

    def multiply(self, a, b):
        result = set()

        for x in a:
            for y in b:
                result.add(x + y)

        return result

    def parse_expression(self):
        result = self.parse_term()

        while self.i < len(self.s) and self.s[self.i] == ',':
            self.i += 1
            result = result | self.parse_term()

        return result

    def parse_term(self):
        result = set([""])

        while self.i < len(self.s) and self.s[self.i] not in "},":
            
            if self.s[self.i] == '{':
                self.i += 1

                current = self.parse_expression()

                self.i += 1   # skip '}'

            else:
                current = set([self.s[self.i]])
                self.i += 1

            result = self.multiply(result, current)

        return result
