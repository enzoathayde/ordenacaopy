randomArray = [11,7,5,3,2,1]
any = 0

for i in range(0,len(randomArray) - 1):
  for j in range(len(randomArray) -1 - i):
    if(randomArray[j] > randomArray[j + 1]):
      any = randomArray[j]
      randomArray[j] = randomArray[j + 1]
      randomArray[j + 1] = any
print(randomArray)
