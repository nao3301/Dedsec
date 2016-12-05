#!/usr/bin/python2
import hashlib
import sys
import getopt

counter = 0
word=''
print "Supports: md5, sha1, sha224, sha256, sha384, sha512"
input_hash_type=raw_input("Hash-Algorithmus: ")
#pashash ='dc76e9f0c0006e8f919e0c515c66dbba3982f785'
pashash=raw_input("\nhash: ")
wordlist=raw_input("Wordlist: default[0] ")
if wordlist == "0":
	wordlist='/home/nao3301/Downloads/crackstation-human-only.txt'

try:
	dictfile = open(wordlist,'r')
except Exception as e:
	print "Unable to open file, make sure you typed the correct filename.", e
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
		print "\nPassword found:{1} words testet:{0} ".format(counter,word)
		dictfile.close()
		sys.exit()
	
	
else :
		print "\nPassword not found. TSested words: {0}".format(counter)
		
dictfile.close()	
sys.exit()
	
	
