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

```
Usage : [sudo] Dedsec
  ~ [command]

```

Dedsec is a command line tool which can be used for pentesting.
This tool supports Linux, and it is planed also for windows.

### login 

nickname:[nickname]

confirm your membership: [password]

###  help

```
use arrowkeys to use history, use tap for auto completion

exit     => closes Dedsec
bash     => opens bash ( come with exit back to Dedsec )
show     => shows you the modulessetglo   => you can set globals, which then will be used by the modules
delglo   => deletes all globals
about    => about
payload  => menu for payloads for the USB rubberducky
pinemod  => write a modul for the wifi pineapple nano
clshist  => clear the history
shutdown => shutdown your machine
c

```

### show

```
fluxion  ==> opens fluxion(tool to crack wlan)
map      ==> maps the wireless networks around you
scan     ==> scans other clients in your network
wifite   ==> starts wifite
set      ==> starts the SEToolkit
ptf      ==> starts the pentestframework
msf      ==> starts metasploit
kicknick ==> kicks one target out of the network
dedpscr  ==> cracks password hash with wordlist (dictionary attack)
lip      ==> shows your ip adress
shhh     ==> starts a listener (for example for the reverse shell from the rubber ducky!)
ssh      ==> sets ssh-connection to a client
logout   ==> logout


```

### Platforms tested :

- Kali Linux

### Platforms comming :

- Windows 

### Installation 

Start a terminal in the Dedsec folder and type:
```
g++ -o Dedsec{,.cpp} -lreadline
```

Make sure you have GCC installed

Install.sh comming soon

### Community

You are invited to use, optimize and change Dedsec! Just do whatever you want!
Because it is still in beta feel free to tell us any improvements, we will fix any issues as fast as possible.
If you add anything to the code and you consider it worth sharing please send us an [email](nao.lupa@gmail.com). We are looking forward to it!
For any other questions contact [us](nao.lupa@gmail.com). We will try to help you as much as we can.

### Credits

Tool developed by [@nao3301](https://github.com/nao3301) & [@lupa](https://github.com/nao3301)

### Tanks to

- all Developers
  -  lupa
  -  d3vil
- [@Hak5](https://hak5.org)
- [@tihmstar](https://github.com/tihmstar)
- [kali linux](https://kali-linux.org)
- [Metasploit project](https://metasploit.org)
- [pentestingframework](http://github.com/ptf)
- github
- gnu projekt








# Dedsec
[will become] command line framework 


compile Dedsec with: g++ -o Dedsec{,.cpp} -lreadline

if you have ideas for new functions or modules send them to me! 
we will check them and load them up!
