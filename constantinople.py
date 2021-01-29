import tkinter
from tkinter import *
from tkinter.constants import DISABLED, NORMAL 
import tkinter as tkr
import random
import re

_nonbmp = re.compile(r'[\U00010000-\U0010FFFF]') #this the emoji conversion function, borrowed from Stack overflow
#indeed, tkinter has a bug concerning emojis, that was a real pain in the ass, not gonna lie
# you can find it here :https://stackoverflow.com/questions/40222971/python-find-equivalent-surrogate-pair-from-non-bmp-unicode-char
def _surrogatepair(match):
    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (
        chr(int.from_bytes(encoded[:2], 'little')) + 
        chr(int.from_bytes(encoded[2:], 'little')))

def with_surrogates(text):
    return _nonbmp.sub(_surrogatepair, text)
#this game is about the fall of constantinople and the main character's name isnt switchable
#starting app
app = tkinter.Tk()
app.title("Constantinopolis launcher")
app.geometry("600x400")
#here go all the fonts
font = ('Helvetica',10)
font2 = ('Helvetica Bold',10)
font3 = ('Helvetica Bold', 15)
#main app dictionaries


Inventory = { #main inventory
    "ring ": False,
    "horse" : False,
    "knife" : True,
    "sword" : False,
    "Cataphract_Armor" : False,
    "diamond" : False,
    "animal_Skin" : False,
    "horse_Armor" : False,
    "water_Liters" : 2,
    "food_Quantity" : 4,
    "vital_Force" : 100,
    "golden_Coins" : 30,
}
abilities = { #mental abilities
    "sneakyEscape" : True,
    "mindTrick" : False,
    "courage": False,
    "MarketAbility" : False,
    "turkishGibberish" : False,
    "mindManipulation" : False,
    "diplomacy" : False,
    "resistance": 0,
}
stateOfWarnings = { #state of bot warning
    "globalWarning" : False,
    "localWarning"  : False,
    "particularCustomWarning" : False
}
stateOfBtn = {
    "knifeUsed" : False,
    "corruptionUsed" : False,
    "trickUsed" : False,
}
capacities = { #capabilities of the main character
    "attack" : 15,
    "armour" : 25,
    "active" : True
}
botCustomAbilities = { #bot capabilities
    "attack" : 10,
    "defense" : 3,
    "active" : True,
    "hasTransmitted" : False,
}
boatState = { #boat state and resistance
    "buoyancy" : 10,
    "hp" : 100,
    "armour" : 1,
    "weaponry": False,
    "active" : True
}
weatherState = { #state of weather
    "clearSea" : True,
    "hurricane" : False,
    "turbulentSea": False,
    "badWind" : False

}
mercenariesCapabilities ={ #mercenaries
    "troops": 50,
    "attack" : 25,
    "defense" : 10,
    "ships" : True,
    "archer" : False,
    "heavyWeaponry" : True
}
lordCapabilities = {  #"first " boss capabilities
    "troops" : 35,
    "attack" : 15,
    "defense": 30,
    "ships" : False,
    "archer" : True
}
piratesCapabilities = { #pirates
    "troops" : 60,
    "attack" : 20,
    "defense" : 5,
    "ships" : True,
    "archer": False,
    "heavyWeaponry": True
}
#main app function     
def mainGameLauncher(): #here is the main app, to be differentiated from the app def which is the launcher 
    maingame = tkr.Tk()
    maingame.title("Constantinopolis")
    maingame.geometry("1000x600")
    def keyBind(event): # prints inventory when i is pressed 
        for element, state in Inventory.items():
            print( element, " : ", state)   
    maingame.bind("<i>",keyBind)
    def armoredCombat(attack): # to be used in other functions to perform combats where an armor might be used
        if Inventory["Cataphract_Armor"] or Inventory["sword"]:
            if capacities["armour"] <= 0:
                capacities["active"] : False
                print("Malheureusement votre armure a déjà pris trop de dégâts 💀")
            else:
                capacities["armour"] -= attack
                print("heureusement votre armure a absorbé une partie des dégâts 🛡️ (" + str(attack)+ ")")
    def casualCombat(): #function defining a casual combat without any armor
        if Inventory["sword"]:
            randAttack = random.randint(10,15)
        elif Inventory["knife"]:
            randAttack = random.randint(5,9)
        else:
            randAttack = 0
        return randAttack
    def customBotFight(): #function building the fight against a bot
        fightRandomCustomBot = random.randint(1,2)
        if capacities["attack"] > botCustomAbilities["defense"] and fightRandomCustomBot == 1:
            print("\nVous tranchez la gorge à ce pauvre Officier de Douane d'un seul coup, 🗡️il n'a pas le temps de donner l'alerte✔️")
            stateOfWarnings["customParticularWarning"] = False
            botCustomAbilities["active"] = False
        elif capacities["attack"] > botCustomAbilities["defense"] and fightRandomCustomBot == 2:
            print("\nVous sabrez ce pauvre officier de douane 🗡️, mais il hurle à la mort et prévient ses collègues. L'alerte totale est donnée⚠️⚠️")
            botCustomAbilities["hasTransmitted"] = True
            stateOfWarnings["globalWarning"] = True
        elif botCustomAbilities["attack"] > capacities["defense"]:
            print("\nL'officer vous sabre🗡️ violamment vous êtes mortellement blessé mais par chance un cheval🐎 est sur votre chemin et vous prenez la fuite avec lui🏃‍♂️, l'alert totale est donnée⚠️👀")
            Inventory["vital_Force"] = 5
            Inventory["horse"] = True
            stateOfWarnings["globalWarning"] = True



    traj2_1 = tkinter.Label(maingame, text="Nous voilà dans la mer de Marmara "+ with_surrogates('🌊') +", mais attention, les navires Ottomans rôdent !!" + with_surrogates('⛵☪️'), font = font)

    willPlayTrj1 = True
    willPlayTrj2 = True
    def trajectory1(): 
        #here is the first trajectory 
        if willPlayTrj1 == True: #blocks the user from choosing the second trajectory if he already chose
            Inventory["golden_Coins"] = 30
            print("\nVous avez "  + str(Inventory["golden_Coins"]) + " pièces d'or💰")
            print("\nVous voilà arrivés à Philippoupoli,👑 dans l'ancien empire Bulgare ! Attention les Ottomans☪️ vous recherchent, soyez discret👀")
            print("\nHolà! Un Homme à l'allure étrange vous arrête👨 ! \n  Il vous propose de venir tromper les fonctionaires du sultan et promet une forte récompense💸 \n Attention, vos chances sont relativement aléatoires ⚖️! ")
            def fourthMission(): 
                print("\n Et voilà notre voyage 🧳 est bientôt terminé, nous voilà à la frontière entre l'empire Ottoman🌙 et le Saint Empire Germanique ✝️👑")
                if stateOfWarnings["particularCustomWarning"]:
                    print("\nAttention ! ⚠️ la douane vous recherche activement ! 🔍")
                    print("Mince ! Un Fonctionnaire des douanes vous surprend !⚠️ ")
                    customBotFight()
                elif stateOfWarnings["particularCustomWarning"] == False:
                    print("\nVous entendez des mercenaires se battre au loin, vous fuyez pour échapper aux combats🏃")
                print("\nUn noble seigneur🤴 vous invite à sa cours de venitie pour faire profiter la cours de vos savoirs📝")
                def acceptCastle():
                    print("\nà la bonne heure mon Ami, nous allons prendre soins de vous !🥘 et nous vous emmenons à Florence !")
                    print("V I C T O I R E✌️")
                    victoryElement = tkinter.Label(maingame, text = "V I C T O I R E" + with_surrogates('✌🏻')).place(x= 400, y=300 )
                    print("voici l'état de vos inventaires et capacités mentales:")
                    for element, state in Inventory.items(): #prints the inventory
                        print( element, " : ", state)
                    for element, state in abilities.items(): #print the mental abilities
                        print( element, " : ", state)      

                    stateOfWarnings["globalWarning"] = False
                    stateOfWarnings["localWarning"] = False
                    stateOfWarnings["particularCustomWarning"] = False
                def refuseCastle():
                    print("\nBon Dieu vous les Byzantins ! S'étouffe le seigneur du domaine😤")
                    print("Il vous enferme dans son cachôt 🏰")
                    print("G 🅰️ M E  O V E R 💀")
                acceptCastleBtn = tkinter.Button(maingame, text = "Accepter l'offre", command = acceptCastle).place(x =280 , y =230)
                refuseCastleBtn  = tkinter.Button(maingame, text = "Refuser l'offre", command = refuseCastle).place(x =190 , y =230)
                #so as you might notice the tkinter layouts function are written as such : yourVar = tkiner.typeOfLayout(yourapp, text="").place
            def thirdMission():
                print("vous voilà dans les plaines de Panonie🏇🏻")
                def attack():
                    if Inventory["horse"]:
                        print("Des bandits ont voulu vous attaquer mais heureusement, vous avez pu prendre la fuite grâce à votre cheval🏇🏻")
                    elif Inventory["horse"] == True and stateOfWarnings["localWarning"] == True:
                        print("\n Des Sipahis ⚔️, la cavalerie ottomane🏇🏻, vous cherchent et se rapproche de vous👀")
                        print("Ils passent à l'attaque !")
                        sipahisRand = random.randint(10,17)
                        armoredCombat(sipahisRand)
                    else:
                        print("\n des mendiants vous demandent de l'argent!💸")
                        def homelessAccept():
                            homelessRand = random.randint(3,10)
                            if Inventory["golden_Coins"] > homelessRand:
                                Inventory["golden_Coins"] -= homelessRand
                                print("\nvous leur donnez " + str(homelessRand) + " pièces d'or")
                                print("\nen récompense ils vous offrent du bouillon🍛, vous gagnez 25PV et deux litres d'eau🚰")
                                Inventory["water_Liters"] += 2
                                Inventory["vital_Force"] += 25
                                stateOfWarnings["localWarning"] = False
                                stateOfWarnings["particularCustomWarning"] = True
                            else:
                                print("\nvous n'avez pas assez de monnaie💸, les mendiants, furieux 👺vous frappent, vous perdez 5PV👊")
                                Inventory["vital_Force"] -= 5
                                Inventory["vital_Force"] += abilities["resistance"]
                            fourthMission() 
                        homelessAcceptBtn = tkinter.Button(maingame, text="Accepter" + with_surrogates('✅'), command = homelessAccept).place(x =250 , y = 190)
                        def homelessRefuse():
                            print("les mendiants, furieux voient que vous mentez👺 !")
                            homelessHP = 6
                            if casualCombat() >= 6:
                                print("\nVous les avez vaincus sans problèmes, mais dans votre infinie sagesse😇 vous ne leur prenez rien")
                            else:
                                print("C'est la débâcle ! Les mendiants ne vous prennent rien mais ils previennent les autorités de votre présence👮👀")
                                stateOfWarnings["globalWarning"] = True
                            fourthMission() 
                        homelessRefuseBtn = tkinter.Button(maingame, text="Refuser" + with_surrogates('🚫'), command = homelessRefuse).place(x =190 , y = 190)
                attack()
                    
            def secondMission():
                print("\n Nous voilà arrivés au marché de Sophia🏫, les Ottomans☪️ y vendent des esclaves mais aussi des biens précieux💎 !")
                print("vous pouvez soit aller faire du troc au marché🏫, soit libérer les esclaves🆓")
                def slaves():
                    print("\nvous avez deux choix pour les libérer mais attention cela peut vous coûter très cher!")
                    def slavesFight():
                        slaveFightRand = random.randint(1,2)
                        if slaveFightRand == 1:
                            goldenRandSlaveFight = random.randint(3,10)
                            print("vous avez ravagé le visage de ce pauvre vendeur avec votre couteau🔪, les esclaves sont libres🆓 et vous débloquez du courage⏫ et "+ str(goldenRandSlaveFight) +" pièces, mais attention \n les autorités commencent à vous chercher👁️")
                            abilities["courage"] = True
                            Inventory["golden_Coins"] += goldenRandSlaveFight
                            stateOfWarnings["localWarning"] = True
                        elif slaveFightRand == 2:
                            print("\nAïe le marchand vous botte les fesses👢 vous perdez votre couteau🔪 et 35PV, et les esclaves restent enfermés.")
                            Inventory["knife"] = False
                            Inventory["vital_Force"] -= 35
                            Inventory["vital_Force"] += abilities["resistance"]
                            thirdMission()
                    slaveFightBtn = tkinter.Button(maingame,text="Se battre" + with_surrogates('🔪'), command = slavesFight).place(x = 450, y = 163)
                        
                    def slavesTrick():
                        if abilities["mindTrick"] == True:
                            if Inventory["diamond"] == False:
                                print("\n Les esclaves sont libérés🆓 grâce à vos excellents talents d'arnaqueur ! Vous lui extorquez aussi un diamand 💎")
                            else:
                                print("\nVous débloquez un Anneau 💍d'une valeur rare ! Et les esclaves sont libérés🆓")
                                Inventory["ring"] = True
                        else:
                            print("\nle marchand vous botte les fesses 👢vous perdez 15PV et 5 pièces d'or")
                            Inventory["golden_Coins"] -= 5
                            Inventory["vital_Force"] -= 15
                            Inventory["vital_Force"] += abilities["resistance"]
                            thirdMission()
                    slavesTrickBtn = tkinter.Button(maingame, text ="Faire un tour de passe passe" + with_surrogates('⚗️'), command = slavesTrick).place(x = 190, y = 163)
                def buyMarket():
                    if abilities["mindTrick"] == True :
                        print("\nvous arrivez à derober des éléments à un marchand, c'est vrai pourquoi payer inutilement?🤷 \n vous arrivez à voler une peau de bête !🐂")
                        Inventory["animal_Skin"] = True
                    elif abilities["sneakyEscape"] == True:
                        print ("\nDans votre tour de passe passe vous arrivez à voler une grande épée 🗡️ et des vivres au pauvre homme 🧆")
                        Inventory["sword"] = True
                        Inventory["food_Quantity"] += 3
                    else:
                        print(" \nVos capacités ne vous permettent pas de voler quoi que ce soit, vous payez donc 25 pièces d'or👛 et achetez à manger🧆")
                        print("\n cependant vous debloquez la capacité de marchandage💬 -> -5 sur le prix des prochains achats")
                        Inventory["golden_Coins"] -= 25
                        Inventory["food_Quantity"] += 5
                        Inventory["water_Liters"] += 5
                    thirdMission()
                slaveBtn = tkinter.Button(maingame, text = " libérer les esclaves" + with_surrogates('🆓'), command = slaves). place(x = 190, y= 135)
                marketBtn = tkinter.Button(maingame, text = " tours de passe passe au marché" + with_surrogates('⚗️'), command = buyMarket).place(x = 305, y=135)
            def acceptFirstMission():
                def knifeUse():
                    if Inventory["knife"]:
                        knifePb = random.randint(1,3)
                        if knifePb == 1:
                            print("\nwow! L'ennemis succombe au premier coup🤪, vous vous accaparez ses biens")
                            print("\nIl semblerait que vous ayez récolté un artefact unique 🛡️! Une armure de Cataphracte! \n Vous gagnez + 30 PV")
                            Inventory["vital_Force"] += 30
                            Inventory["golden_Coins"] += 15
                            Inventory["water_Liters"] += 2
                        elif knifePb == 2:
                            print("\nle combat fait rage !⚔️ Vous perdez 25 points de vie mais l'ennemi est vaincu !")
                            print("\nvous récupérez un artefact unique ! L'armure de cataphracte🛡️, vous gagnez 30 PV")
                            Inventory["vital_Force"] += 5
                            Inventory["golden_Coins"] += 5
                        else:
                            print("\nVous prenez la déculottée du siècle vous perdez  35 PV et vous prenez la fuite🏃‍♀️")
                            Inventory["vital_Force"] -= 35
                            Inventory["vital_Force"] += abilities["resistance"]
                    else:
                        print("\nVotre couteau vous fait défaut !🔪 Vous perdez de la nourriture🍲 et 5 pièces💸 en vous sauvant🏃‍♀️")
                        Inventory["food_Quantity"] -= 1
                        Inventory["golden_Coins"] -= 5
                    stateOfBtn["knifeUsed"] = True
                    print("\n Allons bon ! Continuons vers notre prochaine destination : Sophia et son grand marché où regnent bandits 👺et grands marchands🧙")
                    secondMission()
                def corruption(): 
                    #corruption choice function
                    if Inventory["golden_Coins"] >= 5:
                        corruptionPb = random.randint(1,2)
                        if corruptionPb == 1:
                            corruptionAmount = random.randint(4,12)
                            print("\nSuper, ça a marché, l'ennemi a été corrompu avec" + str(corruptionAmount) + " pièce d'or💸 bien placées")
                            Inventory["golden_Coins"] -= corruptionAmount
                        else:
                            hpLoss = random.randint(1,35)
                            print("\nHélas ce n'a pas marché ! l'ennemi vous frappe violamment👊, vous perdez " + str(hpLoss) + "PV")
                            Inventory["vital_Force"] -=  hpLoss
                            Inventory["vital_Force"] += abilities["resistance"]
                            abilityLoss = random.randint(1,2)
                            if abilityLoss == 1:
                                print("\nArgh ! Le coup vous a violamment touché la tête🤕 vous pertez votre capacité à vous échapper facilement ")
                                abilities["sneakyEscape"] = False
                    stateOfBtn["corruptionUsed"] = True
                    print("\n Allons bon ! Continuons vers notre prochaine destination : Sophia et son grand marché où regnent bandits et grands marchands🧙")
                    secondMission()
                     
                def trick():
                    if abilities["sneakyEscape"]:
                        abilityRand = random.randint(1,3)
                        if abilityRand == 1:
                            abilities["turkishGibberish"] = True
                            print("\nvotre blabla fonctionne,🗣️ vous débloquez la l'abilité de baragouiner en Turc !")
                        elif abilityRand == 2:
                            print("\nVous réussisez à anarquer l'homme, vous lui volez un diamand💎 et débloquez la capacité d'arnaque !")
                            Inventory["diamond"] = True
                            abilities["mindTrick"] = True
                        else:
                            print("\nAie ! L'homme se rend compte de vos tentative de passe-passe et vous agresse👊 ! \n vous perdez 15PV et 10 pièces!💸")
                            print("\nCependant vous arrivez à dérober un cheval🐎 et vous disparraissez")
                            Inventory["horse"] == True
                            Inventory["vital_Force"] -= 15
                            Inventory["vital_Force"] += abilities["resistance"]
                            Inventory["golden_Coins"] -= 10
                    else:
                        
                        print("L'ennemi vous repère👀, il vous tabasse violamment au sol👊, vous perdez 50PV")
                        print("mais vous débloquez la capacité à prendre des coups⚔️ !")
                        abilities["resistance"] += 5
                    stateOfBtn["trickUsed"] = True
                    print("\n Allons bon ! Continuons vers notre prochaine destination : Sophia et son grand marché où regnent bandits et grands marchands🧙")
                    secondMission()

                knifeBtn = tkinter.Button(maingame, text= "Utiliser le couteau", command = knifeUse).place(x=190, y=105) 
                corruptionBtn = tkinter.Button(maingame, text = "Utiliser la corruption", command = corruption).place(x=297, y=105) 
                trickBTn = tkinter.Button(maingame,text = "Utiliser un tour de passe passe", command = trick).place(x=420, y=105) 
                
            def refuseFirstMission():
                print("Sagouin ! Vous me le payerez ! \n l'homme vous pousse violamment👊 et vous prends 10 pièces d'or 💸!")
                Inventory["golden_Coins"] -= 10 
                print("Vous vous enfuyez en courant🏃")
                secondMission()
        pEvent1Btn1 = tkinter.Button(maingame, text="Accepter " + with_surrogates('⚔️'), command = acceptFirstMission).place(x=190, y=80)   
        pEvent1Btn2 = tkinter.Button(maingame, text="Refuser " + with_surrogates('❌‍'), command = refuseFirstMission).place(x=330, y=80) 
        
        willPlayTrj2 = False
    def arrivalToFlorence():
        print("V I C T O I R E vous êtes arrivé à Florence ✌🏻!")
        print("\n voici votre inventaire : ")
        victoryElement = tkinter.Label(maingame, text= "V I C T O I R E " + with_surrogates('✌🏻'), font = font3).place(x = 400 , y = 300)
        for element, state in Inventory.items():
            print( element, " : ", state)     
    def pirateFight():
        print("Deux options se présentent à vous : ")
        def artillery():
            artilleryPrecision = random.randint(1,3)
            if artilleryPrecision < 3:
                print("touché en plein dans le mille !💥")
                piratesCapabilities["defense"] = 0
                piratesCapabilities["troops"] -= 35
                piratesCapabilities["ships"] = False
            else:
                print("c'est raté nous devons passer à l'abordage !🗡️")
                if mercenariesCapabilities["attack"]  > piratesCapabilities["defense"]:
                    print("abordage réussi !! les pirates sont vaincus !🗡️✌️")
                else:
                    print("c'est la débâcle, mais vous arrivez à fuire⛵")
            arrivalToFlorence()
        artilleryBtn = tkinter.Button(maingame, text = "Tirer l'artillerie" + with_surrogates('💣'), command = artillery).place( x =700 , y = 210)
        def boarding():
            ennemyArtillery = random.randint(1,5)
            if ennemyArtillery > 1:
                print("\nvous êtes sévèrement touchés 🤕! Vous perdez 15 hommes !")
                mercenariesCapabilities["troops"] -= 15
                print("mais l'abordage est lancé !")
                if mercenariesCapabilities["troops"] + mercenariesCapabilities["attack"] + 1 > piratesCapabilities["troops"] + piratesCapabilities["defense"]:
                    print("l'attaque est victorieuse !✌️ vous l'emportez sur l'ennemi !🗡️")
                    Inventory["golden_Coins"] += 50
                    Inventory["water_liters"] += 5
                    Inventory["food_Quantity"] += 5
                else :
                    print("\nc'est un échec❌, vous battez en retraite et perdez l'ensemble des mercenaires🤕")
                    mercenariesCapabilities["troops"] = 0
                    mercenariesCapabilities["ships"] = False
                    print('G 🅰️ M E  O V E R 💀')
            else:
                print("\nl'artillerie ennemi ne vous touche pas, vous réduisez en pièce les pirates💥")
                Inventory["golden_Coins"] += 50
                Inventory["water_Liters"] += 5
                Inventory["food_Quantity"] += 5
            arrivalToFlorence()
        boardingBtn = tkinter.Button(maingame, text= "à l'abordage" + with_surrogates('🗡️'), command = boarding).place(x =590 , y =210 )

    def trajectory2():
        if willPlayTrj2 == True:
            Inventory["golden_coins"] = 25
            print("Vous avez "  + str(Inventory["golden_Coins"]) + " pièces d'or💰")
            def adriaticSea():
                print("nous voilà arrivés dans la mer adriatique🌊")
                print("des pirates vous attaquent !!🗡️")
                pirateFight()   
            def creteCastle():
                print("Vous voilà débarqué en Crète🏝️, le seigneur Byzantin local vous y accueille🥰 et vous propose de l'aider")
                def helpLord():
                    print("\nÀ la bonne heure ! ")
                    print("Le seigneur vous invite à sa cours vous en faire profiter🤩")
                    adriaticSea()
                helpLordBtn = tkinter.Button(maingame, text = "Aider le Seigneur" + with_surrogates('✔️'), command = helpLord).place(x =590 , y = 150)
                
                def refuseLord():
                    print("Sagouin ! 👺 Ce sera donc la guerre !")
                    def warWithLord():
                        print("\nContre toutes attentes les mercenaires vous nomment chef de leur garnison!👑 \n trois choix s'offrent à vous :")
                        def castleBombing():
                            print("nous allons bombarder la forteresse avec nos navires💣 !")
                            archerStatus = random.randint(1,2)
                            if archerStatus == 1:
                                lordCapabilities["archer"] = False
                                print("les archés de l'ennemi sont neutralisé🏹! À l'assaut !")
                            else:
                                print("Les archés sont intacts !!🏹")
                            defenseStatus = random.randint(12,30)
                            troopsLoss = random.randint(15,35)
                            lordCapabilities["troops"] -= troopsLoss
                            lordCapabilities["defense"] -= defenseStatus
                            print("cependant ils ont perdu aussi 🤕" + str(defenseStatus)+ "points de défense sur 30")
                            if defenseStatus < 15:
                                print("\nmalheureusement leur défense🛡️ sont trop fortes, nous devons battre en retraite🏃‍♂️.")
                                print("Vous devez vous replier🏃‍♂️, vous perdez la moitié de vos effectifs🤕")
                                mercenariesCapabilities["troops"] -= 25
                            else:
                                print("c'est une vraie réussite à l'assaut !!🤺")
                                if lordCapabilities["troops"] > mercenariesCapabilities["troops"] / 2:
                                    print("Nous subissons de lourdes pertes !☠️ Mais le Château est à nous 🏯 !!")
                                else:
                                    print("C'est une grande victoire ! Vous ne subissez presque aucunes pertes ✔️!")
                                    print("Vous récoltez des un diamand 💎 et des anneaux ! 💍")
                                    Inventory["ring"] = True
                                    Inventory["diamond"] = True
                            adriaticSea()
                        castleBombingBtn = tkinter.Button(maingame, text = "Bombarder le Château" + with_surrogates('💥'), command = castleBombing).place(x =590 , y = 180)
                        def directAssault():
                            print("vous débarquez sans préparation d'artillerie💥")
                            yourLoss = random.randint(17,32)
                            print("les archers ennemis terrassent " + str(yourLoss)+ " de vos hommes 🏹!")
                            if yourloss > 23:
                                print("c'est la débandade ! Vous repartez à vos navires !⚓🏃‍♂️")
                            else:
                                print("\nC'est un succès ! L'ennemi est terrassé ! Vous prenez la citadelle🏯")
                                print("vous récuperez un diamand💎 et des anneaux💍")
                                Inventory["ring"] = True
                                Inventory["diamond"] = True
                            adriaticSea()
                        directAssaultBtn = tkinter.Button(maingame, text = " Assaut direct" + with_surrogates('🤺'), command = directAssault).place(x =500 , y = 180)
                        def longSiege():
                            print("\nvous menez un long siège contre le chateau du seigneur🤺, mais les jours passent et vos rations s'amenenuisent🍲")
                            if Inventory["food_Quantity"] < 3:
                                print("vous devez abandonner le siège !❌")
                            else:
                                print("Le seigneur finit par se rendre, vous débloquez diplomacie💬 ! Et gagnez 100 pièces d'or 💸!")
                                abilities["diplomacy"] = True
                                Inventory["golden_Coins"] = True
                            adriaticSea()
                        longSiegeBtn = tkinter.Button(maingame, text = "Assieger la ville", command = longSiege).place(x =750 , y = 180)
                    warWithLord()
                refuseLordBtn = tkinter.Button(maingame, text = "Piller son fief", command = refuseLord).place(x =700 , y = 150)


            def navalFight(): 
                #here defines the function doing the naval fight once
                print("vous êtes attaqués par des navires Ottomans ! 🌙")
                if abilities["MarketAbility"]:
                    print("Heureusement vos amis Mercenaire s'en chargent !🏴󠁶󠁮󠁳󠁧󠁿")
                    print("Vous pouvez cependant prendre part à la bataille !🤺")
                    def takePart():
                        print("\nLa bataille est une grande victoire⚔️, les navires ennemis sont détruits⛵, les capacités de votre navires sont considérablement augmentées⛵🆙")
                        boatState["weaponry"] = True
                        boatState["buoyancy"] = 10
                        boatState["hp"] = 100
                        creteCastle()
                    takePartBtn = tkinter.Button(maingame, text = "Prendre part" + with_surrogates('🤺'), command = takePart).place(x =600 , y =115)
                    def noFight():
                        print("la bataille fait rage🎆, les mercenaires ont des pertes, 🏴󠁶󠁮󠁳󠁧󠁿ils vous extorquent 5 pièces de plus💸, mais le combat est gagné.")
                        Inventory["golden_Coins"] -= 5
                        creteCastle()
                    noFightBtn = tkinter.Button(maingame, text = "Ne pas prendre part" + with_surrogates('❌'), command = noFight).place(x =690 , y =115)
                else:
                    print("\nMalheureusement vous n'avez pas d'escorte❌⛵, vous avez deux choix, combattre jusqu'à votre mort💀, ou vous échapper🏃‍♀️")
                    def escape():
                        print("sage décision ! Vous gagnez la compétence courage ! 🤣")
                        abilities["courage"] = True
                    escapeBtn = tkinter.Button(maingame, text = "S'échapper"+ with_surrogates("🏃‍♂️"), command = escape).place(x =750 , y =125)
                    def fightToDeath():
                        print("C'est une véritable débâcle🏃‍♀️, votre navire est assailli de toute part ⛵! Vous décédez au champ d'honneur 💀!")
                        print("G 🅰️ M E  O V E R 💀")
                    fightToDeathBtn = tkinter.Button(maingame, text = "Combattre jusqu'à la mort" + with_surrogates("💀"), command = fightToDeath).place(x =590 , y =125)
                    
            def crete():
                print("Vous arrivez bientôt en Crète🏝️, là-bas des dignitaires byzantins👑 vous y attendent, mais attention, le temps se gâte 🌩️")
                def isTheWeatherWorsening():
                    #this function checks if the weather will be worsening
                    weather = random.randint(0,3)
                    if weather < 2:
                        print("\nVous avez de la chance ! Les nuages s'éclairsissent au loin ! 🌞")
                        navalFight()
                    elif weather == 2:
                        print("\nUn ouragan frappe votre bateau ! 💨")
                        weatherState["hurricane"] = True
                        if boatState["buoyancy"] <= 7:
                            print("\nLa tempête se prépare et votre bâteau est en mauvais état ⛵! Vous risquez de chavirer")
                            print("\nvous avez le choix entre éviter la tempête🏃‍♂️ ou foncer la tête baissée😏")
                            def avoidHurricane():
                                print("vous avez évité la tempête avec succès.💨 Mais à quel prix? \n Votre eau🧴 et votre nourriture🍲 sont réduites au minumum")
                                Inventory["water_Liters"]  = 1
                                Inventory["food_Quantity"] = 0
                                print("mais au moins, la Crète est en vue🏝️ !")
                                creteCastle()
                            def goThrough():
                                hurricaneRand = random.randint(1,4)
                                if hurricaneRand > 1:
                                    print("votre bateau est une véritable épave⛵, il perd 2 points de flottabilité, mais il survit! La Crète🏝️ est en vue")
                                    boatState["buoyancy"] -= 2
                                else:
                                    print("L'ouragan ravage💨 votre navire qui se retourne, la mer vous emporte, vous perdez tout sauf votre bourse💸")
                                    boatState["active"] = False
                                    Inventory["water_Liters"] = 0
                                    Inventory["food_Quantity"] = 0
                                creteCastle()
                        else:
                            navalFight() 

                    elif weather == 3:
                        print("\nLa mer s'âgite brusquement 🌊")
                        weatherState["turbulentSea"] = True
                        def goTurbSea():
                            print("vous avez traversé la mer agitée🌊💨, la Crète 🏝️est maintenant en vue, mais vous réserves de nourritures🍲 et d'eau🧴 sont épuisées")
                            Inventory["food_Quantity"] = 0
                            Inventory["water_Liters"] = 0
                            creteCastle()
                        goTurbSeaBtn = tkinter.Button(maingame, text = "Traverser", command = goTurbSea).place(x =590 , y = 125 )
                        def goAround():
                            navalFight()
                            creteCastle()
                        goAroundBtn = tkinter.Button(maingame, text = "Contourner", command = goAround).place(x = 700 , y = 125) 
                isTheWeatherWorsening()
            def cyclades():
                print("\nVous êtes arrivés dans les Cyclades!🏝️ Mais d'un seul coup, un navire apparaît🚢, ce sont des mercenaires ils vous proposent leurs services")
                def mercenaries():
                    print("Les mercenaires sont ravis😄, mais ils vous chargent 15 pièces💰 d'escorte ⚔️ jusqu'à la Crète🏝️")
                    abilities["MarketAbility"] = True
                    abilities["turkishGibberish"] = True
                    Inventory["golden_Coins"] -= 15
                    crete()
                mercenariesBtn = tkinter.Button(maingame, text="Accepter leur aide", command = mercenaries).place(x = 600, y = 80)
                def noMercenaries():
                    randPvLoss = random.randint(15,20)
                    randomBuoyancy = random.randint(1,4)
                    print("Les mercenaires vous font payer le prix de votre insolence, et vous tabassent👊, vous perdez " + str(randPvLoss) + "PV")
                    print("votre navire 🚢lui aussi est endommagé🤕, sa flottabilité est réduite à "+ str(10 - randomBuoyancy)+ "/10 ⚙️")
                    Inventory["vital_Force"] -= randPvLoss
                    crete()
                noMercenariesBtn = tkinter.Button(maingame, text = "Refuser leur aide"  + with_surrogates('❌'), command = noMercenaries).place(x = 710, y = 80)
                
            cyclades()

        willPlayTrj1 = False
        
        
    buttonTrj1 = tkinter.Button(maingame, text="Prendre le premier trajet", width = 25, command = trajectory1, font = font)
    buttonTrj2 = tkinter.Button(maingame, text="Prendre le second trajet", width = 25, command = trajectory2, font = font)
    def showInstructions():
        print("\nPour cela vous disposez de 2 litres d'eau🍼, un couteau🔪, 30 pièces d'or💸, 4 jours de rations🍲 et une carte de la mer Égée🗺️")
        print("\nVous avez deux choix, passer par les Balkans en prenant le risque de croiser des Ottomans🗺️☪️")
        print("\nOu passer par la mer Égée🌊, la Crète et la mer Adriatique🏝️, mais attention aux Pirates!")
        buttonTrj1.place(x=190, y=50)
        buttonTrj2.place(x=595, y=50)
    order = tkinter.Label(maingame, text ="Andréas ! Constantinople"+ with_surrogates('🕌') +" vient de tomber, vous devez rejoindre Florence au plus vite.").pack()
    button_start_game = tkinter.Button(maingame, text="Commencer l'aventure" + with_surrogates('😉'), width = 25, command = showInstructions).pack()
#app.iconbitmap('ss117n.jpg')
start = tkinter.Label(app, text ="Bonjour Andréas ! Par Constantin vous êtes arrivé !" + with_surrogates('😉'))
keyBind = tkinter.Label(app, text ="Vous pourrez appuyer sur i à tout moment si vous voulez consulter votre inventaire. \n Celui-ci s'affichera dans le prompt, ainsi que le texte. \n seulement les boutons seront dans la fenêtre" + with_surrogates('📜') ) 
instructions = tkinter.Label(app, text ="J'ai une importante mission pour vous !"+ with_surrogates('📜'))

def startFunction():
    #this function launches the maingame so the game starts
    global app
    app.destroy()
    mainGameLauncher()
button_start = tkinter.Button(app, text="Commencer le jeu"  + with_surrogates('▶️'), width = 25, command = startFunction)
start.pack()
button_start.pack()
keyBind.pack()
app.mainloop()

#Thanks for your time Sir !
