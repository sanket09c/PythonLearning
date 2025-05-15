def countNumberOfDigit(no):
    count = 0
    while (no != 0):
        count = count + 1
        no = int(no/10)
    print(count)


def main():
    num = int(input("Enter number: "))
    countNumberOfDigit(num)

if __name__ == "__main__":
    main()    



