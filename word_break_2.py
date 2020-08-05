s = "catsanddogs"
wordDict = ["cat","cats","and","sand","dogs"]

n = len(s)

stringset = set(s)
wordset = set(''.join(wordDict))
wordDict = set(wordDict)

if stringset - wordset:
	print([])
	exit(0)
sentence_list = []
def make_sentences(so_far = [], ind  = 0):
	if ind == n:
		sentence_list.append(' '.join(so_far))

	for i in range(ind,n+1):
		if s[ind:i] in wordDict:
			make_sentences(so_far + [s[ind:i]], i)

make_sentences()
print(sentence_list)