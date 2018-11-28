'''Apratim's Kitchen'''

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import datetime

global final
root = Tk()
root.title("Apratim's Kitchen")
#------------------------------Creating the Frames---------------------------
TopFrame = Frame(root,width=1350,height=100,bd=12,relief='raise',)
TopFrame.pack(side=TOP)
TopFrame.config(background='black')

BottomFrame = Frame(root,width=1350,height=650,bd=12,relief='raise',bg='blue')
BottomFrame.pack(side=TOP)

LeftFrame = Frame(BottomFrame,width=450,height=650,bd=12,relief='raise')
LeftFrame.pack(side=LEFT)

MidFrame = Frame(BottomFrame,width=450,height=650,bd=12,relief='raise',bg='green')
MidFrame.pack(side=LEFT)
MidTopFrame = Frame(MidFrame,width=450,height=350,bd=6,relief='raise',)
MidTopFrame.pack(side=TOP)
MidBottomFrame = Frame(MidFrame,width=450,height=300,bd=6,relief='sunken',)
MidBottomFrame.pack(side=BOTTOM)

RightFrame = Frame(BottomFrame,width=450,height=650,bd=12,relief='raise',)
RightFrame.pack(side=LEFT)
#----------------------------Heading of the App-----------------------------
AppTitle = Label(TopFrame,text="            APRATIM'S KITCHEN            ",fg='red',
                 font=('Verdana',50,'bold','italic'),bg='midnightblue')
AppTitle.grid(row=0,column=0)

def GrandTotal():
    global final
    valFries = float(varFries.get())*60
    ValSalad = float(varSalad.get())*45
    ValVegSand = float(varVegSandwich.get())*90
    ValChickSand = float(varChickSandwich.get())*120
    ValVegPasta = float(varVegPasta.get())*150
    ValChickPasta = float(varChickPasta.get())*180
    ValPPops = float(varPotatoPops.get())*100
    ValCPops = float(varChickPops.get())*150
    
    ValApple = float(varApple.get())*60
    ValGrape = float(varGrape.get())*50
    ValOrange = float(varOrange.get())*50
    ValMosambi = float(varMosambi.get())*50
    
    ValPaneer = float(varPaneer.get())*180
    ValMushroom = float(varMushroom.get())*150
    ValFish = float(varFish.get())*220
    ValChicken = float(varChicken.get())*200
    ValMutton = float(varMutton.get())*260
    ValDuck = float(varDuck.get())*300
    
    ValVHakka = float(varVegHakka.get())*180
    ValCHakka = float(varChickHakka.get())*210
    ValPorkHakka = float(varPorkHakka.get())*230
    ValPrawnHakka = float(varPrawnHakka.get())*250
    ValChinese = float(varChinese.get())*200
    ValAmerican = float(varAmerican.get())*200
    ValCanadian = float(varCanadian.get())*220
    ValDragon = float(varDragon.get())*220
    
    ValBanana = float(varBanana.get())*40
    ValMango = float(varMango.get())*60
    ValPome = float(varPome.get())*70
    ValOreo = float(varOreo.get())*50

    sub = float(valFries+ValSalad+ValVegSand+ValChickSand+ValVegPasta+ValChickPasta+
           ValPPops+ValCPops+ValApple+ValGrape+ValOrange+ValMosambi+ValPaneer+
           ValMushroom+ValFish+ValChicken+ValMutton+ValDuck+ValVHakka+ValCHakka+
           ValPorkHakka+ValPrawnHakka+ValChinese+ValAmerican+ValCanadian+
           ValDragon+ValBanana+ValMango+ValPome+ValOreo)

    tax = round(float(0.18*sub),2)

    final = round((sub+tax),2)

    varSubTotal.set(sub)
    varGST.set(tax)
    varTotal.set(final)

def Change():
    global final
    paid = float(varPaid.get())
    p = round(paid-final)
    varChange.set(p)
     

