# functions

# void functions / not returning function
def addThenSquareThenCubicThenFactorialOf7(a, b):
    sum = a + b
    square = sum * sum
    cubic = square * square * square

    print(cubic)

# addThenSquareThenCubicThenFactorialOf7(4, 8)


def subtractThreeValues(a, b, c):
    print(a-b-c)


#subtractThreeValues(9, 7, 1)

# return type function / function
def sum(a, b):
    return a + b


x = sum(2, 5)

result = sum(5, 2)
print('Result: ', result)
