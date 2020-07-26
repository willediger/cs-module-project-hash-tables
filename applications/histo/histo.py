import re

# Read in all the words in one go
with open("applications/histo/robin.txt") as f:
    words = f.read()

words = re.sub('[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&\!\?]+', '', words.lower())
words = re.split("[ \n]+", words)
words = [w for w in words if len(w) > 0]

word_dist = {}
for word in words:
    if word in word_dist:
        word_dist[word] += 1
    else:
        word_dist[word] = 1

word_dist = {k: v for k, v in sorted(word_dist.items(), key=lambda x: x[1], reverse=True)}

max_len = max([len(k) for k, v in word_dist.items()])

for word in word_dist.items():
    print(word[0] + " "*(max_len-len(word[0])+2) + "#"*word[1])