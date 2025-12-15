# main.py

from math_utils import add, divide
from string_utils import capitalize_words, is_palindrome

def run_demo():
    print("=== Math Demo ===")
    print("5 + 3 =", add(5, 3))
    print("10 / 2 =", divide(10, 2))

    print("\n=== String Demo ===")
    print(capitalize_words("hello world from python"))
    print("Is 'madam' palindrome?", is_palindrome("madam"))

if __name__ == "__main__":
    run_demo()
