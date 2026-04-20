class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = dict()
        for s in strs:
            counter = self.countChars(s)
            if counter not in ana_dict.keys():
                ana_dict[counter] = [s]
            else:
                ana_dict[counter].append(s)
        
        ana_list = []
        for value in ana_dict.values():
            ana_list.append(value)
        
        return ana_list

    def countChars(self, s: str) -> tuple[int]:
        count_list = [0] * 26
        for c in s:
            code = ord(c) - 97
            count_list[code] += 1
        
        return tuple(count_list)