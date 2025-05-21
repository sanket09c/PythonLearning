def main():
    listX = list()
    size = int(input("Enter the size of list: "))

    print("Enter the numbers ")
    for i in range(size):
        listX.append(int(input()))
    print(listX)

    sum = 0
    for i in listX:
        sum = sum + i

    print("sum: ",sum)

if __name__ == "__main__":
    main()    