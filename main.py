import argparse
from generate_key import generate_key
from rsa import RSAPrivateKey, RSAPublicKey

parser = argparse.ArgumentParser(
                    prog='RSA Operator',
                    description='''This program can create, save and upload RSA keys and use them for encryption and decryption of messages''',
                    epilog='') 

parser.add_argument('filename')         
parser.add_argument('-g', '--generate',
                    action='store_true')
parser.add_argument('-s', '--size')
parser.add_argument('-e', '--encrypt',
                    action='store_true')
parser.add_argument('-d', '--decrypt',
                    action='store_true')
parser.add_argument('-v', '--view', action='store_true')

args = parser.parse_args()
if args.generate:
    key = generate_key(int(args.size))
    key.export(args.filename)
elif args.encrypt:
    key = RSAPublicKey.import_from_file(args.filename)
    text = input("Enter text to encrypt:\n")
    print(key.encrypt(text))
elif args.decrypt:
    key = RSAPrivateKey.import_from_file(args.filename)
    ciphertext = input("Enter ciphertext to decrypt:\n")
    print(key.decrypt(int(ciphertext)))
elif args.view:
    private = False
    with open(args.filename, 'r') as f:
        first = f.readline()
        if first == 'RSA PRIVATE KEY\n':
            private = True
        elif first != 'RSA PUBLIC KEY\n':
            print(first)
            print("Error! Not an RSA Key file, exiting")
            exit(0)
    if private:
        key = RSAPrivateKey.import_from_file(args.filename)
        print(str(key))
    else:
        key = RSAPublicKey.import_from_file(args.filename)
        print(str(key))
else:
    parser.print_help()
