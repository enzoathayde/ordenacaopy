import random
from datetime import datetime


choose = 31289321893
a = 0

wa = list(range(1,1000000,1)) # ordered list with one million elements ascending
xa = list(range(1,1000,1))  # ordered list with one thousand elements ascending
ya = list(range(1,10000,1)) # ordered list with ten thousand elements ascending
za = list(range(1,100000,1)) # ordered list with one hundred thousand elements ascending
xd = list(range(1000,1,1))  # ordered list with one hundred elements descending
yd = list(range(10000,1,1)) # ordered list with one thousand elements descending
zd = list(range(100000,1,1)) # ordered list with ten thousand elements descending
wd = list(range(1000000,1,1)) # ordered list with one million elements descending


# gen an random list with one hundred elements
xr = []
for i in range(1000):
	a = random.randint(0,1000)
	xr.append(a)
# print(xr)
# gen an random list with one thousand elements
yr = []
for i in range(10000):
	a = random.randint(1,10000)
	yr.append(a)
# print(yr)

# gen an random list with ten thousand elements
zr = []
for i in range(100000):
	a = random.randint(0,100000)
	zr.append(a)
# print(zr)


wr = []
for i in range(1000000):
	a = random.randint(0,1000000)
	wr.append(a)
# print(zr)

def bubbleSort(list):
	startBubbleSortSecond = datetime.now()
	any = 0
	i = 0
	swap = True
	while(swap != False):
		swap = False
		for i in range(len(list) - 1):
				if(list[i] > list[i + 1]):
					any = list[i]
					list[i] = list[i+1]
					list[i+1] = any
					swap = True
	endBubbleSortSecond = datetime.now()
	diffTimeBubbleSort = endBubbleSortSecond - startBubbleSortSecond
	print(diffTimeBubbleSort)


def selectionSort(list):
	startSelectionSortSecond = datetime.now()
	any = 0
	for i in range(len(list)):
		min = i 
		for j in range(i + 1,len(list)):
			if(list[j] < list[min]):
					min = j
		any = list[i]
		list[i] = list[min]
		list[min] = any
	endSelectionSortSecond = datetime.now()
	diffTimeSelectionSort = endSelectionSortSecond - startSelectionSortSecond
	print(diffTimeSelectionSort)

def insertionSort(list):
	startInsertionSortSecond = datetime.now()
	for i in range(1,len(list)):
		any = list[i]  # fixa a posição do indice 1, segundo da lista
		j = i - 1  # indice 0, primeiro da lista    
		while(j >= 0 and any < list[j]):
			list[j + 1] = list[j]
			j = j - 1
		list[j + 1] = any
	endInsertionSortSecond = datetime.now()
	diffTimeInsertionSort = endInsertionSortSecond - startInsertionSortSecond
	print(diffTimeInsertionSort)
		


def quickSort(list,left,right):
	startQuickSortSecond = datetime.now()
	if (left < right):
		partitionPosition = partition(list,left,right)
		quickSort(list,left,partitionPosition - 1)
		quickSort(list,partitionPosition + 1, right)
	endQuickSortSecond = datetime.now()
	diffQuickSortTime = endQuickSortSecond - startQuickSortSecond
	print(diffQuickSortTime)

def partition(list,left,right):
	i = left
	j = right - 1
	pivot = list[right]
	while (i < j):
		while (i < right) and (list[i] < pivot):
			i += 1
		while (j > left) and (list[j] >= pivot):
			j -= 1
		if (i < j):
			list[i], list[j] = list[j], list[i]

		if list[i] > pivot:
			list[i], list[right] = list[right], list[i]

	return i






# quickSort(zr,0,99999)
bubbleSort(xd)
print(xd)
# insertionSort(x)
# print(xr)
# selectionSort(zr)
# insertionSort(xr)