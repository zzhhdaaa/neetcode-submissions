class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # first, we format the word into pattern map: cat -> *at, c*t, ca*
        wordToPat = defaultdict(list)
        patToWord = defaultdict(list) # key: pattern -> value: a list of words
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pat = word[0:i] + '*' + word[i+1:len(word)]
                wordToPat[word].append(pat)
                patToWord[pat].append(word)
        
        print(wordToPat)

        # then, we perform a bfs to find the shortest path
        queue = deque()
        queue.append([beginWord, 0])
        visit = set()

        while queue:
            currWord, path = queue.popleft()

            # find result
            if currWord == endWord:
                return path+1
            
            # check visit
            if currWord in visit:
                continue
            visit.add(currWord)

            # spread out
            for pat in wordToPat[currWord]:
                print(pat)
                for word in patToWord[pat]:
                    print(word)
                    if word != currWord:
                        print(word, path+1)
                        queue.append([word, path+1])
        
        # not found
        return 0

            
