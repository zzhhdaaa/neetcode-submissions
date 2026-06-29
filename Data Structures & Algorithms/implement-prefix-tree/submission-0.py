class PrefixTree:

    def __init__(self):
        self.prefixes = set()
        self.words = set()
        

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            self.prefixes.add(word[0:i+1])
        self.words.add(word)


    def search(self, word: str) -> bool:
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes
        
        