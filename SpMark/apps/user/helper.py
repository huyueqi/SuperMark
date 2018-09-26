import hashlib

from django.conf import settings


def new_password(val):
    tokey = settings.SECRET_KEY
    password = tokey + val
    h = hashlib.md5(password.encode('utf-8'))
    return h.hexdigest()
