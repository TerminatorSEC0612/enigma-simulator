# utils/rotor_utils.py
import os
import pickle
import random
from enigma.rotor import Rotor

def load_or_generate_rotor(filename):
    """
    Loads a rotor wiring from file if it exists, otherwise generates
    a new random rotor wiring, saves it, and returns the Rotor instance.
    """
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            wiring = pickle.load(f)
    else:
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        random.shuffle(letters)
        wiring = ''.join(letters)
        with open(filename, "wb") as f:
            pickle.dump(wiring, f)
    return Rotor(wiring)
