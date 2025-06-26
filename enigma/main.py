from .rotor import Rotor
from .reflector import Reflector
from .plugboard import Plugboard
from .enigma_machine import EnigmaMachine

def get_classic_rotors():
    return [
        Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch='Q'),
        Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", notch='E'),
        Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", notch='V'),
    ]

def get_classic_reflector():
    return Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

def main():
    rotors = get_classic_rotors()
    reflector = get_classic_reflector()
    plugboard = Plugboard([("A", "M"), ("G", "L"), ("E", "T")])

    machine = EnigmaMachine(rotors, reflector, plugboard)

    message = "ENIGMA"
    ciphertext = machine.encrypt_message(message)
    print(f"Plaintext:  {message}")
    print(f"Ciphertext: {ciphertext}")

if __name__ == "__main__":
    main()
