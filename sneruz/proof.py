

class Proof(object):

    def __init__(self, steps: list=None):
        super().__init__()
        self._steps =  steps if steps else []

    def __len__(self):
        return len(self._steps)
    
    def add_step(self, prop):
        self._steps.append(prop)

    def get_step(self, prop_i) -> "Prop":
        """Return a step in the sequence from [1,len]"""
        return self._steps[i-1]

    def last(self) -> "Prop":
        """Returns the last proposition added"""
        return self._steps[-1]
