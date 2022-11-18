## Usage


### Import

```python
from rot_base64_crypt.crypt import *
```

### Create Instance

```python
crypt = Crypt(key = privateKey)
```

### Encrypt

```python
crypt.encrypt('String to encrypt')

# Encrypt format XXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#                ^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                 P1                P2
# P1: Public key
# P2: Encoded string

```

### Decrypt

```python
crypt.decrypt('String to decrypt')
```