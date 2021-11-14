# get the frequency of each word in "The World of Chance" and replace
# it with the another word of the same frequency
from random import choice

world = open("chance.txt", "r")

p = {}
for line in world:
    for word in line.split():
        if p.get(word, None):
            p[word] += 1
        else:
            p[word] = 1


words = {}
for key, val in p.items():
    if words.get(val, None):
        words[val].append(key)
    else:
        words[val] = [key]

novel = open("novel.txt", "w+")
world.seek(0, 0)


def matchcase(word, new):
    if word.isupper():
        return new.upper()
    elif word[0].isupper():
        return new.lower().capitalize()
    else:
        return new.lower()


for line in world:
    word = ""
    whitespace = ""
    for i in range(len(line)):
        if not line[i].isspace():
            if whitespace != "":
                novel.write(whitespace)
                whitespace = ""
            word += line[i]
        else:
            if word != "":
                novel.write(matchcase(word, choice(words[p[word]])))
                word = ""
            whitespace += line[i]
    novel.write("\n")

novel.close()
world.close()
