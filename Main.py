import ctypes
import random
import re
import os
import threading
import time
import colorama
import requests
import sys
from colorama import Fore
from termcolor import colored
from itertools import product

import sys
colorama.init()

ctypes.windll.kernel32.SetConsoleTitleW("Proxy Scraper - Made by Flex#8629")

try:
    os.remove("Tested Http/Https Proxies.txt")
    os.remove("HTTP Proxies.txt")
except:
    pass

validproxies = []
proxiescheck = []
kill = False
global proxycount
proxycount = 0

global workingproxies
workingproxies = 0
global badproxies
badproxies = 0
global reamming
reamming = 1

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

### HTTP/HTTPS
URL = ""
def startingfortestproxies():
    global proxycount, kill
    while not kill:
        proxycount += 1
        if proxycount > len(proxiescheck) - 1:
            kill = True
        try:
            proxytouse = proxiescheck[proxycount]
            testproxies(proxytouse)
        except:
            pass

def startingfortestproxies_input():
    global proxycount, kill
    while not kill:
        proxycount += 1
        if proxycount > len(proxiescheck) - 1:
            kill = True
        try:
            proxytouse = proxiescheck[proxycount]
            testproxies_input(proxytouse)
        except:
            pass

def testproxies(proxytotest):
    global workingproxies, badproxies

    try:
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        proxies = {
            'http': 'http://' + proxytotest,
            'https': 'https://' + proxytotest,
        }
        r = requests.get("https://www.google.com/", proxies=proxies, headers=headers, timeout=10)
        if int(r.status_code) == 200:
            validproxies.append(proxytotest)
            workingproxies += 1
        else:
            badproxies += 1
    except:
        badproxies += 1
        pass

def testproxies_input(proxytotest):
    global workingproxies, badproxies

    try:
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        proxies = {
            'http': 'http://' + proxytotest,
            'https': 'https://' + proxytotest,
        }
        r = requests.get("{}".format(URL), proxies=proxies, headers=headers, timeout=10)
        if int(r.status_code) == 200:
            validproxies.append(proxytotest)
            workingproxies += 1
        else:
            badproxies += 1
    except:
        badproxies += 1
        pass

def printrqs():
    global workingproxies, badproxies, reamming
    while True:

        efok = workingproxies + badproxies
        reamming = len(proxiescheck) - efok
        time.sleep(0.10)
        print(Fore.GREEN + "Good: [{}] | ".format(workingproxies) + Fore.RESET + Fore.RED + "Bad: [{}] | ".format(badproxies) + Fore.RESET + Fore.CYAN + "Remaining: [{}]".rstrip().format(reamming), end="\r")
        if reamming == 1:
            break
### HTTP/HTTPS


###sOCKS4
URL_4 = ""
def startingfortestproxies4():
    global proxycount, kill
    while not kill:
        proxycount += 1
        if proxycount > len(proxiescheck) - 1:
            kill = True
        try:
            proxytouse = proxiescheck[proxycount]
            testproxies4(proxytouse)
        except:
            pass

def startingfortestproxies_input4():
    global proxycount, kill
    while not kill:
        proxycount += 1
        if proxycount > len(proxiescheck) - 1:
            kill = True
        try:
            proxytouse = proxiescheck[proxycount]
            testproxies_input4(proxytouse)
        except:
            pass

def testproxies4(proxytotest):
    global workingproxies, badproxies

    try:
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        proxies = {
            'http': 'socks4://' + proxytotest,
            'https': 'socks4://' + proxytotest,
        }
        r = requests.get("https://www.google.com/", proxies=proxies, headers=headers, timeout=10)
        if int(r.status_code) == 200:
            validproxies.append(proxytotest)
            workingproxies += 1
        else:
            badproxies += 1
    except:
        badproxies += 1
        pass

def testproxies_input4(proxytotest):
    global workingproxies, badproxies
    URL_4

    try:
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        proxies = {
            'http': 'http://' + proxytotest,
            'https': 'https://' + proxytotest,
        }
        r = requests.get("{}".format(URL_4), proxies=proxies, headers=headers, timeout=10)
        if int(r.status_code) == 200:
            validproxies.append(proxytotest)
            workingproxies += 1
        else:
            badproxies += 1
    except:
        badproxies += 1
        pass

