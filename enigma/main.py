from .rotor import Rotor
import random
import string
from .reflector import Reflector
from .plugboard import Plugboard
from .enigma_machine import EnigmaMachine

def get_classic_rotors():
    return [
        Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch='Q'),
        Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", notch='E'),
        Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", notch='V'),
    ]

def generate_random_wiring():
    letters = list(string.ascii_uppercase)
    random.shuffle(letters)
    return ''.join(letters)

def get_random_rotors():
    rotors = []
    for _ in range(3):
        wiring = generate_random_wiring()
        notch = random.choice(string.ascii_uppercase)
        position = random.randint(0,25)
        rotor = Rotor(wiring=wiring, notch=notch, position=position)
        rotors.append(rotor)
    return rotors

def get_classic_reflector():
    return Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

def main():
    mode = input("Select rotor mode: (1) Classic (2) Random: ")
    if mode == "1":
        rotors = get_classic_rotors()
    elif mode == "2":
        rotors = get_random_rotors()
    else:
        print("Envalid mode selected.")
        return
    
    reflector = get_classic_reflector()
    plugboard = Plugboard([("A", "M"), ("G", "L"), ("E", "T")])

    machine = EnigmaMachine(rotors, reflector, plugboard)

    message = input("Please Enter a message")
    ciphertext = machine.encrypt_message(message)
    print(f"Plaintext:  {message}")
    print(f"Ciphertext: {ciphertext}")

if __name__ == "__main__":
    main()
