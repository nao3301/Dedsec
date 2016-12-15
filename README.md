# DEDSEC

```
                                
                                            @@@@@@@@   @@@@@@@@@         
                             @@@@@@@      @@@@@@@@@@@ @@@@@@@@@@@@             
                           @@@@@@@@@@@@  @@@@@@ @@@@@ @@@@@@@@@@@@@  @@@@      
  @@@@          @@@@@@@@@@ @@@@@@@@@@@@@ @@@@@@ @@@@  @@@@@%   @@@ @@@@@@@@@   
@@@@@@@@@    @@@@@@@@@@@@@ #@@@@@@@@@@@@ @@@@@@      @@@@@@@     @@@@@@@@@@@@@ 
@@@@@@@@@@   @@@@@@@@@@@@  @@@@@  @@@@@ #&&&&&&&&    @@@@@@@@@@ @@@@@@ @@@@@@@@
 @@@@@@@@@@   @@@@@@@@@@@@  @@@@@  @@@@@ #&&&&&&&&   @@@@@@@@@@ @@@@@   @@@@@@@
  @@@@@@@@@@&  @@@@@@@@@    @@@@&  &&&&&  &&&&&&&&% &&&&&&&&@  &@@@@    @@@@@@@
   @@@@  %@&&&  @@@&&&       &&&&&  &&&&    &&&&&&& &&&&      &&&&@     (@@@@# 
    @@@&   &&&&  &&&&&.      &&&&&  &&&&      %%%% %&&&      &&&&              
     &&&&   &&&%  &&%%%%%%%%  %%%%  %%%% /%%   %%% %%%%%%%  %&&& &&&&&&        
      &&&&   %%%#  %%%%%%%%#  %%%%  %%%% %%%%%%%%% %%%%%%% %%%%&&&&&&          
       %%%%   %%%   %######   ##### #### ########  ##%%%%  %%%%%%%&            
        %%%%   ###  #####      #### #### (######             %%%%               
         %###  ####  #((((     ((((((((/   (##                                  
          ####  #(((  (((( (((( ((((((                                         
           ##(( ((((   ((////// (((                                            
            ((((((((/   ///////                                               
             ((((((//    ///                                                   
              ///////                                          
               ////                                     


                   ++++++++++++++++++++++++++++++++++++++++                    
                    Developed by: Luna (nao3301 & lupa)                      
                    Version: 0.2.0 beta                                        
                   ++++++++++++++++++++++++++++++++++++++++                    
```

[![Platform](https://img.shields.io/badge/platform-multiples-yellowgreen.svg)](https://github.com/nao3301/Dedsec#platforms-tested-) 
[![Packagist](https://img.shields.io/badge/license-MIT-orange.svg)](https://github.com/nao3301/Dedsec/blob/master/LICENSE)&nbsp;

```
Usage : [sudo] Dedsec
 help,  print all Functions
 show,  print all Modules

```

Dedsec is a command line tool which can be used for pentesting.
This tool supports Linux, and it is planed also for windows.

###  help

```
use arrowkeys to use history, use tap for auto completion
exit => closes Dedsec
bash => opens bash ( come with exit back to Dedsec )
show => shows you the modules
setglo => you can set globals, which then will be used by the modules
delglo => deletes all globals
about => about
clshist => clear the history
shutdown => shutsdown your machine
c

```

### show

```
fluxion ==> opens fluxion(tool to crack wlan)
map => maps the wireless networks around you
scan ==> scans other clients in your network
wifite ==> starts wifite
set ==> starts the SEToolkit
ptf ==> starts the pentestframework
msf ==> starts metasploit
kick => kicks everybody out of the network
kicknick ==> kicks one target out of the network
dedpscr ==> cracks password hash with wordlist (dictionary attack)
lip ==> shows your ip adress
shhh ==> starts a listener (for example for the reverse shell from the rubber ducky!)
ssh ==> sets ssh-connection to a client
logout ==> logout

```

### Demo

Here is a demo of Dedsec running on Kali Linux. 

[![Dedsec demo](https://asciinema.org/a/6jo8dd7d66ljrso5xon8ob5ub.png)](https://asciinema.org/a/6jo8dd7d66ljrso5xon8ob5ub)

### Platforms tested :

- Linux

### Platforms comming :

- Windows

### TODO

The TODO list is [here](https://github.com/nao3301/Dedsec/projects/1)

### Installation 

I wrote a Makefile to build Dedsec run `make` & `sudo make install` to build and install

Make sure you have GCC installed

By default, the install directory is `/usr/bin/`, you can change it by modifying `INSTALL_DIR` variable in the [Makefile](https://github.com/nao3301/Dedsec/blob/master/Makefile#L4) 



### Credits

Tool developed by [@nao3301](https://github.com/nao3301) & [@lupa](https://github.com/nao3301)

### Tanks to

- all Developers
  -  lupa
  -  blub
- [@Hak5](https://hak5.org)
- [@tihmstar](https://github.com/tihmstar)