def printrqs4():
    global workingproxies, badproxies, reamming
    while True:

        efok = workingproxies + badproxies
        reamming = len(proxiescheck) - efok
        time.sleep(0.10)
        print(Fore.GREEN + "Good: [{}] | ".format(workingproxies) + Fore.RESET + Fore.RED + "Bad: [{}] | ".format(badproxies) + Fore.RESET + Fore.CYAN + "Remaining: [{}]".rstrip().format(reamming), end="\r")
        if reamming == 1:
            break
###sOCKS4


###sOCKS5
URL_5 = ""
def startingfortestproxies5():
    global proxycount, kill
    while not kill:
        proxycount += 1
        if proxycount > len(proxiescheck) - 1:
            kill = True
        try:
            proxytouse = proxiescheck[proxycount]
            testproxies5(proxytouse)
        except:
            pass

def startingfortestproxies_input5():
    global proxycount, kill
    while not kill:
        proxycount += 1
        if proxycount > len(proxiescheck) - 1:
            kill = True
        try:
            proxytouse = proxiescheck[proxycount]
            testproxies_input5(proxytouse)
        except:
            pass

def testproxies5(proxytotest):
    global workingproxies, badproxies

    try:
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        proxies = {
            'http': 'socks5://' + proxytotest,
            'https': 'socks5://' + proxytotest,
        }
        r = requests.get("https://www.google.com/", proxies=proxies, headers=headers, timeout=10)
        if int(r.status_code) == 200:
            validproxies.append(proxytotest)
            workingproxies += 1
        else:
            badproxies += 1
    except:
        badproxies += 1
        pass

def testproxies_input5(proxytotest):
    global workingproxies, badproxies , URL_5


    try:
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        proxies = {
            'http': 'http://' + proxytotest,
            'https': 'https://' + proxytotest,
        }
        r = requests.get("{}".format(URL_5), proxies=proxies, headers=headers, timeout=10)
        if int(r.status_code) == 200:
            validproxies.append(proxytotest)
            workingproxies += 1
        else:
            badproxies += 1
    except:
        badproxies += 1
        pass

def printrqs5():
    global workingproxies, badproxies, reamming
    while True:

        efok = workingproxies + badproxies
        reamming = len(proxiescheck) - efok
        time.sleep(0.10)
        print(Fore.GREEN + "Good: [{}] | ".format(workingproxies) + Fore.RESET + Fore.RED + "Bad: [{}] | ".format(badproxies) + Fore.RESET + Fore.CYAN + "Remaining: [{}]".rstrip().format(reamming), end="\r")
        if reamming == 1:
            break
###sOCKS5


