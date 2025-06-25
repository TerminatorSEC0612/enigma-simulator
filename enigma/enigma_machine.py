from .rotor import Rotor
from .plugboard import Plugboard

class EnigmaMachine:
    def init(self, rotors, plugboard):
        self.rotors = rotors 
        self.plugboard = plugboard

    def step_rotors(self):
        self.rotors[-1].step()

    def encrypt_char(self, c):
        if not c.isalpha():
            return c

        c = c.upper()

        self.step_rotors()

        c = self.plugboard.swap(c)

        for rotor in reversed(self.rotors):
            c = rotor.encode_forward(c)

        c = chr(ord('Z') - (ord(c) - ord('A')))


        for rotor in self.rotors:
            c = rotor.encode_backward(c)

        c = self.plugboard.swap(c)
        return c

    def encrypt_message(self, message):
        return ''.join(self.encrypt_char(c) for c in message)
