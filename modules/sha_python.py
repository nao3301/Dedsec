#!/usr/bin/python2
import hashlib
import sys
import getopt

counter = 0
word=''
#print "Supports: md5, sha1, sha224, sha256, sha384, sha512"
if sys.argv[1] != "0":
    input_hash_type = sys.argv[1]
else :
    input_hash_type=raw_input("Hash-Algorithmus: ")

if sys.argv[2] != "0":
    pashash = sys.argv[2]
else:
    pashash=raw_input("\nHSash: ")
   
if sys.argv[3] != "0":
    wordlist = sys.argv[3]
else :
    wordlist=raw_input("Wordlist: default[0] ")


if wordlist == "0":
	wordlist='pasawd_lists/common-passwords.txt'

try:
	dictfile = open(wordlist,'r')
except Exception as e:
	print "unable to open file, make sure you typed the correct filename.", e
	sys.exit()
	
if input_hash_type == "md5":
	htype = hashlib.md5
elif input_hash_type == "sha1":
	htype = hashlib.sha1
elif input_hash_type == "sha224":
	htype = hashlib.sha224
elif input_hash_type == "sha256":
	htype = hashlib.sha256
elif input_hash_type == "sha384":
	htype = hashlib.sha384
elif input_hash_type == "sha512":
	htype = hashlib.sha512
	
for word in dictfile:
	counter +=1
	word = word.strip()
	hashed = htype(word).hexdigest()
	
	if pashash == hashed:
		print "\npassword found:{1} words testet:{0} ".format(counter,word)
		dictfile.close()
		sys.exit()
	
	
else :
		print "\npassword not found. words testet: {0}".format(counter)
		
dictfile.close()	
sys.exit()
	
	
