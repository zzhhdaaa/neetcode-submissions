class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for c in s:
            if c in ('(', '{', '['):
                brackets.append(c)
            else:
                if len(brackets) != 0 and self.isMatch(brackets[-1], c):
                    brackets.pop()
                else:
                    return False
        
        return len(brackets) == 0
    
    def isMatch(self, left: str, right: str) -> bool:
        if left == '(' and right == ')':
            return True
        elif left == '{' and right == '}':
            return True
        elif left == '[' and right == ']':
            return True
        else:
            return False
