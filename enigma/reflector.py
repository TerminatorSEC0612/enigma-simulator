class Reflector:
    def __init__(self, wiring: str):
        self.wiring = wiring
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def reflect(self, c: str) -> str:
        idx = self.alphabet.index(c)
        return self.wiring[idx]