def Reset():
    varFries.set('0')
    varSalad.set('0')
    varVegSandwich.set('0')
    varChickSandwich.set('0')
    varVegPasta.set('0')
    varChickPasta.set('0')
    varPotatoPops.set('0')
    varChickPops.set('0')
    
    varApple.set('0')
    varGrape.set('0')
    varOrange.set('0')
    varMosambi.set('0')
    
    varPaneer.set('0')
    varMushroom.set('0')
    varFish.set('0')
    varChicken.set('0')
    varMutton.set('0')
    varDuck.set('0')
    
    varVegHakka.set('0')
    varChickHakka.set('0')
    varPorkHakka.set('0')
    varPrawnHakka.set('0')
    varChinese.set('0')
    varAmerican.set('0')
    varCanadian.set('0')
    varDragon.set('0')
    
    varBanana.set('0')
    varMango.set('0')
    varPome.set('0')
    varOreo.set('0')
    
    varPayment.set('Cash')
    varChange.set('0')
    varGST.set('0')
    varSubTotal.set('0')
    varTotal.set('0')
    varPaid.set('Enter Amt. Paid')

    friesEntry.configure(state=DISABLED)
    saladEntry.configure(state=DISABLED)
    vegSandwichEntry.configure(state=DISABLED)
    chickSandwichEntry.configure(state=DISABLED)
    vegPastaEntry.configure(state=DISABLED)
    chickPastaEntry.configure(state=DISABLED)
    potatoPopsEntry.configure(state=DISABLED)
    chickPopsEntry.configure(state=DISABLED)

    appleEntry.configure(state=DISABLED)
    grapeEntry.configure(state=DISABLED)
    orangeEntry.configure(state=DISABLED)
    mosambiEntry.configure(state=DISABLED)

    paneerEntry.configure(state=DISABLED)
    mushroomEntry.configure(state=DISABLED)
    fishEntry.configure(state=DISABLED)
    chickenEntry.configure(state=DISABLED)
    muttonEntry.configure(state=DISABLED)
    duckEntry.configure(state=DISABLED)

    vegHakkaEntry.configure(state=DISABLED)
    chickHakkaEntry.configure(state=DISABLED)
    porkHakkaEntry.configure(state=DISABLED)
    prawnHakkaEntry.configure(state=DISABLED)
    chineseChopEntry.configure(state=DISABLED)
    americanChopEntry.configure(state=DISABLED)
    canadianChopEntry.configure(state=DISABLED)    
    dragonChopEntry.configure(state=DISABLED)

    bananaEntry.configure(state=DISABLED)
    mangoEntry.configure(state=DISABLED)
    pomeEntry.configure(state=DISABLED)
    oreoEntry.configure(state=DISABLED)    

    changeEntry.configure(state=DISABLED)
    GSTentry.configure(state=DISABLED)
    subtotalEntry.configure(state=DISABLED)
    totalEntry.configure(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)

