import random


choose = 31289321893
a = 0

x = range(1,100,1)  # ordered list with one hundred elements
y = range(1,1000,1) # ordered list with one thousand elements
z = range(1,10000,1) # ordered list with ten thousand elements

# gen a random list with one hundred elements
def gen_random_hundred():
	xr = []
	for i in range(1,100):
		a = random.randint(1,100)
		xr.append(a)
	print(xr)

# gen a random list with one thousand elements
def gen_random_o_thousand():
	yr = []
	for i in range(1,1000):
		a = random.randint(1,1000)
		yr.append(a)
	print(yr)

# gen a random list with ten thousand elements
def gen_random_t_thousand():
	zr = []
	for i in range(1,10000):
		a = random.randint(1,10000)
		zr.append(a)
	print(zr)

# def bubbleSort():
# 	for i in range(1,100)

print("1: Print 100 ordered list itens.")
print("2: Print 1000 ordered list itens.")
print("3: Print 10000 ordered list itens.")
print("4: Print 100 random list itens.")
print("5: Print 1000 random list itens.")
print("6: Print 10000 random list itens.")
print("0: Quit")
choose = input("Choose: ")

while (choose != 0):
	if choose == '1':	
			print(list(x))
	elif choose == '2':	
			print(list(y))
	elif choose == '3':	
			print(list(z))
	elif choose == '4':	
		gen_random_hundred()
	elif choose == '5':	
		gen_random_o_thousand()
	elif choose == '6':	
		gen_random_t_thousand()
	elif choose == '0':
			print("you_chose_quit")
			break

	print("1: Print 100 ordered list itens.")
	print("2: Print 1000 ordered list itens.")
	print("3: Print 10000 ordered list itens.")
	print("4: Print 100 random list itens.")
	print("5: Print 1000 random list itens.")
	print("6: Print 10000 random list itens.")
	print("0: Quit")
	choose = input("Choose: ")
else:
	print("you_chose_quit")