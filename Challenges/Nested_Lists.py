list = []

if __name__ == '__main__':
    for k in range(int(input())):
        list.append([input(), float(input())])
        
    list = sorted(list, key=lambda x: x[1])
    list.pop(0)
    for b in range(int(len(list))):
        print(list[b][1])
    for j in range(int(len(list))):
        print(list[j][0])