var1 = IntVar(); var1.set(0); varFries = StringVar(); varFries.set('0')
var2 = IntVar(); var2.set(0); varSalad = StringVar(); varSalad.set('0')
var3 = IntVar(); var3.set(0); varVegSandwich = StringVar(); varVegSandwich.set('0')
var4 = IntVar(); var4.set(0); varChickSandwich = StringVar(); varChickSandwich.set('0')
var5 = IntVar(); var5.set(0); varVegPasta = StringVar(); varVegPasta.set('0')
var6 = IntVar(); var6.set(0); varChickPasta = StringVar(); varChickPasta.set('0')
var7 = IntVar(); var7.set(0); varPotatoPops = StringVar(); varPotatoPops.set('0')
var8 = IntVar(); var8.set(0); varChickPops = StringVar(); varChickPops.set('0')
var9 = IntVar(); var9.set(0); varApple = StringVar(); varApple.set('0')
var10 = IntVar(); var10.set(0); varGrape = StringVar(); varGrape.set('0')
var11 = IntVar(); var11.set(0); varOrange = StringVar(); varOrange.set('0')
var12 = IntVar(); var12.set(0); varMosambi = StringVar(); varMosambi.set('0')
var13 = IntVar(); var13.set(0); varPaneer = StringVar(); varPaneer.set('0') 
var14 = IntVar(); var14.set(0); varMushroom = StringVar(); varMushroom.set('0')
var15 = IntVar(); var15.set(0); varFish = StringVar(); varFish.set('0')
var16 = IntVar(); var16.set(0); varChicken = StringVar(); varChicken.set('0')
var17 = IntVar(); var17.set(0); varMutton = StringVar(); varMutton.set('0')
var18 = IntVar(); var18.set(0); varDuck = StringVar(); varDuck.set('0')
var19 = IntVar(); var19.set(0); varVegHakka = StringVar(); varVegHakka.set('0')
var20 = IntVar(); var20.set(0); varChickHakka = StringVar(); varChickHakka.set('0')
var21 = IntVar(); var21.set(0); varPorkHakka = StringVar(); varPorkHakka.set('0')
var22 = IntVar(); var22.set(0); varPrawnHakka = StringVar(); varPrawnHakka.set('0')
var23 = IntVar(); var23.set(0); varChinese = StringVar(); varChinese.set('0')
var24 = IntVar(); var24.set(0); varAmerican = StringVar(); varAmerican.set('0')
var25 = IntVar(); var25.set(0); varCanadian = StringVar(); varCanadian.set('0')
var26 = IntVar(); var26.set(0); varDragon = StringVar(); varDragon.set('0')
var27 = IntVar(); var27.set(0); varBanana = StringVar(); varBanana.set('0')
var28 = IntVar(); var28.set(0); varMango = StringVar(); varMango.set('0')
var29 = IntVar(); var29.set(0); varPome = StringVar(); varPome.set('0')
var30 = IntVar(); var30.set(0); varOreo = StringVar(); varOreo.set('0')
                                                                   


#==========ITEMS ON THE LEFT FRAME==========
#-------------------------------------------
#---STARTER LABEL---
starter = Label(LeftFrame,text='STARTERS\t\t\n',font=('Helvetica',18,'underline'))
starter.grid(row=0,column=0)
#---1.FRIES----
def chkFries():
    if(var1.get()==1):
        friesEntry.configure(state=NORMAL)
        varFries.set('')
    else:
        friesEntry.configure(state=DISABLED)
        varFries.set('0')
    
fries = Checkbutton(LeftFrame,text='French Fries\t\tRs.60',variable=var1,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkFries)
fries.grid(row=1,column=0,sticky=W)
friesEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                  textvariable=varFries,justify='right')
friesEntry.grid(row=1,column=1)
#---2.SALAD---
def chkSalad():
    if(var2.get()==1):
        saladEntry.configure(state=NORMAL)
        varSalad.set('')
    else:
        saladEntry.configure(state=DISABLED)
        varSalad.set('0')
        
salad = Checkbutton(LeftFrame,text='Salad\t\t\tRs.45',variable=var2,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkSalad)
salad.grid(row=2,column=0,sticky=W)
saladEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varSalad,justify='right')
saladEntry.grid(row=2,column=1)
#---3.VEG SANDWICH---
def chkVegSand():
    if(var3.get()==1):
        vegSandwichEntry.configure(state=NORMAL)
        varVegSandwich.set('')
    else:
        vegSandwichEntry.configure(state=DISABLED)
        varVegSandwich.set('0')        

vegSandwich = Checkbutton(LeftFrame,text='Veg Sandwich\t\tRs.90',variable=var3,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkVegSand)
vegSandwich.grid(row=3,column=0,sticky=W)
vegSandwichEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varVegSandwich,justify='right')
vegSandwichEntry.grid(row=3,column=1)
#---4.CHICKEN SANDWICH---
def chkChickSand():
    if(var4.get()==1):
        chickSandwichEntry.configure(state=NORMAL)
        varChickSandwich.set('')
    else:
        chickSandwichEntry.configure(state=DISABLED)
        varChickSandwich.set('0')        

