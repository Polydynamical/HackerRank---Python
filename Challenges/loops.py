# My solution:

n = int(input())
for i in range(0, n):
    print(i**2) 
   
# Much cleaner solution I found:

n = int(input())
print(*[num**2 for num in range(n)], sep='\n')
