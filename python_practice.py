# Print the prime number from 2 to 100

def print_prime_number():
    p = 2
    while p <= 100:
        is_prime = True
        for i in range(2, p):
            if p % i == 0:
                is_prime = False
                break
        if is_prime == True:
            print(p)
        p = p + 1
