while True:
    try:
        n = int(input())
    except EOFError:
        break
    b = 1
    while b % n != 0:
        b = (10*b + 1)
    print(len(str(b)))