class Solution:
    def intToRoman(self, num: int) -> str:
        res = []

        # M
        count = num//1000
        num %= 1000
        res.append("M"*count)

        # CM, DCCC, DCC, DC, D, CD, CCC, CC, C
        count = num//100
        num %= 100
        if count == 9:
            res.append("CM")
        elif 8 >= count >= 5:
            res.append("D"+"C"*(count-5))
        elif count == 4:
            res.append("CD")
        elif count >= 1:
            res.append("C"*count)
        
        # XC, LXXX, LXX, LX, L, XL, XXX, XX, X
        count = num//10
        num %= 10
        if count == 9:
            res.append("XC")
        elif 8 >= count >= 5:
            res.append("L"+"X"*(count-5))
        elif count == 4:
            res.append("XL")
        elif count >= 1:
            res.append("X"*count)
        
        # IX, VIII, VII, VI, V, IV, III, II, I
        count = num
        if count == 9:
            res.append("IX")
        elif 8 >= count >= 5:
            res.append("V"+"I"*(count-5))
        elif count == 4:
            res.append("IV")
        elif count >= 1:
            res.append("I"*count)
        
        return "".join(res)