chickSandwich = Checkbutton(LeftFrame,text='Chicken Sandwich\t\tRs.120',variable=var4,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkChickSand)
chickSandwich.grid(row=4,column=0,sticky=W)
chickSandwichEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varChickSandwich,justify='right')
chickSandwichEntry.grid(row=4,column=1)
#---5.VEG PASTA---
def chkVegPasta():
    if(var5.get()==1):
        vegPastaEntry.configure(state=NORMAL)
        varVegPasta.set('')
    else:
        vegPastaEntry.configure(state=DISABLED)
        varVegPasta.set('0')
        
vegPasta = Checkbutton(LeftFrame,text='Veg Pasta\t\tRs.150',variable=var5,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkVegPasta)
vegPasta.grid(row=5,column=0,sticky=W)
vegPastaEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varVegPasta,justify='right')
vegPastaEntry.grid(row=5,column=1)
#---6.CHICKEN PASTA---
def chkChickPasta():
    if(var6.get()==1):
        chickPastaEntry.configure(state=NORMAL)
        varChickPasta.set('')
    else:
        chickPastaEntry.configure(state=DISABLED)
        varChickPasta.set('0')
        
chickPasta = Checkbutton(LeftFrame,text='Chicken Pasta\t\tRs.180',variable=var6,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkChickPasta)
chickPasta.grid(row=6,column=0,sticky=W)
chickPastaEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varChickPasta,justify='right')
chickPastaEntry.grid(row=6,column=1)
#---7.POTATO POPS---
def chkPotato():
    if(var7.get()==1):
        potatoPopsEntry.configure(state=NORMAL)
        varPotatoPops.set('')
    else:
        potatoPopsEntry.configure(state=DISABLED)
        varPotatoPops.set('0')
        
potatoPops = Checkbutton(LeftFrame,text='Potato Pops\t\tRs.100',variable=var7,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkPotato)
potatoPops.grid(row=7,column=0,sticky=W)
potatoPopsEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varPotatoPops,justify='right')
potatoPopsEntry.grid(row=7,column=1)
#---8.CHICKEN POPS---
def chkChicken():
    if(var8.get()==1):
        chickPopsEntry.configure(state=NORMAL)
        varChickPops.set('')
    else:
        chickPopsEntry.configure(state=DISABLED)
        varChickPops.set('0')
        
chickPops = Checkbutton(LeftFrame,text='Chicken Pops\t\tRs.150',variable=var8,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkChicken)
chickPops.grid(row=8,column=0,sticky=W)
chickPopsEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varChickPops,justify='right')
chickPopsEntry.grid(row=8,column=1)


#---FRESH JUICE LABEL---
juice = Label(LeftFrame,text='\nFRESH JUICE\t\t\n',font=('Helvetica',18,'underline'))
juice.grid(row=11,column=0)
#---APPLE JUICE---
def chkApple():
    if(var9.get()==1):
        appleEntry.configure(state=NORMAL)
        varApple.set('')
    else:
        appleEntry.configure(state=DISABLED)
        varApple.set('0')
        
apple = Checkbutton(LeftFrame,text='Apple Juice\t\tRs.60',variable=var9,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkApple)
apple.grid(row=12,column=0,sticky=W)
appleEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varApple,justify='right')
appleEntry.grid(row=12,column=1)
#---GRAPE JUICE---
def chkGrape():
    if(var10.get()==1):
        grapeEntry.configure(state=NORMAL)
        varGrape.set('')
    else:
        grapeEntry.configure(state=DISABLED)
        varGrape.set('0')
        
grape = Checkbutton(LeftFrame,text='Grape Juice\t\tRs.50',variable=var10,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkGrape)
grape.grid(row=13,column=0,sticky=W)
grapeEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varGrape,justify='right')
grapeEntry.grid(row=13,column=1)
#---ORANGE JUICE---
def chkOrange():
    if(var11.get()==1):
        orangeEntry.configure(state=NORMAL)
        varOrange.set('')
    else:
        orangeEntry.configure(state=DISABLED)
        varOrange.set('0')
        
