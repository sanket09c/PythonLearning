def chkPrime(listChk):

    primeList = list()
    for i in listChk:
        print("i: ", i)
        prime = 1
        for j in range(2, i):
            print("j: ", j)
            if (i % j) == 0:
                prime = 0
                break
        if (prime == 1):
            primeList.append(i)
        

    print("Prime no. are: ", primeList)
    sum = 0
    for m in primeList:
        sum = sum + m

    print("Sum of prime numbers is ", sum)    
    