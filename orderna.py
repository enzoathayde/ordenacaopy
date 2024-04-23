import random
from datetime import datetime


choose = 31289321893
a = 0


xa = range(1,1000,1)  # ordered list with one thousand elements ascending
ya = range(1,10000,1) # ordered list with ten thousand elements ascending
za = range(1,100000,1) # ordered list with one hundred thousand elements ascending
xd = range(1000,1,1)  # ordered list with one hundred elements descending
yd = range(10000,1,1) # ordered list with one thousand elements descending
zd = range(100000,1,1) # ordered list with ten thousand elements descending


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

def bubbleSort(list):
	startBubbleSortSecond = datetime.now()
	any = 0
	for i in range(len(list)):
		for j in range(i + 1,len(list)):
			if(list[i] > list[j]):
				any = list[i]
				list[i] = list[j]
				list[j] = any
	endBubbleSortSecond = datetime.now()
	diffTimeBubbleSort = endBubbleSortSecond - startBubbleSortSecond
	print(diffTimeBubbleSort)
	print(list)

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
	print(list)

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
	print(list)				



# def quickSort(list):
# 	pivot = len(list) / 2
	 
					
	

bubbleSort(zr)
# insertionSort(x)
# print(xr)
# selectionSort(zr)
# insertionSort(xr)