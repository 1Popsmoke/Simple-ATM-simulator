#import os
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

Name= input ("Enter your name: ")
speak.speak("Welcome to ATM")
speak.speak(Name)

balance = 1000000

while True:
    print("======Welcome to ATM======", Name)
    print('1. Check balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    speak.speak("Enter Your choice ")
    time = 1
    speak.speak('1. check balance')
    speak.speak('2. Deposit')
    speak.speak('3. withdraw')
    speak.speak('4. Exit')
    choice = int(input("Enter your choice: "))
    

    if choice ==1:
        print("Your balance is: ", balance)
        speak.speak("your current balance is")
        speak.speak(balance)
    elif choice ==2:
        amount =int(input("Enter the amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            
            print("Your new balance is: ", balance)
            speak.speak("Your balance is")
            speak.speak(balance)
            
        else:
            print ("Invalid amount")
            speak.speak("Invalid amount")
    elif choice == 3:
        amount =int(input("Enter the Amount to Withdraw: "))
        if amount> 0 and amount <= balance:
            transaction = 25
            balance = balance - amount- transaction
            print ("Your balance is: ", balance)
            speak.speak("your balance is")
            speak.speak(balance)
        elif amount <= 0:
            print ("Invalid amount") 
            speak.speak("Invalid amount")
        elif amount > balance:
        
            print ("Your account is low on funds😒😒") 
            speak.speak("your acount is low on funds")   
    else:
        exit()                     