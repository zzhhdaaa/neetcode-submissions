class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for c in tokens:
            if c not in ('+', '-', '*', '/'):
                operands.append(int(c))
            else:
                right = operands.pop()
                left = operands.pop()
                if c == '+':
                    operands.append(left + right)
                elif c == '-':
                    operands.append(left - right)
                elif c == '*':
                    operands.append(left * right)
                elif c == '/':
                    operands.append(int(left/right))
        
        return operands[0]