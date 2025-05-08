import binascii

def encode_str(text: str) -> int:
    return int.from_bytes(text.encode(encoding='ascii'))

def decode_int(num: int, length: int) -> str:
    return num.to_bytes(1 + length // 8).decode(encoding='ascii')

def bin_power(num: int, e: int, N: int) -> int:
    result = 1
    exponent = e
    current_power = num
    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_power
            result %= N
        current_power *= current_power
        current_power %= N
        exponent //= 2
    return result