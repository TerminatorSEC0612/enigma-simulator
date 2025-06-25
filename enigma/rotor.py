class Rotor:
    def __init__(self, wiring, notch="Z"):
        self.wiring = wiring
        self.inverse_wiring = self._invert_wiring(wiring)
        self.position = 0
        self.notch = notch

    def _invert_wiring(self, wiring):
        inverse = [""] * 26
        for i, c in enumerate(wiring):
            inverse[ord(c)-ord("A")] = chr(i + ord("A"))
            return "".join(inverse)
    
    def encode_forward(self,c):
        index = (ord(c) - ord("A") + self.position) % 26
        return self.wiring[index]
    
    def encode_backward(self, c):
        index = (ord(c) - ord("A") + self.position) % 26
        return self.inverse_wiring[index]
    
    def step(self):
        self.position = (self.position + 1) % 26
