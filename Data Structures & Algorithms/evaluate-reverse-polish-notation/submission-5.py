class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            operator = None
            match token:
                case '+':
                    operator = lambda a, b: a + b
                case '-':
                    operator = lambda a, b: a - b
                case '*':
                    operator = lambda a, b: a * b
                case '/':
                    operator = lambda a, b: int(a / b)
                case _:
                    stack.append(int(token))
            if operator is not None:
                b = stack.pop()
                a = stack.pop()
                c = operator(a, b)
                stack.append(c)
        return stack[0]