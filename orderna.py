import random


choose = 31289321893
a = 0

x = range(1,100,1)  # ordered list with one hundred elements
y = range(1,1000,1) # ordered list with one thousand elements
z = range(1,10000,1) # ordered list with ten thousand elements

# gen an random list with one hundred elements
xr = []
for i in range(100):
	a = random.randint(0,100)
	xr.append(a)
# print(xr)

# gen an random list with one thousand elements
yr = []
for i in range(1000):
	a = random.randint(1,1000)
	yr.append(a)
# print(yr)

# gen an random list with ten thousand elements
zr = []
for i in range(10000):
	a = random.randint(0,9999)
	zr.append(a)
# print(zr)

def bubbleSort(list):
	any = 0
	for i in range(len(list)):
		for j in range(len(list)):
			if(list[i] < list[j]):
				any = list[i]
				list[i] = list[j]
				list[j] = any
	print(list)



def insertionSort(list):
	
	for i in range(100,1):
		print(list)




					
					
					


# bubbleSort(zr)
insertionSort(x)