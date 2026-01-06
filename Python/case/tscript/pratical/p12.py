def is_prime(n):
    result = 0
    for i in range(2, n):
        result = n % i
        if result == 0:
            print(f'{n} is not a prime number')
            break
    if result != 0:
        print(f'{n} is a prime number')

number = int(input())
is_prime(number)