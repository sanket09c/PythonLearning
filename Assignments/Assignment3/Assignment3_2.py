def main():
    listX = list()
    print("Enter the size of list ")
    size = int(input())

    print("Enter the elements of list ")
    for i in range(size):
        listX.append(int(input()))
    print(listX)

    max = listX[0]
    for i in listX:
        if i > max:
            max = i

    print("Max no in list is: ", max)         

if __name__ == "__main__":
    main()    