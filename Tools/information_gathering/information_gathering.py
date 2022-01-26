from os import *
from  time import  sleep
#from scapy.all import  IP
 
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
# sqlmap 1
# nmap   2
# sherlock 3
# setoolkit  4
# metasploit faremwork 5
# Osintgram  6
# nikto
# ICMP
def sherlock () : 
    menu_sherlock = f"""
    
{color.IMPORTANT}\t\t\t.dP"Y8    88  88  888888  88""Yb  88         dP"Yb    dP"Yb  88  dP{color.END}
{color.RED}\t\t\t`Ybo."    88  88  88__    88__dP  88        dP   Yb  dp      88odP {color.END}
{color.WARNING}\t\t\t o.`Y8b   888888  88""    88"Yb   88        Yb   dP  Yb      88"Yb {color.END} 
{color.NOTICE}\t\t\t 8bodP'   88  88  888888  88  Yb  YBYBYBYBY  YbodP    YbodP  88  Yb{color.END} 
        
        
    """
    system('clear')
    USERNAME_TARGET =  input(f"{color.HEADER}please enter Target  username  >> {color.END}")
    if USERNAME_TARGET == "": 
            sherlock() 
    while True : 
       
        system("clear")
        try : 
            print(menu_sherlock)
            print(f"""
            ==============================================================================================================
            |[1]---------sherlock  Output sites where the username was not found [sherlock --print-all]
            |[2]---------sherlock  Output sites where the username was found [sherlock --print-found]
            |[3]---------sherlock  Time (in seconds) to wait for response to requests [sherlock --time out ]
            |[4]---------sherlock  Create Comma-Separated Values (CSV) File.  [sherlock  --CSV  ]
            |[5]---------sherlock  show version  [sherlock --version]
            |[6]---------return in main menu 
            ==============================================================================================================
             
            """)
            print(f"\t\t\t\t\t{color.RED} The target is =>  {color.END} >> "+color.OKBLUE+USERNAME_TARGET+color.END)
            print("\n\n\n")
            response = float(input(f"information gathering ("+f"{color.RED}sherlock{color.END}"+")" + ">> "))
            if response == 1 : 
                output = system("sudo sherlock --timeout 1 --print-all " + USERNAME_TARGET )
                continue 
            elif response == 2: 
                output = system("sudo sherlock --timeout 1 --print-found " + USERNAME_TARGET ) 
            elif response == 3 : 
                output = system("sudo sherlock --timeout 1 " + USERNAME_TARGET )
            elif response == 4 : 
                output = system("sudo sherlock --timeout 1   --csv " + USERNAME_TARGET )
            elif response == 5: 
                output = system("clear && sudo sherlock --version  ")
            elif response == 6  : 
                main() 
            else  : 
                print(f"{color.WARNING}[{color.END}" + f"{color.OKBLUE}#{color.END}" + f"{color.WARNING}]{color.END}" + str(response) + f"{color.RED} incorrect choice please try again {color.END}") 
                

        except ValueError as error  : 
            
            
            continue 
            
        except KeyboardInterrupt as error2 :
            system("clear"),print(error2)
            
            continue 
            

