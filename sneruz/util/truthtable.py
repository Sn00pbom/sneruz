from itertools import product

from sneruz.proof import Proof


class TruthTable(object):

    def __init__(self, proof: Proof=None):
        super().__init__()
        self._steps = []
        self._rows = []

    def set_column_names(names: list):
        self._columns = names
    
    def add_column(self, prop):
        self._steps.add(prop)

    def set_steps(self, props):
        """Sets steps to props if props is list. If props is Proof, imports steps"""
        if isinstance(props, list):
            self._steps = props
        elif isinstance(props, Proof):
            self._steps = props.get_steps()

    def generate(self):
        pass

    def export_csv(self):
        pass

    def export_md(self):
        pass