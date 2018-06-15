import webbrowser
import time
import os

#clears the terminal before run code
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

print("""

 ███████╗██╗███╗   ██╗██████╗ ███╗   ███╗██╗   ██╗██████╗ ██████╗ ███████╗
 ██╔════╝██║████╗  ██║██╔══██╗████╗ ████║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝
 █████╗  ██║██╔██╗ ██║██║  ██║██╔████╔██║ ╚████╔╝ ██████╔╝██║  ██║█████╗  
 ██╔══╝  ██║██║╚██╗██║██║  ██║██║╚██╔╝██║  ╚██╔╝  ██╔═══╝ ██║  ██║██╔══╝  
 ██║     ██║██║ ╚████║██████╔╝██║ ╚═╝ ██║   ██║   ██║     ██████╔╝██║     
 ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝     ╚═╝   ╚═╝   ╚═╝     ╚═════╝ ╚═╝
 """)

# user will choose the option
time.sleep(.1)
print("\n 1 - Search")
print("\n 2 - Exit")
menu = int(input("\n OPTION: "))

# the program will put the name of the .PDF you want and use google as search engine
if(menu==1):
    book = str(input("\n [x] ENTER THE DESIRED .PDF: "))
    book.replace("","+"); #replace blank spaces
    url = 'https://www.google.com/search?q="' + book + '"+filetype%3Apdf'
    webbrowser.open(url) #open the url in browser
    print ("\n [!] SEARCH COMPLETED !!")
    time.sleep(3)
else:
    raise SystemExit
