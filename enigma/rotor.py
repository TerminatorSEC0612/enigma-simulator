from .rotor_utils import invert_wiring

class Rotor:
    def __init__(self, wiring: str, notch: str = 'Z', position: int = 0):
        self.wiring = wiring
        self.inverse_wiring = invert_wiring(wiring)
        self.notch = notch
        self.position = position
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode_forward(self, c: str) -> str:
        idx = (self.alphabet.index(c) + self.position) % 26
        return self.wiring[idx]

    def encode_backward(self, c: str) -> str:
        letter = self.alphabet[(self.inverse_wiring.index(c) - self.position) % 26]
        return letter

    def step(self) -> bool:
        self.position = (self.position + 1) % 26
        return self.alphabet[self.position] == self.notch

