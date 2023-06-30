while True:
    ans = 0
    word = list(input())

    if word == ['#']:
        break
    else:
        for i in word:
            if i in 'aeiouAEIOU':
                ans += 1
        print(ans)