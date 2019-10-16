# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass
from cryptography.fernet import Fernet
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
def mohit_asymmetric(a,b):
    if a == 'e':
        pu_key = RSA.import_key(b[4])

        inp = b[3]

        message = inp.encode()
        #Instantiating PKCS1_OAEP object with the public key for encryption
        cipher = PKCS1_OAEP.new(key=pu_key)
        #Encrypting the message with the PKCS1_OAEP object
        cipher_text = cipher.encrypt(message)
        b[3] = cipher_text
        print(b)




    if a == 'd':
        print('Decryption Asymmetric')
        pr_key = RSA.import_key(b[4])
        cipher_text = b[3]
        #Instantiating PKCS1_OAEP object with the private key for decryption
        decrypt = PKCS1_OAEP.new(key=pr_key)
        #Decrypting the message with the PKCS1_OAEP object
        decrypted_message = decrypt.decrypt(cipher_text)
        print(decrypted_message.decode())

#mohit_asymmetric('e',[3, '0000 0000 0000 0001', '3', 'mohit', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvKQJyKb51Bk7F+PwikcN\nU65JM6clXVvizLOV9zQfvFs2FSC9Lrr4su89wNXd7J43JJN5/aOsKrLBP4fx2z4x\nxzD525GSC1aT5CkvgVBD+U3uwRMbApdmP3wyYr0SDfnDQFScDJoSoS3Qg/QVAqdn\nrX/c1HbburuiLDjAagm6QxkqIlA5FZqktgWCV33HgHswq7fnwZSGgP21U21qlM1m\nQbHAgnWzSwnBJgGRHJ5ewEKu1LgPY9KEfV5wKVOA+UXgWWXhoq31SBcad5kZwWuD\nvR+8zLGoHD6NrY99VD+021OTd89s5ZHbvI9i9Cl6Bi9oYu/KxVRzRcsfzsAsGd1B\nlwIDAQAB\n-----END PUBLIC KEY-----', 'MTL', 'NYC'])


mohit_asymmetric('d',[3, '0000 0000 0000 0001', '3', b"1l\x9epS\x92Q\xbexM\xa8\x0c\xfc\xc1J\xec\x86*Z\xa3\xb60I\xeeD\x06T[\xf3q\xa7\xf8\x14\t\xb0nD\x80\xde\x13S\xaeW\x88 \xcf\xed\x8f\x88?,z\xe8\xbe\xe5y\x04\x8dT\xc9\x9c\xdc\xb2\xe9J\xd8\xe7a\xcc\x1a\x86\xcfpm\x83\xf9@\xa6^\xe1\xf2;D\xe85\x91\x97\x9d7\xcb\x9b\xfc\x81\x19A\x99\xaaW\x134\xed\xfa,\xf3\x95)\xb7\xbb\x98\x91\x88\x17\xbb8\xc9C\xbd\x97\xaa0j\x87}\x13\x94\xb1\xf4\x0fYG`0.\x88zd\xb9cd\x8aa\xb3|+\xf2\x89\rRV\xbbv\x91\xf3\x19\x10[\x04\x83\xfb\xbe\x94?\x1b\x12\xe7\xa1\xbc\xb4o\xd9\xf1WT`\xa8v(5\x12\xff\xe13NGQ\x9d@Ni\x15\x17\x9c\xd1\xee\x01+\x0b\x06\xad\xec\xa9;\xc0\x1a\x1d\xaa\r\x8d~%U\xe5\xb0/\xef'\xf2S3]FS\x92S/\xff]p\x16\xd4@\xd9\xd6q\x90\x0c\xda\xd2\xa5\x9d\x86\xb4\xca\xe8\x83\xda^\x7f\x81\xd5\xd2Y\x96\xa3\xbeW", '-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAvKQJyKb51Bk7F+PwikcNU65JM6clXVvizLOV9zQfvFs2FSC9Lrr4su89wNXd7J43JJN5/aOsKrLBP4fx2z4xxzD525GSC1aT5CkvgVBD+U3uwRMb\nApdmP3wyYr0SDfnDQFScDJoSoS3Qg/QVAqdnrX/c1HbburuiLDjAagm6QxkqIlA5\nFZqktgWCV33HgHswq7fnwZSGgP21U21qlM1mQbHAgnWzSwnBJgGRHJ5ewEKu1LgP\nY9KEfV5wKVOA+UXgWWXhoq31SBcad5kZwWuDvR+8zLGoHD6NrY99VD+021OTd89s\n5ZHbvI9i9Cl6Bi9oYu/KxVRzRcsfzsAsGd1BlwIDAQABAoIBABTeCd2yEuV9MQXw\nh2r/IctFoVVfF7QJy79HMmoD0GrpUBnq4uKTePAaT6N6769oGm4ns5FKP2utwHuC\n/KR7Gc3mGLhK6ck/94uAFCri3Sdr5o23IQAauAstIEm/OTW7O6JseaKvPIEAl2tc\nCc2fBR9dNel5iHmnSJufCjHwsjO6bmCN6DcEMcKg9ID117ditg3F9k1zbK2rYZg3\nsmIVzM+L2lGNGW6ZoH5B1ry9QGEcujgckmN57SNWnUav1ZO/YmXuVsF5piy0OWvp\nRndoxueXHSqdWFAo5J0VIC8YlPjxSBjQ/CDr9s6RjE/nE/HrXIrA+LZ2Jy05T4OO\nCjN7TIECgYEAxsSiFULdQSifQmTlGjJOBQpxnrtKs1DzFisNpg/MuUF5R85SvoOv\nwcnAtGL4jHZnc3faP65qA/3ipuu0LoHRVzcE2sXnA6lty2dyCBpKigWXf6WHl0ht\n4czUc57DbzrLMVEUuCGy3dBr5hH7mmDHVs7e1mBh+KxI+2W/a+H/YtcCgYEA8vTp\nTrHTjJROnBFaR8aBKX6A43/1ovvHFYmf7oxpZCbdH8wiSSxUdkWJOnhGHy9kZTmS\n2ZUfOD2HjwAp8pX6Vt/NO9ZA730TzihpLuP5eUxA9uFGkKaSvgFqSCT5PRYr5mQi\nSjJn8Pe4XgdKQg+IHZqatrZqqIb20n28K/7X/0ECgYAxd4I29FsH+koYRe/WYyqT\nipPYQxhGJCE7JR/SciArAqZiPnDNRQyal9FDk1Xz7wuz6uH/8zIjKC4eCI7g/CHT\nKLgmkhX6DVJryqTQa2qdiuK3O8TQ24+tIELHO3270s/6yAj2Ajz3gwU3TsZlFyzE\n59sBUx9OueG33wySlr3uJQKBgQC2guUBCPUylfa3pxF6+dPtp+qK/IU6eomD1G8g\ndLp3Ufqq+F6JOZP5hSMhmViT9LYmlKmMakmZph8/fZAFfEUjHdy/JqSBRCSsqg7Z\n+sheJrpmu7SW1YtG0SlWKPBSw2UXHgHkWxlaG72UZUWTerd2Bb5To5VcJIcmeO3y\n3u7EAQKBgQCsF1ap4ZBkKCU+kEliTeh93tKvAN8PFHTjZiy99kevq2PM72ulYnsP\naIP7Yy7jTwdcvI48HmQUNljUbNPnr4FBg4gXDoBlz/J0wcwYI590LhsspoGGoO3F\nqscj0Sbo7/HMoRCXuvDaYBkO8H1gHFRwWeY7HMMEPALB8jqirgLrBw==\n-----END RSA PRIVATE KEY-----', 'MTL', 'NYC'])
