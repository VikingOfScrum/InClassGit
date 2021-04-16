def calc(a, b):
    sumOf = a + b
    print(sumOf)
    sub = a - b
    print(sub)
    multiply = a * b
    print(multiply)
    divide = a/b
    print(divide)
    mylist = [sumOf, sub, multiply, divide]
    sumMyList = sum(mylist)
    print(sumMyList)

calc(7, 4)