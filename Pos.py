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

unigramDictionary = dict()
bigramDictionary = dict()

for line in f:
	corpusList = corpusList + line.split()
	lineList = line.split()
	
	for i in range(0,len(lineList)-1):
		bigramList.append(lineList[i]+lineList[i+1])
count = 0
randomSentence = ""
while (count < 10):
	randomSentence = randomSentence + " " + random.choice(corpusList)
	count = count + 1

print (randomSentence)
#print (unigramFunction(corpusList))
#print (bigramFunction(bigramList))

