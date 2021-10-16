vocab = set()

for tweet in open("tweets.txt", "r").readlines():
	_, _, text = tweet.partition(', ')	
	words = list(map(lambda w: w.lower(), text.split()))
	vocab.update(set(words))


print("The unique words")
print(vocab)
