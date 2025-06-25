class Plugboard:
    def init(self, wiring_pairs=None):
        self.wiring = self._generate_wiring(wiring_pairs or [])

    def _generate_wiring(self, pairs):
        wiring = {chr(i): chr(i) for i in range(ord('A'), ord('Z')+1)}
        for a, b in pairs:
            wiring[a] = b
            wiring[b] = a
        return wiring

    def swap(self, c):
        return self.wiring.get(c, c)
