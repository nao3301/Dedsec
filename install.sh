#!/bin/bash
# install.sh - install Dedsec


if [ "${UID}" != "0" ]; then
	echo -e "\e[1;31m[!] This script must be run as root\e[0m" 1>&2
	exit 1
else
	if ! [ -a /usr/share/Dedsec/Dedsec ]; then
		git clone --recursive https://github.com/nao3301/dedsec.git /usr/share/Dedsec
		cd /usr/share/Dedsec
		g++ -o Dedsec{,.cpp} -lreadline
		cd
	fi
	cp /usr/share/Dedsec/bin/Dedsec /usr/local/bin/Dedsec
	cd /usr/local/bin/
	chmod +x Dedsec
	cd
	
fi

#g++ -o Dedsec{,.cpp} -lreadline
#cp /usr/share/Dedsec/bin/Dedsec /usr/local/bin/Dedsec
