import MarvellousNum

def main():
    listX = list()
    print("Enter the size of list ")
    size = int(input())

    print("Enter the elements of list ")
    for i in range(size):
        listX.append(int(input()))
    print(listX)

    MarvellousNum.chkPrime(listX)

if __name__ == "__main__":
    main()    