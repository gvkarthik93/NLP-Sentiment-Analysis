f = open("/Users/karthik/Development/NLP-Sentiment-Analysis/SentimentDataset/Train/pos.txt")

unigramCorpusList = list()
bigramCorpusList = list()
uniqueUnigramCorpusList = list()
uniqueBigramCorpusList = list()

unigramCountDictionary = dict()
bigramCountDictionary = dict()

probabilityMatrixData = dict()

for line in f:
	line = "#start#" + " " + line + " " + "#stop#"
	unigramCorpusList = unigramCorpusList + line.split()
	biGramLine = line.split()
	for x in range(0,len(biGramLine)-1):
		bigramCorpusList.append(biGramLine[x] + " " + biGramLine[x+1])

uniqueUnigramCorpusList = list(set(unigramCorpusList));
uniqueBigramCorpusList = list(set(bigramCorpusList));

for x in uniqueUnigramCorpusList:
	wordCount = unigramCorpusList.count(x)
	unigramCountDictionary[x] = wordCount

for y in uniqueBigramCorpusList:
	bigramWordCount = bigramCorpusList.count(y)
	bigramCountDictionary[y] = bigramWordCount

for k in range(0,len(uniqueUnigramCorpusList)):
	rowDictionary = dict()
	for j in range(0,len(uniqueUnigramCorpusList)):
		bigramString = uniqueUnigramCorpusList[k] + " " + uniqueUnigramCorpusList[j]
		print (bigramString)
		try:
			probabilityValue = bigramCorpusList.count(bigramString) / unigramCorpusList(uniqueUnigramCorpusList[k])
		except:
			probabilityValue = 0
		rowDictionary[uniqueUnigramCorpusList[j]] = probabilityValue
	probabilityMatrixData[uniqueUnigramCorpusList[k]] = rowDictionary


