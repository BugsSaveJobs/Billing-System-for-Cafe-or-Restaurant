from tkinter import *
import random
import time;
import datetime
from tkinter import Tk,StringVar,ttk,IntVar,messagebox

root=Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management system")

Tops = Frame(root, width =1350, height=100, bd=12, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="              INDIAN CUISINE              ")
lblTitle.grid(row=0, column=0)

BottomMainFrame = Frame(root, width =1350, height=650, bd=4, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame(BottomMainFrame, width =450, height=650, bd=4, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(BottomMainFrame, width =450, height=650, bd=4, relief="raise")
f2.pack(side=LEFT)
f2TOP = Frame(f2, width =450, height=350, bd=4, relief="raise")
f2TOP.pack(side=TOP)
f2BOTTOM = Frame(f2, width =450, height=300, bd=4, relief="raise")
f2BOTTOM.pack(side=BOTTOM)

f3 = Frame(BottomMainFrame, width=450, height=650, bd=12, relief="raise")
f3.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()
var37=IntVar()
var38=IntVar()
var39=IntVar()
var40=IntVar()
var41=IntVar()
var42=IntVar()
var43=IntVar()
var44=IntVar()






temptotal = StringVar()
varTax = StringVar()
varSubTotal = StringVar()
varTotal = StringVar()
varAfghaniChickenBiryani = StringVar()
varVegbiryani = StringVar()
varChickenCheeseBurger = StringVar()
varVegCheeseBurger = StringVar()
varChickenSpicyBurger = StringVar()
varPaneerTikka = StringVar()
varMalaipaneerTikka = StringVar()
varStirFryChicken = StringVar()
varMurgBasilTikka = StringVar()
varTandooriLollypop = StringVar()
varVegbiryani = StringVar()
varChickenReshmiKabab = StringVar()
varPaneerTikkaHarimirch = StringVar()
varGobiMasala = StringVar()
varVegKolhapuri = StringVar()
varMixVegetable = StringVar()
varPaneerButterMasala = StringVar()
varKadhaiChicken = StringVar()
varCoffee = StringVar()
varTea = StringVar()
varCaféLatte = StringVar()
varCoconutSoup = StringVar()
varVegManchowSoup = StringVar()
varMangoLassi = StringVar()
varSweetLassi = StringVar()
varSodaPop = StringVar()
varAlooKulcha = StringVar()
varCheeseGarlicNaan = StringVar()
varOnionkulcha = StringVar()
varButterNaan = StringVar()
varPaneerKulcha = StringVar()
varPlainKulcha = StringVar()
varPaneerParatha = StringVar()
varGarlicNaan = StringVar()
varChillyParatha = StringVar()
varChickenSingaporeNoodles = StringVar()
varJeeraRice = StringVar()
varVegDumBiryani = StringVar()
varMixFriedRice = StringVar()
varEggFriedRice = StringVar()
varOnionSalad = StringVar()
varGreenSalad = StringVar()
varAlooRaita = StringVar()
varMixVegRaita = StringVar()

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
var31.set(0)
var32.set(0)
var33.set(0)
var34.set(0)
var35.set(0)
var36.set(0)
var37.set(0)
var38.set(0)
var39.set(0)
var40.set(0)
var41.set(0)
var42.set(0)
var43.set(0)
var44.set(0)


varAfghaniChickenBiryani.set('0')
varVegbiryani.set('0')
varChickenCheeseBurger.set('0')
varVegCheeseBurger.set('0')
varChickenSpicyBurger.set('0')
varPaneerTikka.set('0')
varMalaipaneerTikka.set('0')
varStirFryChicken.set('0')
varMurgBasilTikka.set('0')
varTandooriLollypop.set('0')
varChickenReshmiKabab.set('0')
varPaneerTikkaHarimirch.set('0')
varVegKolhapuri.set('0')
varMixVegetable.set('0')
varPaneerButterMasala.set('0')
varKadhaiChicken.set('0')
varGobiMasala.set('0')
varCoffee.set('0')
varTea.set('0')
varCaféLatte.set('0')
varCoconutSoup.set('0')
varVegManchowSoup.set('0')
varMangoLassi.set('0')
varSweetLassi.set('0')
varSodaPop.set('0')
varAlooKulcha.set('0')
varCheeseGarlicNaan.set('0')
varOnionkulcha.set('0')
varButterNaan.set('0')
varPaneerKulcha.set('0')
varPlainKulcha.set('0')
varPaneerParatha.set('0')
varGarlicNaan.set('0')
varChillyParatha.set('0')
varChickenSingaporeNoodles.set('0')
varJeeraRice.set('0')
varVegDumBiryani.set('0')
varMixFriedRice.set('0')
varEggFriedRice.set('0')
varOnionSalad.set('0')
varGreenSalad.set('0')
varAlooRaita.set('0')
varMixVegRaita.set('0')

varTax.set('0')
varSubTotal.set('0')
varTotal.set('0')



def iExit():
	qExit = messagebox.askyesno("Quit System","Are you Sure ?")
	if qExit > 0:
		root.destroy()
		return

def Reset():

	varTax.set('0')
	varSubTotal.set('0')
	varTotal.set('0')

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
	var31.set(0)
	var32.set(0)
	var33.set(0)
	var34.set(0)
	var35.set(0)
	var36.set(0)
	var37.set(0)
	var38.set(0)
	var39.set(0)
	var40.set(0)
	var41.set(0)
	var42.set(0)
	var43.set(0)
	var44.set(0)
	varAfghaniChickenBiryani.set('0')
	varVegbiryani.set('0')
	varChickenCheeseBurger.set('0')
	varVegCheeseBurger.set('0')
	varChickenSpicyBurger.set('0')
	varPaneerTikka.set('0')
	varMalaipaneerTikka.set('0')
	varMurgBasilTikka.set('0')
	varTandooriLollypop.set('0')
	varChickenReshmiKabab.set('0')
	varPaneerTikkaHarimirch.set('0')
	varVegKolhapuri.set('0')
	varMixVegetable.set('0')
	varPaneerButterMasala.set('0')
	varKadhaiChicken.set('0')
	varCoffee.set('0')
	varTea.set('0')
	varCaféLatte.set('0')
	varCoconutSoup.set('0')
	varVegManchowSoup.set('0')
	varMangoLassi.set('0')
	varSweetLassi.set('0')
	varSodaPop.set('0')
	varAlooKulcha.set('0')
	varCheeseGarlicNaan.set('0')
	varOnionkulcha.set('0')
	varButterNaan.set('0')
	varPaneerKulcha.set('0')
	varPlainKulcha.set('0')
	varPaneerParatha.set('0')
	varGarlicNaan.set('0')
	varChillyParatha.set('0')
	varChickenSingaporeNoodles.set('0')
	varJeeraRice.set('0')
	varVegDumBiryani.set('0')
	varMixFriedRice.set('0')
	varEggFriedRice.set('0')
	varOnionSalad.set('0')
	varGreenSalad.set('0')
	varAlooRaita.set('0')
	varMixVegRaita.set('0')


	txtAfghaniChickenBiryani.configure(state=DISABLED)
	txtVegbiryani.configure(state=DISABLED)
	txtChickenCheeseBurger.configure(state=DISABLED)
	txtVegCheeseBurger.configure(state=DISABLED)
	txtChickenSpicyBurger.configure(state=DISABLED)
	txtPaneerTikka.configure(state=DISABLED)
	txtMalaipaneerTikka.configure(state=DISABLED)
	txtStirFryChicken.configure(state=DISABLED)
	txtMurgBasilTikka.configure(state=DISABLED)
	txtTandooriLollypop.configure(state=DISABLED)
	txtChickenReshmiKabab.configure(state=DISABLED)
	txtPaneerTikkaHarimirch.configure(state=DISABLED)
	txtGobiMasala.configure(state=DISABLED)
	txtVegKolhapuri.configure(state=DISABLED)
	txtMixVegetable.configure(state=DISABLED)
	txtPaneerButterMasala.configure(state=DISABLED)
	txtKadhaiChicken.configure(state=DISABLED)
	txtCoffee.configure(state=DISABLED)
	txtTea.configure(state=DISABLED)
	txtCaféLatte.configure(state=DISABLED)
	txtCoconutSoup.configure(state=DISABLED)
	txtVegManchowSoup.configure(state=DISABLED)
	txtMangoLassi.configure(state=DISABLED)
	txtSweetLassi.configure(state=DISABLED)
	txtSodaPop.configure(state=DISABLED)
	txtAlooKulcha.configure(state=DISABLED)
	txtCheeseGarlicNaan.configure(state=DISABLED)
	txtOnionkulcha.configure(state=DISABLED)
	txtButterNaan.configure(state=DISABLED)
	txtPaneerKulcha.configure(state=DISABLED)
	txtPlainKulcha.configure(state=DISABLED)
	txtPaneerParatha.configure(state=DISABLED)
	txtGarlicNaan.configure(state=DISABLED)
	txtChillyParatha.configure(state=DISABLED)
	txtChickenSingaporeNoodles.configure(state=DISABLED)
	txtJeeraRice.configure(state=DISABLED)
	txtVegDumBiryani.configure(state=DISABLED)
	txtMixFriedRice.configure(state=DISABLED)
	txtEggFriedRice.configure(state=DISABLED)
	txtOnionSalad.configure(state=DISABLED)
	txtGreenSalad.configure(state=DISABLED)
	txtAlooRaita.configure(state=DISABLED)
	txtMixVegRaita.configure(state=DISABLED)


def chkVegbiryani():
	if (var1.get() == 1):
		txtVegbiryani.configure(state=NORMAL)
		varVegbiryani.set("")
	elif (var1.get() == 0):
		txtVegbiryani.configure(state=DISABLED)
		varVegbiryani.set("0")

def chkPaneerTikkaHarimirch():
	if (var2.get() == 1):
		txtPaneerTikkaHarimirch.configure(state=NORMAL)
		varPaneerTikkaHarimirch.set("")
	elif (var2.get() == 0):
		txtPaneerTikkaHarimirch.configure(state=DISABLED)
		varPaneerTikkaHarimirch.set("0")

def chkGobiMasala():
	if (var3.get() == 1):
		txtGobiMasala.configure(state=NORMAL)
		varGobiMasala.set("")
	elif (var3.get() == 0):
		txtGobiMasala.configure(state=DISABLED)
		varGobiMasala.set("0")


def chkVegKolhapuri():
	if (var4.get() == 1):
		txtVegKolhapuri.configure(state=NORMAL)
		varVegKolhapuri.set("")
	elif (var4.get() == 0):
		txtVegKolhapuri.configure(state=DISABLED)
		varVegKolhapuri.set("0")

def chkMixVegetable():
	if (var5.get() == 1):
		txtMixVegetable.configure(state=NORMAL)
		varMixVegetable.set("")
	elif (var5.get() == 0):
		txtMixVegetable.configure(state=DISABLED)
		varMixVegetable.set("0")

def chkPaneerButterMasala():
	if (var6.get() == 1):
		txtPaneerButterMasala.configure(state=NORMAL)
		varPaneerButterMasala.set("")
	elif (var6.get() == 0):
		txtPaneerButterMasala.configure(state=DISABLED)
		varPaneerButterMasala.set("0")

def chkVegCheeseBurger():
	if (var7.get() == 1):
		txtVegCheeseBurger.configure(state=NORMAL)
		varVegCheeseBurger.set("")
	elif (var7.get() == 0):
		txtVegCheeseBurger.configure(state=DISABLED)
		varVegCheeseBurger.set("0")

def chkPaneerTikka():
	if (var8.get() == 1):
		txtPaneerTikka.configure(state=NORMAL)
		varPaneerTikka.set("")
	elif (var8.get() == 0):
		txtPaneerTikka.configure(state=DISABLED)
		varPaneerTikka.set("0")

def chkMalaipaneerTikka():
	if (var9.get() == 1):
		txtMalaipaneerTikka.configure(state=NORMAL)
		varMalaipaneerTikka.set("")
	elif (var9.get() == 0):
		txtMalaipaneerTikka.configure(state=DISABLED)
		varMalaipaneerTikka.set("0")

#=========================== NON - VEG ITEMS =========================================


def chkAfghaniChickenBiryani():
	if (var10.get() == 1):
		txtAfghaniChickenBiryani.configure(state=NORMAL)
		varAfghaniChickenBiryani.set("")
	elif (var10.get() == 0):
		txtAfghaniChickenBiryani.configure(state=DISABLED)
		varAfghaniChickenBiryani.set("0")

def chkStirFryChicken():
	if (var11.get() == 1):
		txtStirFryChicken.configure(state=NORMAL)
		varStirFryChicken.set("")
	elif (var11.get() == 0):
		txtStirFryChicken.configure(state=DISABLED)
		varStirFryChicken.set("0")

def chkMurgBasilTikka():
	if (var12.get() == 1):
		txtMurgBasilTikka.configure(state=NORMAL)
		varMurgBasilTikka.set("")
	elif (var12.get() == 0):
		txtMurgBasilTikka.configure(state=DISABLED)
		varMurgBasilTikka.set("0")

def chkTandooriLollypop():
	if (var13.get() == 1):
		txtTandooriLollypop.configure(state=NORMAL)
		varTandooriLollypop.set("")
	elif (var13.get() == 0):
		txtTandooriLollypop.configure(state=DISABLED)
		varTandooriLollypop.set("0")

def chkChickenSpicyBurger():
	if (var14.get() == 1):
		txtChickenSpicyBurger.configure(state=NORMAL)
		varChickenSpicyBurger.set("")
	elif (var14.get() == 0):
		txtChickenSpicyBurger.configure(state=DISABLED)
		varChickenSpicyBurger.set("0")

def chkChickenReshmiKabab():
	if (var15.get() == 1):
		txtChickenReshmiKabab.configure(state=NORMAL)
		varChickenReshmiKabab.set("")
	elif (var15.get() == 0):
		txtChickenReshmiKabab.configure(state=DISABLED)
		varChickenReshmiKabab.set("0")

def chkChickenCheeseBurger():
	if (var16.get() == 1):
		txtChickenCheeseBurger.configure(state=NORMAL)
		varChickenCheeseBurger.set("")
	elif (var16.get() == 0):
		txtChickenCheeseBurger.configure(state=DISABLED)
		varChickenCheeseBurger.set("0")

def chkKadhaiChicken():
	if (var17.get() == 1):
		txtKadhaiChicken.configure(state=NORMAL)
		varKadhaiChicken.set("")
	elif (var17.get() == 0):
		txtKadhaiChicken.configure(state=DISABLED)
		varKadhaiChicken.set("0")

#=============================  SOUPS AND BEVERAGES  ====================



def chkCoffee():
	if (var18.get() == 1):
		txtCoffee.configure(state=NORMAL)
		varCoffee.set("")
	elif (var18.get() == 0):
		txtCoffee.configure(state=DISABLED)
		varCoffee.set("0")


def chkTea():
	if (var19.get() == 1):
		txtTea.configure(state=NORMAL)
		varTea.set("")
	elif (var19.get() == 0):
		txtTea.configure(state=DISABLED)
		varTea.set("0")

def chkCaféLatte():
	if (var20.get() == 1):
		txtCaféLatte.configure(state=NORMAL)
		varCaféLatte.set("")
	elif (var20.get() == 0):
		txtCaféLatte.configure(state=DISABLED)
		varCaféLatte.set("0")

def chkCoconutSoup():
	if (var21.get() == 1):
		txtCoconutSoup.configure(state=NORMAL)
		varCoconutSoup.set("")
	elif (var21.get() == 0):
		txtCoconutSoup.configure(state=DISABLED)
		varCoconutSoup.set("0")

def chkVegManchowSoup():
	if (var22.get() == 1):
		txtVegManchowSoup.configure(state=NORMAL)
		varVegManchowSoup.set("")
	elif (var22.get() == 0):
		txtVegManchowSoup.configure(state=DISABLED)
		varVegManchowSoup.set("0")

def chkMangoLassi():
	if (var23.get() == 1):
		txtMangoLassi.configure(state=NORMAL)
		varMangoLassi.set("")
	elif (var23.get() == 0):
		txtMangoLassi.configure(state=DISABLED)
		varMangoLassi.set("0")

def chkSweetLassi():
	if (var24.get() == 1):
		txtSweetLassi.configure(state=NORMAL)
		varSweetLassi.set("")
	elif (var24.get() == 0):
		txtSweetLassi.configure(state=DISABLED)
		varSweetLassi.set("0")

def chkSodaPop():
	if (var25.get() == 1):
		txtSodaPop.configure(state=NORMAL)
		varSodaPop.set("")
	elif (var25.get() == 0):
		txtSodaPop.configure(state=DISABLED)
		varSodaPop.set("0")


#========================================  MAIN COURSE  =====================================


def chkAlooKulcha():
	if (var26.get() == 1):
		txtAlooKulcha.configure(state=NORMAL)
		varAlooKulcha.set("")
	elif (var26.get() == 0):
		txtAlooKulcha.configure(state=DISABLED)
		varAlooKulcha.set("0")

def chkCheeseGarlicNaan():
	if (var27.get() == 1):
		txtCheeseGarlicNaan.configure(state=NORMAL)
		varCheeseGarlicNaan.set("")
	elif (var27.get() == 0):
		txtCheeseGarlicNaan.configure(state=DISABLED)
		varCheeseGarlicNaan.set("0")

def chkOnionkulcha():
	if (var28.get() == 1):
		txtOnionkulcha.configure(state=NORMAL)
		varOnionkulcha.set("")
	elif (var28.get() == 0):
		txtOnionkulcha.configure(state=DISABLED)
		varOnionkulcha.set("0")

def chkButterNaan():
	if (var29.get() == 1):
		txtButterNaan.configure(state=NORMAL)
		varButterNaan.set("")
	elif (var29.get() == 0):
		txtButterNaan.configure(state=DISABLED)
		varButterNaan.set("0")

def chkPaneerKulcha():
	if (var30.get() == 1):
		txtPaneerKulcha.configure(state=NORMAL)
		varPaneerKulcha.set("")
	elif (var30.get() == 0):
		txtPaneerKulcha.configure(state=DISABLED)
		varPaneerKulcha.set("0")

def chkGarlicNaan():
	if (var31.get() == 1):
		txtGarlicNaan.configure(state=NORMAL)
		varGarlicNaan.set("")
	elif (var31.get() == 0):
		txtGarlicNaan.configure(state=DISABLED)
		varGarlicNaan.set("0")

def chkPlainKulcha():
	if (var32.get() == 1):
		txtPlainKulcha.configure(state=NORMAL)
		varPlainKulcha.set("")
	elif (var32.get() == 0):
		txtPlainKulcha.configure(state=DISABLED)
		varPlainKulcha.set("0")

def chkPaneerParatha():
	if (var33.get() == 1):
		txtPaneerParatha.configure(state=NORMAL)
		varPaneerParatha.set("")
	elif (var33.get() == 0):
		txtPaneerParatha.configure(state=DISABLED)
		varPaneerParatha.set("0")



def chkChillyParatha():
	if (var34.get() == 1):
		txtChillyParatha.configure(state=NORMAL)
		varChillyParatha.set("")
	elif (var34.get() == 0):
		txtChillyParatha.configure(state=DISABLED)
		varChillyParatha.set("0")

def chkChickenSingaporeNoodles():
	if (var35.get() == 1):
		txtChickenSingaporeNoodles.configure(state=NORMAL)
		varChickenSingaporeNoodles.set("")
	elif (var35.get() == 0):
		txtChickenSingaporeNoodles.configure(state=DISABLED)
		varChickenSingaporeNoodles.set("0")

def chkJeeraRice():
	if (var36.get() == 1):
		txtJeeraRice.configure(state=NORMAL)
		varJeeraRice.set("")
	elif (var36.get() == 0):
		txtJeeraRice.configure(state=DISABLED)
		varJeeraRice.set("0")

def chkVegDumBiryani():
	if (var37.get() == 1):
		txtVegDumBiryani.configure(state=NORMAL)
		varVegDumBiryani.set("")
	elif (var37.get() == 0):
		txtVegDumBiryani.configure(state=DISABLED)
		varVegDumBiryani.set("0")

def chkMixFriedRice():
	if (var38.get() == 1):
		txtMixFriedRice.configure(state=NORMAL)
		varMixFriedRice.set("")
	elif (var38.get() == 0):
		txtMixFriedRice.configure(state=DISABLED)
		varMixFriedRice.set("0")

def chkEggFriedRice():
	if (var39.get() == 1):
		txtEggFriedRice.configure(state=NORMAL)
		varEggFriedRice.set("")
	elif (var39.get() == 0):
		txtEggFriedRice.configure(state=DISABLED)
		varEggFriedRice.set("0")

def chkOnionSalad():
	if (var40.get() == 1):
		txtOnionSalad.configure(state=NORMAL)
		varOnionSalad.set("")
	elif (var40.get() == 0):
		txtOnionSalad.configure(state=DISABLED)
		varOnionSalad.set("0")

def chkGreenSalad():
	if (var41.get() == 1):
		txtGreenSalad.configure(state=NORMAL)
		varGreenSalad.set("")
	elif (var41.get() == 0):
		txtGreenSalad.configure(state=DISABLED)
		varGreenSalad.set("0")

def chkAlooRaita():
	if (var42.get() == 1):
		txtAlooRaita.configure(state=NORMAL)
		varAlooRaita.set("")
	elif (var42.get() == 0):
		txtAlooRaita.configure(state=DISABLED)
		varAlooRaita.set("0")

def chkMixVegRaita():
	if (var43.get() == 1):
		txtMixVegRaita.configure(state=NORMAL)
		varMixVegRaita.set("")
	elif (var43.get() == 0):
		txtMixVegRaita.configure(state=DISABLED)
		varMixVegRaita.set("0")



def TotalCost():
	val1=float(varVegbiryani.get())
	val2=float(varPaneerTikkaHarimirch.get())
	val3=float(varGobiMasala.get())
	val4=float(varVegKolhapuri.get())
	val5=float(varMixVegetable.get())
	val6=float(varPaneerButterMasala.get())
	val7=float(varVegCheeseBurger.get())
	val8=float(varPaneerTikka.get())
	val9=float(varMalaipaneerTikka.get())
	val10=float(varAfghaniChickenBiryani.get())
	val11=float(varStirFryChicken.get())
	val12=float(varMurgBasilTikka.get())
	val13=float(varTandooriLollypop.get())
	val14=float(varChickenSpicyBurger.get())
	val15=float(varChickenReshmiKabab.get())
	val16=float(varChickenCheeseBurger.get())
	val17=float(varKadhaiChicken.get())
	val18=float(varCoffee.get())
	val19=float(varTea.get())
	val20=float(varCaféLatte.get())
	val21=float(varCoconutSoup.get())
	val22=float(varVegManchowSoup.get())
	val23=float(varMangoLassi.get())
	val24=float(varSweetLassi.get())
	val25=float(varSodaPop.get())
	val26=float(varAlooKulcha.get())
	val27=float(varCheeseGarlicNaan.get())
	val28=float(varOnionkulcha.get())
	val29=float(varButterNaan.get())
	val30=float(varPaneerKulcha.get())
	val31=float(varGarlicNaan.get())
	val32=float(varPlainKulcha.get())
	val33=float(varPaneerParatha.get())
	val34=float(varChillyParatha.get())
	val35=float(varChickenSingaporeNoodles.get())
	val36=float(varJeeraRice.get())
	val37=float(varVegDumBiryani.get())
	val38=float(varMixFriedRice.get())
	val39=float(varEggFriedRice.get())
	val40=float(varOnionSalad.get())
	val41=float(varGreenSalad.get())
	val42=float(varAlooRaita.get())
	val43=float(varMixVegRaita.get())
	temptotal = ((val1*140.0) + (val2*210.0) + (val3*140.0) + (val4*220.0) +  (val5*180.0) +  (val6*160.0) + (val7*70.0) + 
		(val8*170.0) + (val9*200.0) + (val10*190.0) + (val11*180.0) + (val12*210.0) + (val13*160.0) + (val14*70.0) + 
		(val15*200.0) + (val16*90.0) + (val17*160.0) + (val18*15.0) + (val19*15.0) + (val20*60.0) + (val21*70.0) + (val22*80.0) + 
		(val23*40.0) + (val24*40.0) + (val25*30.0) + (val26*40.0) + (val27*70.0) + (val28*40.0) + (val29*40.0) +(val30*50.0) + 
		(val31*45.0) + (val32*35.0) + (val33*50.0) + (val34*40.0) + (val35*90.0) + (val36*125.0) + (val37*170.0) + (val38*180.0) + 
		(val39*160.0) + (val40*45.0) + (val41*60.0) + (val42*70.0) + (val43*70.0))

	tax=(temptotal*0.2)
	varTax.set(tax)
	varSubTotal.set(temptotal)
	varTotal.set(temptotal+tax)


#======================================FIRST BLOCK=================================================================

lblMeal = Label(f1, font=('arial', 18, 'bold'), text="\nVEG. MENU\n")
lblMeal.grid(row=0, column=0)


Vegbiryani= Checkbutton(f1, text='Veg. Biryani\t\t( Rs. 140 )', variable=var1, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'), command=lambda: chkVegbiryani()).grid(row=1, column=0, sticky=W)
txtVegbiryani = Entry(f1, font=('arial', 12, 'bold'), textvariable=varVegbiryani, width=6, justify='right', state=DISABLED)
txtVegbiryani.grid(row = 1, column = 1)

PaneerTikkaHarimirch= Checkbutton(f1, text='Paneer Tikka Harimirch\t( Rs. 210 )', variable=var2, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkPaneerTikkaHarimirch()).grid(row=2, column=0, sticky=W)
txtPaneerTikkaHarimirch = Entry(f1, font=('arial', 12, 'bold'), textvariable=varPaneerTikkaHarimirch, width=6, justify='right', state=DISABLED)
txtPaneerTikkaHarimirch.grid(row = 2, column = 1)

GobiMasala= Checkbutton(f1, text='Gobi Masala\t\t( Rs. 140 )', variable=var3, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkGobiMasala()).grid(row=3, column=0, sticky=W)
txtGobiMasala = Entry(f1, font=('arial', 12, 'bold'), textvariable=varGobiMasala, width=6, justify='right', state=DISABLED)
txtGobiMasala.grid(row = 3, column = 1)

VegKolhapuri= Checkbutton(f1, text='Veg Kolhapuri\t\t( Rs. 220 )', variable=var4, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkVegKolhapuri()).grid(row=4, column=0, sticky=W)
txtVegKolhapuri = Entry(f1, font=('arial', 12, 'bold'), textvariable=varVegKolhapuri, width=6, justify='right', state=DISABLED)
txtVegKolhapuri.grid(row = 4, column = 1)

MixVegetable= Checkbutton(f1, text='Mix Vegetable\t\t( Rs. 180 )', variable=var5, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkMixVegetable()).grid(row=5, column=0, sticky=W)
txtMixVegetable = Entry(f1, font=('arial', 12, 'bold'), textvariable=varMixVegetable, width=6, justify='right', state=DISABLED)
txtMixVegetable.grid(row = 5, column = 1)

PaneerButterMasala= Checkbutton(f1, text='Paneer Butter Masala\t( Rs. 160 )', variable=var6, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkPaneerButterMasala()).grid(row=6, column=0, sticky=W)
txtPaneerButterMasala = Entry(f1, font=('arial', 12, 'bold'), textvariable=varPaneerButterMasala, width=6, justify='right', state=DISABLED)
txtPaneerButterMasala.grid(row = 6, column = 1)

VegCheeseBurger= Checkbutton(f1, text='Veg Cheese Burger\t( Rs. 70 )', variable=var7, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'), command=lambda: chkVegCheeseBurger()).grid(row=7, column=0, sticky=W)
txtVegCheeseBurger = Entry(f1, font=('arial', 12, 'bold'), textvariable=VegCheeseBurger, width=6, justify='right', state=DISABLED)
txtVegCheeseBurger.grid(row = 7, column = 1)

PaneerTikka= Checkbutton(f1, text='Paneer Tikka\t\t( Rs. 170 )', variable=var8, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkPaneerTikka()).grid(row=8, column=0, sticky=W)
txtPaneerTikka = Entry(f1, font=('arial', 12, 'bold'), textvariable=varPaneerTikka, width=6, justify='right', state=DISABLED)
txtPaneerTikka.grid(row = 8, column = 1)

MalaipaneerTikka= Checkbutton(f1, text='Malai paneer Tikka\t\t( Rs. 200 )', variable=var9, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkMalaipaneerTikka()).grid(row=9, column=0, sticky=W)
txtMalaipaneerTikka = Entry(f1, font=('arial', 12, 'bold'), textvariable=varMalaipaneerTikka, width=6, justify='right', state=DISABLED)
txtMalaipaneerTikka.grid(row = 9, column = 1)


lblMeal = Label(f1, font=('arial', 18, 'bold'), text="\n\nNON-VEG MENU\n")
lblMeal.grid(row=10, column=0)

AfghaniChickenBiryani= Checkbutton(f1, text='Afghani Chicken Biryani\t( Rs. 190 )', variable=var10, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'), command=lambda: chkAfghaniChickenBiryani()).grid(row=11, column=0, sticky=W)
txtAfghaniChickenBiryani = Entry(f1, font=('arial', 13, 'bold'), textvariable=varAfghaniChickenBiryani, width=6, justify='right', state=DISABLED)
txtAfghaniChickenBiryani.grid(row = 11, column = 1)

StirFryChicken= Checkbutton(f1, text='Stir Fry Chicken\t\t( Rs. 180 )', variable=var11, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkStirFryChicken()).grid(row=12, column=0, sticky=W)
txtStirFryChicken = Entry(f1, font=('arial', 12, 'bold'), textvariable=varStirFryChicken, width=6, justify='right', state=DISABLED)
txtStirFryChicken.grid(row = 12, column = 1)

MurgBasilTikka= Checkbutton(f1, text='Murg Basil Tikka\t\t( Rs. 210 )', variable=var12, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkMurgBasilTikka()).grid(row=13, column=0, sticky=W)
txtMurgBasilTikka = Entry(f1, font=('arial', 12, 'bold'), textvariable=varMurgBasilTikka, width=6, justify='right', state=DISABLED)
txtMurgBasilTikka.grid(row = 13, column = 1)

TandooriLollypop= Checkbutton(f1, text='Tandoori Lollypop\t\t( Rs. 160 )', variable=var13, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkTandooriLollypop()).grid(row=14, column=0, sticky=W)
txtTandooriLollypop = Entry(f1, font=('arial', 12, 'bold'), textvariable=varTandooriLollypop, width=6, justify='right', state=DISABLED)
txtTandooriLollypop.grid(row = 14, column = 1)

ChickenSpicyBurger= Checkbutton(f1, text='Chicken Spicy Burger\t( Rs. 70 )', variable=var14, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkChickenSpicyBurger()).grid(row=15, column=0, sticky=W)
txtChickenSpicyBurger = Entry(f1, font=('arial', 12, 'bold'), textvariable=varChickenSpicyBurger, width=6, justify='right', state=DISABLED)
txtChickenSpicyBurger.grid(row = 15, column = 1)

ChickenReshmiKabab= Checkbutton(f1, text='Chicken Reshmi Kabab\t( Rs. 200 )', variable=var15, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkChickenReshmiKabab()).grid(row=16, column=0, sticky=W)
txtChickenReshmiKabab = Entry(f1, font=('arial', 12, 'bold'), textvariable=varChickenReshmiKabab, width=6, justify='right', state=DISABLED)
txtChickenReshmiKabab.grid(row = 16, column = 1)

ChickenCheeseBurger= Checkbutton(f1, text='Chicken Cheese Burger\t( Rs. 90 )', variable=var16, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'), command=lambda: chkChickenCheeseBurger()).grid(row=17, column=0, sticky=W)
txtChickenCheeseBurger = Entry(f1, font=('arial', 12, 'bold'), textvariable=varChickenCheeseBurger, width=6, justify='right', state=DISABLED)
txtChickenCheeseBurger.grid(row = 17, column = 1)

KadhaiChicken= Checkbutton(f1, text='Kadhai Chicken\t\t( Rs. 160 )', variable=var17, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkKadhaiChicken()).grid(row=18, column=0, sticky=W)
txtKadhaiChicken = Entry(f1, font=('arial', 12, 'bold'), textvariable=varKadhaiChicken, width=6, justify='right', state=DISABLED)
txtKadhaiChicken.grid(row = 18, column = 1)




lblspace=Label(f1, text="\n\n\n\n\n\n\n\n\n\n")
lblspace.grid(row=19, column=0)


#==================================


lblMeal = Label(f2TOP, font=('arial', 18, 'bold'), text="\n\tSOUPS AND BEVERAGES\t\n")
lblMeal.grid(row=0, column=0)


Coffee= Checkbutton(f2TOP, text='Coffee\t\t\t( Rs. 15 )', variable=var18, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkCoffee()).grid(row=1, column=0, sticky=W)
txtCoffee = Entry(f2TOP, font=('arial', 12, 'bold'), textvariable=varCoffee, width=6, justify='right', state=DISABLED)
txtCoffee.grid(row = 1, column = 1)

Tea= Checkbutton(f2TOP, text='Tea\t\t\t( Rs. 15 )', variable=var19, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkTea()).grid(row=2, column=0, sticky=W)
txtTea = Entry(f2TOP, font=('arial', 12, 'bold'), textvariable=varTea, width=6, justify='right', state=DISABLED)
txtTea.grid(row = 2, column = 1)

CaféLatte= Checkbutton(f2TOP, text='Café Latte\t\t( Rs. 60 )', variable=var20, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkCaféLatte()).grid(row=3, column=0, sticky=W)
txtCaféLatte = Entry(f2TOP, font=('arial', 12, 'bold'), textvariable=varCaféLatte, width=6, justify='right', state=DISABLED)
txtCaféLatte.grid(row = 3, column = 1)

CoconutSoup= Checkbutton(f2TOP, text='Coconut Soup\t\t( Rs. 70 )', variable=var21, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkCoconutSoup()).grid(row=4, column=0, sticky=W)
txtCoconutSoup = Entry(f2TOP, font=('arial', 12, 'bold'), textvariable=varCoconutSoup, width=6, justify='right', state=DISABLED)
txtCoconutSoup.grid(row = 4, column = 1)

VegManchowSoup= Checkbutton(f2TOP, text='Veg Manchow Soup\t( Rs. 80 )', variable=var22, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkVegManchowSoup()).grid(row=5, column=0, sticky=W)
txtVegManchowSoup = Entry(f2TOP, font=('arial', 12, 'bold'), textvariable=varVegManchowSoup, width=6, justify='right', state=DISABLED)
txtVegManchowSoup.grid(row = 5, column = 1)

MangoLassi= Checkbutton(f2TOP, text='Mango Lassi\t\t( Rs. 40 )', variable=var23, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkMangoLassi()).grid(row=6, column=0, sticky=W)
txtMangoLassi = Entry(f2TOP, font=('arial', 12, 'bold'), textvariable=varMangoLassi, width=6, justify='right', state=DISABLED)
txtMangoLassi.grid(row = 6, column = 1)

SweetLassi= Checkbutton(f2TOP, text='Sweet Lassi\t\t( Rs. 40 )', variable=var24, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkSweetLassi()).grid(row=7, column=0, sticky=W)
txtSweetLassi = Entry(f2TOP, font=('arial', 12, 'bold'), textvariable=varSweetLassi, width=6, justify='right', state=DISABLED)
txtSweetLassi.grid(row = 7, column = 1)

SodaPop= Checkbutton(f2TOP, text='Soda Pop\t\t( Rs. 30 )', variable=var25, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkSodaPop()).grid(row=8, column=0, sticky=W)
txtSodaPop = Entry(f2TOP, font=('arial', 12, 'bold'), textvariable=varSodaPop, width=6, justify='right', state=DISABLED)
txtSodaPop.grid(row = 8, column = 1)


lblspace=Label(f2TOP, text="\n\n")
lblspace.grid(row=9, column=0)

#================================

lblPaymentmethod = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="Payment method", bd=10, width=16, anchor='w')
lblPaymentmethod.grid(row=0, column=0)


cmbPaymentMethod = ttk.Combobox(f2BOTTOM, textvariable= var44, state='readonly', font=('arial', 10, 'bold'), width=20)
cmbPaymentMethod['value']=('cash', 'Master Card', 'Visa Card', 'Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1, column=0)

lblTax = Label(f2BOTTOM, font=('arial', 14, 'bold'),text="Tax\t", bd=10, anchor='w')
lblTax.grid(row=1, column=1)
txtTax = Entry(f2BOTTOM, font=('arial', 11, 'bold'), textvariable= varTax, width=9, justify='right', state=DISABLED)
txtTax.grid(row=1, column=2)

lblSubTotal = Label(f2BOTTOM, font=('arial', 14, 'bold'), text='Sub Total\t\t', bd=10, width=8, anchor='w')
lblSubTotal.grid(row=2, column=1)
txtSubTotal = Entry(f2BOTTOM, font=('arial', 11, 'bold'), textvariable=varSubTotal, width=9, justify='right', state=DISABLED)
txtSubTotal.grid(row=2, column=2)

lblTotal= Label(f2BOTTOM, font=('arial', 14, 'bold'), text='Total\t\t', bd=10, width=6, anchor='w')
lblTotal.grid(row=3, column=1)
txtTotal = Entry(f2BOTTOM, font=('arial', 11, 'bold'), textvariable= varTotal, width=9, justify='right', state=DISABLED)
txtTotal.grid(row=3, column=2)

#=====================================
btnTotal = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('arial',16, 'bold'), width=4, 
			text="Total", command=lambda: TotalCost()).grid(row=4,column=0)

btnReset = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=4, 
			text="Reset", command=lambda: Reset()).grid(row=4,column=1)

btnExit = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=4, 
			text="Exit", command=lambda: iExit()).grid(row=4,column=2)

lblspace=Label(f2BOTTOM, text="\n\n\n\n\n\n\n")
lblspace.grid(row=5, column=0)



#======================================

lblMeal = Label(f3, font=('arial', 18, 'bold'), text="\nMAIN COURSE\n")
lblMeal.grid(row=0, column=0)

AlooKulcha= Checkbutton(f3, text='Aloo Kulcha\t\t( Rs. 40 )', variable=var26, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkAlooKulcha()).grid(row=1, column=0, sticky=W)
txtAlooKulcha = Entry(f3, font=('arial', 12, 'bold'), textvariable=varAlooKulcha, width=6, justify='right', state=DISABLED)
txtAlooKulcha.grid(row = 1, column = 1)

CheeseGarlicNaan= Checkbutton(f3, text='Cheese Garlic Naan\t( Rs. 70 )', variable=var27, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkCheeseGarlicNaan()).grid(row=2, column=0, sticky=W)
txtCheeseGarlicNaan = Entry(f3, font=('arial', 12, 'bold'), textvariable=varCheeseGarlicNaan, width=6, justify='right', state=DISABLED)
txtCheeseGarlicNaan.grid(row = 2, column = 1)

Onionkulcha= Checkbutton(f3, text='Onion kulcha\t\t( Rs. 40 )', variable=var28, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkOnionkulcha()).grid(row=3, column=0, sticky=W)
txtOnionkulcha = Entry(f3, font=('arial', 12, 'bold'), textvariable=varOnionkulcha, width=6, justify='right', state=DISABLED)
txtOnionkulcha.grid(row = 3, column = 1)

ButterNaan= Checkbutton(f3, text='Butter Naan\t\t( Rs. 40 )', variable=var29, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkButterNaan()).grid(row=4, column=0, sticky=W)
txtButterNaan = Entry(f3, font=('arial', 12, 'bold'), textvariable=varButterNaan, width=6, justify='right', state=DISABLED)
txtButterNaan.grid(row = 4, column = 1)

PaneerKulcha= Checkbutton(f3, text='Paneer Kulcha\t\t( Rs. 50 )', variable=var30, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkPaneerKulcha()).grid(row=5, column=0, sticky=W)
txtPaneerKulcha = Entry(f3, font=('arial', 12, 'bold'), textvariable=varPaneerKulcha, width=6, justify='right', state=DISABLED)
txtPaneerKulcha.grid(row = 5, column = 1)

GarlicNaan= Checkbutton(f3, text='Garlic Naan\t\t( Rs. 45 )', variable=var31, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkGarlicNaan()).grid(row=6, column=0, sticky=W)
txtGarlicNaan = Entry(f3, font=('arial', 12, 'bold'), textvariable=varGarlicNaan, width=6, justify='right', state=DISABLED)
txtGarlicNaan.grid(row = 6, column = 1)

PlainKulcha= Checkbutton(f3, text='Plain Kulcha\t\t( Rs. 35 )', variable=var32, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkPlainKulcha()).grid(row=7, column=0, sticky=W)
txtPlainKulcha = Entry(f3, font=('arial', 12, 'bold'), textvariable=varPlainKulcha, width=6, justify='right', state=DISABLED)
txtPlainKulcha.grid(row = 7, column = 1)

PaneerParatha= Checkbutton(f3, text='Paneer Paratha\t\t( Rs. 50 )', variable=var33, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkPaneerParatha()).grid(row=8, column=0, sticky=W)
txtPaneerParatha = Entry(f3, font=('arial', 12, 'bold'), textvariable=varPaneerParatha, width=6, justify='right', state=DISABLED)
txtPaneerParatha.grid(row = 8, column = 1)

ChillyParatha= Checkbutton(f3, text='Chilly Paratha\t\t( Rs. 40 )', variable=var34, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkChillyParatha()).grid(row=9, column=0, sticky=W)
txtChillyParatha = Entry(f3, font=('arial', 12, 'bold'), textvariable=varChillyParatha, width=6, justify='right', state=DISABLED)
txtChillyParatha.grid(row = 9, column = 1)

ChickenSingaporeNoodles= Checkbutton(f3, text='Chicken Singapore Noodles\t( Rs. 90 )', variable=var35, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkChickenSingaporeNoodles()).grid(row=10, column=0, sticky=W)
txtChickenSingaporeNoodles = Entry(f3, font=('arial', 12, 'bold'), textvariable=varChickenSingaporeNoodles, width=6, justify='right', state=DISABLED)
txtChickenSingaporeNoodles.grid(row = 10, column = 1)

JeeraRice= Checkbutton(f3, text='Jeera Rice\t\t( Rs. 125 )', variable=var36, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkJeeraRice()).grid(row=11, column=0, sticky=W)
txtJeeraRice = Entry(f3, font=('arial', 12, 'bold'), textvariable=varJeeraRice, width=6, justify='right', state=DISABLED)
txtJeeraRice.grid(row = 11, column = 1)

VegDumBiryani= Checkbutton(f3, text='VegDum Biryani\t\t( Rs. 170 )', variable=var37, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkVegDumBiryani()).grid(row=12, column=0, sticky=W)
txtVegDumBiryani = Entry(f3, font=('arial', 12, 'bold'), textvariable=varVegDumBiryani, width=6, justify='right', state=DISABLED)
txtVegDumBiryani.grid(row = 12, column = 1)

MixFriedRice= Checkbutton(f3, text='Mix Fried Rice\t\t( Rs. 180 )', variable=var38, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkMixFriedRice()).grid(row=13, column=0, sticky=W)
txtMixFriedRice = Entry(f3, font=('arial', 12, 'bold'), textvariable=varMixFriedRice, width=6, justify='right', state=DISABLED)
txtMixFriedRice.grid(row = 13, column = 1)

EggFriedRice= Checkbutton(f3, text='Egg Fried Rice\t\t( Rs. 160 )', variable=var39, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkEggFriedRice()).grid(row=14, column=0, sticky=W)
txtEggFriedRice = Entry(f3, font=('arial', 12, 'bold'), textvariable=varEggFriedRice, width=6, justify='right', state=DISABLED)
txtEggFriedRice.grid(row = 14, column = 1)

OnionSalad= Checkbutton(f3, text='Onion Salad\t\t( Rs. 45 )', variable=var40, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkOnionSalad()).grid(row=15, column=0, sticky=W)
txtOnionSalad = Entry(f3, font=('arial', 12, 'bold'), textvariable=varOnionSalad, width=6, justify='right', state=DISABLED)
txtOnionSalad.grid(row = 15, column = 1)

GreenSalad= Checkbutton(f3, text='Kadhai Chicken\t\t( Rs. 60 )', variable=var41, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkGreenSalad()).grid(row=16, column=0, sticky=W)
txtGreenSalad = Entry(f3, font=('arial', 12, 'bold'), textvariable=varGreenSalad, width=6, justify='right', state=DISABLED)
txtGreenSalad.grid(row = 16, column = 1)

AlooRaita= Checkbutton(f3, text='Aloo Raita\t\t( Rs. 70 )', variable=var42, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkAlooRaita()).grid(row=17, column=0, sticky=W)
txtAlooRaita = Entry(f3, font=('arial', 12, 'bold'), textvariable=varAlooRaita, width=6, justify='right', state=DISABLED)
txtAlooRaita.grid(row = 17, column = 1)

MixVegRaita= Checkbutton(f3, text='Mix Veg Raita\t\t( Rs. 70 )', variable=var43, onvalue=1, offvalue=0, 
					font=('arial', 12, 'bold'),  command=lambda: chkMixVegRaita()).grid(row=18, column=0, sticky=W)
txtMixVegRaita = Entry(f3, font=('arial', 12, 'bold'), textvariable=varMixVegRaita, width=6, justify='right', state=DISABLED)
txtMixVegRaita.grid(row = 18, column = 1)



lblspace=Label(f3, text="\n\n\n\n\n\n\n")
lblspace.grid(row=19, column=0)


root.mainloop()

