from rot_base64_crypt.crypt import *

if __name__ == '__main__':
    mycrypt = Crypt('123')
    encoded = mycrypt.encrypt('123')
    decoded = mycrypt.decrypt(encoded)
    print(encoded)
    print(decoded)