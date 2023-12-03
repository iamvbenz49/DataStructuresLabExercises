n = int(input("Enter the number : "))
res = 1
for i in range(1,n+1):
    res*=i
print(f"the factorial of {n} is {res}")