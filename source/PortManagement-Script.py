from os import system
import os
import time
import sys
import platform
import colorama
from colorama import Fore, init, Style
import win32ui
import requests
import subprocess
import ctypes


mytitle = "Eno's Universal Port Management Script v1.0"

## Console Input Echos ##
ENTER_CHOICE_CONSOLE_ECHO = (f"""{Fore.BLUE}
╭─({Fore.RED}root@3n3scan{Fore.BLUE})-[{Style.RESET_ALL}~{Fore.BLUE}]
╰─{Fore.RED}#{Fore.LIGHTGREEN_EX} Enter the number of your choice:{Style.RESET_ALL} """)
ENTER_NAME_PORT_CONSOLE_ECHO = (f"""{Fore.BLUE}
╭─({Fore.RED}root@3n3scan{Fore.BLUE})-[{Style.RESET_ALL}~{Fore.BLUE}]
╰─{Fore.RED}#{Fore.LIGHTGREEN_EX} Enter a name for the Port:{Style.RESET_ALL} """)
ENTER_NUMBER_PORT_CONSOLE_ECHO =(f"""{Fore.BLUE}
╭─({Fore.RED}root@3n3scan{Fore.BLUE})-[{Style.RESET_ALL}~{Fore.BLUE}]
╰─{Fore.RED}#{Fore.LIGHTGREEN_EX} Enter the number of the Port:{Style.RESET_ALL} """)
ENTER_PROTOCOL_PORT_CONSOLE_ECHO = (f"""{Fore.BLUE}
╭─({Fore.RED}root@3n3scan{Fore.BLUE})-[{Style.RESET_ALL}~{Fore.BLUE}]
╰─{Fore.RED}#{Fore.LIGHTGREEN_EX} Enter the protocol (ex. UDP/TCP) of the Port:{Style.RESET_ALL} """)
ENTER_ACTION_ON_PORT_CONSOLE_ECHO = (f"""{Fore.BLUE}
╭─({Fore.RED}root@3n3scan{Fore.BLUE})-[{Style.RESET_ALL}~{Fore.BLUE}]
╰─{Fore.RED}#{Fore.LIGHTGREEN_EX} Do you want to allow or block the port? Enter 'allow' or 'block':{Style.RESET_ALL} """)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def add_port():
    if is_admin():
        try:
            # Einen Bestimmten Port öffnen
            port_name = input(ENTER_NAME_PORT_CONSOLE_ECHO)
            while True:
                port_str = input(ENTER_NUMBER_PORT_CONSOLE_ECHO)
                if port_str.isdigit():
                    port = int(port_str)
                    break
                else:
                    print(f"{Fore.RED}> Invalid port number. Please enter a numeric value! <{Style.RESET_ALL}")
            protocol = input(ENTER_PROTOCOL_PORT_CONSOLE_ECHO).upper()
            action = input(ENTER_ACTION_ON_PORT_CONSOLE_ECHO).lower()
            
            command = f"netsh advfirewall firewall add rule name=\"{port_name}_{port}_{protocol}\" protocol={protocol} localport={port} action={action} dir=in"
            subprocess.call(command, shell=True)

            win32ui.MessageBox(f"Successfully added the following Port {port}\n\nPort Informations:\nPort Name = {port_name}\nPort = {port}\nProtocol = {protocol}\nAction = {action}\n\nThank you for using this script!", f"{mytitle}")
            time.sleep(3)
            main()

        except requests.RequestException as e:
            win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
            time.sleep(2)
            sys.exit()
    else:
        win32ui.MessageBox("Administrator privileges required to add user-specific ports.", f"{mytitle}")
        sys.exit()


