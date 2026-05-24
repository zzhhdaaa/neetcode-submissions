class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordMap = defaultdict(list) # key is starting letter, value is a list of word
        for word in wordDict:
            wordMap[word[0]].append(word)
        
        LEN = len(s)
        curr = ""
        res = []
        def dfs(i: int):
            nonlocal curr

            # successfully reach the end
            if i == LEN:
                res.append(curr)
                return
            
            # nothing to append
            if s[i] not in wordMap:
                return
            
            # try to append new words
            for word in wordMap[s[i]]:
                target = i + len(word)
                if target <= LEN and word == s[i:target]:
                    back = len(curr)
                    curr = curr + ("" if back==0 else " ") + word
                    dfs(target)
                    curr = curr[:back]
        
        dfs(0)
        return res
                