def Nmap():
    system("clear")
    print(color.OKGREEN + "\t\texample => www.site.com or 127.0.0.1  ")
    Target_nmap = input(color.WARNING + "\nenter Target website  or IP addresse" + color.END + color.RED + "=>" + color.END)
    if Target_nmap ==  "" :
        Nmap()

    while True:
        try :

            print(color.OKGREEN + '''
               \t\t\t88b 88 8b    d8    db    88""Yb
               \t\t\t88Yb88 88b  d88   dPYb   88__dP
               \t\t\t88 Y88 88YbdP88  dP__Yb  88"""
               \t\t\t88  Y8 88 YY 88 dP""""Yb 88 ''' + color.END)
            print(color.RED + "\t\t\t\tthe Target is => " + color.END + Target_nmap)

            print(color.IMPORTANT + """
                        <1>--------namp List Scan - simply list targets to scan [nmap -sL]
                        <2>--------nmap Ping Scan - disable port scan [nmap -sn]
                        <3>--------nmap Show all packets sent and received [nmap  --packet-trace]
                        <4>--------nmap UDP Scan [nmap  -sU]
                        <5>--------nmap Treat all hosts as online -- skip host discovery [nmap -Pn]
                        <6>--------nmap stealth scan [nmap -sS]
                        <7>--------namp update Update the script database [nmap --script-updatedb]
                        <99>------=retrun main mneu""" + color.END)
            response = float(input(color.WARNING + "\nWeb Sacn ~#" + color.END))
            # 1
            if response == 1:
                print("\n\n")
                choice = input(
                    color.OKBLUE + "do you need use /24 if you have need please enter (yes) if you have not need please enter (no) => " + color.END)
                if choice == "yes":
                    nmap_Output = system("sudo nmap -sL " + Target_nmap + "/24")
                    i = input()
                elif choice == "no":
                    nmap_Output = system("sudo nmap -sL " + Target_nmap)
                    i = input()
                else:
                    system("clear")
                    print(color.HEADER + " the => " + choice + " : incorrect choice ")
            # 2
            elif response == 2:
                choice = input(
                    color.WARNING + "do you need use /24 if you have need please enter (yes) if you have not need please enter (no) => " + color.END)
                if choice == "yes":
                    nmap_Output = system("sudo nmap -sn  " + Target_nmap + "/24")
                    i = input()
                elif choice == "no":
                    nmap_Output = system("sudo nmap -sn  " + Target_nmap)
                    i = input()
                else:
                    system("clear")
                    print(color.HEADER + " the => " + choice + " : incorrect choice ")
            elif response == 4:

                choice = input(
                    color.WARNING + "do you need use /24 if you have need please enter (yes) if you have not need please enter (no) => " + color.END)
                if choice == "yes":
                    nmap_Output = system("sudo nmap --sU  " + Target_nmap + "/24")
                    i = input()
                elif choice == "no":
                    nmap_Output = system("sudo nmap --sU  " + Target_nmap)
                    i = input()
                else:
                    system("clear")
                    print(color.HEADER + " the => " + str(choice) + " : incorrect choice ")
            elif response == 3:
                choice = input(
                    color.WARNING + "do you need use /24 if you have need please enter (yes) if you have not need please enter (no) => " + color.END)
                if choice.lower() == "yes":
                    system("clear")
                    system("sudo nmap --packet-trace " + Target_nmap + "/24")
                elif choice.lower() == "no":
                    system("clear")
                    system("sudo nmap --packet-trace " + Target_nmap)
                else:
                    system("clear")
                    print(color.HEADER + " the => " + str(choice) + " : incorrect choice " + color.END)



            elif response == 4:
                choice = input(
                    color.WARNING + "do you need use /24 if you have need please enter (yes) if you have not need please enter (no) => " + color.END)
                if choice == "yes":
                    nmap_Output = system("sudo nmap -sU  " + Target_nmap + "/24")
                    i = input()
                elif choice == "no":
                    nmap_Output = system("sudo nmap -sU " + Target_nmap)
                    i = input()
                else:
                    system("clear")
                    print(color.HEADER + " the => " + str(choice) + " : incorrect choice ")
            elif response == 5:

                choice = input(
                    color.WARNING + "do you need use /24 if you have need please enter (yes) if you have not need please enter (no) => " + color.END)
                if choice.lower() == "yes":
                    system("clear")
                    system("sudo nmap  -Pn " + Target_nmap + "/24")
                elif choice.lower() == "no":
                    system("clear")
                    system("sudo nmap  -Pn " + Target_nmap)
                else:
                    print(color.HEADER + " the => " + str(choice) + " : incorrect choice ")





            elif response == 6:
                choice = input(
                    color.WARNING + "do you need use /24 if you have need please enter (yes) if you have not need please enter (no) => " + color.END)
                if choice == "yes":
                    nmap_Output = system("sudo nmap -sS  " + Target_nmap + "/24")
                    i = input()
                elif choice == "no":
                    nmap_Output = system("sudo nmap -sS  " + Target_nmap)
                    i = input()
                else:
                    system("clear")
                    print(color.HEADER + " the => " + str(choice) + " : incorrect choice ")
            elif response == 7:
                system("clear")
                system("sudo nmap --script-updatedb")

            elif response == 99:
                main()

            else:
                system("clear")
                print(
                    color.OKGREEN + "[" + color.END + color.WARNING + str(
                        choice) + color.END + color.OKGREEN + "]" + color.END + color.RED + " the =>" + response + " [not found]  " + color.END)

        except ValueError as error :
            system("clear"), print(error)
            continue
        except KeyboardInterrupt as error2 :
            system("clear"),print(error2)
            continue
        except NameError as error :
            system("clear"),print()
            continue
 #
