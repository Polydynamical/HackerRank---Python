# My solution:

n = int(input())
for index in range(0, n):
    print(index**2) 
   
# Much cleaner solution I found:

n = int(input())
print(*[num**2 for num in range(n)], sep='\n')
