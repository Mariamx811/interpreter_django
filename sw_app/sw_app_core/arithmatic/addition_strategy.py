from arithmatic.arithmaticstrategy import ArithmaticStrategy

class AdditionStrategy(ArithmaticStrategy):
    def execute(self, left, right):
        return left + right