menu_sqlmap = f"""
\t\t\t\t        ___
\t\t\t\t      __H__
\t\t\t\t  ___ ___[{color.RED}"{color.END}]_____ ___ ___ 
\t\t\t\t |_ -| . [{color.RED}.{color.END}]     | .'| . |
\t\t\t\t |___|_  [{color.RED}.{color.END}]_|_|_|__,|  _|
\t\t\t\t       |_|V...       |_|
      """
def sqlmap():
    system("clear")
    print(color.OKGREEN + "\t\texample => http://www.site.com/vuln.php?id=1 ")
    sqlmap_Target = input(color.WARNING + "\nenter Target Website " + color.END + color.RED + "[URL]" + color.END + color.NOTICE + " => " + color.END)
    if sqlmap_Target == "":
        sqlmap()
    system("clear")
    while True:
        try  :
            print("\t\t\t" + color.WARNING + menu_sqlmap + color.END)
            print(color.RED + "\t\t\t\tTarget URL => " + sqlmap_Target + color.END)

            print(color.IMPORTANT + """
                     ==========================================================================
                     {1}----sqlmap database sqlmap [sqlmap --dbs]                             |  
                     {2}----sqlmap Enumerate DBMS database tables [sqlmap --tables ]          |
                     {3}----sqlmap Dump DBMS database table entries [sqlmap --dump]           |
                     {4}----sqlmap Enumerate DBMS database table columns [sqlmap --columns]   |
                     {5}----sqlmap Target URL [sqlmap -u URL]                                 |
                     {6}----sqlmap Retrieve DBMS banner [--banner]                            |
                     {99}---retrun main menu                                                  |
                     ==========================================================================
                     """ + color.END)
            response = float(input(color.NOTICE + "sqlmap ~#" + color.END))
            if response == 1:
                system("clear")
                Output = system("sudo sqlmap -u" + sqlmap_Target + " --dbs")
                print(Output)
            elif response == 2:
                sqlmap_tables = input(color.OKBLUE + "if you have name tables please enter (yes) if you have not name tables (no) " + color.END + color.HEADER + "=>" + color.END)
                if sqlmap_Target == "":
                    sqlmap()
                if sqlmap_tables == "yes":
                    database = input(color.OKGREEN + "enter the database => " + color.END)
                    if database == "":
                        sqlmap()
                    tables = input(color.NOTICE + "enter tables => " + color.END)
                    if tables == "":
                        sqlmap()
                    Output_sqlmap_tables = system(
                        "sudo sqlmap -u " + sqlmap_Target + " --dbs " + database + " --tables " + tables)
                elif sqlmap_tables == "no":
                    database = input(color.OKGREEN + "enter the database => " + color.END)
                    if database == "":
                        sqlmap()
                    Output_sqlmap_tables = system(
                        "sudo sqlmap -u " + sqlmap_Target + " --dbs " + database + " --tables ")
                else:
                    system("clear")
                    print(color.RED + sqlmap_tables + " not found " + color.END)
            elif response == 3:
                system("clear")
                sqlmap_dump = input(color.OKBLUE + "if you have name databse,tables,columns please enter (yes) if you have not name databse,tables,columns (no) " + color.END + color.HEADER + "=>" + color.END)
                if sqlmap_dump == "":
                    sqlmap()
                if sqlmap_dump == "yes":
                    database = input(color.OKGREEN + "enter the database => " + color.END)
                    if database == "":
                        sqlmap()
                    tables = input(color.NOTICE + "enter tables => " + color.END)
                    if tables == "":
                        sqlmap()
                    sqlmap_columns = input(color.NOTICE + "enter columns => " + color.END)
                    if sqlmap_columns == "":
                        sqlmap()
                    output_sqlmap_dump = system(
                        "sqlmap -u " + sqlmap_Target + " --dbs " + database + " --tables " + tables + " --columns " + sqlmap_columns + " --dump ")
                    print(color.WARNING + "==========================================" + color.END)
                    print(
                        color.RED + "the hacking website was completed       " + color.END + color.WARNING + "|" + color.END)
                    print(color.WARNING + "==========================================" + color.END)
                elif sqlmap_dump == "no":
                    Output = system("sudo sqlmap -u" + sqlmap_Target + " --dbs")
                    database = input(color.OKGREEN + "enter the database => " + color.END)
                    if database == "":
                        sqlmap()
                    Output_sqlmap_tables = system(
                        "sudo sqlmap -u " + sqlmap_Target + " --dbs " + database + " --tables ")
                    tables = input(color.NOTICE + "enter tables => " + color.END)
                    if tables == "":
                        sqlmap()
                    Output_sqlmap_columns = system(
                        "sqlmap -u " + sqlmap_Target + " --dbs " + database + " --tables " + tables + " --column ")
                    sqlmap_columns = input(color.NOTICE + "enter columns => " + color.END)
                    if sqlmap_columns == "" :
                        sqlmap()
                    output_sqlmap_dump = system(
                        "sqlmap -u " + sqlmap_Target + " --dbs " + database + " --tables " + tables + " --columns " + sqlmap_columns + " --dump ")
                    print(color.WARNING + "==========================================" + color.END)
                    print(
                        color.RED + "the hacking website was completed       " + color.END + color.WARNING + "|" + color.END)
                    print(color.WARNING + "==========================================" + color.END)
                    i = input()
                elif response == 99:
                    system("clear")
                    main()

                else:
                    print(sqlmap_dump + " not found ")

            elif response == 4:

                system("clear")
                sqlmap_columns = input(
                    color.OKBLUE + "if you have name column please enter (yes) if you have not name columns (no) " + color.END + color.HEADER + "=>" + color.END)
                if sqlmap_columns == "yes":
                    database = input(color.OKGREEN + "enter the database => " + color.END)
                    tables = input(color.NOTICE + "enter tables => " + color.END)
                    Output_sqlmap_columns = system(
                        "sqlmap -u " + sqlmap_Target + " --dbs " + database + " --tables " + tables + " --column ")
                elif sqlmap_columns == "no":
                    Output = system("sudo sqlmap -u" + sqlmap_Target + " --dbs")
                    database = input(color.OKGREEN + "enter the database => " + color.END)
                    Output_sqlmap_tables = system(
                        "sudo sqlmap -u " + sqlmap_Target + " --dbs " + database + " --tables ")
            elif response == 5:
                system("clear")
                Output = system("sudo sqlmap " + sqlmap_Target)
            elif response == 6:
                system("clear")
                Output = system("sudo sqlmap " + sqlmap_Target + " --banner ")
            else:
                system("clear")
                print(
                    color.WARNING + "[" + color.END + color.RED + "!" + color.END + color.WARNING + "]" + color.END + '[' + color.OKGREEN + str(
                        response) + color.END + " not found please try again ")

        except ValueError as error :
            system('clear')
            print(error)
            continue
        except KeyboardInterrupt as error3 :
            system('clear')
            print(error3)
            continue

