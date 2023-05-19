def luckyNumber(name):
    lickyNumber = len(name) * 10
    print("your licky number is: "+str(lickyNumber))


luckyNumber("hello world")

print(1 < int("2"))
print(not 42 == "answer")
print(42 < 50 and not 42 < 41)
print(42 > 50 and 42 < 43)
print(32 < 31 or 32 > 31)
print("\n")


def evenOrODD(number):
    if (number % 2) == 0:
        even = print("Even")
        return even
    odd = print("Odd")
    return odd


evenOrODD(1)
