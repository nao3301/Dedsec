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
                    Version: 0.2.2 beta                                        
                   ++++++++++++++++++++++++++++++++++++++++                    
```


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
show     => shows you the modules
setglo   => you can set globals, which then will be used by the modules
delglo   => deletes all globals
about    => about
clshist  => clear the history
shutdown => shutdown your machine
time     => shows time and date
note     => save your output in a note file
logout   ==> logout
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
ducky    ==> opens the DuckToolkit to encode ducky scrips
lip      ==> shows your ip adress
shhh     ==> starts a listener (for example for the reverse shell from the rubber ducky!)
ssh      ==> sets ssh-connection to a client
turtcon  ==> connects to your Lan-Turtle (ssh)
pinecon  ==> connects to your WIFI-Pineapple (ssh)


```

### Platforms tested :

- Kali Linux
- Arch Linux

### Platforms comming :

- Windows 

### Installation 

Download the install.sh and make it executable. This can be done like this:
Start a terminal in the folder and type:
```
sudo chmod +x install.sh
```
Then type the following to run the install.sh:
```
sudo ./install.sh
```

Make sure you have GCC installed


### Community

You are invited to use, optimize and change Dedsec! Just do whatever you want!
Because it is still in beta feel free to tell us any improvements, we will fix any issues as fast as possible.
If you add anything to the code and you consider it worth sharing please send us an [email](nao.lupa@gmail.com). We are looking forward to it!
For any other questions contact [us](nao.lupa@gmail.com). We will try to help you as much as we can.

### Credits

Tool developed by [@nao3301](https://github.com/nao3301) & [@lupa](https://github.com/nao3301)

#### Updates

2_0
- help
- modules

2_1
- autocompletion
- example

2_2
- install.sh
- note

### Tanks to

- all Developers
  -  lupa
  -  d3vil
- [@Hak5](https://hak5.org)
- [@tihmstar](https://github.com/tihmstar)
- [kali linux](https://kali.org)
- [Metasploit project](https://www.metasploit.com)
- [pentestingframework](https://github.com/trustedsec/ptf)
- Wifite
- github
- gnu projekt
