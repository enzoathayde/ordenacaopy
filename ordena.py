import random
from datetime import datetime
import sys
sys.setrecursionlimit(1000000000)
a=0


def generate_ordered_list(start, end):
  """Generates a list of integers in ascending order from start (inclusive) to end (exclusive).

  Args:
      start: The starting value of the list (inclusive).
      end: The ending value of the list (exclusive).

  Returns:
      A list of integers in ascending order.
  """
  return list(range(start, end))

# Ordered lists with different sizes
wa = generate_ordered_list(1,10000001) # 1000000 elements
xa = generate_ordered_list(1, 1001)  # 1000 elements
ya = generate_ordered_list(1, 10001)  # 10000 elements
za = generate_ordered_list(1, 100001)  # 100000 elements

def generate_descending_list(start, end):

  return list(range(start, 0, -1))

wd = generate_descending_list(1000000, 0) # 1000000 elements descending
xd = generate_descending_list(1000, 0)  # 1000 elements descending
yd = generate_descending_list(10000, 0)  # 10000 elements descending
zd = generate_descending_list(100000, 0)  # 100000 elements descending

def generate_random_list(size, min_value=0, max_value=1000):
  """Generates a list of random integers within a specified range.

  Args:
      size: The size of the random list.
      min_value: The minimum value (inclusive) for random numbers (default: 0).
      max_value: The maximum value (exclusive) for random numbers (default: 1000).

  Returns:
      A list of random integers.
  """
  return [random.randint(min_value, max_value - 1) for _ in range(size)]

xr = generate_random_list(1000)  # 1000 random elements
yr = generate_random_list(10000)  # 10000 random elements
zr = generate_random_list(100000)  # 100000 random elements
wr = generate_random_list(1000000)  # 1000000 random elements

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



quickSort(wd,1,999998)
