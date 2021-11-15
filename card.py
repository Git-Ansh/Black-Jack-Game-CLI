import sms
import os
import math
import smtplib
import pwinput
import random
import sys
import config
import fig
import mysql.connector as m
from playsound import playsound
from prompt_toolkit import prompt
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
db = m.connect(host="localhost", user="root", passwd="Anshshah2003")
c = db.cursor(buffered=True)
c.execute("create database if not exists blackjack")
c.execute("use blackjack")
c.execute("create table if not exists players(username varchar(20) references login(username), full_name varchar(50), balance int, total_games_won int, total_games_lost int, total_games_played_and_draws int)")
def bmenu():
    li=[]
    lil=[]
    while True:
        print("<------MENU------>")
        cho = (input("Enter 1 to play black jack \nEnter 2 to view leaderboard \nEnter 3 to View Account details \nEnter 4 deposit funds in you account \nEnter 5 to withdraw balance \nEnter 6 to log out \n>"))
        if cho == '1':
            dealer()
        if cho == '2':
            c.execute("select username,total_games_won from players order by total_games_won DESC")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLEADERBOARD\nRank, User, Wins")
            for k in c:
                ki = (str(k).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                li.append(ui)
            '''num_fields = len(c.description)
            field_names = [i[0] for i in c.description]
            print(field_names)'''
            n_indices = 1
            nk=0
            for f in range(0, len(li), n_indices):
                nk+=1
                print(nk,"  ,",*li[f:f + n_indices])
            while True:
                bip=input("\n\nPress 'B' to play blackjack \nPress 'M' to return to menu \n> ")
                if bip=='b':
                    dealer()
                if bip=='m':
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    bmenu()
                if bip!='b' and bip!='m':
                    print("please enter a valid input(B/M)")
                    continue
        if cho=='3':
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(str(config.usrnm),"'s","Account")
            print("User,  Full Name,  B,  W,  L,  P/D  ")
            c.execute("select * from players where username='"+str(config.usrnm)+"'")
            for k in c:
                ki = (str(k).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                lil.append(ui)
            print(*lil)
            bip = input("\n\nPress 'B' to play blackjack \nPress 'M' to return to menu \n> ")
            if bip == 'b':
                dealer()
            if bip == 'm':
                print(
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                bmenu()
            if bip != 'b' and bip != 'm':
                print("please enter a valid input(B/M)")
                continue
        if cho=='6':
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("> Loggged-out of", str(config.usrnm))
            print("\n")
            while True:
                print("<--Exit Menu--->")
                n=input("Enter 1 to login again \nEnter 2 to sign-up \nEnter 3 to exit \n>")
                if n=='1':
                    login()
                if n=='2':
                    signup()
                if n=='3':
                    sys.exit()
                if n!='1' and n!='2' and n!='3':
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    continue
        if cho=='4':
            pl=[]
            c.execute("select balance from players where username='" + str(config.usrnm) + "'")
            for i in c:
                ki = (str(i).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                pl.append(ui)
            bet.buyin = int(pl[0])
            while True:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<---DEPOSIT--->")
                print("Current Balance: ", bet.buyin,"$")
                b = int(input("Enter Amount you want to buy-in (min. 15$) $: "))
                if b < 15:
                    print("min. buy-in is 15$")
                    continue
                if b >= 15:
                    bet.buyin += b
                    c.execute("update players set balance='"+str(bet.buyin)+"' where username='"+str(config.usrnm)+"'")
                    db.commit()
                    break
        if cho=='5':
            withdraw()
        if cho!='1' and cho!='2' and cho!='3' and cho!='4' and cho!='5' and cho!='6':
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter correct option(1/2/3).")
            continue




def bet():
    bet.buyin=0



x = [' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', 10, ' A', ' K', ' Q', ' J']
l = ['♠', '♡', '♢', '♧']


def dealer():
    pl=[]
    global qi, hi, fi, di, dit, fit, f, d
    dealer.dsum = 0
    dealer.psum = 0
    dealer.bet = 0
    dealer.p = random.choice(l)
    dealer.k = random.choice(x)
    c.execute("select balance from players where username='"+str(config.usrnm)+"'")
    for i in c:
        ki = (str(i).strip('()').replace('\'', ''))
        ui = ki.strip(',').replace('\'', '')
        pl.append(ui)
    bet.buyin=int(pl[0])
    try:
        if bet.buyin == 0 or bet.buyin<15:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<------BLACK JACK------>")
            while True:
                print("Your Account Balance is low")
                print("Current Balance: ", bet.buyin,"$")
                b = int(input("Enter Amount you want to buy-in (min. 15$) $: "))
                if b < 15:
                    print("min. buy-in is 15$")
                    continue
                if b >= 15:
                    bet.buyin += b
                    c.execute("update players set balance='"+str(bet.buyin)+"' where username='"+str(config.usrnm)+"'")
                    db.commit()
                    break
        else:
            pass
        while True:
            print(
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<------BLACK JACK------>")
            print("Current Balance: ", bet.buyin, "$")
            btb=int(input("Enter your bet(min. 5$) $: "))
            if btb<5:
                print("min. bet is 5$")
                continue
            if btb>bet.buyin:
                print("insufficient balance")
                continue
            if btb>=5:
                dealer.bet+=btb
                bet.buyin-=dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                break        
    except:
        print("error")
    finally:
        if dealer.bet == 0 or dealer.bet < 5:
            dealer()
        if dealer.bet != 0:
            lw = []
            c.execute("select total_games_won from players where username='" + config.usrnm + "'")
            for i in c:
                ki = (str(i).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                lw.append(ui)
            dealer.tw = int(lw[0])
            ll = []
            c.execute("select total_games_lost from players where username='" + config.usrnm + "'")
            for i in c:
                ki = (str(i).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                ll.append(ui)
            dealer.tl = int(ll[0])
            li = []
            c.execute("select total_games_played_and_draws from players where username='" + config.usrnm + "'")
            for i in c:
                ki = (str(i).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                li.append(ui)
            dealer.tp = int(li[0])
            dealer.tp += 1
            c.execute("update players set total_games_played_and_draws='" + str(dealer.tp) + "' where username='" + str(
                config.usrnm) + "'")
            db.commit()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE DEALER IS DEALING THE CARDS\n\n")

            print("DEALER'S CARDS")
            for i in range(0,2):
                playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
            print("-------------    --------------")
            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |", dealer.k, "        |")
            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |    ", dealer.p, "     |")
            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |        ", dealer.k, "|")
            print("-------------    --------------")
            if dealer.k == x[9]:
                dealer.dsum += 11
            elif dealer.k == x[10]:
                dealer.dsum += 10
            elif dealer.k == x[11]:
                dealer.dsum += 10
            elif dealer.k == x[12]:
                dealer.dsum += 10
            else:
                ko = int(dealer.k)
                dealer.dsum += ko
            h = random.choice(x)
            w = random.choice(x)
            q = random.choice(l)
            z = random.choice(l)
            print("YOUR CARDS")
            for i in range(0,2):
                playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
            print("-------------    --------------")
            print("|", h, "       |    |", w, "        |")
            print("|           |    |            |")
            print("|           |    |            |")
            print("|   ", q, "     |    |    ", z, "     |")
            print("|           |    |            |")
            print("|           |    |            |")
            print("|       ", h, "|    |        ", w, "|")
            print("-------------    -------------- ")
            if h == x[10]:
                dealer.psum += 10
            elif h == x[11]:
                dealer.psum += 10
            elif h == x[12]:
                dealer.psum += 10
            elif h != x[9] and h != x[10] and h != x[11] and h != x[12]:
                ho = int(h)
                dealer.psum += ho
            if w == x[10]:
                dealer.psum += 10
            elif w == x[11]:
                dealer.psum += 10
            elif w == x[12]:
                dealer.psum += 10
            elif w != x[9] and w != x[10] and w != x[11] and w != x[12]:
                wok = int(w)
                dealer.psum += wok
            if h == x[9]:
                while True:
                    print("Dealer's Total:", dealer.dsum)
                    print("Your Total:", dealer.psum)
                    ak = int(input("Do you want 'A' to be 1 or 11(card 1)? \n>"))
                    if ak == 1:
                        dealer.psum += 1
                        break
                    if ak == 11:
                        dealer.psum += 11
                        break
                    else:
                        print("Please enter correct value(1/11)")
                        continue
            if w == x[9]:
                while True:
                    print("Dealer's Total:", dealer.dsum)
                    print("Your Total:", dealer.psum)
                    ak = int(input("Do you want 'A' to be 1 or 11(card 2)? \n>"))
                    if ak == 1:
                        dealer.psum += 1
                        break
                    if ak == 11:
                        dealer.psum += 11
                        break
                    else:
                        print("Please enter correct value(1/11)")
                        continue

            if dealer.psum > 21:
                dealer.tl += 1
                c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                    config.usrnm) + "'")
                db.commit()
                print("Dealer's Total:", dealer.dsum)
                print("Your Total:", dealer.psum)
                print("DEALER WINS! BETTER LUCK NEXT TIME.")
                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                dealer.bet = dealer.bet / 2
                bet.buyin+=dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                print("Current Balance: ", bet.buyin,"$")
                while True:
                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                    if ch == 'p':
                        dealer()
                        break
                    if ch == 'e':
                        bmenu()
                    else:
                        print("Enter a valid option(p/e)")
                        continue
            if dealer.psum == 21:
                print("CONGRATULATIONS! YOU ARE BLACKJACK! DOUBLE MONEY!")
                dealer.tw += 1
                c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                    config.usrnm) + "'")
                db.commit()
                print("Dealer's Total:", dealer.dsum)
                print("Your Total:", dealer.psum)
                playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                dealer.bet = dealer.bet * 2
                bet.buyin += dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                print("Current Balance: ", bet.buyin,"$")
                while True:
                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                    if ch == 'p':
                        dealer()
                        break
                    if ch == 'e':
                        bmenu()
                    else:
                        print("Enter a valid option(p/e)")
                        continue
            if dealer.psum < 21:
                while True:
                    print("Dealer's Total:", dealer.dsum)
                    print("Your Total:", dealer.psum)
                    ask = input("press 'H' to hit or 'S' to stand \n> ")
                    if ask == 's':
                        player()
                    if ask == 'h':
                        try:
                            playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                            d = random.choice(x)
                            f = random.choice(l)
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDEALER'S CARDS")
                            print("-------------    --------------")
                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |", dealer.k, "        |")
                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |    ", dealer.p, "     |")
                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |        ", dealer.k, "|")
                            print("-------------    --------------")
                            print("YOUR CARDS")
                            print("-------------    --------------    --------------")
                            print("|", h, "       |    |", w, "        |    |", d, "        |")
                            print("|           |    |            |    |            |")
                            print("|           |    |            |    |            |")
                            print("|   ", q, "     |    |    ", z, "     |    |    ", f, "     |")
                            print("|           |    |            |    |            |")
                            print("|           |    |            |    |            |")
                            print("|       ", h, "|    |        ", w, "|    |        ", d, "|")
                            print("-------------    --------------    --------------")
                            if d == x[9]:
                                while True:
                                    print("Dealer's Total:", dealer.dsum)
                                    print("Your Total:", dealer.psum)
                                    ak = int(input("Do you want 'A' to be 1 or 11? \n>"))
                                    if ak == 1:
                                        dealer.psum += 1
                                        break
                                    if ak == 11:
                                        dealer.psum += 11
                                        break
                                    else:
                                        print("Please enter correct value(1/11)")
                                        continue
                            if d == x[10]:
                                dealer.psum += 10
                            elif d == x[11]:
                                dealer.psum += 10
                            elif d == x[12]:
                                dealer.psum += 10
                            elif d != x[9] and d != x[10] and d != x[11] and d != x[12]:
                                koy = int(d)
                                dealer.psum += koy
                        except:
                            print("error")
                        finally:
                            print("Dealer's Total:", dealer.dsum)
                            print("Your Total:", dealer.psum)
                            if dealer.psum > 21:
                                dealer.tl += 1
                                c.execute("update players set total_games_lost='" + str(
                                    dealer.tl) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("DEALER WINS! BETTER LUCK NEXT TIME.")
                                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                                dealer.bet = dealer.bet / 2
                                bet.buyin += dealer.bet
                                c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("Current Balance: ", bet.buyin,"$")
                                while True:
                                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                    if ch == 'p':
                                        dealer()
                                        break
                                    if ch == 'e':
                                        bmenu()
                                    else:
                                        print("Enter a valid option(p/e)")
                                        continue
                            if dealer.psum == 21:
                                print("CONGRATULATIONS! YOU ARE BLACKJACK! DOUBLE MONEY!")
                                dealer.tw += 1
                                c.execute("update players set total_games_won='" + str(
                                    dealer.tw) + "' where username='" + str(config.usrnm) + "'")
                                db.commit()
                                playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                                dealer.bet = dealer.bet * 2
                                bet.buyin += dealer.bet
                                c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("Current Balance: ", bet.buyin,"$")
                                while True:
                                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                    if ch == 'p':
                                        dealer()
                                        break
                                    if ch == 'e':
                                        bmenu()
                                    else:
                                        print("Enter a valid option(p/e)")
                                        continue
                            if dealer.psum < 21:
                                while True:
                                    print("Dealer's Total:", dealer.dsum)
                                    print("Your Total:", dealer.psum)
                                    ask = input("press 'H' to hit or 'S' to stand \n> ")
                                    if ask == 's':
                                        player()
                                    if ask == 'h':
                                        try:
                                            playsound(
                                                "C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                                            print(
                                                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDEALER'S CARDS")
                                            print("-------------    --------------")
                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |", dealer.k, "        |")
                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |    ", dealer.p, "     |")
                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |        ", dealer.k, "|")
                                            print("-------------    --------------")
                                            hi = random.choice(x)
                                            qi = random.choice(l)
                                            print("YOUR CARDS")
                                            print("-------------    -------------    --------------    --------------")
                                            print("|", h, "       |    |", d, "       |    |", w, "        |    |", hi,"        |")
                                            print("|           |    |           |    |            |    |            |")
                                            print("|           |    |           |    |            |    |            |")
                                            print("|   ", q, "     |    |    ", f, "    |    |    ", z, "     |    |    ", qi,"     |")
                                            print("|           |    |           |    |            |    |            |")
                                            print("|           |    |           |    |            |    |            |")
                                            print("|       ", h, "|    |      ", d, " |    |        ", w, "|    |        ", hi,"|")
                                            print("-------------    -------------    --------------    --------------")
                                            if hi == x[9]:
                                                while True:
                                                    print("Dealer's Total:", dealer.dsum)
                                                    print("Your Total:", dealer.psum)
                                                    ak = int(input("Do you want 'A' to be 1 or 11? \n>"))
                                                    if ak == 1:
                                                        dealer.psum += 1
                                                        break
                                                    if ak == 11:
                                                        dealer.psum += 11
                                                        break
                                                    else:
                                                        print("Please enter correct value(1/11)")
                                                        continue
                                            if hi == x[10]:
                                                dealer.psum += 10
                                            elif hi == x[11]:
                                                dealer.psum += 10
                                            elif hi == x[12]:
                                                dealer.psum += 10
                                            elif hi != x[9] and hi != x[10] and hi != x[11] and hi != x[12]:
                                                koyil = int(hi)
                                                dealer.psum += koyil
                                            print("Dealer's Total:", dealer.dsum)
                                            print("Your Total:", dealer.psum)
                                        except:
                                            print("error")
                                        finally:
                                            if dealer.psum > 21:
                                                dealer.tl += 1
                                                c.execute("update players set total_games_lost='" + str(
                                                    dealer.tl) + "' where username='" + str(
                                                    config.usrnm) + "'")
                                                db.commit()
                                                print("DEALER WINS! BETTER LUCK NEXT TIME.")
                                                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                                                dealer.bet = dealer.bet / 2
                                                bet.buyin += dealer.bet
                                                c.execute("update players set balance='" + str(
                                                    bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                                                db.commit()
                                                print("Current Balance: ", bet.buyin,"$")
                                                while True:
                                                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                                    if ch == 'p':
                                                        dealer()
                                                        break
                                                    if ch == 'e':
                                                        bmenu()
                                                    else:
                                                        print("Enter a valid option(p/e)")
                                                        continue
                                            if dealer.psum == 21:
                                                print("CONGRATULATIONS! YOU ARE BLACKJACK! DOUBLE MONEY!")
                                                dealer.tw += 1
                                                c.execute("update players set total_games_won='" + str(
                                                    dealer.tw) + "' where username='" + str(config.usrnm) + "'")
                                                db.commit()
                                                playsound(
                                                    "C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                                                dealer.bet = dealer.bet * 2
                                                bet.buyin += dealer.bet
                                                c.execute("update players set balance='" + str(
                                                    bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                                                db.commit()
                                                print("Current Balance: ", bet.buyin,"$")
                                                while True:
                                                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                                    if ch == 'p':
                                                        dealer()
                                                        break
                                                    if ch == 'e':
                                                        bmenu()
                                                    else:
                                                        print("Enter a valid option(p/e)")
                                                        continue
                                            if dealer.psum < 21:
                                                while True:
                                                    print("Dealer's Total:", dealer.dsum)
                                                    print("Your Total:", dealer.psum)
                                                    ask = input("press 'H' to hit or 'S' to stand \n> ")
                                                    if ask == 's':
                                                        player()
                                                    if ask == 'h':
                                                        try:
                                                            playsound(
                                                                "C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                                                            print(
                                                                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDEALER'S CARDS")
                                                            print("-------------    --------------")
                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |", dealer.k, "        |")
                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |    ", dealer.p, "     |")
                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |        ", dealer.k, "|")
                                                            print("-------------    --------------")
                                                            di = random.choice(x)
                                                            fi = random.choice(l)
                                                            print("YOUR CARDS")
                                                            print("-------------    -------------    -------------    --------------    --------------")
                                                            print("|", h, "       |    |", d, "       |    |", hi, "       |    |",w, "        |    |", di, "        |")
                                                            print("|           |    |           |    |           |    |            |    |            |")
                                                            print("|           |    |           |    |           |    |            |    |            |")
                                                            print("|   ", q, "     |    |   ", f, "     |    |    ", qi,"    |    |    ", z, "     |    |    ", fi, "     |")
                                                            print("|           |    |           |    |           |    |            |    |            |")
                                                            print("|           |    |           |    |           |    |            |    |            |")
                                                            print("|       ", h, "|    |       ", d, "|    |      ", hi," |    |        ", w, "|    |        ", di, "|")
                                                            print("-------------    -------------    -------------    --------------    --------------")
                                                            if di == x[9]:
                                                                while True:
                                                                    print("Dealer's Total:", dealer.dsum)
                                                                    print("Your Total:", dealer.psum)
                                                                    ak = int(input("Do you want 'A' to be 1 or 11? \n>"))
                                                                    if ak == 1:
                                                                        dealer.psum += 1
                                                                        break
                                                                    if ak == 11:
                                                                        dealer.psum += 11
                                                                        break
                                                                    else:
                                                                        print("Please enter correct value(1/11)")
                                                                        continue
                                                            if di == x[10]:
                                                                dealer.psum += 10
                                                            elif di == x[11]:
                                                                dealer.psum += 10
                                                            elif di == x[12]:
                                                                dealer.psum += 10
                                                            elif di != x[9] and di != x[10] and di != x[11] and di != x[12]:
                                                                koyid = int(di)
                                                                dealer.psum += koyid
                                                        except:
                                                            print("error")
                                                        finally:
                                                            print("Dealer's Total:", dealer.dsum)
                                                            print("Your Total:", dealer.psum)
                                                            if dealer.psum > 21:
                                                                dealer.tl += 1
                                                                c.execute("update players set total_games_lost='" + str(
                                                                    dealer.tl) + "' where username='" + str(
                                                                    config.usrnm) + "'")
                                                                db.commit()
                                                                print("DEALER WINS! BETTER LUCK NEXT TIME.")
                                                                playsound(
                                                                    "C:\\Users\dh1011tu\Downloads\mixkit-sad-game-over-trombone-471 (mp3cut.net).wav")
                                                                dealer.bet = dealer.bet / 2
                                                                bet.buyin += dealer.bet
                                                                c.execute("update players set balance='" + str(
                                                                    bet.buyin) + "' where username='" + str(
                                                                    config.usrnm) + "'")
                                                                db.commit()
                                                                print("Current Balance: ", bet.buyin,"$")
                                                                while True:
                                                                    ch = input(
                                                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                                                    if ch == 'p':
                                                                        dealer()
                                                                        break
                                                                    if ch == 'e':
                                                                        bmenu()
                                                                    else:
                                                                        print("Enter a valid option(p/e)")
                                                                        continue
                                                            if dealer.psum == 21:
                                                                print("CONGRATULATIONS! YOU ARE BLACKJACK! DOUBLE MONEY!")
                                                                dealer.tw += 1
                                                                c.execute("update players set total_games_won='" + str(
                                                                    dealer.tw) + "' where username='" + str(
                                                                    config.usrnm) + "'")
                                                                db.commit()
                                                                playsound(
                                                                    "C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                                                                dealer.bet = dealer.bet * 2
                                                                bet.buyin += dealer.bet
                                                                c.execute("update players set balance='" + str(
                                                                    bet.buyin) + "' where username='" + str(
                                                                    config.usrnm) + "'")
                                                                db.commit()
                                                                print("Current Balance: ", bet.buyin,"$")
                                                                while True:
                                                                    ch = input(
                                                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                                                    if ch == 'p':
                                                                        dealer()
                                                                        break
                                                                    if ch == 'e':
                                                                        bmenu()
                                                                    else:
                                                                        print("Enter a valid option(p/e)")
                                                                        continue
                                                            if dealer.psum < 21:
                                                                while True:
                                                                    print("Dealer's Total:", dealer.dsum)
                                                                    print("Your Total:", dealer.psum)
                                                                    ask = input("press 'H' to hit or 'S' to stand \n> ")
                                                                    if ask == 's':
                                                                        player()
                                                                    if ask == 'h':
                                                                        try:
                                                                            playsound(
                                                                                "C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                                                                            print(
                                                                                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDEALER'S CARDS")
                                                                            print("-------------    --------------")
                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |", dealer.k, "        |")
                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |    ", dealer.p, "     |")
                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |        ", dealer.k, "|")
                                                                            print("-------------    --------------")
                                                                            dit = random.choice(x)
                                                                            fit = random.choice(l)
                                                                            print("YOUR CARDS")
                                                                            print(
                                                                                "-------------    -------------    -------------    -------------    --------------    --------------")
                                                                            print("|", h, "       |    |", hi, "       |    |", di,
                                                                                  "       |    |", d, "       |    |", w,
                                                                                  "        |    |", dit, "        |")
                                                                            print(
                                                                                "|           |    |           |    |           |    |           |    |            |    |            |")
                                                                            print(
                                                                                "|           |    |           |    |           |    |           |    |            |    |            |")
                                                                            print("|   ", q, "     |    |   ", qi, "     |    |   ", fi,
                                                                                  "     |    |    ", f, "    |    |    ", z,
                                                                                  "     |    |    ", fit, "     |")
                                                                            print(
                                                                                "|           |    |           |    |           |    |           |    |            |    |            |")
                                                                            print(
                                                                                "|           |    |           |    |           |    |           |    |            |    |            |")
                                                                            print("|       ", h, "|    |       ", hi, "|    |       ",
                                                                                  di, "|    |      ", d, "|    |        ", w,
                                                                                  "|    |        ", dit, "|")
                                                                            print(
                                                                                "-------------    -------------    -------------    -------------    --------------    --------------")
                                                                            if dit == x[9]:
                                                                                while True:
                                                                                    print("Dealer's Total:", dealer.dsum)
                                                                                    print("Your Total:", dealer.psum)
                                                                                    ak = int(
                                                                                        input("Do you want 'A' to be 1 or 11? \n>"))
                                                                                    if ak == 1:
                                                                                        dealer.psum += 1
                                                                                        break
                                                                                    if ak == 11:
                                                                                        dealer.psum += 11
                                                                                        break
                                                                                    else:
                                                                                        print("Please enter correct value(1/11)")
                                                                                        continue
                                                                            if dit == x[10]:
                                                                                dealer.psum += 10
                                                                            elif dit == x[11]:
                                                                                dealer.psum += 10
                                                                            elif dit == x[12]:
                                                                                dealer.psum += 10
                                                                            elif dit != x[9] and dit != x[10] and dit != x[
                                                                                11] and dit != x[12]:
                                                                                koyidt = int(dit)
                                                                                dealer.psum += koyidt
                                                                        except:
                                                                            print("error")
                                                                        finally:
                                                                            print("Dealer's Total:", dealer.dsum)
                                                                            print("Your Total:", dealer.psum)
                                                                            if dealer.psum > 21:
                                                                                dealer.tl += 1
                                                                                c.execute(
                                                                                    "update players set total_games_lost='" + str(
                                                                                        dealer.tl) + "' where username='" + str(
                                                                                        config.usrnm) + "'")
                                                                                db.commit()
                                                                                print("DEALER WINS! BETTER LUCK NEXT TIME.")
                                                                                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                                                                                dealer.bet = dealer.bet / 2
                                                                                bet.buyin += dealer.bet
                                                                                c.execute(
                                                                                    "update players set balance='" + str(
                                                                                        bet.buyin) + "' where username='" + str(
                                                                                        config.usrnm) + "'")
                                                                                db.commit()
                                                                                print("Current Balance: ", bet.buyin,"$")
                                                                                while True:
                                                                                    ch = input(
                                                                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                                                                    if ch == 'p':
                                                                                        dealer()
                                                                                        break
                                                                                    if ch == 'e':
                                                                                        bmenu()
                                                                                    else:
                                                                                        print("Enter a valid option(p/e)")
                                                                                        continue
                                                                            if dealer.psum == 21:
                                                                                print(
                                                                                    "CONGRATULATIONS! YOU ARE BLACKJACK! DOUBLE MONEY!")
                                                                                dealer.tw += 1
                                                                                c.execute(
                                                                                    "update players set total_games_won='" + str(
                                                                                        dealer.tw) + "' where username='" + str(
                                                                                        config.usrnm) + "'")
                                                                                db.commit()
                                                                                playsound(
                                                                                    "C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                                                                                dealer.bet = dealer.bet * 2
                                                                                bet.buyin += dealer.bet
                                                                                c.execute(
                                                                                    "update players set balance='" + str(
                                                                                        bet.buyin) + "' where username='" + str(
                                                                                        config.usrnm) + "'")
                                                                                db.commit()
                                                                                print("Current Balance: ", bet.buyin,"$")
                                                                                while True:
                                                                                    ch = input(
                                                                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                                                                    if ch == 'p':
                                                                                        dealer()
                                                                                        break
                                                                                    if ch == 'e':
                                                                                        bmenu()
                                                                                    else:
                                                                                        print("Enter a valid option(p/e)")
                                                                                        continue
                                                                            if dealer.psum < 21:
                                                                                while True:
                                                                                    print("Dealer's Total:",
                                                                                          dealer.dsum)
                                                                                    print("Your Total:", dealer.psum)
                                                                                    ask = input("press 'H' to hit or 'S' to stand \n> ")
                                                                                    if ask == 's':
                                                                                        player()
                                                                                    if ask == 'h':
                                                                                        try:
                                                                                            playsound(
                                                                                                "C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                                                                                            print(
                                                                                                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDEALER'S CARDS")
                                                                                            print("-------------    --------------")
                                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |", dealer.k,
                                                                                                  "        |")
                                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |    ", dealer.p,
                                                                                                  "     |")
                                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |            |")
                                                                                            print("|⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉⛉|    |        ", dealer.k,
                                                                                                  "|")
                                                                                            print("-------------    --------------")
                                                                                            kit = random.choice(x)
                                                                                            lit = random.choice(l)
                                                                                            print("YOUR CARDS")
                                                                                            print(
                                                                                                "-------------    -------------    -------------    -------------    -------------    --------------    --------------")
                                                                                            print("|", h, "       |    |", hi,
                                                                                                  "       |    |", di, "       |    |", d,
                                                                                                  "       |    |", dit, "       |    |", w,
                                                                                                  "        |    |", kit, "        |")
                                                                                            print(
                                                                                                "|           |    |           |    |           |    |           |    |           |    |            |    |            |")
                                                                                            print(
                                                                                                "|           |    |           |    |           |    |           |    |           |    |            |    |            |")
                                                                                            print("|   ", q, "     |    |   ", qi,
                                                                                                  "     |    |   ", fi, "     |    |   ", f,
                                                                                                  "     |    |    ", fit, "    |    |    ",
                                                                                                  z, "     |    |    ", lit, "     |")
                                                                                            print(
                                                                                                "|           |    |           |    |           |    |           |    |           |    |            |    |            |")
                                                                                            print(
                                                                                                "|           |    |           |    |           |    |           |    |           |    |            |    |            |")
                                                                                            print("|       ", h, "|    |       ", hi,
                                                                                                  "|    |       ", di, "|    |       ", d,
                                                                                                  "|    |      ", dit, "|    |        ", w,
                                                                                                  "|    |        ", kit, "|")
                                                                                            print(
                                                                                                "-------------    -------------    -------------    -------------    -------------    --------------    --------------")
                                                                                            if dit == x[9]:
                                                                                                while True:
                                                                                                    print("Dealer's Total:", dealer.dsum)
                                                                                                    print("Your Total:", dealer.psum)
                                                                                                    ak = int(input(
                                                                                                        "Do you want 'A' to be 1 or 11? \n>"))
                                                                                                    if ak == 1:
                                                                                                        dealer.psum += 1
                                                                                                        break
                                                                                                    if ak == 11:
                                                                                                        dealer.psum += 11
                                                                                                        break
                                                                                                    else:
                                                                                                        print(
                                                                                                            "Please enter correct value(1/11)")
                                                                                                        continue
                                                                                            if kit == x[10]:
                                                                                                dealer.psum += 10
                                                                                            elif kit == x[11]:
                                                                                                dealer.psum += 10
                                                                                            elif kit == x[12]:
                                                                                                dealer.psum += 10
                                                                                            elif kit != x[9] and kit != x[10] and kit != x[
                                                                                                11] and kit != x[12]:
                                                                                                koyidtk = int(kit)
                                                                                                dealer.psum += koyidtk
                                                                                        except:
                                                                                            print("error")
                                                                                        finally:
                                                                                            print("Dealer's Total:", dealer.dsum)
                                                                                            print("Your Total:", dealer.psum)
                                                                                            if dealer.psum > 21:
                                                                                                dealer.tl += 1
                                                                                                c.execute(
                                                                                                    "update players set total_games_lost='" + str(
                                                                                                        dealer.tl) + "' where username='" + str(
                                                                                                        config.usrnm) + "'")
                                                                                                db.commit()
                                                                                                print("DEALER WINS! BETTER LUCK NEXT TIME.")
                                                                                                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                                                                                                dealer.bet = dealer.bet / 2
                                                                                                bet.buyin += dealer.bet
                                                                                                c.execute(
                                                                                                    "update players set balance='" + str(
                                                                                                        bet.buyin) + "' where username='" + str(
                                                                                                        config.usrnm) + "'")
                                                                                                db.commit()
                                                                                                print("Current Balance: ", bet.buyin,"$")
                                                                                                while True:
                                                                                                    ch = input(
                                                                                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                                                                                    if ch == 'p':
                                                                                                        dealer()
                                                                                                        break
                                                                                                    if ch == 'e':
                                                                                                        bmenu()
                                                                                                    else:
                                                                                                        print("Enter a valid option(p/e)")
                                                                                                        continue
                                                                                            if dealer.psum == 21:
                                                                                                print(
                                                                                                    "CONGRATULATIONS! YOU ARE BLACKJACK! DOUBLE MONEY!")
                                                                                                dealer.tw += 1
                                                                                                c.execute(
                                                                                                    "update players set total_games_won='" + str(
                                                                                                        dealer.tw) + "' where username='" + str(
                                                                                                        config.usrnm) + "'")
                                                                                                db.commit()
                                                                                                playsound(
                                                                                                    "C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                                                                                                dealer.bet = dealer.bet * 2
                                                                                                bet.buyin += dealer.bet
                                                                                                c.execute(
                                                                                                    "update players set balance='" + str(
                                                                                                        bet.buyin) + "' where username='" + str(
                                                                                                        config.usrnm) + "'")
                                                                                                db.commit()

                                                                                                print("Current Balance: ", bet.buyin,"$")
                                                                                                while True:
                                                                                                    ch = input(
                                                                                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                                                                                    if ch == 'p':
                                                                                                        dealer()
                                                                                                        break
                                                                                                    if ch == 'e':
                                                                                                        bmenu()
                                                                                                    else:
                                                                                                        print("Enter a valid option(p/e)")
                                                                                                        continue
                                                                                            else:
                                                                                                player()
                                                                                    if ask != 's' and ask != 'h':
                                                                                        print(
                                                                                            "please enter a valid input(H/S)")
                                                                                        continue
                                                                    if ask != 's' and ask != 'h':
                                                                        print("please enter a valid input(H/S)")
                                                                        continue
                                                    if ask != 's' and ask != 'h':
                                                        print("please enter a valid input(H/S)")
                                                        continue
                                    if ask != 's' and ask != 'h':
                                        print("please enter a valid input(H/S)")
                                        continue
                    if ask!='s' and ask!='h':
                        print("please enter a valid input(H/S)")
                        continue


def player():
    o = random.choice(x)
    n = random.choice(l)
    u = random.choice(x)
    e = random.choice(l)
    if dealer.dsum < 17:
        print("DEALER'S CARDS")
        playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
        print("-------------    --------------")
        print("|", o, "       |    |", dealer.k, "        |")
        print("|           |    |            |")
        print("|           |    |            |")
        print("|   ", n, "     |    |    ", dealer.p, "     |")
        print("|           |    |            |")
        print("|           |    |            |")
        print("|       ", o, "|    |        ", dealer.k, "|")
        print("-------------    -------------- ")
        if o == x[9]:
            if dealer.dsum <= 10:
                dealer.dsum += 11
            if dealer.dsum > 10:
                dealer.dsum += 1
        elif o == x[10]:
            dealer.dsum += 10
        elif o == x[11]:
            dealer.dsum += 10
        elif o == x[12]:
            dealer.dsum += 10
        elif o != x[9] and o != x[10] and o != x[11] and o != x[12]:
            kok = int(o)
            dealer.dsum += kok
        if dealer.dsum > 21:
            print("Dealer's total: ", dealer.dsum)
            print("Your total: ", dealer.psum)
            print("CONGRATULATIONS! YOU WIN")
            dealer.tw += 1
            c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                config.usrnm) + "'")
            db.commit()
            playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
            dealer.bet = dealer.bet * 1.5
            bet.buyin += dealer.bet
            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
            db.commit()
            print("Current Balance: ", bet.buyin,"$")
            while True:
                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                if ch == 'p':
                    dealer()
                    break
                if ch == 'e':
                    bmenu()
                else:
                    print("Enter a valid option(p/e)")
                    continue
        if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum > 21:
            print("Dealer's total: ", dealer.dsum)
            print("Your total: ", dealer.psum)
            print("CONGRATULATIONS! YOU WIN")
            dealer.tw += 1
            c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                config.usrnm) + "'")
            db.commit()
            playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
            dealer.bet = dealer.bet * 1.5
            bet.buyin += dealer.bet
            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
            db.commit()
            print("Current Balance: ", bet.buyin,"$")
            while True:
                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                if ch == 'p':
                    dealer()
                    break
                if ch == 'e':
                    bmenu()
                else:
                    print("Enter a valid option(p/e)")
                    continue
        if dealer.dsum == 21:
            dealer.tl += 1
            c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                config.usrnm) + "'")
            db.commit()
            print("Dealer's total: ", dealer.dsum)
            print("Your total: ", dealer.psum)
            print("DEALER WINS! BETTER LUCK NEXT TIME")
            playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
            dealer.bet = dealer.bet / 2
            bet.buyin += dealer.bet
            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
            db.commit()
            print("Current Balance: ", bet.buyin,"$")
            while True:
                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                if ch == 'p':
                    dealer()
                    break
                if ch == 'e':
                    bmenu()
                else:
                    print("Enter a valid option(p/e)")
                    continue
        if dealer.dsum == dealer.psum:
            print("Dealer's total: ", dealer.dsum)
            print("Your total: ", dealer.psum)
            print("IT'S A PUSH, NO ONE WINS.")
            dealer.tp += 1
            c.execute("update players set total_games_played_and_draws='" + str(dealer.tp) + "' where username='" + str(
                config.usrnm) + "'")
            db.commit()
            playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-retro-game-over-1947 (mp3cut.net).wav")
            bet.buyin += dealer.bet
            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
            db.commit()
            print("Current Balance: ", bet.buyin,"$")
            while True:
                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                if ch == 'p':
                    dealer()
                    break
                if ch == 'e':
                    bmenu()
                else:
                    print("Enter a valid option(p/e)")
                    continue
        if dealer.dsum > dealer.psum and dealer.dsum >= 17 and dealer.dsum <= 21:
            print("Dealer's total: ", dealer.dsum)
            print("Your total: ", dealer.psum)
            print("DEALER WINS! BETTER LUCK NEXT TIME.")
            dealer.tl += 1
            c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                config.usrnm) + "'")
            db.commit()
            playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
            dealer.bet = dealer.bet / 2
            bet.buyin += dealer.bet
            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
            db.commit()
            print("Current Balance: ", bet.buyin,"$")
            while True:
                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                if ch == 'p':
                    dealer()
                    break
                if ch == 'e':
                    bmenu()
                else:
                    print("Enter a valid option(p/e)")
                    continue
        if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum < 21:
            print("Dealer's total: ", dealer.dsum)
            print("Your total: ", dealer.psum)
            print("CONGRATULATIONS! YOU WIN")
            dealer.tw += 1
            c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                config.usrnm) + "'")
            db.commit()
            playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
            dealer.bet = dealer.bet * 1.5
            bet.buyin += dealer.bet
            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
            db.commit()
            print("Current Balance: ", bet.buyin,"$")
            while True:
                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                if ch == 'p':
                    dealer()
                    break
                if ch == 'e':
                    bmenu()
                else:
                    print("Enter a valid option(p/e)")
                    continue
        if dealer.dsum < 17:
            print("DEALER DRAWS A CARD")
            playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
            print("-------------    --------------    --------------")
            print("|", o, "       |    |", dealer.k, "        |    |", u, "        |")
            print("|           |    |            |    |            |")
            print("|           |    |            |    |            |")
            print("|   ", n, "     |    |    ", dealer.p, "     |    |    ", e, "     |")
            print("|           |    |            |    |            |")
            print("|           |    |            |    |            |")
            print("|       ", o, "|    |        ", dealer.k, "|    |        ", u, "|")
            print("-------------    --------------    --------------")
            if u == x[9]:
                if dealer.dsum <= 10:
                    dealer.dsum += 11
                if dealer.dsum > 10:
                    dealer.dsum += 1
            elif u == x[10]:
                dealer.dsum += 10
            elif u == x[11]:
                dealer.dsum += 10
            elif u == x[12]:
                dealer.dsum += 10
            elif u != x[9] and u != x[10] and u != x[11] and u != x[12]:
                koc = int(u)
                dealer.dsum += koc
            if dealer.dsum > 21:
                print("Dealer's total: ", dealer.dsum)
                print("Your total: ", dealer.psum)
                print("CONGRATULATIONS! YOU WIN")
                dealer.tw += 1
                c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                    config.usrnm) + "'")
                db.commit()
                playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                dealer.bet = dealer.bet * 1.5
                bet.buyin += dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                print("Current Balance: ", bet.buyin,"$")
                while True:
                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                    if ch == 'p':
                        dealer()
                        break
                    if ch == 'e':
                        bmenu()
                    else:
                        print("Enter a valid option(p/e)")
                        continue
            if dealer.dsum == 21:
                dealer.tl += 1
                c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                    config.usrnm) + "'")
                db.commit()
                print("Dealer's total: ", dealer.dsum)
                print("Your total: ", dealer.psum)
                print("DEALER WINS! BETTER LUCK NEXT TIME")
                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                dealer.bet = dealer.bet / 2
                bet.buyin += dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                print("Current Balance: ", bet.buyin,"$")
                while True:
                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                    if ch == 'p':
                        dealer()
                        break
                    if ch == 'e':
                        bmenu()
                    else:
                        print("Enter a valid option(p/e)")
                        continue
            if dealer.dsum == dealer.psum:
                print("Dealer's total: ", dealer.dsum)
                print("Your total: ", dealer.psum)
                print("IT'S A PUSH, NO ONE WINS.")
                dealer.tp += 1
                c.execute("update players set total_games_played_and_draws='" + str(dealer.tp) + "' where username='" + str(
                    config.usrnm) + "'")
                db.commit()
                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-retro-game-over-1947 (mp3cut.net).wav")
                bet.buyin += dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                print("Current Balance: ", bet.buyin,"$")
                while True:
                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                    if ch == 'p':
                        dealer()
                        break
                    if ch == 'e':
                        bmenu()
                    else:
                        print("Enter a valid option(p/e)")
                        continue
            if dealer.dsum > dealer.psum and dealer.dsum >= 17 and dealer.dsum <= 21:
                print("Dealer's total: ", dealer.dsum)
                print("Your total: ", dealer.psum)
                print("DEALER WINS! BETTER LUCK NEXT TIME.")
                dealer.tl += 1
                c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                    config.usrnm) + "'")
                db.commit()
                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                dealer.bet = dealer.bet / 2
                bet.buyin += dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                print("Current Balance: ", bet.buyin,"$")
                while True:
                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                    if ch == 'p':
                        dealer()
                        break
                    if ch == 'e':
                        bmenu()
                    else:
                        print("Enter a valid option(p/e)")
                        continue
            if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum < 21:
                print("Dealer's total: ", dealer.dsum)
                print("Your total: ", dealer.psum)
                print("CONGRATULATIONS! YOU WIN")
                dealer.tw += 1
                c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                    config.usrnm) + "'")
                db.commit()
                playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                dealer.bet = dealer.bet * 1.5
                bet.buyin += dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                print("Current Balance: ", bet.buyin,"$")
                while True:
                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                    if ch == 'p':
                        dealer()
                        break
                    if ch == 'e':
                        bmenu()
                    else:
                        print("Enter a valid option(p/e)")
                        continue
            if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum > 21:
                print("Dealer's total: ", dealer.dsum)
                print("Your total: ", dealer.psum)
                print("CONGRATULATIONS! YOU WIN")
                dealer.tw += 1
                c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                    config.usrnm) + "'")
                db.commit()
                playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                dealer.bet = dealer.bet * 1.5
                bet.buyin += dealer.bet
                c.execute(
                    "update players set balance='" + str(bet.buyin) + "' where username='" + str(config.usrnm) + "'")
                db.commit()
                print("Current Balance: ", bet.buyin,"$")
                while True:
                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                    if ch == 'p':
                        dealer()
                        break
                    if ch == 'e':
                        bmenu()
                    else:
                        print("Enter a valid option(p/e)")
                        continue
            if dealer.dsum < 17:
                du = random.choice(x)
                eu = random.choice(l)
                print("DEALER DRAWS ANOTHER CARD")
                playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                print("-------------    -------------    --------------    --------------")
                print("|", o, "       |    |", dealer.k, "       |    |", u, "        |    |", du, "        |")
                print("|           |    |           |    |            |    |            |")
                print("|           |    |           |    |            |    |            |")
                print("|   ", n, "     |    |    ", dealer.p, "    |    |    ", e, "     |    |    ", eu, "     |")
                print("|           |    |           |    |            |    |            |")
                print("|           |    |           |    |            |    |            |")
                print("|       ", o, "|    |      ", dealer.k, " |    |        ", u, "|    |        ", du, "|")
                print("-------------    -------------    --------------    --------------")
                if du == x[9]:
                    if dealer.dsum <= 10:
                        dealer.dsum += 11
                    if dealer.dsum > 10:
                        dealer.dsum += 1
                elif du == x[10]:
                    dealer.dsum += 10
                elif du == x[11]:
                    dealer.dsum += 10
                elif du == x[12]:
                    dealer.dsum += 10
                elif du != x[9] and du != x[10] and du != x[11] and du != x[12]:
                    kocu = int(du)
                    dealer.dsum += kocu
                if dealer.dsum > 21:
                    print("Dealer's total: ", dealer.dsum)
                    print("Your total: ", dealer.psum)
                    print("CONGRATULATIONS! YOU WIN")
                    dealer.tw += 1
                    c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                    dealer.bet = dealer.bet * 1.5
                    bet.buyin += dealer.bet
                    c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    print("Current Balance: ", bet.buyin,"$")
                    while True:
                        ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                        if ch == 'p':
                            dealer()
                            break
                        if ch == 'e':
                            bmenu()
                        else:
                            print("Enter a valid option(p/e)")
                            continue
                if dealer.dsum > 21:
                    print("Dealer's total: ", dealer.dsum)
                    print("Your total: ", dealer.psum)
                    print("CONGRATULATIONS! YOU WIN")
                    dealer.tw += 1
                    c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                    dealer.bet = dealer.bet * 1.5
                    bet.buyin += dealer.bet
                    c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    print("Current Balance: ", bet.buyin,"$")
                    while True:
                        ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                        if ch == 'p':
                            dealer()
                            break
                        if ch == 'e':
                            bmenu()
                        else:
                            print("Enter a valid option(p/e)")
                            continue
                if dealer.dsum == 21:
                    dealer.tl += 1
                    c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    print("Dealer's total: ", dealer.dsum)
                    print("Your total: ", dealer.psum)
                    print("DEALER WINS! BETTER LUCK NEXT TIME")
                    playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                    dealer.bet = dealer.bet / 2
                    bet.buyin += dealer.bet
                    c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    print("Current Balance: ", bet.buyin,"$")
                    while True:
                        ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                        if ch == 'p':
                            dealer()
                            break
                        if ch == 'e':
                            bmenu()
                        else:
                            print("Enter a valid option(p/e)")
                            continue
                if dealer.dsum == dealer.psum:
                    print("Dealer's total: ", dealer.dsum)
                    print("Your total: ", dealer.psum)
                    print("IT'S A PUSH, NO ONE WINS.")
                    dealer.tp += 1
                    c.execute("update players set total_games_played_and_draws='" + str(dealer.tp) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-retro-game-over-1947 (mp3cut.net).wav")
                    bet.buyin += dealer.bet
                    c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    print("Current Balance: ", bet.buyin,"$")
                    while True:
                        ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                        if ch == 'p':
                            dealer()
                            break
                        if ch == 'e':
                            bmenu()
                        else:
                            print("Enter a valid option(p/e)")
                            continue
                if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum > 21:
                    print("Dealer's total: ", dealer.dsum)
                    print("Your total: ", dealer.psum)
                    print("CONGRATULATIONS! YOU WIN")
                    dealer.tw += 1
                    c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(config.usrnm) + "'")
                    db.commit()
                    playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                    dealer.bet = dealer.bet * 1.5
                    bet.buyin += dealer.bet
                    c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    print("Current Balance: ", bet.buyin,"$")
                    while True:
                        ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                        if ch == 'p':
                            dealer()
                            break
                        if ch == 'e':
                            bmenu()
                        else:
                            print("Enter a valid option(p/e)")
                            continue
                if dealer.dsum > dealer.psum and dealer.dsum >= 17 and dealer.dsum <= 21:
                    print("Dealer's total: ", dealer.dsum)
                    print("Your total: ", dealer.psum)
                    print("DEALER WINS! BETTER LUCK NEXT TIME.")
                    dealer.tl += 1
                    c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                    dealer.bet = dealer.bet / 2
                    bet.buyin += dealer.bet
                    c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    print("Current Balance: ", bet.buyin,"$")
                    while True:
                        ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                        if ch == 'p':
                            dealer()
                            break
                        if ch == 'e':
                            bmenu()
                        else:
                            print("Enter a valid option(p/e)")
                            continue
                if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum < 21:
                    print("Dealer's total: ", dealer.dsum)
                    print("Your total: ", dealer.psum)
                    print("CONGRATULATIONS! YOU WIN")
                    dealer.tw += 1
                    c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                    dealer.bet = dealer.bet * 1.5
                    bet.buyin += dealer.bet
                    c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                        config.usrnm) + "'")
                    db.commit()
                    print("Current Balance: ", bet.buyin,"$")
                    while True:
                        ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                        if ch == 'p':
                            dealer()
                            break
                        if ch == 'e':
                            bmenu()
                        else:
                            print("Enter a valid option(p/e)")
                            continue
                if dealer.dsum < 17:
                    dud = random.choice(x)
                    fu = random.choice(l)
                    print("DEALER DRAWS A CARD AGAIN")
                    playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                    print("-------------    -------------    -------------    --------------    --------------")
                    print("|", o, "       |    |", dealer.k, "       |    |", u, "       |    |", du, "        |    |",dud, "        |")
                    print("|           |    |           |    |           |    |            |    |            |")
                    print("|           |    |           |    |           |    |            |    |            |")
                    print("|   ", n, "     |    |   ", dealer.p, "     |    |    ", e, "    |    |    ", eu,"     |    |    ", fu, "     |")
                    print("|           |    |           |    |           |    |            |    |            |")
                    print("|           |    |           |    |           |    |            |    |            |")
                    print("|       ", o, "|    |       ", dealer.k, "|    |      ", u, " |    |        ", du,"|    |        ", dud, "|")
                    print("-------------    -------------    -------------    --------------    --------------")
                    if dud == x[9]:
                        if dealer.dsum <= 10:
                            dealer.dsum += 11
                        if dealer.dsum > 10:
                            dealer.dsum += 1
                    elif dud == x[10]:
                        dealer.dsum += 10
                    elif dud == x[11]:
                        dealer.dsum += 10
                    elif dud == x[12]:
                        dealer.dsum += 10
                    elif dud != x[9] and dud != x[10] and dud != x[11] and dud != x[12]:
                        kocud = int(dud)
                        dealer.dsum += kocud
                    if dealer.dsum > 21:
                        print("Dealer's total: ", dealer.dsum)
                        print("Your total: ", dealer.psum)
                        print("CONGRATULATIONS! YOU WIN")
                        dealer.tw += 1
                        c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                        dealer.bet = dealer.bet * 1.5
                        bet.buyin += dealer.bet
                        c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        print("Current Balance: ", bet.buyin,"$")
                        while True:
                            ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                            if ch == 'p':
                                dealer()
                                break
                            if ch == 'e':
                                bmenu()
                            else:
                                print("Enter a valid option(p/e)")
                                continue
                    if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum > 21:
                        print("Dealer's total: ", dealer.dsum)
                        print("Your total: ", dealer.psum)
                        print("CONGRATULATIONS! YOU WIN")
                        dealer.tw += 1
                        c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                        dealer.bet = dealer.bet * 1.5
                        bet.buyin += dealer.bet
                        c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        print("Current Balance: ", bet.buyin,"$")
                        while True:
                            ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                            if ch == 'p':
                                dealer()
                                break
                            if ch == 'e':
                                bmenu()
                            else:
                                print("Enter a valid option(p/e)")
                                continue
                    if dealer.dsum == 21:
                        print("Dealer's total: ", dealer.dsum)
                        print("Your total: ", dealer.psum)
                        print("DEALER WINS! BETTER LUCK NEXT TIME")
                        dealer.tl += 1
                        c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                        dealer.bet = dealer.bet / 2
                        bet.buyin += dealer.bet
                        c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        print("Current Balance: ", bet.buyin,"$")
                        while True:
                            ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                            if ch == 'p':
                                dealer()
                                break
                            if ch == 'e':
                                bmenu()
                            else:
                                print("Enter a valid option(p/e)")
                                continue
                    if dealer.dsum == dealer.psum:
                        print("Dealer's total: ", dealer.dsum)
                        print("Your total: ", dealer.psum)
                        print("IT'S A PUSH, NO ONE WINS.")
                        dealer.tp += 1
                        c.execute("update players set total_games_played_and_draws='" + str(
                            dealer.tp) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-retro-game-over-1947 (mp3cut.net).wav")
                        bet.buyin += dealer.bet
                        c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        print("Current Balance: ", bet.buyin,"$")
                        while True:
                            ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                            if ch == 'p':
                                dealer()
                                break
                            if ch == 'e':
                                bmenu()
                            else:
                                print("Enter a valid option(p/e)")
                                continue
                    if dealer.dsum > dealer.psum and dealer.dsum >= 17 and dealer.dsum <= 21:
                        print("Dealer's total: ", dealer.dsum)
                        print("Your total: ", dealer.psum)
                        print("DEALER WINS! BETTER LUCK NEXT TIME.")
                        dealer.tl += 1
                        c.execute("update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(config.usrnm) + "'")
                        db.commit()
                        playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                        dealer.bet = dealer.bet / 2
                        bet.buyin += dealer.bet
                        c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        print("Current Balance: ", bet.buyin,"$")
                        while True:
                            ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                            if ch == 'p':
                                dealer()
                                break
                            if ch == 'e':
                                bmenu()
                            else:
                                print("Enter a valid option(p/e)")
                                continue
                    if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum < 21:
                        print("Dealer's total: ", dealer.dsum)
                        print("Your total: ", dealer.psum)
                        print("CONGRATULATIONS! YOU WIN")
                        dealer.tw += 1
                        c.execute("update players set total_games_won='" + str(dealer.tw) + "' where username='" + str(config.usrnm) + "'")
                        db.commit()
                        playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                        dealer.bet = dealer.bet * 1.5
                        bet.buyin += dealer.bet
                        c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                            config.usrnm) + "'")
                        db.commit()
                        print("Current Balance: ", bet.buyin,"$")
                        while True:
                            ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                            if ch == 'p':
                                dealer()
                                break
                            if ch == 'e':
                                bmenu()
                            else:
                                print("Enter a valid option(p/e)")
                                continue
                    if dealer.dsum < 17:
                        dude = random.choice(x)
                        fud = random.choice(l)
                        print("ONE MORE CARD IS DRAWN BY THE DEALER")
                        playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                        print("-------------    -------------    -------------    -------------    --------------    --------------")
                        print("|", o, "       |    |", dealer.k, "       |    |", u, "       |    |", du,"       |    |", dud, "        |    |", dude, "        |")
                        print("|           |    |           |    |           |    |           |    |            |    |            |")
                        print("|           |    |           |    |           |    |           |    |            |    |            |")
                        print("|   ", n, "     |    |   ", dealer.p, "     |    |   ", e, "     |    |    ", eu,"    |    |    ", fu, "     |    |    ", fud, "     |")
                        print("|           |    |           |    |           |    |           |    |            |    |            |")
                        print("|           |    |           |    |           |    |           |    |            |    |            |")
                        print("|       ", o, "|    |       ", dealer.k, "|    |       ", u, "|    |      ", du," |    |        ", dud, "|    |        ", dude, "|")
                        print("-------------    -------------    -------------    -------------    --------------    --------------")
                        if dude == x[9]:
                            if dealer.dsum <= 10:
                                dealer.dsum += 11
                            if dealer.dsum > 10:
                                dealer.dsum += 1
                        elif dude == x[10]:
                            dealer.dsum += 10
                        elif dude == x[11]:
                            dealer.dsum += 10
                        elif dude == x[12]:
                            dealer.dsum += 10
                        elif dude != x[9] and dude != x[10] and dude != x[11] and dude != x[12]:
                            kocude = int(dude)
                            dealer.dsum += kocude
                        if dealer.dsum > 21:
                            print("Dealer's total: ", dealer.dsum)
                            print("Your total: ", dealer.psum)
                            print("CONGRATULATIONS! YOU WIN")
                            dealer.tw += 1
                            c.execute("update players set total_games_won='" + str(
                                dealer.tw) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                            dealer.bet = dealer.bet * 1.5
                            bet.buyin += dealer.bet
                            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            print("Current Balance: ", bet.buyin,"$")
                            while True:
                                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                if ch == 'p':
                                    dealer()
                                    break
                                if ch == 'e':
                                    bmenu()
                                else:
                                    print("Enter a valid option(p/e)")
                                    continue
                        if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum > 21:
                            print("Dealer's total: ", dealer.dsum)
                            print("Your total: ", dealer.psum)
                            print("CONGRATULATIONS! YOU WIN")
                            dealer.tw += 1
                            c.execute("update players set total_games_won='" + str(
                                dealer.tw) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                            dealer.bet = dealer.bet * 1.5
                            bet.buyin += dealer.bet
                            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            print("Current Balance: ", bet.buyin,"$")
                            while True:
                                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                if ch == 'p':
                                    dealer()
                                    break
                                if ch == 'e':
                                    bmenu()
                                else:
                                    print("Enter a valid option(p/e)")
                                    continue
                        if dealer.dsum == 21:
                            print("Dealer's total: ", dealer.dsum)
                            print("Your total: ", dealer.psum)
                            print("DEALER WINS! BETTER LUCK NEXT TIME")
                            dealer.tl += 1
                            c.execute(
                                "update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                                    config.usrnm) + "'")
                            db.commit()
                            playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                            dealer.bet = dealer.bet / 2
                            bet.buyin += dealer.bet
                            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            print("Current Balance: ", bet.buyin,"$")
                            while True:
                                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                if ch == 'p':
                                    dealer()
                                    break
                                if ch == 'e':
                                    bmenu()
                                else:
                                    print("Enter a valid option(p/e)")
                                    continue
                        if dealer.dsum == dealer.psum:
                            print("Dealer's total: ", dealer.dsum)
                            print("Your total: ", dealer.psum)
                            print("IT'S A PUSH, NO ONE WINS.")
                            dealer.tp += 1
                            c.execute("update players set total_games_played_and_draws='" + str(
                                dealer.tp) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-retro-game-over-1947 (mp3cut.net).wav")
                            bet.buyin += dealer.bet
                            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            print("Current Balance: ", bet.buyin,"$")
                            while True:
                                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                if ch == 'p':
                                    dealer()
                                    break
                                if ch == 'e':
                                    bmenu()
                                else:
                                    print("Enter a valid option(p/e)")
                                    continue
                        if dealer.dsum > dealer.psum and dealer.dsum >= 17 and dealer.dsum <= 21:
                            print("Dealer's total: ", dealer.dsum)
                            print("Your total: ", dealer.psum)
                            print("DEALER WINS! BETTER LUCK NEXT TIME.")
                            dealer.tl += 1
                            c.execute(
                                "update players set total_games_lost='" + str(dealer.tl) + "' where username='" + str(
                                    config.usrnm) + "'")
                            db.commit()
                            playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                            dealer.bet = dealer.bet / 2
                            bet.buyin += dealer.bet
                            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            print("Current Balance: ", bet.buyin,"$")
                            while True:
                                ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                if ch == 'p':
                                    dealer()
                                    break
                                if ch == 'e':
                                    bmenu()
                                else:
                                    print("Enter a valid option(p/e)")
                                    continue
                        if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum < 21:
                            print("Dealer's total: ", dealer.dsum)
                            print("Your total: ", dealer.psum)
                            print("CONGRATULATIONS! YOU WIN")
                            dealer.tw += 1
                            c.execute("update players set total_games_won='" + str(
                                dealer.tw) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                            dealer.bet = dealer.bet * 1.5
                            bet.buyin += dealer.bet
                            c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                config.usrnm) + "'")
                            db.commit()
                            print("Current Balance: ", bet.buyin,"$")
                            while True:
                                ch = input(
                                    "press 'P' to play again or 'E' to go to the main menu \n>")
                                if ch == 'p':
                                    dealer()
                                    break
                                if ch == 'e':
                                    bmenu()
                                else:
                                    print("Enter a valid option(p/e)")
                                    continue
                        if dealer.dsum < 17:
                            due = random.choice(x)
                            fue = random.choice(l)
                            print("DEALER SWIPES ANOTHER CARD FROM THE DECK")
                            playsound("C:\\Users\\dh1011tu\\Downloads\\240777__f4ngy__dealing-card (mp3cut.net).wav")
                            print("-------------    -------------    -------------    -------------    -------------    --------------    --------------")
                            print("|", o, "       |    |", dealer.k, "       |    |", u, "       |    |", du,"       |    |", dud, "       |    |", dude, "        |    |", due, "        |")
                            print("|           |    |           |    |           |    |           |    |           |    |            |    |            |")
                            print("|           |    |           |    |           |    |           |    |           |    |            |    |            |")
                            print("|   ", n, "     |    |   ", dealer.p, "     |    |   ", e, "     |    |   ", eu,"     |    |    ", fu, "    |    |    ", fud, "     |    |    ", fue, "     |")
                            print("|           |    |           |    |           |    |           |    |           |    |            |    |            |")
                            print("|           |    |           |    |           |    |           |    |           |    |            |    |            |")
                            print("|       ", o, "|    |       ", dealer.k, "|    |       ", u, "|    |       ", du,"|    |      ", dud, "  |    |        ", dude, "|    |        ", due, "|")
                            print("-------------    -------------    -------------    -------------    -------------    --------------    --------------")
                            if due == x[9]:
                                if dealer.dsum <= 10:
                                    dealer.dsum += 11
                                if dealer.dsum > 10:
                                    dealer.dsum += 1
                            elif due == x[10]:
                                dealer.dsum += 10
                            elif due == x[11]:
                                dealer.dsum += 10
                            elif due == x[12]:
                                dealer.dsum += 10
                            elif due != x[9] and due != x[10] and due != x[11] and due != x[12]:
                                kocudet = int(due)
                                dealer.dsum += kocudet
                            if dealer.dsum > 21:
                                print("Dealer's total: ", dealer.dsum)
                                print("Your total: ", dealer.psum)
                                print("CONGRATULATIONS! YOU WIN")
                                dealer.tw += 1
                                c.execute("update players set total_games_won='" + str(
                                    dealer.tw) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                                dealer.bet = dealer.bet * 1.5
                                bet.buyin += dealer.bet
                                c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("Current Balance: ", bet.buyin,"$")
                                while True:
                                    ch = input("press 'P' to play again or 'E' to go to the main menu \n>")
                                    if ch == 'p':
                                        dealer()
                                        break
                                    if ch == 'e':
                                        bmenu()
                                    else:
                                        print("Enter a valid option(p/e)")
                                        continue
                            if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum > 21:
                                print("Dealer's total: ", dealer.dsum)
                                print("Your total: ", dealer.psum)
                                print("CONGRATULATIONS! YOU WIN")
                                dealer.tw += 1
                                c.execute("update players set total_games_won='" + str(
                                    dealer.tw) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                                dealer.bet = dealer.bet * 1.5
                                bet.buyin += dealer.bet
                                c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("Current Balance: ", bet.buyin,"$")
                                while True:
                                    ch = input(
                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                    if ch == 'p':
                                        dealer()
                                        break
                                    if ch == 'e':
                                        bmenu()
                                    else:
                                        print("Enter a valid option(p/e)")
                                        continue
                            if dealer.dsum == 21:
                                print("Dealer's total: ", dealer.dsum)
                                print("Your total: ", dealer.psum)
                                print("DEALER WINS! BETTER LUCK NEXT TIME")
                                dealer.tl += 1
                                c.execute("update players set total_games_lost='" + str(
                                    dealer.tl) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                                dealer.bet = dealer.bet / 2
                                bet.buyin += dealer.bet
                                c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("Current Balance: ", bet.buyin,"$")
                                while True:
                                    ch = input(
                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                    if ch == 'p':
                                        dealer()
                                        break
                                    if ch == 'e':
                                        bmenu()
                                    else:
                                        print("Enter a valid option(p/e)")
                                        continue
                            if dealer.dsum == dealer.psum:
                                print("Dealer's total: ", dealer.dsum)
                                print("Your total: ", dealer.psum)
                                print("IT'S A PUSH, NO ONE WINS.")
                                dealer.tp += 1
                                c.execute("update players set total_games_played_and_draws='" + str(
                                    dealer.tp) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                playsound(
                                    "C:\\Users\\dh1011tu\\Downloads\\mixkit-retro-game-over-1947 (mp3cut.net).wav")
                                bet.buyin += dealer.bet
                                c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("Current Balance: ", bet.buyin,"$")
                                while True:
                                    ch = input(
                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                    if ch == 'p':
                                        dealer()
                                        break
                                    if ch == 'e':
                                        bmenu()
                                    else:
                                        print("Enter a valid option(p/e)")
                                        continue
                            if dealer.dsum > dealer.psum and dealer.dsum >= 17 and dealer.dsum <= 21:
                                print("Dealer's total: ", dealer.dsum)
                                print("Your total: ", dealer.psum)
                                print("DEALER WINS! BETTER LUCK NEXT TIME.")
                                dealer.tl += 1
                                c.execute("update players set total_games_lost='" + str(
                                    dealer.tl) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                playsound("C:\\Users\\dh1011tu\\Downloads\\mixkit-sad-game-over-trombone-471 (mp3cut.net) (1).wav")
                                dealer.bet = dealer.bet / 2
                                bet.buyin += dealer.bet
                                c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("Current Balance: ", bet.buyin,"$")
                                while True:
                                    ch = input(
                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                    if ch == 'p':
                                        dealer()
                                        break
                                    if ch == 'e':
                                        bmenu()
                                    else:
                                        print("Enter a valid option(p/e)")
                                        continue
                            if dealer.dsum < dealer.psum and dealer.dsum >= 17 and dealer.dsum < 21:
                                print("Dealer's total: ", dealer.dsum)
                                print("Your total: ", dealer.psum)
                                print("CONGRATULATIONS! YOU WIN")
                                dealer.tw += 1
                                c.execute("update players set total_games_won='" + str(
                                    dealer.tw) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                playsound("C:\\Users\dh1011tu\Downloads\\391539__mativve__electro-win-sound.wav")
                                dealer.bet = dealer.bet * 1.5
                                bet.buyin += dealer.bet
                                c.execute("update players set balance='" + str(bet.buyin) + "' where username='" + str(
                                    config.usrnm) + "'")
                                db.commit()
                                print("Current Balance: ", bet.buyin,"$")
                                while True:
                                    ch = input(
                                        "press 'P' to play again or 'E' to go to the main menu \n>")
                                    if ch == 'p':
                                        dealer()
                                        break
                                    if ch == 'e':
                                        bmenu()
                                    else:
                                        print("Enter a valid option(p/e)")
                                        continue
hidden = [True]
bindings = KeyBindings()
@bindings.add("c-t")
def _(event):
    hidden[0] = not hidden[0]


def login():
    li=[]
    lik=[]
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Loggged-out of", str(config.usrnm))
    print("\n")
    print("-------------------LOGIN----------------------\n")
    while True:
        count = 0
        c.execute("select username from login")
        for i in c:
            ki=(str(i).strip('()').replace('\'', ''))
            ui=ki.strip(',').replace('\'', '')
            li.append(ui)
        res = li
        c.execute("select cast(AES_DECRYPT(password,'C-TAG') as char) from login")
        for i in c:
            kik = (str(i).strip('()').replace('\'', ''))
            uik = kik.strip(',').replace('\'', '')
            lik.append(uik)
        resl = lik
        combined = zip(res, resl)
        valdict = {}
        for keys, value in combined:
            valdict[keys] = value
        fig.usrnm()
        username = str(config.usrnm)
        if username not in valdict:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("This is not a valid username, input username again!")
            count+=1
            continue
        else:
            pass
        while True:
            if count == 3:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                j=input("seems like you forgot your password, do want to reset it(y/n)? \n> ")
                if j=='y':
                    sms.verify()
                if j=='n':
                    break
                else:
                    print("please enter a valid choice")
                    continue
            print("press Control+T to toggle password visibility.")
            password = prompt("Enter Password: ", is_password=Condition(lambda: hidden[0]), key_bindings=bindings)
            if username in valdict and password in valdict:
                pass
            elif password != valdict[username]:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("Password is not valid. ")
                print(f"username: {username}")
                count += 1
                continue
            elif password == valdict[username]:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("LOGIN SUCCESSFUL")
                print(f"WELCOME TO BLACK JACK, {username} ")
                bmenu()


def withdraw():
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<------BLACKJACK CASH OUT------>")
    while True:
        try:
            p = []
            c.execute("select balance from players where username='" + str(config.usrnm) + "'")
            for i in c:
                ki = (str(i).strip('()').replace('\'', ''))
                ui = ki.strip(',').replace('\'', '')
                p.append(ui)
            co = int(p[0])
            if co <= 0:
                print("looks like there's no money in your account :(, play blackjack to deposit money")
                while True:
                    bip = input("\n\nPress 'B' to play blackjack \nPress 'M' to return to menu \n> ")
                    if bip == 'b':
                        dealer()
                    if bip == 'm':
                        bmenu()
                    if bip != 'b' and bip != 'm':
                        print("please enter a valid input(B/M)")
                        continue
            print("Current balance: ", co)
            amt = int(input("Enter amount to be cashed out: "))
            tb = co - amt
            if tb < 0:
                print("insufficient balance")
                continue
            if tb>=0:
                print("LOADING PLEASE WAIT...")
                count=0
                em = []
                user = str(config.usrnm)
                c.execute("select e_mail from login where username='" + user + "'")
                for i in c:
                    mi = (str(i).strip('()').replace('\'', ''))
                    ei = mi.strip(',').replace('\'', '')
                    em.append(ei)
                digits = "0123456789"
                OTP = ""
                for i in range(6):
                    OTP += digits[math.floor(random.random() * 10)]
                otp = OTP + " is your BlackJack OTP. \nUse this to authenticate your transaction."
                msg = otp
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("blackjack.client@gmail.com", "exynwbhdifirbtgi")
                while True:
                    emailid = em[0]
                    s.sendmail('&&&&&&&&&&&', emailid, msg)
                    print("An OTP has been sent to the email registered with your User ID(", em[0], ")")
                    a = input("Enter OTP to proceed with the transaction: ")
                    if count == 3:
                        print("too many invalid inputs, OTP expired")
                        bmenu()
                    if a == OTP:
                        print("OTP Verified")
                        c.execute("update players set balance='" + str(tb) + "' where username='" + str(config.usrnm) + "'")
                        db.commit()
                        print("Withdraw Successful")
                        print("amount withdrawn: ", amt, "$")
                        while True:
                            bip = input("\n\nPress 'B' to play blackjack \nPress 'M' to return to menu \n> ")
                            if bip == 'b':
                                dealer()
                            if bip == 'm':
                                bmenu()
                            if bip != 'b' and bip != 'm':
                                print("please enter a valid input(B/M)")
        except:
            print("Please enter valid input")
            continue


def signup():
    li=[]
    count=0
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNew member Sign Up: ")
    c.execute("select username from login")
    for i in c:
        ki = (str(i).strip('()').replace('\'', ''))
        ui = ki.strip(',').replace('\'', '')
        li.append(ui)
    while True:
        fulnm=input("Enter Your Full Name: ")
        if fulnm=="":
            print("This field cannot be empty")
            continue
        else:
            break
    while True:
        if count==3:
            ch=input("seems like you already have an account would you like to sign in(y/n)?\n>")
            if ch=='y':
                login()
            if ch=='n':
                continue
            else:
                print("please enter a valid choice")
        usrnm = input("\nEnter new username: ")
        if usrnm in li:
            print("Username already exists")
            count+=1
            continue
        else:

            break
    while True:
        print("press Control+T to toggle password visibility.")
        password = prompt("Enter new Password: ", is_password=Condition(lambda: hidden[0]), key_bindings=bindings)
        if len(password) <= 6:
            print("Password too short")
            continue
        else:
            while True:
                print("press Control+T to toggle password visibility.")
                cp = prompt("Confirm password: ", is_password=Condition(lambda: hidden[0]), key_bindings=bindings)
                if cp == password:
                    em=[]
                    cpr=str(cp)
                    c.execute("select e_mail from login")
                    for i in c:
                        mi = (str(i).strip('()').replace('\'', ''))
                        ei = mi.strip(',').replace('\'', '')
                        em.append(ei)
                    eml=input("Enter Your Email address: ")
                    while True:
                        if eml in em:
                            print("this email is already registered, please enter another one")
                            continue
                        if eml not in em:
                            break
                    c.execute("insert into login (username,password,e_mail) values('" + usrnm + "',AES_ENCRYPT('" + cpr + "','C-TAG'),'"+eml+"')")
                    c.execute("insert into players (username,full_name) values('"+usrnm+"','"+fulnm+"')")
                    c.execute("update players set balance=0,total_games_played=0,total_games_won=0,total_games_lost=0 where username='"+usrnm+"'")
                    print("Account Saved successfully")
                    db.commit()
                    login()
                else:
                    print("passwords do not match please reconfirm password")
                    continue
bet()