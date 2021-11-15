print("<------BLACKJACK------> \nLOADING RESOURCES FOR BLACKJACK \nPLEASE WAIT...")
import Login
import sys
def entry():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while True:
        print("<------BLACKJACK-ENTRY MENU------>")
        ch=(input("PRESS 1 TO LOGIN \nPRESS 2 TO SIGN UP \nPRESS 3 TO EXIT \nENTER YOUR CHOICE: "))
        if ch=='1':
            Login.login()
        if ch=='2':
            Login.signup()
        if ch=='3':
            sys.exit()
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnter a valid choice")
            continue
entry()