import sys
import sqlite3
import os
import hashlib

from manager import Manager



print "Hello! Write /? for getting list of commands :)"
print "->"

while True:
    command = raw_input()
    if command == "exit":
    	sys.exit()
    if command == "/?":
    	print "-------------------------------"
    	print "- exit     exit from programm -"
    	print "- register  register new user -"
    	print "- login         login as user -"
    	print "- logout               logout -"
    	print "-------------------------------"
    if command == "register":
    	print "You username:"
    	username = raw_input()
    	print "You password:"
    	password = raw_input()
    	manager.register_user(username, password)
    if command == "login"
        print "You username:"
        username = raw_input()
        print "You password:"
        password = raw_input()
        manager.login(username, password)
    if command == "logout":
    	manager.logout()