def nikto_tool() :
    Target_nikto = input(f"{color.RED}please enter Target website >> {color.END}")
    if Target_nikto == "" :
        nikto_tool()
    output = system("sudo nikto -h "+Target_nikto)
def setoolkit (): 
    system("clear && sudo set") 
def metasploit_framework():
    system("clear && sudo apt  install metasploit-framework && clear && sudo msfconsole")
def main():

        while True:
            try :
                print(color.RED+menu+color.END)
                print("\t\t" + color.RED + "=================================" + color.END)
                print("\t\t" + color.RED + "|" + color.OKGREEN + "[" + color.END + color.WARNING + "1" + color.END + color.OKGREEN + "]" + color.END + color.IMPORTANT + "-------" + color.END + color.RED + "nmap                 |" + color.END)
                print("\t\t" + color.RED + "|" + color.OKGREEN + "[" + color.END + color.WARNING + "2" + color.END + color.OKGREEN + "]" + color.END + color.IMPORTANT + "-------" + color.END + color.RED + "sqlmap               |" + color.END)
                print("\t\t" + color.RED + "|" + color.OKGREEN + "[" + color.END + color.WARNING + "3" + color.END + color.OKGREEN + "]" + color.END + color.IMPORTANT + "-------" + color.END + color.RED + "nikto                |" + color.END)
                print("\t\t" + color.RED + "|" + color.OKGREEN + "[" + color.END + color.WARNING + "4" + color.END + color.OKGREEN + "]" + color.END + color.IMPORTANT + "-------" + color.END + color.RED + "setoolkit            |" + color.END)
                print("\t\t" + color.RED + "|" + color.OKGREEN + "[" + color.END + color.WARNING + "5" + color.END + color.OKGREEN + "]" + color.END + color.IMPORTANT + "-------" + color.END + color.RED + "metasploit-framework |" + color.END)
                print("\t\t" + color.RED + "|" + color.OKGREEN + "[" + color.END + color.WARNING + "6" + color.END + color.OKGREEN + "]" + color.END + color.IMPORTANT + "-------" + color.END + color.RED + "sherlock             |" + color.END)
                print("\t\t" + color.RED + "|" + color.OKGREEN + "[" + color.END + color.WARNING + "7" + color.END + color.OKGREEN + "]" + color.END + color.IMPORTANT + "-------" + color.END + color.RED + "Osintgram            |" + color.END)
                print("\t\t" + color.RED + "|" + color.OKGREEN + "[" + color.END + color.WARNING + "99" + color.END + color.OKGREEN + "]" + color.END + color.IMPORTANT + "-------" + color.END + color.RED + "retrun in main menu |" + color.END)
                print("\t\t" + color.RED + "=================================" + color.END)
                print("\n\n")
                response = float(input("skynet"+"("+color.RED+"information gathering"+color.END+")"+"  >> "))
                if response == 1:
                    Nmap()
                elif response == 2 :
                    sqlmap()
                elif response == 3: 
                    nikto_tool() 
                elif response == 4 : 
                    setoolkit() 
                elif response == 5:
                    metasploit_framework()
                elif response == 6 : 
                    sherlock() 
                elif response == 7  : 
                    system("python3 tool.py")
                    break
                elif response == 99 :
                    chdir("..")
                    chdir("..")
                    system("sudo python3 skynetv2.py")
                    break
                else  : 
                    system("clear")
                    print(f"{color.WARNING}[{color.END}" + f"{color.OKBLUE}#{color.END}" + f"{color.WARNING}]{color.END}" + str(response) + f"{color.RED} incorrect choice please try again {color.END}")
                    
                

            except  :
                system("clear")
                
                continue
if __name__ == "__main__" : 
    main()

