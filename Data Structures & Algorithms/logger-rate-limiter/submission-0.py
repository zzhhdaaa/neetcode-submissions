class Logger:

    def __init__(self):
        self.interval = 10
        self.cooldown = dict() # message -> cooldown til
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.cooldown and self.cooldown[message] > timestamp:
            return False
        else:
            self.cooldown[message] = timestamp + self.interval
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
