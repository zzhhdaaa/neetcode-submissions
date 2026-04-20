class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        
        def backtracking(open: int, close: int, s: str):
            if len(s) == 2*n:
                if open == close:
                    result.append(s)
                return
            
            if open == close:
                backtracking(open+1, close, s+'(')
            elif open > close:
                backtracking(open+1, close, s+'(')
                backtracking(open, close+1, s+')')
            else:
                return

        backtracking(0, 0, "")
        return result
