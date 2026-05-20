class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = 0
        num2_int = 0

        for i in range(len(num1)-1, -1, -1):
            power1 = len(num1) - i - 1
            num1_int += int(num1[i]) * 10**power1
            print(num1_int)

        for j in range(len(num2)-1, -1, -1):
            power2 = len(num2) - j - 1
            num2_int += int(num2[j]) * 10**power2
            print(num2_int)
        
        return str(num1_int * num2_int)
        