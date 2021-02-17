from ecc import PrivateKey
from helper import hash256, little_endian_to_int, decode_base58, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx

secret = little_endian_to_int(hash256(b'my first secret key'))
private_key = PrivateKey(secret)
print(private_key.point.address(testnet=True))

secret2 = little_endian_to_int(hash256(b'my second secret key'))
private_key2 = PrivateKey(secret2)
print(private_key2.point.address(testnet=True))
