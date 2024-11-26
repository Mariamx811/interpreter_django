from arithmatic.arithmaticstrategy import ArithmaticStrategy

class SubtractionStrategy(ArithmaticStrategy):
    def execute(self, left, right):
        return left - right
