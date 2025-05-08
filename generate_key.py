import random
import egcd
import gmpy2
import math
from rsa import RSAPrivateKey


def generate_prime(min_val: int, max_val: int) -> int:
    maxiter = int(math.log2(max_val) * 1000)
    for _ in range(maxiter):
        candidate = random.randint(min_val, max_val)
        if gmpy2.is_prime(candidate) and gmpy2.is_prime(candidate * 2 + 1):
            return candidate
    raise Exception("Not found any Sofie Germain prime")
    return -1

def generate_key(len: int) -> RSAPrivateKey:
    p = generate_prime(2**(len//2), 2**(len//2 + 1))
    q = generate_prime(2**(len - len//2), 2**(len - len//2 + 1))
    N = p*q
    phi = N - p - q + 1
    e = 0
    result = egcd.egcd(e, phi)
    while result[0] != 1:
        e = random.randint(1, phi)
        result = egcd.egcd(e, phi)
    
    return RSAPrivateKey(N, e, len, result[1] % phi)
