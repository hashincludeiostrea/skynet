from math import *
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
def Arithmetic_operations() :
    while True :
        try :
            numbers = float(eval(input(">>")))

            print(numbers)
        except ValueError as error :
            system("clear")
            print("ERROR")
            continue
        except SyntaxError   as error :
            continue
def cosin_number () :
    try :
       while True :
           print(color.RED + """

                               [1]---------Radian
                               [2]---------digress
                               [3]---------clear screen 
                               [4]---------retrun in main menu 
                  """+color.END)
           response = float(input(f"calculator {color.RED}({color.END}cosin{color.RED}){color.END} >> "))
           if response == 1 :
               try :
                   x = float(input("cos(x) :: please enter number >> "))
                   if x == "" :
                       cosin_number()
                   system("clear")
                   print(f"cos{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = ",end="")
                   print(cos(x))
               except KeyboardInterrupt as error :
                   system("clear"), print(error)
                   continue
               except ValueError as error:
                   system("clear"), print(error)
                   continue
           elif response == 2 :
               try :
                   x = float(input("cos(x) :: please enter number >> "))
                   if x == "" :
                       cosin_number()
                   system("clear")
                   angle = cos(x * pi / 1 )
                   print(f"cos{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = ",end="")
                   print(angle)
               except KeyboardInterrupt as error :
                   system("clear"), print(error)
                   continue
               except ValueError as error:
                   system("clear"), print(error)
                   continue
           elif response == 3 :
               system("clear")
           elif response == 4 :
               main()
           else :
               system("clear")
               print(f"{color.WARNING}[{color.END}" + f"{color.OKBLUE}#{color.END}" + f"{color.WARNING}]{color.END}" + str(response) + f"{color.RED} incorrect choice please try again{color.END}")
    except KeyboardInterrupt as error:
        system("clear"), print(error)
        cosin_number()
    except ValueError as error:
        system("clear"), print(error)
        cosin_number()
def square_root () :
    try :
        x = float(input(f"{color.IMPORTANT}sqrt(x) :: please enter number  >> "))
        system("clear")
        print(f"sqrt{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} =  {sqrt(x)}")

    except KeyboardInterrupt as error:
        system("clear"), print(error)
        square_root()
    except ValueError as error:
        system("clear"), print(error)
        square_root()

def sine_number():
        try:
            while True:
                print(color.RED + """

                                   [1]---------Radian
                                   [2]---------digress
                                   [3]---------clear screen 
                                   [4]---------retrun in main menu 
                      """ + color.END)
                response = float(input(f"calculator {color.RED}({color.END}sine{color.RED}){color.END} >> "))
                if response == 1:
                    try:
                        x = float(input("sin(x) :: please enter number >> "))
                        if x == "":
                            sine_number()
                        system("clear")
                        print(f"sin{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = ", end="")
                        print(sin(x))
                    except KeyboardInterrupt as error:
                        system("clear"), print(error)
                        continue
                    except ValueError as error:
                        system("clear"), print(error)
                        continue
                elif response == 2:
                    try:
                        x = float(input("sin(x) :: please enter number >> "))
                        if x == "":
                            sine_number()
                        system("clear")
                        angle = sin(x * pi / 180)
                        print(f"sin{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = ", end="")
                        print(angle)
                    except KeyboardInterrupt as error:
                        system("clear"), print(error)
                        continue
                    except ValueError as error:
                        system("clear"), print(error)
                        continue
                elif response == 3:
                    system("clear")
                elif response == 4:
                    main()
                else:
                    system("clear")
                    print(
                        f"{color.WARNING}[{color.END}" + f"{color.OKBLUE}#{color.END}" + f"{color.WARNING}]{color.END}" + str(
                            response) + f"{color.RED} incorrect choice please try again{color.END}")
        except  ValueError as error  :
            system("clear"),print(error)
            sine_number()
        except KeyboardInterrupt as error2 :
            system("clear"), print(error2)
            sine_number()
        except SyntaxError as error3 :
            system("clear"), print(error3)
            sine_number()


def  tangent() :
    try :
        x = float(input("tan(X) :: please enter number >> "))
        system("clear")
        print(f"tan{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = " , end="")
        print(tan(x))
    except ValueError as error :
        system("clear"),print(error)
        tangent()
    except KeyboardInterrupt as error2 :
        system("clear"), print(error2)
        tangent()
