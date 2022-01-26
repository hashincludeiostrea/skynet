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
def main() :
    try :
        while True :
            print(color.RED  + """
                 =============================================
                 # [1]------zphisher                         #
                 # [2]------setoolkit                        #
                 # [3]------blackeye                         #
                 # [4]------PyPhisher                        #
                 # [5]------retrun in main menu (skynet)     #
                 ============================================= 
                  
                  
            """ + color.END )
            response_attack_password = float(input(f'skynet({color.RED}attack password{color.END}) >> '))
            if  response_attack_password == 1:
                system("chmod +x zphisher.sh && ./zphisher.sh")
            elif response_attack_password == 2 :
                system("bash setoolkit.sh ")
            elif response_attack_password == 3 :
                system("chmod +x blackeye.sh && ./blackeye.sh")

            elif response_attack_password == 4 :
                system("chmod +x PyPhisher.sh && ./PyPhisher.sh")
            elif response_attack_password == 5 :
                chdir("..")
                chdir("..")
                system("sudo python3 skynetv2.py")
                break
            else :
                print(f"{color.WARNING}[{color.END}" + f"{color.OKBLUE}#{color.END}" + f"{color.WARNING}]{color.END}" + str(response_attack_password) + f"{color.RED} incorrect choice please try again{color.END}")





    except ValueError as error :
        system("clear"),print(error)
        main()
if __name__ == "__main__"  :
    main()