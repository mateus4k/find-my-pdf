#!/usr/bin/env python 
# -*- coding: utf-8 -*-

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
                                                                         

# Local onde o usuário irá escolher a opção
time.sleep(.1)
print("\n 1 - Pesquisar")
print("\n 2 - Exit")
menu = int(input("\n OPTION: "))

# Parte o qual o programa irá colocar o nome do PDF o qual deseja
# E o programa usará o Google como fonte de pesquisa
if(menu==1):
    url = "https://www.google.com/search?q="
    book = str(input("\n [x] INSIRA O PDF DESEJADO: "))
    url += '"' + book + '"'
    url += " filetype:pdf"
    webbrowser.open(url) # parte o qual o programa manda o navegador padrão abrir a URL que já está no programa
    print ("\n [!] PESQUISA CONCLUÍDA!!")
    time.sleep(4)
else:
    raise SystemExit
