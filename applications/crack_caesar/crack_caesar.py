# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

import re

# Read in all the words in one go
with open("applications/crack_caesar/ciphertext.txt") as f:
    words = f.read()

freqs = {"E":0.1153,"T":0.0975,"A":0.0846,"O":0.0808,"H":0.0771,"N":0.0673,"R":0.0629,"I":0.0584,"S":0.0556,"D":0.0474,"L":0.0392,"W":0.0308,"U":0.0259,"G":0.0248,"F":0.0242,"B":0.0219,"M":0.0218,"Y":0.0202,"C":0.0158,"P":0.0108,"K":0.0084,"V":0.0059,"Q":0.0017,"J":0.0007,"X":0.0007,"Z":0.0003}

letter_dist = {}
for char in freqs:
    letter_dist[char] = {"freq": 0, "match": None}

for char in words:
    if char in letter_dist:
        letter_dist[char]["freq"] += 1

letter_dist = {k: v for k, v in sorted(letter_dist.items(), key=lambda x: x[1]["freq"], reverse=True)}

freq_list = list(freqs.keys())

i = 0
for c in letter_dist:
    letter_dist[c]["match"] = freq_list[i]
    i += 1

new_words = [c if c not in letter_dist else letter_dist[c]["match"] for c in words]

new_words = ''.join(new_words)

print(new_words)