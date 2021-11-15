import configure
from easygui import *
import mysql.connector as m
import sys
import sms
import pwinput
import config
import fig
import card
import pyaes
import os
from prompt_toolkit import prompt
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
db = m.connect(host="localhost", user="root", passwd="Anshshah2003")
c = db.cursor(buffered=True)
c.execute("create database if not exists blackjack")
c.execute("use blackjack")
c.execute("create table if not exists login(username varchar(20) primary key,password varbinary(300), e_mail varchar(50))")
c.execute("create table if not exists players(username varchar(20) references login(username), full_name varchar(50), balance int, total_games_won int, total_games_lost int, total_games_played_and_draws int)")
hidden = [True]
bindings = KeyBindings()
@bindings.add("c-t")
def _(event):
    hidden[0] = not hidden[0]
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
def login():
    li=[]
    lik=[]
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
                card.bmenu()
