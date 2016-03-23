from lib.megapi import *

def onReadHumiture(hum):
	print "Humiture:"+str(hum)+"%";
	bot.humitureSensorRead(port,1,onReadTemperature);

def onReadTemperature(temp):
	print "Temperature:"+str(temp)+" C";

if __name__ == '__main__':
	bot = MegaPi()
	bot.start()
	port = 6;
	while 1:
		sleep(1);
		bot.humitureSensorRead(port,0,onReadHumiture);