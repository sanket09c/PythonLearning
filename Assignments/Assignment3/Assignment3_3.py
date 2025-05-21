def main():
    listX = list()
    print("Enter the size of list ")
    size = int(input())

    print("Enter the elements of list ")
    for i in range(size):
        listX.append(int(input()))
    print(listX)

    min = listX[0]
    for i in listX:
        if i < min:
            min = i

    print("Min no in list is: ", min)         

if __name__ == "__main__":
    main()    