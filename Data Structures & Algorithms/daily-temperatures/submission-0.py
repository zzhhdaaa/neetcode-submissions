class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 30, 38, 30, 36, 35, 40, 28
        # __ -> put [30, 0] in a stack
        #     __ -> remove [30, 0] from the stack, add [38, 1] to the stack
        # the newest item in stack is always the easiest to satisfy

        stack = []
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            temperature = temperatures[i]

            # when we want to pop:
            # the latest in the stack is less than the current
            # when we want to append:
            # always
            while len(stack) != 0 and stack[-1][0] < temperature:
                item = stack.pop()
                result[item[1]] = i - item[1]
            
            stack.append([temperature, i])
        
        return result