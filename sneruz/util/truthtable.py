from itertools import product

from sneruz.proof import Proof


class TruthTable(object):

    def __init__(self, proof: Proof):
        super().__init__()
        self._columns = []
        self._rows = []
        self._proof = proof

    def generate(self, column_names=None):
        self._columns = column_names
        if column_names is None:
            self._columns = [" " for _ in len(self._proof)]
        
        for v in product([True, False], repeat=len(self._proof.premises)):
            s = []
            for i in range(len(v)):
                self._proof.premises[i].set(v[i])

            for p in self._proof:
                s.append(p())

            self._rows.append(s)

    def export_csv(self):
        pass

    def export_md(self):
        s = [c for c in self._columns]
        print('|'.join(s))
        s = [':---:' for _ in self._columns]
        print('|'.join(s))
        for row in self._rows:
            s = ['T' if r else 'F' for r in row]
            print('|'.join(s))

    def export_html(self):
        pass