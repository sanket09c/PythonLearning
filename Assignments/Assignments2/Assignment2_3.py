def main():
    print("Enter the number for finding factorial: ")
    num = int(input())

    fact = 1
    for i in range(1, num+1):
        fact = fact * i
        i += 1

    print("factorial is: ", fact)

if __name__ == "__main__":
    main()    