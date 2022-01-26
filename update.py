from os import * 

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
menu = """

                      ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888::::::::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::::::::::::''
                      ``:::::::::''
"""
# start update 
def update():
    system("bash  updateandinstall.sh ")
    print(color.OKGREEN+"installtion tool and update  "+color.END)


    print("\n\n")
    system("sudo apt update -y ")
    system("sudo apt upgrade -y ")
    system("sudo apt-get update -y ")
    system("sudo apt-get upgrade -y ")
    system("sudo apt full-upgrade -y ")
    system("sudo apt-get full-upgrade -y ")
    
    system("sudo apt install sherlock -y ")
    system("sudo apt install nmap -y")
    system("sudo apt install hashcat -y")
    system("sudo apt install tor -y")
    system("sudo apt install sqlmap -y")
    system("sudo apt install unzip -y")
    system("sudo apt install curl -y")
    system("sudo apt set -y")
    system("sudo apt install python -y")
    system("sudo apt install python-pip -y")
    system("sudo apt install python2 -y")
    system("sudo apt install python3 -y")
    system("sudo apt install python3-pip -y" )
    system("sudo python3 skynetv2.py")
    exit()
    quit()     

    



if __name__ == "__main__" :
      update() 

   