orange = Checkbutton(LeftFrame,text='Orange Juice\t\tRs.50',variable=var11,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkOrange)
orange.grid(row=14,column=0,sticky=W)
orangeEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varOrange,justify='right')
orangeEntry.grid(row=14,column=1)
#---MOSAMBI JUICE---
def chkMosambi():
    if(var12.get()==1):
        mosambiEntry.configure(state=NORMAL)
        varMosambi.set('')
    else:
        mosambiEntry.configure(state=DISABLED)
        varMosambi.set('0')
        
mosambi = Checkbutton(LeftFrame,text='Mosambi Juice\t\tRs.50',variable=var12,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkMosambi)
mosambi.grid(row=15,column=0,sticky=W)
mosambiEntry = Entry(LeftFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varMosambi,justify='right')
mosambiEntry.grid(row=15,column=1)
#---BOTTOM SPACE LABEL---
space = Label(LeftFrame,text='                                          ')
space.grid(row=16,column=0)

#==========ITEMS ON THE TOP MID FRAME==========
#----------------------------------------------
#---MEALS LABEL---
meals = Label(MidTopFrame,text='STEAK MEALS\t\t\n',font=('Helvetica',18,'underline'))
meals.grid(row=0,column=0)
#---PANEER MEAL---
def chkPaneerM():
    if(var13.get()==1):
        paneerEntry.configure(state=NORMAL)
        varPaneer.set('')
    else:
        paneerEntry.configure(state=DISABLED)
        varPaneer.set('0')
        
paneer = Checkbutton(MidTopFrame,text='Paneer Steak\t\tRs.180',variable=var13,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkPaneerM)
paneer.grid(row=1,column=0,sticky=W)
paneerEntry = Entry(MidTopFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                  textvariable=varPaneer,justify='right')
paneerEntry.grid(row=1,column=1)
#---MUSHROOM MEAL---
def chkMushroomM():
    if(var14.get()==1):
        mushroomEntry.configure(state=NORMAL)
        varMushroom.set('')
    else:
        mushroomEntry.configure(state=DISABLED)
        varMushroom.set('0')
        
mushroom = Checkbutton(MidTopFrame,text='Mushroom Steak\t\tRs.150',variable=var14,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkMushroomM)
mushroom.grid(row=2,column=0,sticky=W)
mushroomEntry = Entry(MidTopFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                  textvariable=varMushroom,justify='right')
mushroomEntry.grid(row=2,column=1)
#---FISH MEAL---
def chkFishM():
    if(var15.get()==1):
        fishEntry.configure(state=NORMAL)
        varFish.set('')
    else:
        fishEntry.configure(state=DISABLED)
        varFish.set('0')
        
fish = Checkbutton(MidTopFrame,text='Fish Steak\t\tRs.220',variable=var15,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkFishM)
fish.grid(row=3,column=0,sticky=W)
fishEntry = Entry(MidTopFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                  textvariable=varFish,justify='right')
fishEntry.grid(row=3,column=1)
#---CHICKEN MEAL---
def chkChickenM():
    if(var16.get()==1):
        chickenEntry.configure(state=NORMAL)
        varChicken.set('')
    else:
        chickenEntry.configure(state=DISABLED)
        varChicken.set('0')
        
chicken = Checkbutton(MidTopFrame,text='Chicken Steak\t\tRs.200',variable=var16,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkChickenM)
chicken.grid(row=4,column=0,sticky=W)
chickenEntry = Entry(MidTopFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                  textvariable=varChicken,justify='right')
chickenEntry.grid(row=4,column=1)
#---MUTTON MEAL---
def chkMuttonM():
    if(var17.get()==1):
        muttonEntry.configure(state=NORMAL)
        varMutton.set('')
    else:
        muttonEntry.configure(state=DISABLED)
        varMutton.set('0')
        
mutton = Checkbutton(MidTopFrame,text='Mutton Steak\t\tRs.260',variable=var17,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkMuttonM)
mutton.grid(row=5,column=0,sticky=W)
muttonEntry = Entry(MidTopFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                  textvariable=varMutton,justify='right')
muttonEntry.grid(row=5,column=1)
#---DUCK MEAL---
def chkDuckM():
    if(var18.get()==1):
        duckEntry.configure(state=NORMAL)
        varDuck.set('')
    else:
        duckEntry.configure(state=DISABLED)
        varDuck.set('0')
        
