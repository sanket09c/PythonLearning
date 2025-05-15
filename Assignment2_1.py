import Arithmetic

def main():

    print("Please print two numbers: ")
    num1 = int(input("Number1: ")) 
    num2 = int(input("Number2: "))

    add = Arithmetic.Add(num1, num2)
    print("Add of above two numbers is: ", add)

    sub = Arithmetic.Sub(num1, num2)
    print("Add of above two numbers is: ", sub)

    mul = Arithmetic.Mul(num1, num2)
    print("Add of above two numbers is: ", mul)

    div = Arithmetic.Div(num1, num2)
    print("Add of above two numbers is: ", div)


if __name__ == "__main__":
    main()