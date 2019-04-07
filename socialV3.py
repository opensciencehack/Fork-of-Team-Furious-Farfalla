import glob
import time
import ujson
import nltk
import os

from nltk.corpus import stopwords
from collections import defaultdict

ITERATIONS = 100000
print("Starting Social Program")


sr = stopwords.words('english')
start_time = time.time()

subcnt = defaultdict(int)
tokens = []
print(os.getcwd())

file_to_open = 'data_new/RC_2016-11-08'


print( os.path.isfile(file_to_open))
i = 0
for fn in glob.iglob(file_to_open):
	with open(fn) as f:
		for line in f:
			# print(line)
			jo = ujson.loads(line)
			body = jo['body']
			tokens += [t for t in body.split()]
			i += 1
			if(i> ITERATIONS):
				break
#			print(jo['body'])
#			subcnt[jo['subreddit']] += 1

clean_tokens = list()
political_words = ['donald','trump','hillary','clinton']

for token in tokens:
    # if token not in political_words:
        # clean_tokens.remove(token)
	if token.lower() in political_words:
		clean_tokens.append(token.lower())
	# elif token in stopwords.words('english') or len(token) <= 4 :
	# 	clean_tokens.remove(token)


freq = nltk.FreqDist(clean_tokens)

print("--- %s seconds ---" % (time.time() - start_time))
# for key,val in freq.items():
	# print(str(key) + ':' + str(val))
freq.plot(30,cumulative = False)
#for k, v in subcnt.items():
#	print(v, k)
#print(tokens)


