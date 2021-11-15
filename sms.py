import os
import math
import random
import smtplib
import mysql.connector as m
import configure1
import pwinput
import fig
import config
import sys
from prompt_toolkit import prompt
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
db = m.connect(host="localhost", user="root", passwd="")
c = db.cursor(buffered=True)
c.execute("create database if not exists blackjack")
c.execute("use blackjack")
c.execute("create table if not exists login(username varchar(20) primary key,password varchar(30), e_mail varchar(50))")
hidden = [True]
bindings = KeyBindings()
@bindings.add("c-t")
def _(event):
    hidden[0] = not hidden[0]
def verify():
    count=0
    print("LOADING PLEASE WAIT...")
    em=[]
    user=str(config.usrnm)
    c.execute("select e_mail from login where username='"+user+"'")
    for i in c:
        mi = (str(i).strip('()').replace('\'', ''))
        ei = mi.strip(',').replace('\'', '')
        em.append(ei)
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your BlackJack OTP."
    msg = otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("example.email@gmail.com", "Your AppPassword")
    while True:
        emailid = em[0]
        s.sendmail('&&&&&&&&&&&', emailid, msg)
        print("An OTP has been sent to the email registered with your User ID(",em[0],")")
        a = input("Enter OTP to reset password: ")
        if count==3:
            print("too many invalid inputs, OTP expired")
            sys.exit()
        if a == OTP:
            print("OTP Verified")
            while True:
                print("press Control+T to toggle password visibility.")
                password = prompt("Enter new Password: ", is_password=Condition(lambda: hidden[0]),key_bindings=bindings)
                if len(password) <= 6:
                    print("Password too short")
                    continue
                else:
                    while True:
                        print("press Control+T to toggle password visibility.")
                        cp = prompt("Confirm password: ", is_password=Condition(lambda: hidden[0]),key_bindings=bindings)
                        if cp == password:
                            c.execute("update login set password=AES_ENCRYPT('" + cp + "','C-TAG') where e_mail='"+emailid+"'")
                            db.commit()
                            print("New password set")
                            configure1.login()
                        else:
                            print("passwords do not match")
                            continue
        else:
            print("Please Check your OTP again")
            count+=1
            continue
