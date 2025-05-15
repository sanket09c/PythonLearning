def addOfDigit(no):
    sum = 0
    while (no != 0):
        rem = int(no%10)
        no = no / 10
        sum = sum + rem
    print(sum)


def main():
    num = int(input("Enter number: "))
    addOfDigit(num)

if __name__ == "__main__":
    main()    



