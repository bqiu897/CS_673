def fibonacci():
    fib_list = [1, 1]
    n1 = fib_list[0]
    n2 = fib_list[1]
    while len(fib_list) < 100:
        n3 = n1 + n2
        fib_list.append(n3)
        n1 = n2
        n2 = n3
    print(fib_list)
    return fib_list


fibonacci()
