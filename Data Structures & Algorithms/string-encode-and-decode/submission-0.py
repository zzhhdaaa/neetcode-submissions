class Solution:

    def encode(self, strs: List[str]) -> str:
        length_str = ""
        for word in strs:
            length_str += str(len(word)) + ","
        length_str += "#"

        encode_str = length_str + "".join(strs)

        return encode_str

    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []
        
        # denote the lengths
        lengths = []
        temp_length = ""
        ptr = 0
        for i in range(len(s)):
            if s[i] == "#":
                ptr = i
                break

            if s[i] == ",":
                lengths.append(int(temp_length))
                temp_length = ""
            else:
                temp_length += s[i]

        # denote the strs
        strs = []
        temp_str = ""
        for length in lengths:
            for i in range(length):
                temp_str += s[ptr+1+i]
            strs.append(temp_str)
            ptr += length
            temp_str = ""
        
        return strs

