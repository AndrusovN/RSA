from auxiliary import encode_str, decode_int, bin_power


class RSAPublicKey:
    N: int
    e: int
    length: int

    def __init__(self, N_: int, e_: int, l: int):
        self.N = N_
        self.e = e_
        self.length = l
    
    def encrypt(self, text: str) -> int:
        while len(text) < self.length // 8:
            text += " "
        return bin_power(encode_str(text), self.e, self.N)
    
    def __str__(self):
        return f"RSA Public Key:\nModulus: {self.N}\nExponent: {self.e}\nMax length of messages: {self.length // 8} symbols"
    
    def export(self, filename: str):
        with open(filename, 'w') as f:
            f.write(f"RSA PUBLIC KEY\n{self.N}\n{self.e}\n{self.length}")
    
    @staticmethod
    def import_from_file(filename: str):
        with open(filename, 'r') as f:
            _, N, e, l = f.readlines()
            return RSAPublicKey(int(N), int(e), int(l))
    
class RSAPrivateKey(RSAPublicKey):
    d: int

    def __init__(self, N_, e_, l, d_):
        super().__init__(N_, e_, l)
        self.d = d_
    
    def decrypt(self, code: int) -> str:
        return decode_int(bin_power(code, self.d, self.N), self.length)
    
    def get_public_key(self):
        return RSAPublicKey(self.N, self.e, self.length)
    
    def __str__(self):
        return f"RSA Private Key:\nModulus: {self.N}\nExponent: {self.e}\nInverter: {self.d}\nMax length of messages: {self.length // 8} symbols"

    def export(self, filename: str):
        super().export(filename + ".pub")
        with open(filename, 'w') as f:
            f.write(f"RSA PRIVATE KEY\n{self.N}\n{self.e}\n{self.d}\n{self.length}")
    
    @staticmethod
    def import_from_file(filename: str):
        with open(filename, 'r') as f:
            _, N, e, d, l = f.readlines()
            return RSAPrivateKey(int(N), int(e), int(l), int(d))
