while True:
    sen = input()
    if sen == 'END':
        break
    sen = sen[-1::-1]
    print(sen)