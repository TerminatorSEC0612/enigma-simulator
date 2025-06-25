class Rotor:
    def init(self, wiring, notch='Q', position=0):
        self.wiring = wiring
        self.inverse_wiring = self._invert_wiring(wiring)
        self.notch = notch  # letter where the next rotor should rotate
        self.position = position  # initial position (0–25)
    
    def _invert_wiring(self, wiring):
        result = [''] * 26
        for i, c in enumerate(wiring):
            result[ord(c) - ord('A')] = chr(i + ord('A'))
        return ''.join(result)

    def rotate(self):
        self.position = (self.position + 1) % 26

    def at_notch(self):
        return chr((self.position + ord('A')) % 26) == self.notch

    def encode_forward(self, c):
        index = (ord(c) - ord('A') + self.position) % 26
        subst = self.wiring[index]
        return chr((ord(subst) - ord('A') - self.position + 26) % 26 + ord('A'))

    def encode_backward(self, c):
        index = (ord(c) - ord('A') + self.position) % 26
        subst = self.inverse_wiring[index]
        return chr((ord(subst) - ord('A') - self.position + 26) % 26 + ord('A'))
