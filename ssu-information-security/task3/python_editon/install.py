#!/usr/bin/env python
import sqlite3

print "Creating users database:"
con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username VARCHAR(100), hash BLOB)')
con.commit()
print "Successfully created database for users!"
