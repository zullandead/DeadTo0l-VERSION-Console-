import os,sys,time,random
from colorama import Fore
import socket
import speedtest
from datetime import datetime,date

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


banner = '''


                                                                                                                                            
                                                                    dddddddd                                                                
DDDDDDDDDDDDD                                                       d::::::d  TTTTTTTTTTTTTTTTTTTTTTT                   000000000     lllllll 
D::::::::::::DDD                                                    d::::::d  T:::::::::::::::::::::T                 00:::::::::00   l:::::l 
D:::::::::::::::DD                                                  d::::::d  T:::::::::::::::::::::T               00:::::::::::::00 l:::::l 
DDD:::::DDDDD:::::D                                                 d:::::d   T:::::TT:::::::TT:::::T              0:::::::000:::::::0l:::::l 
  D:::::D    D:::::D     eeeeeeeeeeee    aaaaaaaaaaaaa      ddddddddd:::::d   TTTTTT  T:::::T  TTTTTTooooooooooo   0::::::0   0::::::0 l::::l 
  D:::::D     D:::::D  ee::::::::::::ee  a::::::::::::a   dd::::::::::::::d           T:::::T      oo:::::::::::oo 0:::::0     0:::::0 l::::l 
  D:::::D     D:::::D e::::::eeeee:::::eeaaaaaaaaa:::::a d::::::::::::::::d           T:::::T     o:::::::::::::::o0:::::0     0:::::0 l::::l 
  D:::::D     D:::::De::::::e     e:::::e         a::::ad:::::::ddddd:::::d           T:::::T     o:::::ooooo:::::o0:::::0 000 0:::::0 l::::l 
  D:::::D     D:::::De:::::::eeeee::::::e  aaaaaaa:::::ad::::::d    d:::::d           T:::::T     o::::o     o::::o0:::::0 000 0:::::0 l::::l 
  D:::::D     D:::::De:::::::::::::::::e aa::::::::::::ad:::::d     d:::::d           T:::::T     o::::o     o::::o0:::::0     0:::::0 l::::l 
  D:::::D     D:::::De::::::eeeeeeeeeee a::::aaaa::::::ad:::::d     d:::::d           T:::::T     o::::o     o::::o0:::::0     0:::::0 l::::l 
  D:::::D    D:::::D e:::::::e         a::::a    a:::::ad:::::d     d:::::d           T:::::T     o::::o     o::::o0::::::0   0::::::0 l::::l 
DDD:::::DDDDD:::::D  e::::::::e        a::::a    a:::::ad::::::ddddd::::::dd        TT:::::::TT   o:::::ooooo:::::o0:::::::000:::::::0l::::::l
D:::::::::::::::DD    e::::::::eeeeeeeea:::::aaaa::::::a d:::::::::::::::::d        T:::::::::T   o:::::::::::::::o 00:::::::::::::00 l::::::l
D::::::::::::DDD       ee:::::::::::::e a::::::::::aa:::a d:::::::::ddd::::d        T:::::::::T    oo:::::::::::oo    00:::::::::00   l::::::l
DDDDDDDDDDDDD            eeeeeeeeeeeeee  aaaaaaaaaa  aaaa  ddddddddd   ddddd        TTTTTTTTTTT      ooooooooooo        000000000     llllllll


                                                      By: ZullanCode
                                                    TG: @ZULLANSELL
                                                      YT: ZullanHack

'''

print(banner)
time.sleep(1.3)
flush('// Установка утилиты...')
os.system('pip install socket')
os.system('pip install speedtest')
os.system('pip install colorama')
flush('// Установка завершена')
time.sleep(1)
os.system('cls')
os.system('python main.py')