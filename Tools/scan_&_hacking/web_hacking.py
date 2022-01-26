from os import * 
from time import *
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
menu_sqlmap = f"""
\t\t\t\t        ___
\t\t\t\t      __H__
\t\t\t\t  ___ ___[{color.RED}"{color.END}]_____ ___ ___ 
\t\t\t\t |_ -| . [{color.RED}.{color.END}]     | .'| . |
\t\t\t\t |___|_  [{color.RED}.{color.END}]_|_|_|__,|  _|
\t\t\t\t       |_|V...       |_|
      """
r = 1 



def setoolkit():
    system("clear")
    system("sudo python3 setoolkit.py")
sqlmap_Target = " "

menu_ping = """
          .::::::::::-.                     .::::::-
                                .hmMMMMMMMMMMNddds\...//M\\.../hddddmMMMMMMNo
                                 :Nm-/NMMMMMMMMMMMMM$$NMMMMm&&MMMMMMMMMMMMMMy
                                 .sm/`-yMMMMMMMMMMMM$$MMMMMN&&MMMMMMMMMMMMMh`
                                  -Nd`  :MMMMMMMMMMM$$MMMMMN&&MMMMMMMMMMMMh`
                                   -Nh` .yMMMMMMMMMM$$MMMMMN&&MMMMMMMMMMMm/
    `oo/``-hd:  ``                 .sNd  :MMMMMMMMMM$$MMMMMN&&MMMMMMMMMMm/
      .yNmMMh//+syysso-``````       -mh` :MMMMMMMMMM$$MMMMMN&&MMMMMMMMMMd
    .shMMMMN//dmNMMMMMMMMMMMMs`     `:```-o++++oooo+:/ooooo+:+o+++oooo++/
    `///omh//dMMMMMMMMMMMMMMMN/:::::/+ooso--/ydh//+s+/ossssso:--syN///os:
          /MMMMMMMMMMMMMMMMMMd.     `/++-.-yy/...osydh/-+oo:-`o//...oyodh+
          -hMMmssddd+:dMMmNMMh.     `.-=mmk.//^^^\\.^^`:++:^^o://^^^\\`::
          .sMMmo.    -dMd--:mN/`           ||--X--||          ||--X--||
........../yddy/:...+hmo-...hdd:............\\=v=//............\\=v=//.........


"""
IP = """
        \t\t\td888888b    88""Yb  
        \t\t\t   88       88__dP  
        \t\t\t   88       88'''       
        \t\t\t  .88.      88        
        \t\t\td888888b    88                     
        """
def ping_host():
    system("clear")
    Target_host = input(color.WARNING+"enter Target IP or host name (ex:www.google.com) "+" > "+color.END)
    if Target_host == "" :
        system("clear")
        ping_host()
    system("clear")

    def find_ipaddress_for_anywebsite():
        return system("sudo ping "+Target_host)
    def use_audible_ping():
        return system("sudo ping -a "+Target_host)
    def flood_ping():
        return system("sudo ping -f "+Target_host)
    def no_dns_name_resolution():
        return system("sudo ping -n "+Target_host)
    def sticky_source_address():
        return system("sudo ping -B "+Target_host)
    def return_main_mneu():
        return Web_scan()
    # use ping IPV2 
    
                
         
    print(menu_ping)
    print(color.LOGGING+"\t\t\tTarget is => "+color.END+Target_host)
    print(color.HEADER+"""
                        {find any ip address for any website}
                        
                        [1]---------find ip address for any website 
                        [2]---------ping use audible ping <ping -a>
                        [3]---------ping flood ping <ping -f> 
                        [4]---------ping no dns name resolution <ping -n>
                        [5]---------ping sticky source address <ping -B>
                        [6]---------ping use IPV2 
                        [99]--------return main mneu {Web scan}
        
        """+color.END)
        
    response = float(input("skynet"+"("+color.RED+"ping"+color.END+") => "))
    if response == 1 : 
            find_ipaddress_for_anywebsite()
    elif response == 2: 
            use_audible_ping()
    elif response == 3: 
            flood_ping()
    elif response == 4: 
            no_dns_name_resolution()
    elif response == 5:
            sticky_source_address()
    elif response == 6: 
            print(IP)
            print(color.RED+"\t\t\tThe target is = "+color.END+Target_host)
            print(color.LOGGING+"""
                        |==========================================================|
                        | <1>-----ping use internet protocal version 4 [ping -4]   |
                        | <2>-----ping allow pinging broadcast [ping -b]           |
                        | <3>-----ping record route [ping -R]                      |
                        | <4>-----return main menu (ping host)                     |
                        | <5>-----return main menu (webscan)                       |
                        |==========================================================| 
            
            """+color.END)
            response  = float(input("skynet"+"("+color.RED+"ping (internet protocal version 4) "+color.END+") => "))
            if response == 1 : 
                system("clear")
                system("clear")
                Output = system("sudo ping -4 "+Target_host)
            elif response == 2 : 
                system("clear")
                Output = system("sudo ping -b " + Target_host)
            elif response == 3: 
                system("clear")
                Output = system("sudo ping -R "+ Target_host )
            elif response == 4: 
                ping_host()
            elif response == 5: 
                Web_scan()
            else:
                system("clear")
                print(color.OKGREEN+"["+color.END+color.WARNING+"+"+color.END+color.OKGREEN+"]"+color.END+color.RED+" [not found]  "+color.END)
            
    elif response == 99 : 
            Web_scan()
    else : 
            system("clear")
            print(color.OKGREEN+"["+"+"+color.OKGREEN+"]"+color.RED+"  { not found please try again }")
 

      
