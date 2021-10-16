import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--word', type=str)
args = parser.parse_args()

if not args.word:
   raise Exception('Must provide a word')
   
count = 0
for tweet in open('tweets.txt', 'r'):
    _, _, text =  tweet.partition(', ')
    if args.word in text:
        count += 1
   
print(f"The phrase '{args.word}' occurs {count} times")
