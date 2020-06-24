#!/usr/bin/python3


#pierwsza metoda - składnia funkcjonalna
def allsubsets1(tab):
	return list(map(lambda i: list(map(lambda k: tab[k],filter(lambda j: i & (1 << j),range(len(tab))))),range(1 << len(tab))))

#druga metoda - listy składane
def allsubsets2(tab):
	subsets =[]
	for i in range(1<<len(tab)):
		subsets += [[tab[j] for j in range(len(tab)) if (i & (1 << j)) ]]
	return subsets	

l = [1,2,3]
if __name__ == "__main__":
	print(allsubsets1(l))
	print(allsubsets2(l))





