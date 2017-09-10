import collections
sentence = ["I am coding this crap .",
        "But I have no idea !",
        "I am coding still ."]

f = open("/Users/karthik/Development/NLP-Sentiment-Analysis/SentimentDataset/Train/pos.txt")
unigram = collections.defaultdict(int)

bigram = {}

# word_count = collections.defaultdict(int)

# collections.defaultdict

# fopen

for line in f:
    line = ["#Start#"]+line.split()
    # for word in line:
    #   # unigram[word] += 1
    #   pass
    for i in range(len(line)-1):
        word, next_word = line[i], line[i+1]
        unigram[word]+=1
        
        if word not in bigram:
            # bigram[word] = collections.defaultdict(int)
            bigram[word] = {}
        if next_word not in bigram[word]:
            bigram[word][next_word] = 0
        bigram[word][next_word]+=1
print (unigram)
print (bigram)

#  generate sentence

import random

print (random.uniform(0,1))