import random


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
	any = 0
	for i in range(len(list)):
		for j in range(i + 1,len(list)):
			if(list[i] > list[j]):
				any = list[i]
				list[i] = list[j]
				list[j] = any
	print(list)



# def insertionSort(list):
# 	for i in range(len(list)):
# 		key = list[i]
# 		for j in range(len(list)):
# 			if(list[j] < key):


def selectionSort(list):
	any = 0
	for i in range(len(list)):
		min = i 
		for j in range(i + 1,len(list)):
			if(list[j] < list[min]):
					min = j
		any = list[i]
		list[i] = list[min]
		list[min] = any
	print(list)

def insertionSort(list):
	any = 0
	


					
					
					


bubbleSort(zr)
# insertionSort(x)
# print(xr)
#selectionSort(zr)