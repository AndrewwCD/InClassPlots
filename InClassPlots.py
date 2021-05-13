import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

_20k_text = np.loadtxt("20k.txt",dtype = str)
_20k_text_lengths = [len(i) for i in _20k_text]
_20k_text_bins = np.linspace(0,np.amax(_20k_text_lengths),15)
plt.hist(_20k_text_lengths,bins="auto")
plt.title("20k.txt Word Length Histogram")
plt.xlabel("Word Length")
plt.ylabel("Occurrence")
plt.show()

'''
char_frequency = {}
for word in _20k_text:
    for letter in word:
        if letter in _20k_text:
            char_frequency [letter] += 1
        else:
            char_frequency [letter] = 1
'''
_20k_concatenated = ''.join(map(str,_20k_text))
char_frequency = Counter(_20k_concatenated)
letter = char_frequency.keys()
occurrence = char_frequency.values()
plt.bar(letter,occurrence)
plt.xlabel("Letter")
plt.ylabel("Occurrence")
plt.title("20k.txt Letter Occurrence")
plt.show()

print(char_frequency)