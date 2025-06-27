import pickle
import os

ROTORS_FILE = "random_rotors.pkl"

def save_rotors(rotors):
    with open(ROTORS_FILE, "wb") as f:
        pickle.dump(rotors, f)

def load_rotors():
    if os.path.exists(ROTORS_FILE):
        with open(ROTORS_FILE, "rb") as f:
            return pickle.load(f)
    return None
