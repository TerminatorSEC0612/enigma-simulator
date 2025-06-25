from enigma.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.enigma_machine import EnigmaMachine
from utils.rotor_utils import load_or_generate_rotor

def get_classic_rotors():
    return [       
        Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch='Q'),  # Rotor I
        Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", notch='E'),  # Rotor II
        Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", notch='V')   # Rotor III
    ]

def get_random_rotors():
    return [
        load_or_generate_rotor("rotor1.pkl"),
        load_or_generate_rotor("rotor2.pkl"),
        load_or_generate_rotor("rotor3.pkl")
    ]

def main():
    mode = input("Select rotor mode: (1) Classic (2) Random: ").strip()
    
    if mode == "1":
        rotors = get_classic_rotors()
    elif mode == "2":
        rotors = get_random_rotors()
    else:
        print("Invalid option.")
        return

    plugboard = Plugboard([("A", "M"), ("F", "I"), ("N", "V")])
    machine = EnigmaMachine(rotors, plugboard)

    plaintext = input("Enter message: ")
    ciphertext = machine.encrypt_message(plaintext)

    print("Encrypted:", ciphertext)

if __name__ == "__main__":
    main()
