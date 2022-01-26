import os

import hashlib
from time import sleep

Open_wordlist = ""



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



def Encode_Passwrod_Hash():
    os.system("clear")
   
    Passwrod_hash = input(color.NOTICE + "enter passwrod hash => " + color.END)
    if Passwrod_hash == "":
        speed_Encode_Passwrod_Hash()

    Wordlist = input(color.NOTICE + "enter Wordlist => " + color.END)
    if Wordlist == "":
        speed_Encode_Passwrod_Hash()
    print(color.WARNING + "==========================================" + color.END)
    try:
        Open_wordlist = open(Wordlist, "r")
    except:
        os.system("clear")
        print(color.RED + "no file found " + color.END)
        quit()
    for Word in Open_wordlist:
        encode_Passwrod = Word.encode('utf-8')
        disget = hashlib.md5(encode_Passwrod.strip()).hexdigest()
        find = 1 

        print(color.OKGREEN + "[" + color.END + "+" + color.OKGREEN + "]" + color.END + color.RED + color.RED + "try in Password" + color.END + color.NOTICE + " =>" + color.END + color.OKGREEN + Word + color.END )
        sleep(1)
        # print(color.OKGREEN+"["+color.END+"+"+color.OKGREEN+"]"+color.END+color.RED+color.RED+"try in Password"+color.END+color.NOTICE+" =>"+color.END+color.OKGREEN+Word+color.END+color.OKBLUE+"ERROR"+color.END+"|")

        if disget == Passwrod_hash:
            os.system("clear ")
            print(color.RED + "Passwrod Found " + color.END)
            print("\n")
            print(
                color.OKGREEN + "[" + color.END + "+" + color.OKGREEN + "]" + color.END + color.RED + "passwrod hash => " + color.END + Passwrod_hash)
            print(
                color.OKGREEN + "[" + color.END + "+" + color.OKGREEN + "]" + color.END + color.RED + "Wordlist  => " + color.END + Wordlist)
            print(
                color.OKGREEN + "[" + color.END + "+" + color.OKGREEN + "]" + color.END + color.WARNING + "the passwrod is  => " + color.END + Word)
            i = input()

    else:
        print(f"{color.RED}[#] {color.END} the password not found in wordlist please try again ")
        i = input()
        sleep(1)



def speed_Encode_Passwrod_Hash():
    os.system("clear")
    
    Passwrod_hash = input(color.NOTICE + "enter passwrod hash => " + color.END)
    if Passwrod_hash == "":
        speed_Encode_Passwrod_Hash()

    Wordlist = input(color.NOTICE + "enter Wordlist => " + color.END)
    if Wordlist == "":
        speed_Encode_Passwrod_Hash()
    print(color.WARNING + "==========================================" + color.END)
    try:
        Open_wordlist = open(Wordlist, "r")
    except:
        os.system("clear")
        print(color.RED + "no file found " + color.END)
        quit()
    for Word in Open_wordlist:
        encode_Passwrod = Word.encode('utf-8')
        disget = hashlib.md5(encode_Passwrod.strip()).hexdigest()
        find = 1

        print(color.OKGREEN + "[" + color.END + "+" + color.OKGREEN + "]" + color.END + color.RED + color.RED + "try in Password" + color.END + color.NOTICE + " =>" + color.END + color.OKGREEN + Word + color.END + color.OKBLUE + "ERROR" + color.END + "/")
        # print(color.OKGREEN+"["+color.END+"+"+color.OKGREEN+"]"+color.END+color.RED+color.RED+"try in Password"+color.END+color.NOTICE+" =>"+color.END+color.OKGREEN+Word+color.END+color.OKBLUE+"ERROR"+color.END+"|")

        if disget == Passwrod_hash:
            os.system("clear ")
            print(color.RED + "Passwrod Found " + color.END)
            print("\n")
            print(
                color.OKGREEN + "[" + color.END + "+" + color.OKGREEN + "]" + color.END + color.RED + "passwrod hash => " + color.END + Passwrod_hash)
            print(
                color.OKGREEN + "[" + color.END + "+" + color.OKGREEN + "]" + color.END + color.RED + "Wordlist  => " + color.END + Wordlist)
            print(
                color.OKGREEN + "[" + color.END + "+" + color.OKGREEN + "]" + color.END + color.WARNING + "the passwrod is  => " + color.END + Word)
            i = input()

    else:
        print(f"{color.RED}[#] {color.END} the password not found in wordlist please try again ")
        i = input()
        sleep(1)


def code_Password():
    os.system("clear")
    Target_code_password = input(
        color.OKGREEN + "code Password please enter password " + color.END + color.RED + "=>" + color.END)
    os.system("echo -n " + Target_code_password + " |md5sum| tr -d \"-\" >> hash.txt")
    show_Password = os.system("cat hash.txt")
    print(show_Password)
    print("\nthe Password hash save in the note hash in folder encode ")

    y = input()


def menu_code_Password():
    r = 1
    while r <= 112:
        try:

            os.system("clear")
            print(f"""  
           {color.HEADER}\t88""Yb    db    .dP"Y8 .dP"Y8 Yb        dP  8888b.{color.RED}  
           {color.IMPORTANT}\t88__dP   dPYb   `Ybo." `Ybo."  Yb  db  dP   8I  Yb{color.RED} 
           {color.OKGREEN}\t88244   dP__Yb  o.4Y8b o.`Y8b   YbdPYbdP    8I  dY{color.RED} 
           {color.WARNING}\t88     dP"d""Yb 8bodP' 8bodP'    YP  YP     8888Y"{color.RED} 
            """)
            # fast encode passwrod hash fast encode passwrod hash  fast encode passwrod hash fast encode passwrod hash
            print(f"""
                       encode password hash type (md5)  
             -----------------------------------------------
           \t{color.RED}[1]{color.END}{color.WARNING}------{color.END}{color.IMPORTANT}code Password {color.END} 
           \t{color.RED}[2]{color.END}{color.WARNING}------{color.END}{color.IMPORTANT}encode Password hash  (slow){color.END}
           \t{color.RED}[3]{color.END}{color.WARNING}------{color.END}{color.IMPORTANT}encode Password hash  (speed){color.END}
           \t{color.RED}[4]{color.END}{color.WARNING}------{color.END}{color.IMPORTANT}show Password hash in file {color.END}
           \t{color.RED}[5]{color.END}{color.WARNING}------{color.END}{color.IMPORTANT}remove list password hash  {color.END}
           \t{color.RED}[99]{color.END}{color.WARNING}------{color.END}{color.IMPORTANT}return in main  menu (skynet){color.END}
           """)
            response = float(input(color.OKGREEN + "\n\nencode passwrod hash ~# " + color.END))
            if response == 1:
                code_Password()
            elif response == 2:
                Encode_Passwrod_Hash()


            elif response == 3:
                speed_Encode_Passwrod_Hash()
            elif response == 4:
                os.system("cat hash.txt")
                i = input()
            elif response == 5:
                os.remove("hash.txt")
                print(f" {color.RED} the password hash list was remove {color.END}")
                i = input()


            elif response == 99:
                os.system("clear")
                os.chdir("..")
                os.chdir("..")
                os.system("python3 skynetv2.py")
                break




        except:
            menu_code_Password()


menu_code_Password()
# FINSGH
