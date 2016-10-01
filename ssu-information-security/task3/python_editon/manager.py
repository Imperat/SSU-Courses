import sqlite3
import os
import hashlib
import sys

class Manager(object):
    def __init__(self):
        self.user = None

    def register_user(self, username, password):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        users = cur.execute('SELECT * FROM users')
        for user in users:
            if username == user[1]:
                raise Exception
        cur.execute('INSERT INTO USERS VALUES(null, %s, %s)' % (
            username, hashlib.sha256(password)))
        con.close()
        os.system("mkdir '.%s'" % username)
        self.user = username

    def logout(self):
        Encryptor.encript(".%s" % username)
        self.user = None

    def login(self, username, password):
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        users = cur.execute('SELECT * FROM users')
        find = False
        for user in users:
            if username == user[1]:
                find = True
                if hashlib.sha256(password) == user[2]:
                    self.user = username
                    Encryptor.dencript(".%s" % username)
                else:
                    raise Exception # Wrong Password
        if not Find:
            raise Exception # User doesn't exists


