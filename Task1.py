import random
import string

with open("The Adventures of Tom Sawyer.txt", "r") as file:
    text = file.read().lower()

items_for_split = set('~@#$%^&*()’_+:;.,!?\”‘-“[]{}|<>—/"')
items_for_split.update(string.whitespace)

tokens = []
currentWord = []
for item in text:
    if item in items_for_split:
        if currentWord:
            tokens.append(''.join(currentWord))
            currentWord = []
    else:
        currentWord.append(item)
if currentWord:
    tokens.append(''.join(currentWord))

token_dict = {}
for i in range(len(tokens) - 1):
    token = tokens[i]
    next_token = tokens[i + 1]
    if token in token_dict:
        token_dict[token].append(next_token)
    else:
        token_dict[token] = [next_token]

word = random.choice(list(token_dict.keys()))
newText = [word]

for i in range(201):
    next_words = token_dict.get(word, [""])
    word = random.choice(next_words)
    newText.append(word)

print(" ".join(newText))
