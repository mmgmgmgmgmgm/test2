

import multiprocessing
import keyboard
import base64

from util.plugins.common import *

threads = 3
cancel_key = "ctrl+x"

def main():
    setTitle(f"Hazard Nuker {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
    if getTheme() == "hazardous":
        banner()
    elif getTheme() == "dark":
        banner("dark")
    elif getTheme() == "fire":
        banner("fire")
    elif getTheme() == "water":
        banner("water")
    elif getTheme() == "neon":
        banner("neon")

    choice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Choice: {Fore.RED}')
    #all options
    if choice == "1":
      print(f"{Fore.CYAN}Here is The Download: https://www.google.com/chrome/downloads/")


    elif choice == '2':
      print(f"{Fore.CYAN}Here is The Download: https://www.microsoft.com/en-us/edge")
      
    elif choice == '3':
      print(f"{Fore.CYAN}Here is The Download: https://www.roblox.com")
                

    elif choice == '4':
        print(f"{Fore.CYAN}Here is The Download: https://www.discord.com")


    elif choice == '5':
       print(f"{Fore.CYAN}Coming Soon!")


    elif choice == '6':
        
       print(f"{Fore.CYAN}Coming Soon!")


    elif choice == '7':
       print(f"{Fore.CYAN}Coming Soon!")

    elif choice == '8':
       print(f"{Fore.CYAN}Coming Soon!")


    elif choice == '9':
       print(f"{Fore.CYAN}Coming Soon!")
    
    elif choice == '10': 
       print(f"{Fore.CYAN}Coming Soon!")

    elif choice == '11':
       print(f"{Fore.CYAN}Coming Soon!")

    elif choice == '12':
       print(f"{Fore.CYAN}Coming Soon!")


    elif choice == '13':
       print(f"{Fore.CYAN}Coming Soon!") 


    elif choice == '14': 
       print(f"{Fore.CYAN}Coming Soon!")


    elif choice == '15':
       print(f"{Fore.CYAN}Coming Soon!")


    elif choice == "16":
       print(f"{Fore.CYAN}Coming Soon!")


    elif choice == '17':
       print(f"{Fore.CYAN}Coming Soon!")


    elif choice == '18':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Theme changer
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Soon!
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] soon!
    {Fore.RESET}[{Fore.RED}4{Fore.RESET}] {Fore.RED}Exit...    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Setting')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
{Fore.GREEN}Hazardous: 1
{Fore.LIGHTBLACK_EX}Dark: 2
{Fore.RED}Fire: 3
{Fore.BLUE}Water: 4
{Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
""")
            themechoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}theme: {Fore.RED}')
            if themechoice == "1":
                setTheme('hazardous')
            elif themechoice == "2":
                setTheme('dark')
            elif themechoice == "3":
                setTheme('fire')
            elif themechoice == "4":
                setTheme('water')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Theme')
                sleep(1.5)
                main()
            SlowPrint(f"{Fore.GREEN}Theme set to {Fore.CYAN}{getTheme()}")
            sleep(0.5)
            main()

        elif secondchoice == "2":
            print(f"{Fore.BLUE}Current amount of threads: {threads}")
            try:
                amount = int(
                    input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Amount of threads: {Fore.RED}'))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid amount')
                sleep(1.5)
                main()
            if amount >= 45:
                print(f"{Fore.RED}Sorry but having this many threads will just get you ratelimited and not end up well")
                sleep(3)
                main()
            elif amount >= 15:
                print(f"{Fore.RED}WARNING! * WARNING! * WARNING! * WARNING! * WARNING! * WARNING! * WARNING!")
                print(f"having the thread amount set to 15 or over can possible get laggy and higher chance of ratelimit\nare you sure you want to set the ratelimit to {Fore.YELLOW}{amount}{Fore.RED}?")
                yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}yes/no: {Fore.RED}')
                if yesno.lower() != "yes":
                    sleep(0.5)
                    main()
            threads = amount
            SlowPrint(f"{Fore.GREEN}Threads set to {Fore.CYAN}{amount}")
            sleep(0.5)
            main()
        
        elif secondchoice == "3":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Current cancel key: {cancel_key}")
            print(f"""{Fore.BLUE}If you want to have ctrl + <key> you need to type out ctrl+<key> | DON'T literally press ctrl + <key>
{Fore.GREEN}Example: shift+Q
{Fore.RED}You can have other modifiers instead of ctrl ⇣
{Fore.YELLOW}All keyboard modifiers:{Fore.RESET}
ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
""")
            sleep(1.5)
            key = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Key: {Fore.RED}')
            cancel_key = key
            SlowPrint(f"{Fore.GREEN}Cancel key set to {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "4":
            setTitle("Exiting. . .")
            choice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Are you sure you want to exit? (Y to confirm): {Fore.RED}')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                clear()
                os._exit(0)
            else:
                main()
    else:
        clear()
        main()



