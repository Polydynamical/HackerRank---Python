if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my = []
    for j in arr:
        if j not in my:
            my.append(j)
    print(sorted(my)[-2])

