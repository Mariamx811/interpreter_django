import re

class RegexStrategy:
    def execute(self, text, pattern):
        """Check if the pattern matches the text."""
        return bool(re.search(pattern, text, re.IGNORECASE))
