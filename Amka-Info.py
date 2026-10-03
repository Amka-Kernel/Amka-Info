#!/usr/bin/env python3
import os
import sys
import time

# ANSI Color Codes
G = '\033[1;32m'  # Bright Green (Text/Content)
C = '\033[1;36m'  # Bright Cyan (Headers/Dividers)
Y = '\033[1;33m'  # Bright Yellow (Menu/Titles)
M = '\033[1;35m'  # Bright Magenta (Option Numbers)
R = '\033[1;31m'  # Bright Red (ASCII Graphics/Icons)
W = '\033[1;37m'  # White
RESET = '\033[0m'

def clear():
    os.system('clear')

def banner():
    print(f"""{R}
               .---.
              /     \\
             | () () |
              \\  ^  /
               |||||
              '-----'
    {RESET}""")
    print(f"{C}=================================================="{RESET})
    print(f"{Y}                   AMKA INFO                      "{RESET})
    print(f"{C}=================================================="{RESET}\n")

def menu():
    print(f"{M}[1]{RESET} About Amka")
    print(f"{M}[2]{RESET} Social Links & Connectivity")
    print(f"{M}[3]{RESET} Active Projects")
    print(f"{M}[4]{RESET} Exit\n")

def about():
    clear()
    
    # Image 1: Main Anonymous Mask (Red)
    print(f"""{R}
            .---.
           /     \\
          | () () |
           \\  ^  /
            |||||
            '---'
    {RESET}""")
    
    print(f"{C}=================================================="{RESET})
    print(f"{Y}                   ABOUT AMKA                     "{RESET})
    print(f"{C}=================================================="{RESET}\n")
    
    print(f"{G}Welcome to my digital space!\n")
    print(f"My name is Amka. I am a hacker and black hat OSINT operator")
    print(f"focused on engineering tools directly from Android and Termux")
    print(f"environments.\n")
    print(f"I operate at the intersection of offensive security, terminal tools,")
    print(f"cybersecurity research, and open-source intelligence gathering.")
    print(f"My objective is to build stealthy, efficient, and powerful digital")
    print(f"utilities that put full control back into the terminal.{RESET}\n")
    
    # Image 2: Core Focus Boxes (Red)
    print(f"""{R}
        ┌──┐ ┌──┐ ┌──┐
        │  │ │  │ │  │
        └──┘ └──┘ └──┘
    {RESET}""")
    
    print(f"{C}[+] CORE FOCUS & SPECIALIZATION{RESET}")
    print(f"{G}• Cyber Operations & Hacker Methodologies{RESET}")
    print(f"{G}• OSINT Reconnaissance & Data Intelligence{RESET}")
    print(f"{G}• Termux Environment & Android Terminal Tools{RESET}")
    print(f"{G}• System Security & Privacy Engineering{RESET}")
    print(f"{G}• Automated Scripts & Network Analysis{RESET}\n")
    
    # Image 3: Featured Projects Stack (Red)
    print(f"""{R}
          .---.----.
          |   |    |
          '---'----'
    {RESET}""")
    
    print(f"{C}[+] FEATURED PROJECTS{RESET}")
    print(f"{G}• AmkaOSINT       - Open-source intelligence terminal utility{RESET}")
    print(f"{G}• Amka Browser    - Lightweight custom mobile web interface{RESET}")
    print(f"{G}• Amka OmniAI     - Multi-modal AI architecture framework{RESET}")
    print(f"{G}• Telegram Bots   - Automated community & network bots{RESET}\n")
    
    # Image 4: Vision Crosshair (Red)
    print(f"""{R}
            .---.
           /  |  \\
          | --+-- |
           \\  |  /
            '---'
    {RESET}""")
    
    print(f"{C}[+] VISION & BLACK HAT PHILOSOPHY{RESET}")
    print(f"{G}Mastering system mechanics, maintaining terminal control, and")
    print(f"developing independent security tools that bypass digital constraints.{RESET}\n")
    
    print(f"{C}--------------------------------------------------{RESET}")
    input(f"{Y}Press Enter to return to the main menu...{RESET}")

def social_links():
    clear()
    banner()
    print(f"{Y}--- SOCIAL & CONNECTIVITY ---{RESET}\n")
    print(f"{C}WhatsApp  :{RESET} {G}+254723353579{RESET}")
    print(f"{C}Telegram  :{RESET} {G}@Amkakernel001{RESET}")
    print(f"{C}GitHub    :{RESET} {G}https://github.com/Amka-Kernel/Amka-Info{RESET}")
    print(f"{C}TikTok    :{RESET} {G}Amka Official{RESET}")
    print(f"{C}Facebook  :{RESET} {G}Amka Official{RESET}\n")
    input(f"{Y}Press Enter to return to menu...{RESET}")

def projects():
    clear()
    banner()
    print(f"{Y}--- ACTIVE PROJECTS ---{RESET}\n")
    print(f"{G}1. AmkaOSINT{RESET}   - Terminal-based OSINT tool for domain & phone intelligence.")
    print(f"{G}2. Amka-Info{RESET}   - Termux CLI personal branding & connectivity hub.")
    print(f"{G}3. Web Signal{RESET}  - Custom WebSocket server & capture interface.\n")
    input(f"{Y}Press Enter to return to menu...{RESET}")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(f"{Y}Select an option [1-4]: {RESET}").strip()
        
        if choice == '1':
            about()
        elif choice == '2':
            social_links()
        elif choice == '3':
            projects()
        elif choice == '4':
            print(f"\n{R}Exiting Amka Info. Stay secure!{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{R}Invalid selection. Try again.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()

