from __future__ import annotations
from itertools import permutations


class Prop(object):

    def __init__(self, value: bool, froms: list=None):
        super().__init__()

        if isinstance(froms, list):
            self._froms = froms
        elif isinstance(froms, Prop):
            self._froms = [froms]
        else:
            self._froms = []

        self._value = value

    def __bool__(self):
        return self.deduce()

    def __str__(self):
        return "T" if self.deduce() else "F"

    def deduce(self):
        return self._value

    def is_tautology(self) -> bool:
        # a wff is a tautology if and only if it is true for all possible truth-value assignments to the statement letters making it up.
        return True

    def is_self_contradiction(self) -> bool:
        # a wff is a self-contradiction if and only if it is false for all possible truth-value assignments to the statement letters making it up.
        return True

    def is_contingent(self) -> bool:
        # A contingent statement is true for some truth-value assignments to its statement letters and false for others.
        return True

    def is_logical_consequence_of(self, wffs: list) -> bool:
        # a wff β is said to be a logical consequence of a set of wffs α1, α2, ..., αn, if and only if there is no truth-value assignment to the statement letters making up these wffs that makes all of α1, α2, ..., αn true but does not make β true.
        return True

    def NOT(p: Prop) -> Prop:
        return Prop(bool(not p), p)

    def AND(p: Prop, q: Prop) -> Prop:
        return Prop(bool(p and q), [p, q])

    def OR(p, q: Prop) -> Prop:
        return Prop(bool(p or q), [p, q])

    def XOR(p, q: Prop) -> Prop:
        return Prop(bool((p and not q) or (not p and q)), [p, q])

    def IMPLIES(p, q: Prop) -> Prop:
        return Prop(bool((not p) or (p and q)), [p, q])

    def IFF(p, q: Prop) -> Prop:
        return Prop(bool(((not p and not q) or (p and q))), [p, q])

    @staticmethod
    def is_consistent(wff1, wff2) -> bool:
        # two wffs are consistent if and only if there is at least one possible truth-value assignment to the statement letters making them up that makes both wffs true.
        # two wffs are inconsistent if and only if there is no truth-value assignment to the statement letters making them up that makes them both true.
        pass

    @staticmethod
    def is_logically_equivalent(prop1: Prop, prop2: Prop) -> bool:
        # wo statements are said to be logically equivalent if and only if all possible truth-value assignments to the statement letters making them up result in the same resulting truth-values for the whole statements.
        pass
