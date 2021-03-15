import socket
import sys
import pyttsx3

sp = pyttsx3.init()
sp.say("Welcome to my simple port scanner\n Bem vindo ao meu simples port scanner")
sp.runAndWait()

wm = print("""\n This is my simple tool for search if certain port is open or closed. 
                made by ~pylover77""")
print('*'*70)
def Scannerxx():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("IP:")
    port = int(input("PORT:"))
    s.settimeout(0.7)

    if s.connect_ex((host, port)):
        print(f"ERROR: The port {port} is closed!")
    else:
        print(f'The port {port} is open!')

    sip = input("would you like to do another search? Y/N: ")
    if sip ==("Y"): 
        Scannerxx()
    elif sip ==("N"):
        sys.exit()
Scannerxx()


