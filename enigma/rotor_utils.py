import random
import string

def invert_wiring(wiring: str) -> str:
    inverse = [''] * 26
    for i, letter in enumerate(wiring):
        index = ord(letter) - ord('A')
        inverse[index] = chr(ord('A') + i)
    return ''.join(inverse)

def generate_random_wiring(seed: int = None) -> str:
    alphabet = list(string.ascii_uppercase)
    if seed is not None:
        random.seed(seed)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def validate_wiring(wiring: str) -> bool:
    return len(wiring) == 26 and sorted(wiring) == list(string.ascii_uppercase)