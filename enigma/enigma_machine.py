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
        ciphertext = ''
        for char in message:
            if not char.isalpha():
                ciphertext += char
                continue
            char = char.upper()

            # --- Rotor stepping logic ---
            if self.rotors[1].at_notch():
                self.rotors[0].rotate()
                self.rotors[1].rotate()  # double stepping
            elif self.rotors[2].at_notch():
                self.rotors[1].rotate()

            self.rotors[2].rotate()

            # --- Encryption process ---
            for rotor in reversed(self.rotors):
                char = rotor.encode_forward(char)
            char = self.plugboard.swap(char)
            for rotor in self.rotors:
                char = rotor.encode_backward(char)

            ciphertext += char
        return ciphertext