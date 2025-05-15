def main():

    print("Enter the number for finding sum of factorial: ")
    num = int(input())

    sum = 1

    for i in range(int(num/2), 1, -1):
        if (num%i == 0):
            sum = sum + i

    print("sum of factors is: ", sum)

if __name__ == "__main__":
    main()