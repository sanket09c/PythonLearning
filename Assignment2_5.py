def checkPrime(no):    
    prime = True
    for i in range(2, int(no/2)+1):
        if (no % i == 0):
            prime = False
            break

    print("The number is Prime? : ", prime)


def main():
    num = int(input("Enter the number: "))
    checkPrime(num)



if __name__ == "__main__":
    main()        