duck = Checkbutton(MidTopFrame,text='Duck Steak\t\tRs.300',variable=var18,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkDuckM)
duck.grid(row=6,column=0,sticky=W)
duckEntry = Entry(MidTopFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                  textvariable=varDuck,justify='right')
duckEntry.grid(row=6,column=1)

#==========ITEMS ON THE RIGHT FRAME==========
#--------------------------------------------
#---NODDLE LABEL---
noddle = Label(RightFrame,text='NODDLE\t\t\n',font=('Helvetica',18,'underline'))
noddle.grid(row=0,column=0,sticky=W)
#---1.VEG HAKKA NODDLE----
def chkVegHakka():
    if(var19.get()==1):
        vegHakkaEntry.configure(state=NORMAL)
        varVegHakka.set('')
    else:
        vegHakkaEntry.configure(state=DISABLED)
        varVegHakka.set('0')
        
vegHakka = Checkbutton(RightFrame,text='Veg Hakka Noddle\t\tRs.180',variable=var19,onvalue=1,
                offvalue=0,font=('Times',15,'italic'),command=chkVegHakka)
vegHakka.grid(row=1,column=0,sticky=W)
vegHakkaEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                  textvariable=varVegHakka,justify='right')
vegHakkaEntry.grid(row=1,column=1,)
#---2.CHICKEN HAKKA NODDLE---
def chkChickHakka():
    if(var20.get()==1):
        chickHakkaEntry.configure(state=NORMAL)
        varChickHakka.set('')
    else:
        chickHakkaEntry.configure(state=DISABLED)
        varChickHakka.set('0')
        
chickHakka = Checkbutton(RightFrame,text='Chicken Hakka Noddle\tRs.210',variable=var20,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkChickHakka)
chickHakka.grid(row=2,column=0,sticky=W)
chickHakkaEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varChickHakka,justify='right')
chickHakkaEntry.grid(row=2,column=1)
#---3.PORK HAKKA NODDLE---
def chkPorkHakka():
    if(var21.get()==1):
        porkHakkaEntry.configure(state=NORMAL)
        varPorkHakka.set('')
    else:
        porkHakkaEntry.configure(state=DISABLED)
        varPorkHakka.set('0')

porkHakka = Checkbutton(RightFrame,text='Pork Hakka Noddle\t\tRs.230',variable=var21,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkPorkHakka)
porkHakka.grid(row=3,column=0,sticky=W)
porkHakkaEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varPorkHakka,justify='right')
porkHakkaEntry.grid(row=3,column=1)
#---4.PRAWN HAKKA NODDLE---
def chkPrawnHakka():
    if(var22.get()==1):
        prawnHakkaEntry.configure(state=NORMAL)
        varPrawnHakka.set('')
    else:
        prawnHakkaEntry.configure(state=DISABLED)
        varPrawnHakka.set('0')

prawnHakka = Checkbutton(RightFrame,text='Prawn Hakka Noddle\tRs.250',variable=var22,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkPrawnHakka)
prawnHakka.grid(row=4,column=0,sticky=W)
prawnHakkaEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varPrawnHakka,justify='right')
prawnHakkaEntry.grid(row=4,column=1)
#---5.CHINESE CHOPSUEY---
def chkChinese():
    if(var23.get()==1):
        chineseChopEntry.configure(state=NORMAL)
        varChinese.set('')
    else:
        chineseChopEntry.configure(state=DISABLED)
        varChinese.set('0')

chineseChop = Checkbutton(RightFrame,text='Chinese Chopsuey\t\tRs.200',variable=var23,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkChinese)
chineseChop.grid(row=5,column=0,sticky=W)
chineseChopEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varChinese,justify='right')
chineseChopEntry.grid(row=5,column=1)
#---6.AMERICAN CHOPSUEY---
def chkAmerican():
    if(var24.get()==1):
        americanChopEntry.configure(state=NORMAL)
        varAmerican.set('')
    else:
        americanChopEntry.configure(state=DISABLED)
        varAmerican.set('0')

