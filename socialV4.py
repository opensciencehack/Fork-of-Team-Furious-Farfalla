import glob
import time
import ujson
import nltk
import os
import datetime

from nltk.corpus import stopwords
from collections import defaultdict

ITERATIONS = 100000
print("Starting Social Program")


sr = stopwords.words('english')
start_time = time.time()

subcnt = defaultdict(int)
tokens = []
print(os.getcwd())

file_to_open = 'data_new/RC_2016-11-??'


print( os.path.isfile(file_to_open))
i = 0

clean_tokens = list()
political_words = ['donald','trump','hillary','clinton']

dates_x = list()
popularity_y = [0] *5 
day = 0
previous_day = 0
day_count = 0
for fn in glob.iglob(file_to_open):
	with open(fn) as f:
		for line in f:
			# print(line)
			jo = ujson.loads(line)
			body = jo['body']
			createdDate = jo['created_utc']
			d = datetime.datetime.utcfromtimestamp(createdDate)
			# print(d.day)
			day = d.day
			if(day != previous_day):
				dates_x.append(day)
				previous_day = day
				day_count += 1
				print(previous_day)
				print(day_count)
			
			# print(d)
			tokens += [t for t in body.split()]
			i += 1
			if(i> ITERATIONS):
				break
			for token in tokens:
    			# if token not in political_words:
       			 # clean_tokens.remove(token)
				if token.lower() in political_words:
					popularity_y[day_count] += 1
					clean_tokens.append(token.lower())
					# day_count += 1
	# elif token in stopwords.words('english') or len(token) <= 4 :
	# 	clean_tokens.remove(token)

#			print(jo['body'])
#			subcnt[jo['subreddit']] += 1
# print(dates_x)




print(popularity_y)
freq = nltk.FreqDist(clean_tokens)
# print(clean_tokens)

print("--- %s seconds ---" % (time.time() - start_time))
# for key,val in freq.items():
	# print(str(key) + ':' + str(val))
freq.plot(30,cumulative = False)
#for k, v in subcnt.items():
#	print(v, k)
#print(tokens)


