primes = open("primes.txt", "r")
primesArray = primes.read().split(',')
primes.close()
for i in range(len(primesArray)):
    primesArray[i] = int(primesArray[i])
i = primesArray[-1] + 1
def lessThan(n):
    lessThan = []
    for i in range(n):
        if(n-i != n and n-i != 1):
            lessThan.append(n-i)
    return lessThan
while True:
    isPrime = False
    for j in range(len(lessThan(i))):
        if(i%lessThan(i)[j] == 0):
            isPrime = False
            break
        else:
            isPrime = True
    if(isPrime):
        primesArray.append(i)
        print(i)
        print(primesArray)
        print("Total primes: ",len(primesArray))
        primesString = ','.join(str(i) for i in primesArray)
        primes = open("primes.txt", "w")
        primes.write(primesString)
        primes.close()
    i+=1
