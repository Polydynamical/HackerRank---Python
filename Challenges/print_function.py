# my sol

n = int(input())
s = ""
for i in range(1, n+1):
    s+=str(i)
print(s)

# super cool sol

print("".join([str(i) for i in range(1,int(input())+1)]))
