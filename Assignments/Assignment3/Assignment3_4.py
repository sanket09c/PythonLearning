def main():
    listX = list()
    print("Enter the size of list ")
    size = int(input())

    print("Enter the elements of list ")
    for i in range(size):
        listX.append(int(input()))
    print(listX)

    print("Enter the no. whose freq is to be found: ")
    num = int(input())
    freq = 0
    for i in listX:
        if num == i:
            freq = freq + 1

    print("The number: " , num, " is present: ", freq, " times ")         

if __name__ == "__main__":
    main()    