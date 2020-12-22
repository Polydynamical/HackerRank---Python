if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i,j,k] for i in list(range(0,x+1)) for j in list(range(0,y+1)) for k in list(range(0,z+1)) if i+j+k is not n])

