def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input("Enter the number : "))
for i in range(n):
    print(f"{i} th fibonacci number {fibo(i)}")
