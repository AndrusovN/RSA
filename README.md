# RSA key management app
This is a simple console app to manage RSA keys.
It can:

- Create RSA keys of a given length (`python3 main.py -g -s SIZE filename`)
- Encrypt text using public key file (`python3 main.py -e path_to_public_key` and then input your text)
- Decrypt ciphertext using private key file (`python3 main.py -d path_to_private_key` and then input your ciphertext)
- Show (public of private) key information (`python3 main.py -v path_to_key`)
- Show info message (`python3 main.py --help`)

This implements a naive RSA which cannot encrypt or decrypt messages with length more than keysize. You can see the info about max message length in information about the key

## Installation (for Linux):
```
git clone git@github.com:AndrusovN/RSA.git
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```
