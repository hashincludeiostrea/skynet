from os  import * 
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
system("sudo git clone https://github.com/Datalux/Osintgram.git ")
chdir("Osintgram")
system("make setup")
username_target_Osintgram = input(f"{color.OKGREEN} please enter username Target >>  {color.END}") 
                    
tool = system("python3 main.py " + username_target_Osintgram  )
