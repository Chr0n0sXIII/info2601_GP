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

def update_bulls(id, bulls):
    cipher = get_cipher_by_id(id)
    if cipher:
        cipher.bulls = bulls
        db.session.add(cipher)
        return db.session.commit()
    return None

def update_cows(id,cows):
    cipher = get_cipher_by_id(id)
    if cipher:
        cipher.cows = cows
        db.session.add(cipher)
        return db.session.commit()
    return None