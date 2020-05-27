import sys


usage = """Usage: python {name} <number1> <number2>
Example:
    python {name} 10 3"""


validPrint = """{:<15} {add}
{:<15} {sub}
{:<15} {mult}
{:<15} {div}
{:<15} {mod}"""


def operations(nb1, nb2):
    addition = nb1 + nb2
    subtraction = nb1 - nb2
    multiplication = nb1 * nb2
    division = "ERROR (div by zero)"
    modulo = "ERROR (modulo by zero)"
    if nb1 != 0 and nb2 != 0:
        division = nb1 / nb2
        modulo = nb1 % nb2
    toPrint = validPrint.format(
        "Sum:",
        "Difference:",
        "Product:",
        "Quotient:",
        "Remainder:",
        add=addition,
        sub=subtraction,
        mult=multiplication,
        div=division,
        mod=modulo
    )
    print(toPrint)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        if len(sys.argv) > 3:
            print("InputError: too many arguments\n")
        print(usage.format(name=sys.argv[0]))
        sys.exit()
    else:
        nb1 = sys.argv[1]
        nb2 = sys.argv[2]
        if not nb1.isdigit() or not nb2.isdigit():
            print("InputError: only numbers\n")
            print(usage.format(name=sys.argv[0]))
            sys.exit()
        else:
            operations(int(nb1), int(nb2))
