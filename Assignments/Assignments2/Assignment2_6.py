def printPattern(no):
    for i in range(1, no+1):
        for j in range (1, no+1,):
            print(" *   ", end = "")
        print("")
        no = no - 1

def main():

    num = int(input("Enter number: "))
    printPattern(num)

if __name__ == "__main__":
    main()    