americanChop = Checkbutton(RightFrame,text='American Chopsuey\tRs.200',variable=var24,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkAmerican)
americanChop.grid(row=6,column=0,sticky=W)
americanChopEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varAmerican,justify='right')
americanChopEntry.grid(row=6,column=1)
#---7.CANADIAN CHOPSUEY---
def chkCanadian():
    if(var25.get()==1):
        canadianChopEntry.configure(state=NORMAL)
        varCanadian.set('')
    else:
        canadianChopEntry.configure(state=DISABLED)
        varCanadian.set('0')

canadianChop = Checkbutton(RightFrame,text='Canadian Chopsuey\tRs.220',variable=var25,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkCanadian)
canadianChop.grid(row=7,column=0,sticky=W)
canadianChopEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varCanadian,justify='right')
canadianChopEntry.grid(row=7,column=1)
#---8.DRAGON CHOPSUEY---
def chkDragon():
    if(var26.get()==1):
        dragonChopEntry.configure(state=NORMAL)
        varDragon.set('')
    else:
        dragonChopEntry.configure(state=DISABLED)
        varDragon.set('0')

dragonChop= Checkbutton(RightFrame,text='Dragon Chopsuey\t\tRs.220',variable=var26,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkDragon)
dragonChop.grid(row=8,column=0,sticky=W)
dragonChopEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varDragon,justify='right')
dragonChopEntry.grid(row=8,column=1)


#---MILKSHAKES LABEL---
juice = Label(RightFrame,text='\nMILK SHAKES\t\t\n',font=('Helvetica',18,'underline'))
juice.grid(row=11,column=0)
#---1.BANANA MILKSHAKE---
def chkBanana():
    if(var27.get()==1):
        bananaEntry.configure(state=NORMAL)
        varBanana.set('')
    else:
        bananaEntry.configure(state=DISABLED)
        varBanana.set('0')

banana = Checkbutton(RightFrame,text='Banana\t\t\tRs.40',variable=var27,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkBanana)
banana.grid(row=12,column=0,sticky=W)
bananaEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varBanana,justify='right')
bananaEntry.grid(row=12,column=1)
#---2.MANGO MILKSHAKE---
def chkMango():
    if(var28.get()==1):
        mangoEntry.configure(state=NORMAL)
        varMango.set('')
    else:
        mangoEntry.configure(state=DISABLED)
        varMango.set('0')

mango = Checkbutton(RightFrame,text='Mango\t\t\tRs.60',variable=var28,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkMango)
mango.grid(row=13,column=0,sticky=W)
mangoEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varMango,justify='right')
mangoEntry.grid(row=13,column=1)
#---3.POMEGRANATE MILKSHAKE---
def chkPome():
    if(var29.get()==1):
        pomeEntry.configure(state=NORMAL)
        varPome.set('')
    else:
        pomeEntry.configure(state=DISABLED)
        varPome.set('0')

pome = Checkbutton(RightFrame,text='Pomegranate\t\tRs.70',variable=var29,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkPome)
pome.grid(row=14,column=0,sticky=W)
pomeEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varPome,justify='right')
pomeEntry.grid(row=14,column=1)
#---4.OREO MILKSHAKE---
def chkOreo():
    if(var30.get()==1):
        oreoEntry.configure(state=NORMAL)
        varOreo.set('')
    else:
        oreoEntry.configure(state=DISABLED)
        varOreo.set('0')

oreo = Checkbutton(RightFrame,text='Oreo\t\t\tRs.50',variable=var30,onvalue=1,
                    offvalue=0,font=('Times',15,'italic'),command=chkOreo)
oreo.grid(row=15,column=0,sticky=W)
oreoEntry = Entry(RightFrame,font=('Verdana',15,'italic'),width=6,state=DISABLED,
                   textvariable=varOreo,justify='right')
oreoEntry.grid(row=15,column=1)
#---BOTTOM SPACE LABEL---
space = Label(RightFrame,text='                                          ')
space.grid(row=16,column=0)

