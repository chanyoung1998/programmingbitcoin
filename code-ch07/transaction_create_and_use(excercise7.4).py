from ecc import PrivateKey
from helper import hash256, little_endian_to_int, decode_base58, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx

secret = little_endian_to_int(hash256(b'my first secret key'))
private_key = PrivateKey(secret)
print(private_key.point.address(testnet= True))

prev_tx = bytes.fromhex('6e7657754799fe7a906b213aa57b6920ad2d660f349fcb52dd384568aaddc2ef')
prev_index = 1
tx_in = TxIn(prev_tx, prev_index)

tx_outs = []
change_amount = int(0.004 * 10000000)
change_h160 = decode_base58('mxUJg9m1dsqpHnbhV15mwJ3GjwPBVMHVmu')
change_script = p2pkh_script(change_h160)
change_output = TxOut(change_amount,change_script)

target_amount = int(0.007 * 10000000)
target_h160 = decode_base58('mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv')
target_script = p2pkh_script(target_h160)
target_output = TxOut(target_amount,target_script)

tx_obj = Tx(1,[tx_in],[change_output,target_output],0,True)
print(tx_obj.sign_input(0,private_key))
print(tx_obj.serialize().hex())