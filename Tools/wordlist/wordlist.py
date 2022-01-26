from os import system,chdir
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
import random 

def creat_wordlist_using_python3(length,file_name) :
    try : 
        file_name = input(f"{color.RED} please enter file name >> {color.END}")
        if file_name == "" : 
              creat_wordlist_using_python3(length, file_name)
        length = int(input(f"{color.RED} please enter length password >> {color.END}"))
    except KeyboardInterrupt as error : 
        creat_wordlist_using_python3(length, file_name)
    while True : 
        lower = "abcdefghijklmnqrtb"
        upper = lower.upper() 
        numbers = "012345678910"
        sambole = "!@#$%^&*()_{}[]<>?\+_)(*/*-+.~|\|"
        all = lower + upper + sambole + numbers + sambole 
        Password = "".join(random.sample(all,length))
        print(f"{color.OKBLUE} the password {color.END} ["+color.RED+str(Password)+color.END+f"]  {color.OKBLUE}save in file {color.OKBLUE} [ "+color.RED+str(file_name)+color.END+f"] {color.NOTICE} length password {color.END} "+ str(len(Password)))
        #save_password_in_wordlist = system("echo \""+str(Password)+"\" >> "+file_name)
        file = open(file_name  , "a")
        file.writelines("\n"+Password)

def numbers() :
    try : 
        file_name = input(f"{color.RED} please enter file name >> {color.END}")
        if file_name == "" : 
              numbers()
        length = int(input(f"{color.RED} please enter length password >> {color.END}"))
    except KeyboardInterrupt as error : 
        numbers()
    while True : 
        
        numbers = "012345678910"
        
        
        Password = "".join(random.sample(numbers,length))
        print(f"{color.OKBLUE} the password {color.END} ["+color.RED+str(Password)+color.END+f"]  {color.OKBLUE}save in file {color.OKBLUE} [ "+color.RED+str(file_name)+color.END+f"] {color.NOTICE} length password {color.END} "+ str(len(Password)))
        #save_password_in_wordlist = system("echo \""+str(Password)+"\" >> "+file_name)
        file = open(file_name  , "a")
        file.writelines("\n"+Password)
def word_wordlist() :
    try : 
        file_name = input(f"{color.RED} please enter file name >> {color.END}")
        if file_name == "" : 
              word_wordlist()
        length = int(input(f"{color.RED} please enter length password >> {color.END}"))
    except KeyboardInterrupt as error : 
        word_wordlist()
    while True : 
        word = "abcdefghijklmnclonsdfrtgfsd"
        Password = "".join(random.sample(word,length))
        print(f"{color.OKBLUE} the password {color.END} ["+color.RED+str(Password)+color.END+f"]  {color.OKBLUE}save in file {color.OKBLUE} [ "+color.RED+str(file_name)+color.END+f"] {color.NOTICE} length password {color.END} "+ str(len(Password)))
        #save_password_in_wordlist = system("echo \""+str(Password)+"\" >> "+file_name)
        file = open(file_name  , "a")
        file.writelines("\n"+Password)
def sambole() :
    try : 
        file_name = input(f"{color.RED} please enter file name >> {color.END}")
        if file_name == "" : 
              sambole()
        length = int(input(f"{color.RED} please enter length password >> {color.END}"))
    except KeyboardInterrupt as error : 
        sambole()
    while True : 
        sambole = "!@#$%^&*()_{}[]<>?\+_)(*/*-+.~|\|"
        Password = "".join(random.sample(sambole,length))
        print(f"{color.OKBLUE} the password {color.END} ["+color.RED+str(Password)+color.END+f"]  {color.OKBLUE}save in file {color.OKBLUE} [ "+color.RED+str(file_name)+color.END+f"] {color.NOTICE} length password {color.END} "+ str(len(Password)))
        #save_password_in_wordlist = system("echo \""+str(Password)+"\" >> "+file_name)
        file = open(file_name  , "a")
        file.writelines("\n"+Password)
def  main_creat_wordlist () :
    while True :
        try :
            print(color.WARNING+"""        
                               
                ##############################################################|
                #[1]========numbers                                           |
                #[2]========word                                              |
                #[3]--------sambole                                           |
                #[4]--------random password (numbers and word and  sambole)   |
                #[99]-------retrun in main menu                               |
                ###############################################################

                  """+color.END)
            response = float(input(f"skynet( "+f"{color.RED}wordlist{color.END} ) >> "))
            if response == 1: 
                numbers()
            elif response == 2:
                word_wordlist()
            elif response == 3: 
                sambole()
            elif response == 4:
                file = ""
                len_password = ""
                creat_wordlist_using_python3(len_password,file)
            elif response == 99:
                chdir("..")
                chdir("..")
                system("python3 skynetv2.py ")
                break 
                
            else : 
                system("clear")
                print(color.OKGREEN+"["+color.END+color.WARNING+"+"+color.END+color.OKGREEN+"] "+color.END+str(response)+color.RED+" [not found]  "+color.END)
        except ValueError as errro :
            system("clear")
            continue
        except KeyboardInterrupt as error2 :
            system("clear")
            continue
if __name__ == "__main__":
   main_creat_wordlist()