"""
Tutorial Link:https://youtu.be/iS2Dw-YKNpQ
"""
import subprocess

data =  subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
L = []

for profile in data:
    if 'All User Profile' in profile:
        profile  = profile.split(':')[1][1:-1]
        L.append(profile)


for profile in L:
    if profile=='Kushal Vijay':
        data = subprocess.check_output(['netsh','wlan','show','profile',profile,'key=clear']).decode('utf-8').split('\n')

for line in data:
    if 'Key Content' in line:
        password = line.split(':')[1][1:-1]
        print("Password for Kushal Vijay Network is",password)

