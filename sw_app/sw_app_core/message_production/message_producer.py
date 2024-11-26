from abc import ABC, abstractmethod

class MessageStrategy(ABC):

    @abstractmethod
    def save(self, data):
        """Save the provided data."""
        pass
