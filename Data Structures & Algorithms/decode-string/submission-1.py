class Solution:
    def decodeString(self, s: str) -> str:
        def is_digit(c: str) -> bool:
            if (c=='0' or c=='1' or c=='2' or c=='3' or c=='4' or 
                c=='5' or c=='6' or c=='7' or c=='8' or c=='9'):
                return True
            return False
        
        res = []
        encoded_stack = [] # the encoded char stack [List[char], multiplier]
        multiplier = 0

        for i in range(len(s)):
            c = s[i]
            if is_digit(c):
                multiplier = multiplier * 10 + int(c)
            elif c == '[':
                # new open bracket, start a new one in encoded stack, take the multiplier
                encoded_stack.append([[], multiplier])
                multiplier = 0
            elif c == ']':
                # closing, means that we need to decode the last one in the stack
                curr, mul = encoded_stack.pop()
                curr = ("".join(curr))*mul
                if encoded_stack:
                    encoded_stack[-1][0].append(curr)
                else:
                    res.append(curr)
            else:
                # appending to stack, or to result
                if encoded_stack:
                    encoded_stack[-1][0].append(c)
                else:
                    res.append(c)
        return "".join(res)
