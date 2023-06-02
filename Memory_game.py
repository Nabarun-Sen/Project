#Memory Game
import os
import time
count=1

def findAndPrintUncommonChars(str1, str2):   
	l1 = len(str1) 
	l2 = len(str2)
	if l1!=l2:
		print("Your input length does not match to the actual text lenghth")
	else:
		for i in range(0, l1):
			if str1[i]!=str2[i]:
				print("\nCharacter mismatch at position: ",i)
				print("The actual character was '"+str1[i]+"' and you entered '"+str2[i]+"'")
    

def presskeytocontinue():
	str4=input("\nPress any key to continue...")
	if str4:
		os.system('resume')

def clearscreen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
if __name__ == "__main__": 
	clearscreen()
	str1="This is the red apple #"+str(count)
	print("Please read the below message carefully\n")
	print("Message -> "+str1+"\n")
	print("The above text will appear for 5 seconds")
	time.sleep(5)
	clearscreen()
	str2=input("Enter the text appeared before : ")
	if len(str2)<20:
		print("Sorry your input does not match to the input length constraint")
		print("Your input contains : ",len(str2)," characters")
		print("Your input should contain atleast 20 characters.")
	else:
		while str1!=str2:
			count=count+1
			print("\nSorry!! Wrong input\n")
			findAndPrintUncommonChars(str1,str2)
			presskeytocontinue()
			clearscreen()
			if count<=3:
				print("Please see the read Message carefully\n")
				str1="This is the red apple #"+str(count)
				print("Message -> "+str1+"\n")
				print("The above text will appear for 5 seconds")
				time.sleep(5)
				clearscreen()
				str2=input("Enter the text appeared before : ")
			else:
				print("Oopss!! Your attempt is over...\n\nBetter luck next time...")
				break
		else:
			print("\nCorrect answer\n")
		
	str3=input("\nPress enter any key to exit ")
	if str3:
		os.system('exit')