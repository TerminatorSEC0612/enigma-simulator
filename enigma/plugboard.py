class Plugboard:
    def __init__(self, wiring_pairs=None):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.wiring = self._generate_wiring(wiring_pairs or [])

    def _generate_wiring(self, pairs):
        wiring = dict(zip(self.alphabet, self.alphabet))
        for a, b in pairs:
            wiring[a] = b
            wiring[b] = a
        return wiring

    def encode(self, c: str) -> str:
        return self.wiring.get(c, c)