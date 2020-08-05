from collections import Counter
A = ["label","roller"]

ldict = Counter(A[0])

for i in A:
 	ldict = ldict & Counter(i)

print(list(ldict.elements()))