#==========WIDGETS ON THE BOTTOM MID FRAME==========
varChange = StringVar(); varChange.set('0')
varGST = StringVar(); varGST.set('0')
varSubTotal = StringVar(); varSubTotal.set('0')
varTotal = StringVar(); varTotal.set('0')
varPayment = StringVar(); varPayment.set('Cash')
varPaid = StringVar(); varPaid.set('Enter Amt. Paid')


#---------------------------------------------------
#Label for payment method
paymentMethod = Label(MidBottomFrame,text='Payment Method',bd=10,width=16
                      ,anchor='w',font=('arial',14,'bold'))
paymentMethod.grid(row=0,column=0)

#Change to be returned to the customer
change = Label(MidBottomFrame,text='Change',bd=10,anchor='w',
               font=('arial',14,'bold'))
change.grid(row=0,column=1)
changeEntry = Entry(MidBottomFrame,font=('arial',18,'bold'),textvariable=varChange,
                    width=6,state=DISABLED,justify='right')
changeEntry.grid(row=0,column=2)

#Select payment method
v = ['Debit Card','Credit Card','Cash','E-Wallet']
paymentCombo = Combobox(MidBottomFrame,textvariable = varPayment,state='readonly',
                        font=('arial',10,'bold'),width=20,value=v)
paymentCombo.grid(row=1,column=0)

#GST Label and Entry
GST = Label(MidBottomFrame,text='GST',bd=10,anchor='w',font=('arial',14,'bold'))
GST.grid(row=1,column=1)
GSTentry = Entry(MidBottomFrame,textvariable=varGST,font=('arial',18,'bold'),
                 width=6,justify='right',state=DISABLED)
GSTentry.grid(row=1,column=2)

#Amount paid by the customer
txtpaid = Entry(MidBottomFrame,font=('arial',12,'bold'),textvariable=varPaid,
                width=20,justify='left',)
txtpaid.grid(row=2,column=0,)

#Subtotal
subtotal = Label(MidBottomFrame,text='Sub Total',font=('arial',14,'bold'),bd=10,
                 width=8,anchor='w')
subtotal.grid(row=2,column=1)
subtotalEntry = Entry(MidBottomFrame,textvariable = varSubTotal,justify='right',
                      state=DISABLED,width=6,font=('arial',18,'bold'))
subtotalEntry.grid(row=2,column=2)
#Total
total = Label(MidBottomFrame,text='Total',font=('arial',14,'bold'),bd=10,width=6,
              anchor='w')
total.grid(row=3,column=1)
totalEntry = Entry(MidBottomFrame,font=('arial',18,'bold'),width=6,justify='right',
                   state=DISABLED,textvariable=varTotal)
totalEntry.grid(row=3,column=2)

#=======BUTTONS=======
def Destroy():
    result = messagebox.askyesno("APRATIM'S KITCHEN",'Are you sure?')
    if(result==True):
        root.destroy()

    
#Total Button
total = Button(MidBottomFrame,text='Total',fg='black',bg='red4',padx=16,pady=1,
               bd=4,font=('Verdana',14,'bold'),width=5,command=GrandTotal)
total.grid(row=5,column=0,sticky=W)
#Reset Button
reset = Button(MidBottomFrame,text='Reset',fg='black',bg='red4',padx=16,pady=1,
               bd=4,font=('Verdana',14,'bold'),width=5,command=Reset)
reset.grid(row=5,column=2,sticky=W)
#Change Button
change = Button(MidBottomFrame,text='Change',fg='black',bg='red4',padx=16,pady=1,
               bd=4,font=('Verdana',14,'bold'),width=5,command=Change)
change.grid(row=6,column=0,sticky=W)
#Close Button
close = Button(MidBottomFrame,text='Exit',fg='black',bg='red4',padx=16,pady=1,
               bd=4,font=('Verdana',14,'bold'),width=5,command=Destroy)
close.grid(row=6,column=2,sticky=W)


#Putting space at the bottom
lastspace = Label(MidBottomFrame,text='\n\n\n')
lastspace.grid(row=6,column=0)





root.geometry('1350x750+0+0')
root.mainloop()
