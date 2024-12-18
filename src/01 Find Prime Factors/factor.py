def is_prime(number: int) -> bool:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True

prime_divisors = []
for i in range(2, 100 + 1):
    if is_prime(i):
        prime_divisors.append(i)


def prime_divisor(number: int) -> int:
    if number < 2:
        return 1

    for divisor in prime_divisors:
        if number % divisor == 0:
            return divisor
    else:
        return number


def get_prime_factors(number: int) -> list:
    factors = []
    while number > 1:
        divisor = prime_divisor(number)
        number = number // divisor
        factors.append(divisor)
    return factors


# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
