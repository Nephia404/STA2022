def isPrime(n):
    for p in range(2, n):
        if n % p == 0:
            print(n)
            return False
    print("prime")

for n in range(30,61):
    isPrime(n)
