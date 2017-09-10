import collections
f = open("/Users/monicasunkara/Downloads/Fall2017/NLP-Sentiment-Analysis/SentimentDataset/Dev/pos.txt")
unigram = collections.defaultdict(int)

bigram = {}

number = 1

for line in f:
    line = "<s>" + " " + line + " " + "</s>"
    wordList = line.split()
    for i in range(len(wordList) - 1):
        word, next_word = wordList[i], wordList[i+1]
        unigram[word]+=1
        if word not in bigram:
            bigram[word] = {}
        if next_word not in bigram[word]:
            bigram[word][next_word] = 0
        bigram[word][next_word]+=1
    unigram["</s>"] += 1

#  generate sentence

import random

# Unigram Random Sentence Generator
count = 0
randomSentence = ""
while (count < 100):
    randomWord = random.choice(list(unigram.keys()))
    if randomWord == "</s>":
        break
    randomSentence = randomSentence + " " + randomWord;
    count = count + 1;

print(randomSentence)

#Bigram Random Sentence Generator
count = 0
prevWord = "<s>";
bigramRandomSentence = ""
my_list = []
while (count < 100):
    iterate = 0;
    for key, value in bigram[prevWord].items():
        my_list = my_list + [key] * value;
    randomWord = random.choice(my_list);
    if randomWord == "</s>":
        break;
    prevWord = randomWord;
    bigramRandomSentence = bigramRandomSentence + " " + randomWord
    count = count + 1

print(bigramRandomSentence)