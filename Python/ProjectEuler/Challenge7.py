def calcPrime(num):
    nonPrime = list(range(2,num+1))
    primeNumbers = []
    for i in range(1,int(num/2)):
        try:    
            primeNumbers.append(nonPrime[0])
        except IndexError:
            return(primeNumbers)
        for j in range(2,int(num/nonPrime[0])+1):
            try:
                nonPrime.remove(nonPrime[0]*j)
            except ValueError:
                pass
        nonPrime.pop(0)

allPrimes = calcPrime(110000)
print(allPrimes[10000])
