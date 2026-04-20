class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def validate(s: str) -> bool:
            open = 0

            for c in s:
                if c == '(':
                    open += 1
                else:
                    open -= 1
                if open < 0:
                    return False

            return open == 0
        
        def dfs(s: str):
            if len(s) == 2 * n:
                if validate(s):
                    result.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs('')
        return result
            



