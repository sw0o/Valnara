import pyfiglet
import os
from InquirerPy import inquirer
from InquirerPy.separator import Separator
from Nmap_menu import Nmap_menu

def print_banner():
    print("="*60)
    print(pyfiglet.figlet_format("V A L N A R A", font="slant"))
    print("="*60)

def Main_menu():
    print_banner()  
    Tool = inquirer.select(
        message="Choose Your Tool:",
        choices=[
            "Nmap - Network Mapper for scanning and discovery.",
            "Zap - for finding web vulnerabilities.",
            "WordPress - Scan WordPress sites for known vulnerabilities.",
            "Quit"
        ]
    ).execute()
    return Tool  

User_Choice = Main_menu()  



if "Nmap" in User_Choice:
    Nmap_menu()  
elif "Zap" in User_Choice:
    print("zap")
elif "WordPress" in User_Choice:
    print("Wordpress")
elif "Quit" in User_Choice:
    os.system("clear")







   

