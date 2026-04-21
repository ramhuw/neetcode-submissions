class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                cc = stack.pop()
                if self.rev(c) != cc:
                    return False
        return len(stack) == 0
    def rev(self, s: str) -> bool:
        match s:
            case ')':
                return '('
            case '}':
                return '{'
            case ']':
                return '['
            case _:
                return None