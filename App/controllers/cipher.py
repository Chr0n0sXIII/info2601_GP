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
    if cipher.digit1 == digit:
        if position == 1 :
            return True
    elif cipher.digit2 == digit:
        if position == 2 :
            return True
        elif cipher.digit3 == digit:
            if position == 3 :
                return True
            elif cipher.digit4 == digit:
                if position == 4 :
                    return True
            
    return False

def iscow(cipher_id , digit):
    cipher = Cipher.query.filter_by(id=cipher_id).first()
    if cipher.digit1 == digit:
        return True
    elif cipher.digit2 == digit:
        return True
    elif cipher.digit3 == digit:
        return True
    elif cipher.digit4 == digit:
        return True

    return False