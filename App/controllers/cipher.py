from App.models import Cipher
from App.database import db

def create_cipher():
    cipher = Cipher()
    db.session.add(cipher)
    db.session.commit()
    return cipher

def get_cipher_by_id(id):
    return Cipher.query.filter_by(id=id).first()

def get_all_cipher():
    return Cipher.query.all()

def get_all_cipher_json():
    ciphers = Cipher.query.all()
    if not ciphers:
        return []
    ciphers = [cipher.get_json() for cipher in ciphers]
    return ciphers


def isbull(cipher_id,digit,position):
    cipher = Cipher.query.filter_by(id=cipher_id).first()
    print(cipher.digit1,cipher.digit2, cipher.digit3, cipher.digit4, digit, position)
    if cipher.digit1 == digit and position == 1 :
        print('bull')
        return True
    if cipher.digit2 == digit and position == 2 :
        print('bull')
        return True
    if cipher.digit3 == digit and position == 3 :
        print('bull')
        return True
    if cipher.digit4 == digit and  position == 4 :
        print('bull')
        return True
    print('no bull')        
    return False

def iscow(cipher_id , digit):
    cipher = Cipher.query.filter_by(id=cipher_id).first()
    print(cipher.get_json(), digit)
    if cipher.digit1 == digit:
        print('cow')
        return True
    if cipher.digit2 == digit:
        print('cow')
        return True
    if cipher.digit3 == digit:
        print('cow')
        return True
    if cipher.digit4 == digit:
        print('cow')
        return True
    print('no cow')
    return False