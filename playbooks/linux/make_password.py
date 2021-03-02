#!/usr/bin/python3
import sys, crypt
if len(sys.argv) == 1 : sys.exit("You must specify a password as an argument") 
print(crypt.crypt(sys.argv[1), crypt.mksalt(crypt.METHOD_SHA512))) 

# chmod u+x make_password.py
# ./make_password.py thisisapassword
