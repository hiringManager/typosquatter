import Levenshtein
import string
from collections import defaultdict

# pip install levenshtein

# US Keyboard Layout
keyboard_layout = {
    'a': ['q', 'w', 's', 'z'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'e': ['w', 'r', 's', 'd', 'f'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['f', 't', 'y', 'h', 'b', 'v'],
    'h': ['g', 'y', 'u', 'j', 'n', 'b'],
    'i': ['u', 'o', 'k', 'j'],
    'j': ['h', 'u', 'i', 'k', 'm', 'n'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p'],
    'm': ['n', 'j', 'k'],
    'n': ['b', 'h', 'j', 'm'],
    'o': ['i', 'p', 'l', 'k'],
    'p': ['o', 'l'],
    'q': ['a', 'w'],
    'r': ['e', 'd', 'f', 't'],
    's': ['a', 'w', 'e', 'd', 'z', 'x'],
    't': ['r', 'f', 'g', 'y'],
    'u': ['y', 'i', 'j', 'h'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'a', 's', 'e'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 's', 'x']
}

def generate_typos(word):
    typos = set()
    for i in range(len(word)):
        for char in string.ascii_lowercase:
            if char != word[i]:
                typo = word[:i] + char + word[i+1:]
                typos.add(typo)
    return list(typos)

def most_common_typos(word, n):
    typos = generate_typos(word)
    frequencies = defaultdict(int)
    for typo in typos:
        distance = Levenshtein.distance(word, typo)
        frequencies[typo] += 1
    sorted_typos = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return [typo for typo, freq in sorted_typos if typo != word][:n]

word = input("what word?")
n = 9
most_common = most_common_typos(word, n)
print(most_common)
