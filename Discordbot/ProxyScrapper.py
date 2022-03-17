
import os
import requests
import random
import string
from colorama import Fore
from pyfiglet import Figlet
import webbrowser


webbrowser.open('(Your URL here)')

os.system('cls')

def render(text, style):
    f = Figlet(font=style)
    print('\n'*10)
    print(f.renderText(text))

color = render(f"CIVO'S PROXIE SCRAPER", "banner3-D")

print(f"{Fore.BLUE}{color}")

ready = input(f"{Fore.RED} This program will autoscrape (HTTP, SOCKS4, SOCKS5) proxies into a file (Press ENTER To Continue)")

url = 'https://api.openproxylist.xyz/http.txt'
r = requests.get(url)
result = r.text
with open("http.txt", "w") as file:
    file.write(result)

url = 'https://api.openproxylist.xyz/socks4.txt'
r = requests.get(url)
result = r.text
with open("socks4.txt", "w") as file:
    file.write(result)

url = 'https://api.openproxylist.xyz/socks5.txt'
r = requests.get(url)
result = r.text
with open("socks5.txt", "w") as file:
    file.write(result)