from InquirerPy import inquirer


def Nmap_menu():
    scan_choice = inquirer.select(
        message="Choose an Nmap Scan:",
        choices=[
            "1. SYN Scan",
            "2. TCP Connect Scan",
            "3. UDP Scan",
            "4. Ping Sweep",
            "5. OS Detection",
            "6. Service Version Detection",
            "7. Stealth Scan",
            "8. NSE Script Scan",
            "9. Aggressive Scan",
            "10.Firewall Evasion Scan",
            "11.Slow Comprehensive Scan",
            "12.All Ports Scan",
            "Back to Main Menu"
        ]
    ).execute()
    if "Back to Main Menu" in scan_choice : 
        return




        
   

