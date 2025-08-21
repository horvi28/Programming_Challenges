def store_prime(prime: int, prime_dict: dict):
    prime_dict[prime] = prime_dict[prime] + 1 if prime in prime_dict else 1


def prime_factorization(N: int, prime_dict: dict):
    prime = 2

    while N >= prime**2:
        if N % prime == 0:
            store_prime(prime, prime_dict)
            N = N / prime
        else:
            prime = prime + 1
    store_prime(int(N), prime_dict)


def convert_prime_dict_to_string(prime_dict: dict):
    s = ""
    for prime, exponent in prime_dict.items():
        if exponent > 1:
            s = s + f"{prime}^{exponent} * "
        else:
            s = s + f"{prime} * "
    return s[0:-3]


def decomp(n):
    prime_dict = {}
    for m in range(2, n + 1):
        prime_factorization(m, prime_dict)

    return convert_prime_dict_to_string(prime_dict)


if __name__ == "__main__":
    print(decomp(3))
    print(decomp(6))
    print(decomp(12))
    print(decomp(22))
    print(decomp(25))
