# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:12:23 2018

@author: Bangun
"""
users = {'paul':'1234', 'pbk':'4321','bangun':'1111'}

def newusers():
    global users
    newname = input('Enter a name: ')
    if users.get(newname):
        print('name exist, use another')
        login()
    else:
        newpass= input('Enter a password: ')
        users[newname] = newpass
    
    
def oldusers():
    global users
    name = input('Enter name: ')
    passw = input('Enter pass: ')
    if users.get(name):
        if users[name] == passw:
            print('{}, welcome back!'.format(name))
        else:
            print('login incorrect')
            login()
    else:
        print('login incorrect')
        login()

def login():
    option = input('(N)ew user login\n(O)ld user login\n(E)xit\n\n>> ')
    if option == 'N':
        newusers()
    elif option == 'O':
        oldusers()
    else:
        print('Exiting program')
        return None

if __name__ == '__main__':
    login()