def cosh_number() :
    try :
        x = float(input(f"{color.OKBLUE}\ncosh(x) :: please enter number >> {color.END}"))
        system("clear")
        print(f"cosh{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = {cosh(x)}")

    except ValueError as error :
        system("clear"), print(error)
        cosh_number()
    except KeyboardInterrupt as error :
        system("clear"), print(error)
        cosh_number()
    except SyntaxError as error :
        system("clear"), print(error)
        cosh_number()


def sinh_number():
    try:
        x = float(input(f"{color.RED}\nsinh(x) :: please enter number >>  {color.END}"))
        system("clear")
        print(f"sinh{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = {sinh(x)}")

    except ValueError as error:
        system("clear"), print(error)
        sinh_number()
    except KeyboardInterrupt as error:
        system("clear"), print(error)
        sinh_number()
    except SyntaxError as error:
        system("clear"), print(error)
        sinh_number()
def tanh_number():
    try:
        x = float(input(f"{color.OKGREEN}\ntanh(x) :: please enter number >> {color.END} "))
        system("clear")
        print(f"tanh{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = {tanh(x)}")

    except ValueError as error:
        system("clear"), print(error)
        tanh_number()
    except KeyboardInterrupt as error:
        system("clear"), print(error)
        tanh_number()
    except SyntaxError as error:
        system("clear"), print(error)
        tanh_number()
def absolute() :
    try  :
        x =  float(input(f"{color.LOGGING}\nabs(x) :: please enter number >> {color.END}"))
        system("clear")
        print(f"abs{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = {abs(x)}")

    except KeyboardInterrupt as error :
        system("clear"), print(error)
        absolute()
    except ValueError as error :
        system("clear"), print(error)
        absolute()
    except SyntaxError as error :
        system("clear"), print(error)
        absolute()
def rounding_number() :
    try:
        x = float(input(f"{color.LOGGING}\nround(x) :: please enter number >> {color.END}"))
        system("clear")
        print(f"round{color.OKBLUE}({color.END}{x}{color.OKBLUE}){color.END} = {round(x)}")

    except KeyboardInterrupt as error:
        system("clear"), print(error)
        rounding_number()
    except ValueError as error:
        system("clear"), print(error)
        rounding_number()
    except SyntaxError as error:
        system("clear"), print(error)
        rounding_number()

def main():
    while True :
        try :
            print(color.WARNING + """
                            =============================================================
                            |[1]---------Arithmetic operations                          |
                            |[2]---------cosin                                          |
                            |[3]---------sine                                           |
                            |[4]---------tangent                                        |
                            |[5]---------cosh                                           |
                            |[6]---------sinh                                           |
                            |[7]---------tanh                                           | 
                            |[8]---------square root                                    |
                            |[9]---------Cube root                                      |
                            |[10]--------absolute                                       |
                            |[11]--------rounding numbers                               |  
                            |[99]--------retrun in main menu                            | 
                            =============================================================
            """+color.END)
            response_calcualator = float(input(f"skynet ({color.RED} calculator {color.END}) >>  "))
            if response_calcualator == 1 :
                Arithmetic_operations()
            elif response_calcualator == 2 :
                cosin_number()
            elif response_calcualator == 3:
                sine_number()
            elif response_calcualator == 4 :
                tangent()
            elif response_calcualator == 5 :
                cosh_number()
            elif response_calcualator == 6:
                sinh_number()
            elif response_calcualator == 7 :
                tanh_number()
            elif response_calcualator == 8 :
                square_root()
            elif response_calcualator == 9 :
               # chdir("Toolsca")

                system("g++ Cube_root.cpp")
                system("./a.out")
            elif response_calcualator == 10 :
                absolute()
            elif response_calcualator == 11 :
                rounding_number()
            elif response_calcualator == 99 :
                system("clear")
                chdir("..")
                chdir("..")
                system("python3 skynetv2.py")
                break

            else  :
                print(f"{color.WARNING}[{color.END}" + f"{color.OKBLUE}#{color.END}" + f"{color.WARNING}]{color.END}" + str(response_calcualator) + f"{color.RED} incorrect choice please try again{color.END}")

        except ValueError as error :
            system("clear"),print(error)
            continue
        except KeyboardInterrupt as error2 :
            system("clear"),print(error2)
            continue
if __name__ == "__main__" :
    main()
