#!/usr/bin/env python 
#coding: utf-8

import webbrowser
import time

print("""

 ███████╗██╗███╗   ██╗██████╗ ███╗   ███╗██╗   ██╗██████╗ ██████╗ ███████╗
 ██╔════╝██║████╗  ██║██╔══██╗████╗ ████║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝
 █████╗  ██║██╔██╗ ██║██║  ██║██╔████╔██║ ╚████╔╝ ██████╔╝██║  ██║█████╗  
 ██╔══╝  ██║██║╚██╗██║██║  ██║██║╚██╔╝██║  ╚██╔╝  ██╔═══╝ ██║  ██║██╔══╝  
 ██║     ██║██║ ╚████║██████╔╝██║ ╚═╝ ██║   ██║   ██║     ██████╔╝██║     
 ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝     ╚═╝   ╚═╝   ╚═╝     ╚═════╝ ╚═╝

 X----------------------------X
 | BY: Mateus4K / Fork: Loock |
 X----------------------------X
 """)

# user will choose the option
time.sleep(.1)
print("\n 1 - Search")
print("\n 2 - Exit")
menu = int(input("\n OPTION: "))

# the program will put the name of the .PDF you want and use google as search engine
if(menu==1):
    url = "https://www.google.com/search?q="
    book = str(input("\n [x] ENTER THE DESIRED .PDF: "))
    url += '"' + book + '"'
    url += " filetype:pdf"
    webbrowser.open(url) #open the url in browser
    print ("\n [!] SEARCH COMPLETED !!")
    time.sleep(3)
else:
    raise SystemExit
