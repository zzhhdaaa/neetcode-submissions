import bisect

class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap.keys():
            self.timeMap[key] = [[timestamp], [value]]
        else:
            i = bisect.bisect_left(self.timeMap[key][0], timestamp)
            self.timeMap[key][0].insert(i, timestamp)
            self.timeMap[key][1].insert(i, value)
        
        print(self.timeMap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap.keys():
            return ""
        
        i = bisect.bisect_right(self.timeMap[key][0], timestamp)
        
        if i == 0:
            return ""
        return self.timeMap[key][1][i-1]

