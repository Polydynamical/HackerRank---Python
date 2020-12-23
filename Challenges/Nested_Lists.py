list = []

if __name__ == '__main__':
    for K in range(int(input())):
        list.append([input(), float(input())])
        
    list = sorted(list, key=lambda x: x[1])
    print(list)
