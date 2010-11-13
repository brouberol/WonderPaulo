# -*- coding: utf-8 -*-
import random

print "#------------------------------#"
print "#---Virtual WonderPaulo v0.2---#"
print "#------------------------------#\n"
print "Le premier simulateur de Paul Adenot !"
print "C'est comme l'avoir en co-TP!\n"
print "Pose tes questions à WonderPaulo !\n"

for i in range(1,10):
    Question=(raw_input(">"))
    Question=Question.lower()
    
    r=random.randint(1,6)

    if "ne" in Question:
        print "Non."
    elif "baise" in Question:
        print "C'est ta mère qu'je baise."
    elif "bisou" in Question or "bisous" in Question:
        print "Arrete, j'ai du boulot, j'suis en 4IF."
    elif "non" in Question:
        print "Si."
    elif "aider"in Question or "faire" in Question:
        print "Pas le temps."
    elif "sudo" in Question:
        print "Ok."
    elif "windows" in Question  or "apple" in Question or "ipod" in Question or "mac" in Question:
Tu        print "Toute façon, c'est d'la merde."
    else:
        if r==1:
            print "TATATATA."
        elif r==2:
            print "Non."
        elif r==3:
            print "C'est d'la merde."
        elif r==4:
            print "J'vais m'prendre un café."
        elif r==5:
            print "Ecoute ma p'tite chatte, j'ai pas le temps pour ces conneries!"
        else:
            print "J'te buttfuck comme une souillon."
    print ""

