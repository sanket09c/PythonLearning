def printPattern(no):
    for i in range(1, no+1):
        for j in range (1, no+1,):
            print("  ",j, end = "")
        print("")

def main():

    num = int(input("Enter number: "))
    printPattern(num)

if __name__ == "__main__":
    main()    



