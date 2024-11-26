class Context:
    def __init__(self, strategy):
        self.strategy = strategy 

    def executeStrategy(self ,a,  b):
        return self.strategy.execute(a, b)