import json
import glob
import time
from collections import defaultdict

start_time = time.time()
print("Starting Social Program");

subcnt = defaultdict(int)

for fn in glob.iglob('../social/english/data/RC_2016-11-??'):
	with open(fn) as f:
		for line in f:
			jo = json.loads(line)
			subcnt[jo['subreddit']] += 1

for k, v in subcnt.items():
	print(v, k)

print("--- %s seconds ---" % (time.time() - start_time))

