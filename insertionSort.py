randomArray = [11,7,5,3,2,1]
any = 0

for i in range(len(randomArray)):
  any = randomArray[i] 
  j = i - 1
  while (j >= 0 and any < randomArray[j]):
    randomArray[j + 1] = randomArray[j]
    j = j - 1
  randomArray[j + 1] = any
print(randomArray)
