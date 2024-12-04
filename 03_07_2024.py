import math

def main():
    print("Welcome to the Math Toolkit Program!")

    while True:
        print("\n Menu:")
        print("\t 1. Calculate the area of a circle")
        print("\t 2. Calculate the square root of a number")
        print("\t 3. Calculate the factorial of a number")
        print("\t 4. Calculate the sine, cosine, and tangent of a number")
        print("\t 5. Calculate the arcsine, arccosine, and arctangent of a number")
        print("\t 6. Calculate the hyperbolic analogues of a number")
        print("\t 7. Exit \n")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * radius ** 2
            print("The area of the circle is:", area)

        elif choice == '2':
            number = float(input("Enter a number to find its square root: "))
            if number < 0:
                print("Cannot calculate square root of a negative number.")
            else:
                sqrt_result = math.sqrt(number)
                print("The square root of", number, "is:", sqrt_result)

        elif choice == '3':
            num = int(input("Enter a number to find its factorial: "))
            fac_result = math.factorial(num)
            print("The factorial of", num, "is:", fac_result)

        elif choice == '4':
            num = int(input("Enter a number to find its sine, cosine, and tangent: "))
            sin_result = math.sin(num)
            cos_result = math.cos(num)
            tan_result = math.tan(num)
            print("The sine of", num, "is: ", sin_result, "\n"
            "The cosine of", num, "is: ", cos_result, "\n"
            "The tangent of", num, "is: ", tan_result)

        elif choice == '5':
            num = int(input("Enter a number to find its arcsine, arcccosine, and arctangent: "))
            sin_result = math.sin(num)
            cos_result = math.cos(num)
            tan_result = math.tan(num)
            asin_result = math.asin(sin_result)
            acos_result = math.acos(cos_result)
            atan_result = math.atan(tan_result)
            print("The arcsine of", num, "is: ", asin_result, "\n"
            "The arccosine of", num, "is: ", acos_result, "\n"
            "The arctangent of", num, "is: ", atan_result)

        elif choice == '6':
            num = int(input("Enter a number to find its hyperbolic analogues: "))
            sinh_result = math.sinh(num)
            cosh_result = math.cosh(num)
            tanh_result = math.tanh(num)
            asinh_result = math.asinh(sinh_result)
            acosh_result = math.acosh(cosh_result)
            atanh_result = math.atanh(tanh_result)
            print("The hyperbolic sine of", num, "is: ", sinh_result, "\n"
            "The hyperbolic cosine of", num, "is: ", cosh_result, "\n"
            "The hyperbolic tangent of", num, "is: ", tanh_result, "\n"
            "The hyperbolic arcsine of", num, "is: ", asinh_result, "\n"
            "The hyperbolic arccosine of", num, "is: ", acosh_result, "\n"
            "The hyperbolic arctangent of", num, "is: ", atanh_result)

        elif choice == '7':
            print("Thank you for using the Math Toolkit Program!")
            print("We hope you have a nice day! :D")
            break

        else:
            print("Nope, try again! Please only pick the options from numbers 1-7, thank you! :]")

if __name__ == "__main__":
    main()
