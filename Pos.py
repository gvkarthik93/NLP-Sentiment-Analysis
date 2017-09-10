import random
import numpy as np
import random

def unigramFunction(corpusList):
	for x in corpusList:
		wordCount = corpusList.count(x)
		unigramDictionary[x] = wordCount
	return unigramDictionary

def bigramFunction(corpusList):
	for x in corpusList:
		wordCount = corpusList.count(x)
		bigramDictionary[x] = wordCount
	return bigramDictionary

f = open("/Users/monicasunkara/Downloads/Project1/SentimentDataset/Dev/pos.txt")

corpusList = list()
bigramList = list()
uniqueCorpusList = list()

unigramDictionary = dict()
bigramDictionary = dict()

# Generating corpus list
for line in f:
	line = "<s>" + " " + line + " " + "</s>"
	corpusList = corpusList + line.split()
	lineList = line.split()
	
	for i in range(0,len(lineList)-1):
		bigramList.append(lineList[i]+ " " + lineList[i+1])

uniqueCorpusList = list(set(corpusList));

#Bigram Probability Matrix
corpusUniqueWordCount = len(uniqueCorpusList);
corpusWordCount = len(corpusList);

print (corpusWordCount)
print (corpusUniqueWordCount)

#bigramMatrix = np.zeros((corpusUniqueWordCount, corpusUniqueWordCount), np.float64);
bigramMatrix = np.zeros((10,10), np.float64);

print(uniqueCorpusList[0])
for i in range(0, 10):
	for j in range(0, 10):
		word1 = uniqueCorpusList[i];
		countOfWord = corpusList.count(word1);
		word2 = uniqueCorpusList[j];
		concatWord = word1 + " " + word2;
		countOfConcatWord = bigramList.count(concatWord);
		bigramProb = countOfConcatWord/countOfWord;
		bigramMatrix[i][j] = bigramProb;

# Unigram Random Sentence Generator
count = 0
randomSentence = ""
while (count < 10000):
	randomWord = random.choice(corpusList)
	if randomWord == "</s>":
		break
	randomSentence = randomSentence + " " + randomWord;
	count = count + 1;

#Bigram Random Sentence Generator
count = 0
prevWord = "<s>";
bigramRandomSentence = ""
while (count < 100):
	iterate = 0;
	for key, value in bigramDic[prevWord].iteritems():
		my_list = my_list + [key] * value;
	randomWord = random.choice(my_list);
	if randomWord == "</s>":
		break;
	prevWord = randomWord;
	bigramRandomSentence = bigramRandomSentence + " " + randomWord
	count = count + 1

print(bigramRandomSentence)

#print (unigramFunction(corpusList))
#print (bigramFunction(bigramList))

