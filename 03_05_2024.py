import math

def hyperbolic_analogues(x):
    """
    Calculate the hyperbolic analogue of a number.
    """
    sinh_x = (math.exp(x) - math.exp(-x)) / 2
    cosh_x = (math.exp(x) + math.exp(-x)) / 2
    tanh_x = sinh_x / cosh_x

    return sinh_x, cosh_x, tanh_x

def main():
    print("Welcome to the Hyperbolic Analogue Calculator!")
    x = float(input("Enter a number: "))
    
    sinh_x, cosh_x, tanh_x = hyperbolic_analogues(x)

    print(f"The hyperbolic sine of {x} is:", sinh_x)
    print(f"The hyperbolic cosine of {x} is:", cosh_x)
    print(f"The hyperbolic tangent of {x} is:", tanh_x)

if __name__ == "__main__":
    main()
