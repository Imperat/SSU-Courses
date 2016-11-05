import sys

from manager import Manager
from my_exceptions import *


print "Hello! Write /? for getting list of commands :)"
print "->"

manager = Manager()
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
        continue
    if command == "register":
        print "You username:"
        username = raw_input()
        print "You password:"
        password = raw_input()
        try:
            manager.register_user(username, password)
        except UserAlreadyExists:
            print "Sorry, user with this username already exists ;("
        finally:
            print "->"
        continue
    if command == "login":
        print "You username:"
        username = raw_input()
        print "You password:"
        password = raw_input()
        try:
            manager.login(username, password)
        except WrongPasswordException:
            print "Your password is incorrect! :("
        except UserDoesntExists:
            print "System don't known user with this username :("
        else:
            print "Sucessfylly login as user: '%s'" % username
        finally:
            print "->"
        continue
    if command == "logout":
        manager.logout()
        print "Good bye!"
        print "->"
        continue
    print "Sorry, I don't know this command ;("
    print "->"

