# commandeMoteur.py

import serial

# Definition classe commandeMoteur
class cmdMoteur:

   # definition de la methode speciale __init__ (constructeur)
   def __init__(self):
	self.ser = serial.Serial("/dev/ttyAMA0")
	print "toto"

   # definition de la methode miseEnForme()
   def envoiCommande(self,Vx,Vy,Omega):	
	#Reglage de Vx
	if Vx >= 0 :
		octet0 = int('A8',16) #On force le PF vx a 1
	if Vx < 0 :
		octet0 = int('A0',16) #On force le PF vx a 0
		Vx = Vx + 127					
	#Reglage de Vy
	if Vy >= 0 :
		octet0 = int('04',16) | octet0 #On force le PF vy a 1
	if Vy < 0 :
		octet0 = int('FB',16) & octet0 #On force le PF vy a 0
		Vy = Vy + 127			
	Omega = (Omega+64)&int('7F',16)	
	octet4 = str(chr((Vx+Vy+Omega)&127))
	octet0 = str(chr(octet0))
	octet1 = str(chr(Vx)) #On impose nos valeur de 0 a 255
	octet2 = str(chr(Vy))#On impose nos valeur de 0 a 256
	octet3 = str(chr(Omega))#On impose nos valeur de 0 a 128
	cmd = octet0 + octet1 + octet2 + octet3 + octet4

	self.ser.write(cmd)
