class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordMap = defaultdict(list) # key is starting letter, value is a list of word
        for word in wordDict:
            wordMap[word[0]].append(word)
        
        LEN = len(s)
        suffix = defaultdict(list)

        def dfs(i: int):
            # successfully reach the end
            if i == LEN:
                return [""]
            
            # nothing to append
            if s[i] not in wordMap:
                suffix[i] = []
                return suffix[i]
            
            # check memo
            if i in suffix:
                return suffix[i]
            
            # try to append new words
            res = []
            for word in wordMap[s[i]]:
                target = i + len(word)
                if target <= LEN and word == s[i:target]:
                    next_suffixes = dfs(target)
                    
                    for suf in next_suffixes:
                        if suf == "":
                            res.append(word)
                        else:
                            res.append(word + " " + suf)
            suffix[i] = res
            return res
        
        return dfs(0)
                