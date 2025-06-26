class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def step_rotors(self):
        rotate_next = self.rotors[0].step()
        for i in range(1, len(self.rotors)):
            if rotate_next:
                rotate_next = self.rotors[i].step()
            else:
                break

    def encrypt_letter(self, c: str) -> str:
        if not c.isalpha():
            return c

        self.step_rotors()
        c = self.plugboard.encode(c)

        for rotor in self.rotors:
            c = rotor.encode_forward(c)

        c = self.reflector.reflect(c)

        for rotor in reversed(self.rotors):
            c = rotor.encode_backward(c)

        c = self.plugboard.encode(c)
        return c

    def encrypt_message(self, message: str) -> str:
        result = []
        for char in message.upper():
            result.append(self.encrypt_letter(char))
        return ''.join(result)
