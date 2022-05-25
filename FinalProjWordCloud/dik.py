import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys


def thingy(puncuations, word):
    punc = []
    for p in punctuations:
        punc += p
    rWord = []
    for letter in word:
        if letter not in punc:
            rWord += letter
        else:
            continue
    return "".join(rWord)

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = "!()[]{};:'\"\,<>./?@#$%^&*_~"
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just", "in", "for", "on", "into", "not"]

    # LEARNER CODE START HERE
    wordClouds = {}
    file_contents = file_contents.split()
    for item in file_contents:
        if item.lower() not in uninteresting_words:
            thingy(puncuations, item)
            if item in wordClouds:
                wordClouds[item] += 1
            else:
                wordClouds[item] = 1
        else:
            continue
    # print(wordClouds)
    wordClouds = dict(sorted(wordClouds.items(), key=lambda item: item[1]))
    del wordClouds
    # The fact that I had a function to do the whole punctuation splitting and you wouldn't let me use it sucks. Jupyter books kinda suck
    print(wordClouds)
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(wordClouds)
    cloud.to_file('cloud.png')

# if __name__ == '__main__':
#     with open("pypro.txt", "r") as f:
#         data = f.read().replace('\n', '')
#     calculate_frequencies(data)
#     f.close()

#using dict comprehensions
sentence = "This is a long sentence that I have just written up for an example!"
dicto = {char:  sentence.count(char) for char in set(sentence)}
print(dicto)#This returns a dictionary with the letter and amount of times it shows up in your sentence
#output:
print({k: v for k, v in sorted(dicto.items(), key=lambda item: item[1])})