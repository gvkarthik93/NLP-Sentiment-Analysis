import collections
sentence = ["I am coding this crap .",
		"But I have no idea !",
		"I am coding still ."]
unigram = collections.defaultdict(int)
delimiter = set([".", "!", "?"])

bigram = {}

# word_count = collections.defaultdict(int)

# collections.defaultdict

# fopen

def generate_n_grams():
	
	for line in sentence:
		line = ["#Start#"]+line.split()
		for i in range(len(line)-1):
			word, next_word = line[i].lower(), line[i+1].lower()
			unigram[word]+=1
			
			if word not in bigram:
				# bigram[word] = collections.defaultdict(int)
				bigram[word] = {}
			if next_word not in bigram[word]:
				bigram[word][next_word] = 0
			bigram[word][next_word]+=1
		unigram[next_word] += 1
	# print unigram
	# print bigram
	
generate_n_grams()
# unigram and bigram generated

#  generate sentences now

import random

def random_sentence_generator_unigram():
	# print unigram
	def pick_random_word_unigram():
		rand_val = random.uniform(0,1) * len(unigram)-1
		total = 0
		for k, v in unigram.items():
			total += v
			if rand_val <= total:
				return k
	
	word = pick_random_word_unigram()
	while word in delimiter:
		word = pick_random_word_unigram()
	sentence = ""
	# while (word != "." or word != "!" or word != "?") and len(sentence) < 100:
	while len(sentence) <100:
		if word in delimiter:
			break
		sentence += word + " "
		word = pick_random_word_unigram()
		
	return sentence+word
	
for i in range(5):
	print random_sentence_generator_unigram()


def random_sentence_generator_bigram():
	def pick_random_word_bigram():
		rand_val = random.uniform(0,1) * len(unigram)-1
		total = 0
		for k, v in unigram.items():
			total += v
			if rand_val <= total:
				return k
	
	word = pick_random_word_unigram()
	while word in delimiter:
		word = pick_random_word_unigram()
	sentence = ""
	# while (word != "." or word != "!" or word != "?") and len(sentence) < 100:
	while len(sentence) <100:
		if word in delimiter:
			break
		sentence += word + " "
		word = pick_random_word_unigram()
		
	return sentence+word
	
	
