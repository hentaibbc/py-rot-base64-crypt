from rot_base64_crypt.crypt import Crypt
from string import Template

privateKey='1qaz3edc5tgb6yhn4rfv2wsx'
tpl = Template("""origin: $origin
encrypt: $encrypt
decrypt: $decrypt""")

if __name__ == '__main__':
    mycrypt = Crypt(privateKey)
    origin = 'This is a test paragraph'
    encoded = mycrypt.encrypt(origin)
    decoded = mycrypt.decrypt(encoded)

    print(tpl.substitute(dict(
        origin=origin,
        encrypt=encoded,
        decrypt=decoded,
    )))
