import random
import re

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# print(words)

words = re.split("[ \n]+", words)
words = [w for w in words if len(w) > 0]

STOP_CHARS = ['.', '?', '!']

word_dict = {}
def create_table(word_list):
    """
    creates dictionary of words with the words that appear next to them
    as well as classifying each word as start or stop, if applicable
    and whether or not they include a quote
    """
    def classify_word(word):
        """
        classifies each word as start/stop, whether or not it has quotes.
        """
        classification = {"start": False, "stop": False, "quote": False}
        
        if word[0].lower() != word[0]:
            classification["start"] = True
        elif len(word) >= 2:
            if (word[0] == '"' and word[1].lower() != word[1]):
                classification["start"] = True
                classification["quote"] = True

        if word[-1] in STOP_CHARS:
            classification["stop"] = True
        elif len(word) >= 2:
            if (word[-2] in STOP_CHARS and word[-1] == '"'):
                classification["stop"] = True
                classification["quote"] = True

        return classification
        
    i = 0
    while i < len(word_list) - 1:
        cur = word_list[i]
        nxt = word_list[i+1]
        if cur in word_dict:
            word_dict[cur]["next"].append(nxt)
        else:
            word_dict[cur] = {"classification": classify_word(cur), "next": [nxt]}
        i += 1
    cur = word_list[i]
    if cur not in word_dict:
        word_dict[cur] = {"classification": classify_word(cur), "next": []}

def construct_sentence():
    """
    creates sentence randomly with a random start word, traveling through a chain of random "next" words
    stopping when a stop word is reached.
    """
    start = random.choice(list({k for (k,v) in word_dict.items() if v["classification"]["start"] == True}))
    sentence = [start]
    cur = start
    stop = word_dict[cur]["classification"]["stop"]
    while not stop:
        nxt = random.choice(word_dict[cur]["next"])
        sentence.append(nxt)
        cur = nxt
        stop = word_dict[cur]["classification"]["stop"]
    return ' '.join(sentence)

create_table(words)

print(construct_sentence())