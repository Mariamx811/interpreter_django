import json
import os
import re


class EquationReader:
    """
    Responsible for fetching the equation from a configuration file and resolving variables.
    """

    def read_formula(self):
        """Fetch the formula from the configuration file."""
        with open(self.config_file,"r") as file:
            config = json.load(file)
        return config

    def resolve_variables(self, formula, variable_resolver):
        """Substitute variables in the formula."""
        return re.sub(r'\bATTR\b',str(variable_resolver),formula)


