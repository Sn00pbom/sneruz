

class Proof(object):

    def __init__(self):
        super().__init__()
        self._steps = []
        self._premises = []

    def __len__(self):
        return len(self._steps)

    def suppose(self, prop):
        """Add a proposition as a step and a premise"""
        self._steps.append(prop)
        self._premises.append(prop)
    
    def therefore(self, prop):
        """Add a proposition as a step"""
        self._steps.append(prop)

    def get_step(self, prop_i) -> "Prop":
        """Return a step in the sequence from [1,len]"""
        return self._steps[i-1]
    
    def get_steps(self) -> list:
        return self._steps

    def last(self) -> "Prop":
        """Returns the last proposition added"""
        return self._steps[-1]