def HTTP():
    print(colored("""
        
         ██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗     ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
         ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░     ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
         ██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░     ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
         ██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░     ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
         ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░     ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝                        
                                                             Dev: Flex#8629

    """, "red"))

    global GOOGLE
    print(Fore.GREEN + "Getting Proxies Please Wait...")
    # https/https
    try:
        w = requests.get("https://proxy-spider.com/api/proxies.example.txt")
        e = requests.get("http://rootjazz.com/proxies/proxies.txt")
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
        t = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
        y = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
        u = requests.get("http://rootjazz.com/proxies/proxies.txt")
        o = requests.get("https://proxy-spider.com/api/proxies.example.txt")
    except:
        print(Fore.RED + "an error has occurred, probably proxy api blocked your IP run a vpn and try again:  ",end="")
        input()
        os.close()


    HTTP = open("http test.txt", "a")
    HTTP.writelines(w.text)
    HTTP.writelines(e.text)
    HTTP.writelines(r.text)
    HTTP.writelines(t.text)
    HTTP.writelines(y.text)
    HTTP.writelines(u.text)
    HTTP.writelines(o.text)
    HTTP.close()

    with open('http test.txt') as result:
        uniqlines = set(result.readlines())
        with open('HTTP Proxies.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))
            result.close()
            os.remove("http test.txt")

    file = open("HTTP Proxies.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    print(Fore.RED + "Found [" + Fore.RESET + Fore.GREEN + str(line_count) + Fore.RESET + Fore.RED + "] Proxies")

    print(Fore.MAGENTA + "Do u Want To Test Downloaded Proxies" + Fore.RESET + Fore.GREEN + " [1 = Yes/2 = No] : " + Fore.RESET + Fore.RED, end="")


    Test_proxies = input()

    if int(Test_proxies) == 1:
        clearConsole()

        print(colored("""
          
         ██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗     ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
         ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░     ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
         ██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░     ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
         ██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░     ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
         ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░     ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝                        
                                                             Dev: Flex#8629
                                                             
               """, "red"))
        print(Fore.MAGENTA + "Test Proxies On " + Fore.RESET + Fore.BLUE + "Google.com " + Fore.RESET + Fore.GREEN + "[ 1 = Yes/ 2 = No, Custom Url] : " + Fore.RESET + Fore.RED, end="")

        GOOGLE = input()

        print("\n")

        if int(GOOGLE) == 1:
            openproxyfile = open("HTTP Proxies.txt", "r")
            proxies = openproxyfile.readlines()


            for line in proxies:
                proxiescheck.append(line)
            for i in range(300):
                x = threading.Thread(target=startingfortestproxies)
                x.start()
            x = threading.Thread(target=printrqs)
            x.start()
            while reamming != 1:
                pass
            filetosave = open("Tested Https Proxies.txt", "a")
            for line in validproxies:
                filetosave.writelines(line)
            filetosave.close()
            time.sleep(1)
            print("\n")
            print(Fore.RED + "Working Proxies Saved To " + Fore.RESET + Fore.GREEN + "Tested Https Proxies.txt" + Fore.RESET)
            print(Fore.RED + "Click Enter To Exit: ", end="")
            input()

        if int(GOOGLE) == 2:
            global URL
            print(Fore.MAGENTA + "Enter Custom Url" + Fore.RESET + Fore.RED + " (Must Include https://): " + Fore.RESET + Fore.GREEN,end="")
            URL = input()

            openproxyfile = open("HTTP Proxies.txt", "r")
            proxies = openproxyfile.readlines()
            print("\n")

            for line in proxies:
                proxiescheck.append(line)
            for i in range(300):
                x = threading.Thread(target=startingfortestproxies_input)
                x.start()
            x = threading.Thread(target=printrqs)
            x.start()
            while reamming != 1:
                pass
            filetosave = open("Tested Https Proxies.txt", "a")
            for line in validproxies:
                filetosave.writelines(line)
            filetosave.close()
            time.sleep(1)
            print("\n")
            print(Fore.RED + "Working Proxies Saved To " + Fore.RESET + Fore.GREEN + "Tested Https Proxies.txt" + Fore.RESET)
            print(Fore.RED + "Click Enter To Exit: ", end="")
            input()

    if int(Test_proxies) == 2:
        print(Fore.MAGENTA + "proxies Saved To " + Fore.RESET + Fore.GREEN + "HTTP Proxies.txt" + Fore.RESET)
        print(Fore.RED + "Click Enter To Exit: ", end="")
        input()

def SOCKS4():
    print(colored("""
       
         ██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗     ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
         ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░     ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
         ██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░     ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
         ██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░     ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
         ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░     ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝                        
                                                             Dev: Flex#8629

        """, "red"))

    global GOOGLE4
    print(Fore.GREEN + "Getting Proxies Please Wait...")

    try:
        p = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
        pp = p.text.replace("\n", "")
        a = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt")
        s = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt")
        f = requests.get("https://www.proxyscan.io/download?type=socks4")
    except:
        print(Fore.RED + "an error has occurred, probably proxy api blocked your IP run a vpn and try again:  ", end="")
        input()
        os.close()

    Socks4 = open("socks4 test.txt", "a")
    Socks4.writelines(pp)
    Socks4.writelines(a.text)
    Socks4.writelines(s.text)
    Socks4.writelines(f.text)
    Socks4.close()

    with open('socks4 test.txt') as result:
        uniqlines = set(result.readlines())
        with open('Socks4 Proxies.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))
            result.close()
            os.remove("socks4 test.txt")

    file = open("Socks4 Proxies.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    print(Fore.RED + "Found [" + Fore.RESET + Fore.GREEN + str(line_count) + Fore.RESET + Fore.RED + "] Proxies")

    print(Fore.MAGENTA + "Do u Want To Test Downloaded Proxies" + Fore.RESET + Fore.GREEN + " [1 = Yes/2 = No] : " + Fore.RESET + Fore.RED,end="")

    Test_proxies = input()

    if int(Test_proxies) == 1:
        clearConsole()

        print(colored("""
           
         ██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗     ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
         ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░     ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
         ██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░     ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
         ██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░     ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
         ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░     ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝                        
                                                             Dev: Flex#8629

               """, "red"))

        print(Fore.MAGENTA + "Test Proxies On " + Fore.RESET + Fore.BLUE + "Google.com " + Fore.RESET + Fore.GREEN + "[ 1 = Yes/ 2 = No, Custom Url] : " + Fore.RESET + Fore.RED,end="")

        GOOGLE4 = input()

        print("\n")

        if int(GOOGLE4) == 1:
            openproxyfile = open("Socks4 Proxies.txt", "r")
            proxies = openproxyfile.readlines()

            for line in proxies:
                proxiescheck.append(line)
            for i in range(300):
                x = threading.Thread(target=startingfortestproxies4)
                x.start()
            x = threading.Thread(target=printrqs4)
            x.start()
            while reamming != 1:
                pass
            filetosave = open("Tested Socks4 Proxies.txt", "a")
            for line in validproxies:
                filetosave.writelines(line)
            filetosave.close()
            time.sleep(1)
            print("\n")
            print(
                Fore.RED + "Working Proxies Saved To " + Fore.RESET + Fore.GREEN + "Tested Socks4 Proxies.txt" + Fore.RESET)
            print(Fore.RED + "Click Enter To Exit: ", end="")
            input()

        if int(GOOGLE4) == 2:
            global URL_4
            print(Fore.MAGENTA + "Enter Custom Url" + Fore.RESET + Fore.RED + " (Must Include https://): " + Fore.RESET + Fore.GREEN, end="")
            URL_4 = input()
            print("\n")

            openproxyfile = open("Socks4 Proxies.txt", "r")
            proxies = openproxyfile.readlines()

            for line in proxies:
                proxiescheck.append(line)
            for i in range(300):
                x = threading.Thread(target=startingfortestproxies_input4)
                x.start()
            x = threading.Thread(target=printrqs4)
            x.start()
            while reamming != 1:
                pass
            filetosave = open("Tested Socks4 Proxies.txt", "a")
            for line in validproxies:
                filetosave.writelines(line)
            filetosave.close()
            time.sleep(1)
            print("\n")
            print(
                Fore.RED + "Working Proxies Saved To " + Fore.RESET + Fore.GREEN + "Tested Socks4 Proxies.txt" + Fore.RESET)
            print(Fore.RED + "Click Enter To Exit: ", end="")
            input()

    if int(Test_proxies) == 2:
        print(Fore.MAGENTA + "proxies Saved To " + Fore.RESET + Fore.GREEN + "Socks4 Proxies.txt" + Fore.RESET)
        print(Fore.RED + "Click Enter To Exit: ", end="")
        input()

def SOCKS5():
    print(colored("""
    
         ██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗     ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
         ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░     ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
         ██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░     ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
         ██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░     ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
         ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░     ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝                        
                                                             Dev: Flex#8629

            """, "red"))

    global GOOGLE5
    print(Fore.GREEN + "Getting Proxies Please Wait...")

    try:
        c = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt")
        v = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt")
        b = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt")
        bb = b.text.replace("\n", "")
    except:
        print(Fore.RED + "an error has occurred, probably proxy api blocked your IP run a vpn and try again:  ", end="")
        input()
        os.close()


    SOCKS5 = open("SOCKS5 test.txt", "a")
    SOCKS5.writelines(c.text)
    SOCKS5.writelines(v.text)
    SOCKS5.writelines(bb)
    SOCKS5.close()

    with open('SOCKS5 test.txt') as result:
        uniqlines = set(result.readlines())
        with open('SOCKS5 Proxies.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))
            result.close()
            os.remove("SOCKS5 test.txt")

    file = open("SOCKS5 Proxies.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    print(Fore.RED + "Found [" + Fore.RESET + Fore.GREEN + str(line_count) + Fore.RESET + Fore.RED + "] Proxies")

    print(
        Fore.MAGENTA + "Do u Want To Test Downloaded Proxies" + Fore.RESET + Fore.GREEN + " [1 = Yes/2 = No] : " + Fore.RESET + Fore.RED,
        end="")

    Test_proxies = input()

    if int(Test_proxies) == 1:
        clearConsole()

        print(colored("""
        
         ██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗     ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
         ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░     ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
         ██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░     ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
         ██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░     ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
         ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░     ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝                        
                                                             Dev: Flex#862  
                   """, "red"))

        print(
            Fore.MAGENTA + "Test Proxies On " + Fore.RESET + Fore.BLUE + "Google.com " + Fore.RESET + Fore.GREEN + "[ 1 = Yes/ 2 = No, Custom Url] : " + Fore.RESET + Fore.RED,
            end="")

        GOOGLE5 = input()

        print("\n")

        if int(GOOGLE5) == 1:
            openproxyfile = open("SOCKS5 Proxies.txt", "r")
            proxies = openproxyfile.readlines()

            for line in proxies:
                proxiescheck.append(line)
            for i in range(300):
                x = threading.Thread(target=startingfortestproxies5)
                x.start()
            x = threading.Thread(target=printrqs5)
            x.start()
            while reamming != 1:
                pass
            filetosave = open("Tested Socks5 Proxies.txt", "a")
            for line in validproxies:
                filetosave.writelines(line)
            filetosave.close()
            time.sleep(1)
            print("\n")
            print(
                Fore.RED + "Working Proxies Saved To " + Fore.RESET + Fore.GREEN + "Tested Socks5 Proxies.txt" + Fore.RESET)
            print(Fore.RED + "Click Enter To Exit: ", end="")
            input()

        if int(GOOGLE5) == 2:
            global URL_5
            print(
                Fore.MAGENTA + "Enter Custom Url" + Fore.RESET + Fore.RED + " (Must Include https://): " + Fore.RESET + Fore.GREEN,
                end="")
            URL_5 = input()
            print("\n")

            openproxyfile = open("SOCKS5 Proxies.txt", "r")
            proxies = openproxyfile.readlines()

            for line in proxies:
                proxiescheck.append(line)
            for i in range(300):
                x = threading.Thread(target=startingfortestproxies_input5)
                x.start()
            x = threading.Thread(target=printrqs5)
            x.start()
            while reamming != 1:
                pass
            filetosave = open("Tested Socks5 Proxies.txt", "a")
            for line in validproxies:
                filetosave.writelines(line)
            filetosave.close()
            time.sleep(1)
            print("\n")
            print(
                Fore.RED + "Working Proxies Saved To " + Fore.RESET + Fore.GREEN + "Tested Socks5 Proxies.txt" + Fore.RESET)
            print(Fore.RED + "Click Enter To Exit: ", end="")
            input()

    if int(Test_proxies) == 2:
        print(Fore.MAGENTA + "proxies Saved To " + Fore.RESET + Fore.GREEN + "Socks5 Proxies.txt" + Fore.RESET)
        print(Fore.RED + "Click Enter To Exit: ", end="")
        input()




print(colored("""

         ██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗     ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
         ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
         ██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░     ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
         ██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░     ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
         ██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░     ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
         ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░     ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝                        
                                                             Dev: Flex#8629
                                                             
""", "red"))
time.sleep(0.5)


print(Fore.GREEN + "  [1] " + Fore.RESET + "-" + Fore.RED + " Http/Https")
print(Fore.GREEN + "  [2] " + Fore.RESET + "-" + Fore.RED + " Socks4")
print(Fore.GREEN + "  [3] " + Fore.RESET + "-" + Fore.RED + " Socks5" + "\n")


print(Fore.RED + " Select Proxy Type: " + Fore.RESET + Fore.GREEN, end="")
user_input = input()



clearConsole()

if int(user_input) == 1:
    HTTP()

if int(user_input) == 2:
    SOCKS4()

if int(user_input) == 3:
    SOCKS5()