def del_port():
    if is_admin():
        try:
            # Einen Bestimmten Port löschen
            port_name = input(ENTER_NAME_PORT_CONSOLE_ECHO)
            while True:
                port_str = input(ENTER_NUMBER_PORT_CONSOLE_ECHO)
                if port_str.isdigit():
                    port = int(port_str)
                    break
                else:
                    print(f"{Fore.RED}> Invalid port number. Please enter a numeric value! <{Style.RESET_ALL}")
            protocol = input(ENTER_PROTOCOL_PORT_CONSOLE_ECHO).upper()
            
            command = f"netsh advfirewall firewall delete rule name=\"{port_name}_{port}_{protocol}\" protocol={protocol} localport={port}"
            subprocess.call(command, shell=True)

            win32ui.MessageBox(f"Successfully deleted the following Port {port}\n\nPort Informations:\nPort Name = {port_name}\nPort = {port}\nProtocol = {protocol}\n\nThank you for using this script!", f"{mytitle}")
            time.sleep(3)
            main()

        except requests.RequestException as e:
            win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
            time.sleep(2)
            sys.exit()
    else:
        win32ui.MessageBox("Administrator privileges required to delete user-specific ports.", f"{mytitle}")
        sys.exit()
        

def get_all_ports():
    if is_admin():
        try:
            # Alle vom Benutzer geöffneten Ports anzeigen
            result = subprocess.check_output("netstat -ano", shell=True, text=True)
            
            # Filtere die Zeilen, die deine Benutzer-ID repräsentieren
            user_pid = str(os.getpid())
            user_ports = [line for line in result.splitlines() if user_pid in line]

            # Ausgabe der gefilterten Ports
            for port_line in user_ports:
                print(port_line)

            win32ui.MessageBox("Successfully retrieved user-specific open ports!\nCheck the console for details.", f"{mytitle}")
            input(f"{Fore.RED}> Press enter to continue... <{Style.RESET_ALL}")
            main()

        except subprocess.CalledProcessError as e:
            win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
            time.sleep(2)
            sys.exit()
    else:
        win32ui.MessageBox("Administrator privileges required to retrieve user-specific open ports.", f"{mytitle}")
        sys.exit()
        

def exit_script():
    system("cls")
    win32ui.MessageBox(f"Exiting... Thank you for using this script!", f"{mytitle}")
    sys.exit()


def main():
    system("title "+mytitle)
    os = platform.system()
    if os == "Windows":
        system("cls")
    else:
        system("clear")
        print(chr(27) + "[2J")
    print(f"""{Fore.CYAN}
──────────────────────────────────────────────────────────────────────────────────────────────

▓█████  ███▄    █  ▒█████    ██████      ██████  ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓
▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▒██    ▒    ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒
▒███   ▓██  ▀█ ██▒▒██░  ██▒░ ▓██▄      ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░
▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░  ▒   ██▒     ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░ 
░▒████▒▒██░   ▓██░░ ████▓▒░▒██████▒▒   ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ 
░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   
 ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░   ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░    
   ░      ░   ░ ░ ░ ░ ░ ▒  ░  ░  ░     ░  ░  ░  ░          ░░   ░  ▒ ░░░         ░      
   ░  ░         ░     ░ ░        ░           ░  ░ ░         ░      ░                    
                                                ░                                       
──────────────────────────────────────────────────────────────────────────────────────────────
{Style.RESET_ALL}
                                {Fore.MAGENTA} > Developed by: 3n3scan{Style.RESET_ALL}
                                
{Fore.CYAN}> Choose an option:{Style.RESET_ALL}
{Fore.GREEN}> [1] Add a open Port{Style.RESET_ALL}
{Fore.RED}> [2] Delete a open Port{Style.RESET_ALL}
{Fore.CYAN}> [3] Get all open Ports{Style.RESET_ALL}
{Fore.YELLOW}> [4] Exit{Style.RESET_ALL}
""")

    choice = input(ENTER_CHOICE_CONSOLE_ECHO)

    if choice == "1":
        add_port()
    elif choice == "2":
        del_port()
    elif choice == "3":
        get_all_ports()
    elif choice == "4":
        exit_script()
    else:
        print(f"{Fore.RED}> Invalid choice. Please enter '{Fore.CYAN}1{Fore.RED}', '{Fore.CYAN}2{Fore.RED}', '{Fore.CYAN}3{Fore.RED}' '{Fore.CYAN}3{Fore.RED}' <{Style.RESET_ALL}")
        time.sleep(2)
        main()
        

if __name__ == "__main__":
    main()