# metasploit 
def metasploit():
    system("msfconsole")
#sqlmap 
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
                print(color.OKGREEN + "[" + color.END + color.WARNING + str(response) + color.END + color.OKGREEN + "]" + color.END + color.RED + " the =>" + str(response) + " [not found]  " + color.END)

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

def nikto_tool():
    system("clear")  
    nikto_target = input(color.WARNING+"enter The Target "+color.END+" > ")
    system("clear")        
    nikto = system("sudo nikto -h "+nikto_target)
def Port_scan():
    system("clear")
    Target = input(color.WARNING+"enter the IP addrss or Website "+color.END+color.RED+"=>"+color.END)
    try:
         portscan = input(color.WARNING+"enter the Port "+color.END+color.RED+"=>"+color.END)
         Port = system("sudo nmap "+Target+" -p "+portscan)
         print(Port)
    except:
        system("clear")
        print("ERROR")

def Web_scan():
    
    while r <= 12:
        try:
           menu_scan = """
\t\t\t.d8888.   .o88b.          88b 88 
\t\t\t88'  YP  d8P  Y8    db    88b 88 
\t\t\t`8bo.    8P        dPYb   88Yb88
\t\t\t`Y8b.    8b       dP__Yb  88 Y88       
\t\t\tdb   8D  Y8b  d8 dP"''"Yb 88  Y8
\t\t\t`8888Y'   `Y88P  dP    Yb'"""
           
           print(color.WARNING+menu_scan+color.END)
           print("\t\t\t"+color.RED+"================================"+color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"1"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"Nmap                |"+color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"2"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"nikto tool          |"+color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"3"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"sqlmap              |" +color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"4"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"setoolkit           |"+color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"5"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"metasploit          |"+color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"6"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"ping                |"+color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"7"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"port scan           |"+color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"8"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"version             |"+color.END)
           print("\t\t\t"+color.OKGREEN+"|["+color.END+color.WARNING+"99"+color.END+color.OKGREEN+"]"+color.END+color.IMPORTANT+"-------"+color.END+color.RED+"retrun in skynet   |"+color.END)
           print("\t\t\t"+color.RED+"================================"+color.END)
           response = float(input(color.WARNING+"\n\nskynet > "+color.END))
           if response == 1:
               Nmap() 
           elif response == 2 : 
               nikto_tool()
           elif response == 3:
              
               sqlmap()
            
           elif response == 4:
               setoolkit() 
           elif response == 5:
               metasploit()
           elif response == 6:
               ping_host()
           elif response == 7:
               Port_scan()
           elif response == 8: 
               system("clear")
               print(color.IMPORTANT+"python version   :   3.9.8 ")
               print(color.OKBLUE+"web sacn version :   2.1.0 ")
               i = input( )
           elif response == 99: 
               chdir("..")
               chdir("..")
               system("sudo python3 skynetv2.py")
               break

           else : 
                 print(color.OKGREEN+"["+color.END+color.WARNING+"+"+color.END+color.OKGREEN+"]"+color.END+color.RED+" the =>"+str(response)+" [not found]  "+color.END)
           
        except:
             system("clear")
             Web_scan()


Web_scan() 

    # python version   :   3.9.8 
    # web sacn version :   2.1.0 

    #end 
