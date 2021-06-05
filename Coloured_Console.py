"""
Tutorial Link:https://youtu.be/El0WJ38167A
"""
import colorama
from colorama import Back,Fore,Style

colorama.init(autoreset=True)

print(Fore.RED + "Savage Programmer")
print(Back.GREEN + "Savage Programmer")

text_fore = f'{Fore.MAGENTA}V{Fore.BLUE}I{Fore.LIGHTBLUE_EX}B{Fore.GREEN}G{Fore.YELLOW}Y{Fore.LIGHTRED_EX}O{Fore.RED}R'
text_back = f'{Back.MAGENTA}V{Back.BLUE}I{Back.LIGHTBLUE_EX}B{Back.GREEN}G{Back.YELLOW}Y{Back.LIGHTRED_EX}O{Back.RED}R'
print(text_fore)
print(text_back)

print(f'{Style.BRIGHT}{Fore.BLUE}Savage Programmer')
