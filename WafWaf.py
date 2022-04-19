print("""
##################################################
# Python3
# Made By Adkali With Love                   A    #
# Need Help? Learn Python!                   D    #
# This Challenge Made For Beginners          K    #
#  H            N                            A    #
#    A        U                              L    #
#      V    F                                I    #
         E
##################################################""")

import time
import random
import hashlib
import os

keep = random.randint(10,55)
password0 = hashlib.md5(b'\ndogs').hexdigest()
up = '\x33\x34'
ra = ''  # I Am Just Nothing But ra...
py = '\x62\x79\x65\x62\x79\x65' 
password1 = 'username'
p = '\x31\x32'
password2 = 'passphrase'
lovely = '\x70\x79\x31\x32\x33\x34'
password3 = 'something'
shell = (p + up + py)
emesu = '\x55\x53\x45\x20\x49\x54\x21'
print('''
Hey, before i will give you that passphrase for the hidden
file inside the picture, you will have to enter the correct password.
''')
time.sleep(1.5)
h = os.system('echo -n aWxvdmVkb2dz')
print('\nUse Me While You Can')
time.sleep(1)
name = input('\nWhat Is Your Name Please? ') # A random number will be given the user
print('Welcome ' + name + str(keep))
time.sleep(1.5)
log = input('What is The password please? ')
if log == shell:
    print('\x70\x75\x70' + lovely,', ' +emesu)
elif log == password3:
    print('password = abcdefghi', 'jklmnopqrstuqxyz')
elif log == password2:
    print('passphrase is...' + password0)
else:
    print('\x57\x72\x6F\x6E\x67 ' 'Password!')
