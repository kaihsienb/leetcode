class ModdedIntBase:
    pass


def ModdedInt(MOD):
    class ModdedInt(ModdedIntBase):
        _MOD = MOD

        def __init__(self, val: int):
            self.val = val % MOD

        def _check_type(self, other):
            match other:
                case ModdedInt():
                    if other._MOD != MOD:
                        raise ValueError(
                            "Cannot operate on ModdedInts with different moduli"
                        )
                    return other.val
                case int():
                    return other % MOD
                case _:
                    return NotImplemented

        def __add__(self, other):
            val = self._check_type(other)
            if val is NotImplemented:
                return NotImplemented
            return ModdedInt(self.val + val)

        def __radd__(self, other):
            return self.__add__(other)

        def __sub__(self, other):
            val = self._check_type(other)
            if val is NotImplemented:
                return NotImplemented
            return ModdedInt(self.val - val)

        def __rsub__(self, other):
            val = self._check_type(other)
            if val is NotImplemented:
                return NotImplemented
            return ModdedInt(val - self.val)

        def __mul__(self, other):
            val = self._check_type(other)
            if val is NotImplemented:
                return NotImplemented
            return ModdedInt(self.val * val)

        def __rmul__(self, other):
            return self.__mul__(other)

        def __pow__(self, exp):
            if not isinstance(exp, int):
                return NotImplemented
            if exp == 1:
                return self
            if exp % 2 == 1:
                return self * (self ** (exp - 1))
            return (self * self) ** (exp // 2)

        def __neg__(self):
            return ModdedInt(-self.val)

        def __eq__(self, other):
            val = self._check_type(other)
            if val is NotImplemented:
                return NotImplemented
            return self.val == val

        def __ne__(self, other):
            val = self._check_type(other)
            if val is NotImplemented:
                return NotImplemented
            return self.val != val

    return ModdedInt
