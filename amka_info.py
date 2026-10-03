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
RESET = '\033[0m'

# Platform Deep Links (Kept strictly in background logic)
WHATSAPP_URL = "https://wa.me/254723353579"
TELEGRAM_URL = "https://t.me/Amkakernel001"
TELEGRAM_GROUP = "https://t.me/GlobalHackersChatCommunity"
FACEBOOK_URL = "https://www.facebook.com/profile.php?id=61576735212627"
TIKTOK_URL = "https://www.tiktok.com/@amkakernel?_r=1&_t=ZN-9AFZiuF472k"
GITHUB_URL = "https://github.com/Amka-Kernel"

def clear():
    os.system('clear')

def open_url(url):
    os.system(f"termux-open-url '{url}'")

def banner():
    print(f"""{R}
               .---.
              /     \\
             | () () |
              \\  ^  /
               |||||
              '-----'
    {RESET}""")
    print(f"{C}=================================================={RESET}")
    print(f"{Y}                   AMKA INFO                      {RESET}")
    print(f"{C}=================================================={RESET}\n")

def menu():
    print(f"{C}                  DISCOVER AMKA{RESET}\n")
    print(f"{M}[1]{RESET} More About Amka\n")
    print(f"{C}       CONNECT AMKA WITH DIFFERENT PLATFORMS{RESET}\n")
    print(f"{M}[2]{RESET} WhatsApp")
    print(f"{M}[3]{RESET} Telegram Channel")
    print(f"{M}[4]{RESET} Telegram Group")
    print(f"{M}[5]{RESET} Facebook")
    print(f"{M}[6]{RESET} TikTok")
    print(f"{M}[7]{RESET} GitHub")
    print(f"{M}[8]{RESET} Exit\n")

def about():
    clear()
    
    # Image 1: Anonymous Mask (Red)
    print(f"""{R}
            .---.
           /     \\
          | () () |
           \\  ^  /
            |||||
            '---'
    {RESET}""")
    
    print(f"{C}=================================================={RESET}")
    print(f"{Y}                   ABOUT AMKA                     {RESET}")
    print(f"{C}=================================================={RESET}\n")
    
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

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(f"{Y}Select an option [1-8]: {RESET}").strip()
        
        if choice == '1':
            about()
        elif choice == '2':
            open_url(WHATSAPP_URL)
        elif choice == '3':
            open_url(TELEGRAM_URL)
        elif choice == '4':
            open_url(TELEGRAM_GROUP)
        elif choice == '5':
            open_url(FACEBOOK_URL)
        elif choice == '6':
            open_url(TIKTOK_URL)
        elif choice == '7':
            open_url(GITHUB_URL)
        elif choice == '8':
            print(f"\n{R}Exiting Amka Info. Stay secure!{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{R}Invalid selection. Try again.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()

