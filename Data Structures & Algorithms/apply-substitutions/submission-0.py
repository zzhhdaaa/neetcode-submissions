class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mapping = dict()
        for key, val in replacements:
            mapping[key] = val
        
        clean = False
        while not clean:
            chars = []
            key = ''
            checking = False
            clean = True
            for i in range(len(text)):
                if checking:
                    if text[i] == '%':
                        checking = False
                        chars.append(mapping[key])
                    else:
                        key = text[i]
                    continue
                if text[i] == '%':
                    checking = True
                    clean = False
                else:
                    chars.append(text[i])
            text = "".join(chars)
        
        return text
