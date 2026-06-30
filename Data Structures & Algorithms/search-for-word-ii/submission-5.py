class Trie:
    def __init__(self):
        self.prefixes = set()
        self.words = set()
    
    def find(self, word: str) -> bool:
        return word in self.words
    
    def findpre(self, pre: str) -> bool:
        return pre in self.prefixes
    
    def insert(self, word: str):
        for i in range(len(word)):
            self.prefixes.add(word[0:i+1])
        self.words.add(word)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        trie = Trie()
        visit = set()
        res = set()

        for word in words:
            trie.insert(word)
        
        def dfs(r: int, c: int, curr: str):
            if not 0<=r<ROW or not 0<=c<COL or (r,c) in visit:
                return

            curr = curr + board[r][c]
            if not trie.findpre(curr):
                return
            if trie.find(curr):
                res.add(curr)
            
            visit.add((r,c))

            dfs(r+1,c,curr)
            dfs(r-1,c,curr)
            dfs(r,c+1,curr)
            dfs(r,c-1,curr)

            visit.remove((r,c))
        
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, "")
        
        return list(res)