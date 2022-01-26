from os import * 
from time import sleep 

'''                                      
           ███████╗   ███╗    ██      ███╗   ██╗  ████████╗  ███╗   ██╗ ███████╗ ████████╗
           ██╔════╝   ███╝  ██        ████╗  ██║  ╚══██╔══╝  ████╗  ██║ ██╔════╝ ╚══██╔══╝
           ███████╗   █████           ██╔██╗ ██║     ██║     ██╔██╗ ██║ █████╗      ██║
           ╚════██║   ███╗ ██         ██║╚██╗██║     ██║     ██║╚██╗██║ ██╔══╝      ██║ 
           ███████║   ███║   ██       ██║ ╚████║     ██║     ██║ ╚████║ ███████╗    ██║
           ╚══════╝   ╚══╝            ╚═╝  ╚═══╝     ╚═╝     ╚═╝  ╚═══╝ ╚══════╝    ╚═╝
                      
                   
                                    this  code by hash 
                                    time : 12:56 
                                    2021/11/27 
                                    Novamber 
                                    [++] this tool use hack [++]
                                    tool -> skynet version 2.0.1 

'''


class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
    
def Encode_Password_hash():
    chdir("Tools")
    chdir("Encode")
    system("python3 enocdePassword.py")
r = 0
def shell_Command(): 
     
    while True:
        try:
            Command_skynet = input(color.UNDERLINE+color.RED+"skynet"+color.END+color.END+color.WARNING+" > "+color.END)
            if Command_skynet.lower() == "exit" or  Command_skynet.lower() == "return" or Command_skynet.lower() == "quit" or Command_skynet.lower() == "break":
                system("clear")
                main()
                break
            elif Command_skynet.lower() == "version":
                system("clear")
                print(color.RED+"skynet shell version : 1.2.12"+color.END)
      
            system(Command_skynet)
        except : 
            continue 


def hash_file() :
    system("python3 hashfile.py")




def main():
    

                
    try:
     
        while r <= 123:

            system("sudo service tor start > .service.txt ")
            ssh = system("sudo service ssh stop > .service.txt")
            system("bash menu_of_skynet.sh ")
            # information_gathering 
            print("=["+color.HEADER+"skynet version 2.0.1"+color.END+"]")
            print("\n\n")
            print(color.OKGREEN+"["+color.END+color.WARNING+"1"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"Password Attacks"+color.END)
            print(color.OKGREEN+"["+color.END+color.WARNING+"2"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"Web SCAN"+color.END)
            print(color.OKGREEN+"["+color.END+color.WARNING+"3"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"Encode Password hash"+color.END)
            print(color.OKGREEN+"["+color.END+color.WARNING+"4"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"calculator "+color.END)
            print(color.OKGREEN+"["+color.END+color.WARNING+"5"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"skynet shell "+color.END)
            print(color.OKGREEN+"["+color.END+color.WARNING+"6"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"information gathering  "+color.END) 
            print(color.OKGREEN+"["+color.END+color.WARNING+"7"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"creat wordlist "+color.END)
            print(color.OKGREEN+"["+color.END+color.WARNING+"8"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"update and install tool "+color.END)
            print(color.OKGREEN+"["+color.END+color.WARNING+"99"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"------"+color.END+color.RED+"Exit "+color.END)
            response = float(input(color.LOGGING+"\n\nSkynet ~# "+color.END))
            if response == 1:
                chdir("Tools")
                chdir("attack_password")
                system("sudo python3 attack_password.py ")
            elif response == 2: 
                chdir("Tools")
                chdir("scan_&_hacking")
                system("sudo python3 web_hacking.py")

            elif response == 3 : 
                system("sudo python3 encode_password_hash_type_md5.py  ")
            elif response == 4  :
                chdir("Tools")
                chdir("calculator")
                system("python3 calculator.py")
            elif response == 5:
                shell_Command()
            elif response == 6 : 
                chdir("Tools")
                chdir("information_gathering")
                system("python3 information_gathering.py ")
            elif response == 7 : 
                chdir("Tools")
                chdir("wordlist")
                system("sudo python3 wordlist.py ")
            elif response == 8  :
                system("sudo python3  update.py")

            elif response == 99:
                system("clear") 
                break
            else  :
                system("clear")
                print(f"{color.WARNING}[{color.END}" + f"{color.RED}+{color.END}" + f"{color.WARNING}]{color.END} " + str(response) + f" {color.WARNING} not found please try again {color.END}" )
    except:
        system("clear")
        main()
  
if __name__ == "__main__" :
    main()





