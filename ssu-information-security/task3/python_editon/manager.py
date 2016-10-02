import sqlite3
import os
import hashlib

from encryptor import Encryptor
from my_exceptions import *


class Manager(object):
    def __init__(self):
        self.user = None
        self.encryptor = Encryptor()

    def register_user(self, username, password):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        users = cur.execute('SELECT * FROM users')
        for user in users:
            if username == user[1]:
                raise UserAlreadyExists
        cur.execute('INSERT INTO USERS VALUES(null, ?, ?)',
                    [username, sqlite3.Binary(hashlib.sha256(password).digest())])
        con.commit()
        con.close()
        os.system("mkdir '.%s'" % username)
        self.user = username

    def logout(self):
        self.encryptor.encrypt(".%s" % self.user)
        self.user = None

    def login(self, username, password):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        users = cur.execute('SELECT * FROM users')
        find = False
        for user in users:
            if username == user[1]:
                find = True
                if hashlib.sha256(password).digest() == bytes(user[2]):
                    self.user = username
                    self.encryptor.decrypt(".%s" % username)
                else:
                    raise WrongPasswordException # Wrong Password
        if not find:
            raise UserDoesntExists # User doesn't exists


