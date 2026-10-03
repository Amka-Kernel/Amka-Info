import os
import sys
import time
import subprocess

# ANSI Color Codes
G = '\033[1;32m'  # Bright Green
C = '\033[1;36m'  # Bright Cyan
Y = '\033[1;33m'  # Bright Yellow
M = '\033[1;35m'  # Bright Magenta
R = '\033[1;31m'  # Bright Red
W = '\033[1;37m'  # White
RESET = '\033[0m'


def clear():
    os.system('clear')


def banner():
    print(R + "\n               .---.\n"
          "              /     \\\n"
          "             | () () |\n"
          "              \\  ^  /\n"
          "               |||||\n"
          "              '-----'\n" + RESET)

    print(f"{C}=================================================={RESET}")
    print(f"{Y}                   AMKA INFO                      {RESET}")
    print(f"{C}=================================================={RESET}\n")


def menu():
    print(f"{M}[1]{RESET} More About Amka")
    print(f"{M}[2]{RESET} WhatsApp")
    print(f"{M}[3]{RESET} Telegram Account")
    print(f"{M}[4]{RESET} Telegram Group")
    print(f"{M}[5]{RESET} Facebook")
    print(f"{M}[6]{RESET} TikTok")
    print(f"{M}[7]{RESET} GitHub")
    print(f"{M}[8]{RESET} Exit\n")


def open_url(url):
    try:
        subprocess.run(['termux-open-url', url])
    except Exception as e:
        print(f"\n{R}Error opening URL: {e}{RESET}")


def about():
    clear()

    print(R + "\n            .---.\n"
          "           /     \\\n"
          "          | () () |\n"
          "           \\  ^  /\n"
          "            |||||\n"
          "            '---'\n" + RESET)

    # FIXED: RESET is now inside the f-string
    print(f"{C}=================================================={RESET}")
    print(f"{Y}                   ABOUT AMKA                     {RESET}")
    print(f"{C}=================================================={RESET}\n")

    print(f"{G}Welcome to my digital space!\n{RESET}")

    print(f"{G}My name is Amka. I am a hacker and black hat OSINT operator{RESET}")
    print(f"{G}focused on engineering tools directly from Android and Termux{RESET}")
    print(f"{G}environments.\n{RESET}")

    print(f"{G}I operate at the intersection of offensive security, terminal tools,{RESET}")
    print(f"{G}cybersecurity research, and open-source intelligence gathering.{RESET}")
    print(f"{G}My objective is to build stealthy, efficient, and powerful digital{RESET}")
    print(f"{G}utilities that put full control back into the terminal.{RESET}\n")

    print(R + "\n        ┌──┐ ┌──┐ ┌──┐\n"
          "        │  │ │  │ │  │\n"
          "        └──┘ └──┘ └──┘\n" + RESET)

    print(f"{C}[+] CORE FOCUS & SPECIALIZATION{RESET}")
    print(f"{G}• Cyber Operations & Hacker Methodologies{RESET}")
    print(f"{G}• OSINT Reconnaissance & Data Intelligence{RESET}")
    print(f"{G}• Termux Environment & Android Terminal Tools{RESET}")
    print(f"{G}• System Security & Privacy Engineering{RESET}")
    print(f"{G}• Automated Scripts & Network Analysis{RESET}\n")

    print(R + "\n          .---.----.\n"
          "          |   |    |\n"
          "          '---'----'\n" + RESET)

    print(f"{C}[+] FEATURED PROJECTS{RESET}")
    print(f"{G}• AmkaOSINT       - Open-source intelligence terminal utility{RESET}")
    print(f"{G}• Amka Browser    - Lightweight custom mobile web interface{RESET}")
    print(f"{G}• Amka OmniAI     - Multi-modal AI architecture framework{RESET}")
    print(f"{G}• Telegram Bots   - Automated community & network bots{RESET}\n")

    print(R + "\n            .---.\n"
          "           /  |  \\\n"
          "          | --+-- |\n"
          "           \\  |  /\n"
          "            '---'\n" + RESET)

    print(f"{C}[+] VISION & BLACK HAT PHILOSOPHY{RESET}")
    print(f"{G}Mastering system mechanics, maintaining terminal control, and{RESET}")
    print(f"{G}developing independent security tools that bypass digital constraints.{RESET}\n")

    print(f"{C}--------------------------------------------------{RESET}")
    input(f"{Y}Press Enter to return to the main menu...{RESET}")


def social_links(platform_name):
    clear()
    banner()

    print(f"{Y}--- CONNECT AMKA WITH DIFFERENT PLATFORMS ---{RESET}\n")

    url = ""

    if platform_name == 'whatsapp':
        url = "https://wa.me/254723353579"
        print(f"{C}WhatsApp         :{RESET} {G}+254723353579{RESET}")

    elif platform_name == 'telegram_account':
        url = "https://t.me/Amkakernel001"
        print(f"{C}Telegram Account :{RESET} {G}{url}{RESET}")

    elif platform_name == 'telegram_group':
        url = "https://t.me/blackhat_community1"
        print(f"{C}Telegram Group   :{RESET} {G}{url}{RESET}")

    elif platform_name == 'facebook':
        url = "https://facebook.com"
        print(f"{C}Facebook         :{RESET} {G}Amka Official{RESET}")

    elif platform_name == 'tiktok':
        url = "https://tiktok.com"
        print(f"{C}TikTok           :{RESET} {G}Amka Official{RESET}")

    elif platform_name == 'github':
        url = "https://github.com/Amka-Kernel/Amka-Info"
        print(f"{C}GitHub           :{RESET} {G}{url}{RESET}")

    print(f"\n{C}--------------------------------------------------{RESET}")

    if url:
        print(f"{Y}Opening platform...{RESET}")
        open_url(url)

    input(f"\n{Y}Press Enter to return to menu...{RESET}")


def main():
    while True:
        clear()
        banner()
        menu()

        choice = input(
            f"{Y}Select an option [1-8]: {RESET}"
        ).strip()

        if choice == '1':
            about()

        elif choice == '2':
            social_links('whatsapp')

        elif choice == '3':
            social_links('telegram_account')

        elif choice == '4':
            social_links('telegram_group')

        elif choice == '5':
            social_links('facebook')

        elif choice == '6':
            social_links('tiktok')

        elif choice == '7':
            social_links('github')

        elif choice == '8':
            print(f"\n{R}Exiting Amka Info. Stay secure!{RESET}\n")
            sys.exit(0)

        else:
            print(f"\n{R}Invalid selection. Try again.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()
