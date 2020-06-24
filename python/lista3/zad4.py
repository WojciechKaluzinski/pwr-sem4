#!/usr/bin/python3


def quicksort(tab):
	
	if len(tab) == 0:
		return tab
	else:
		pivot = tab[0]
		#pierwsza metoda - listy składane
		lower = quicksort([x for x in tab[1:] if x < pivot])
		#druga metoda - składnia funkcjonalna
		greater = quicksort(list(filter(lambda x: x >= pivot, tab[1:])))
		return (lower+[pivot]+greater)


l = [10, 12, 3, -1, 15, 10, 7, 222]
if __name__ == "__main__":
	print(list(quicksort(l)))
