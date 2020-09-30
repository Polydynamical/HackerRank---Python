# required if main equals main forces this solution

def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
# This is a cleaner sol

print("-".join(input().split()))
