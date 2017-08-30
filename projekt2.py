#Potezna igra, kjer mora igralec premagati nasprotnika v čimmanj potezah.
#Istočasno kot igralec izvede potezo tudi nasprotnik, katerega poteza je naključna.
#Igralec ima na voljo 4 poteze:
#[0] zdravljenje;pozdravi se za 40hp in oddstrani vsa stanja
#[1] ognjena krogla;naredi 90dmg in ima 50% možnost vžiga za dodatnih 20 dmg
#[2] strela; naredi 100dmg + 10dmg za vsako zaporedno strelo(do 3x)
#[3] leden vihar; naredi 80dmg in ima 40% možnost zamrznitve(prepreči nasprotnikovo potezo)
#Nasprotnik ima tudi na voljo 4 poteze, katerih škoda se povečuje z redkostjo. Nasprotnik
#lahko povzroči tudi da je igralec zastrupljen(kar naredi 10dmg(+10 za vsako dodatno zastrupitev)
#vsako rundo, dokler se ne pozdravi) ali gori(kar naredi 15dmg le naslednjo rundo).
#Igralec ne more biti istočasno zastrupljen in goreč, podobno nasprotnik ne more biti zastrupljen
#in zamrznjen.
#Igra se zaključi ko igralec ali nasprotnik izgubita ves hp. Če zmaga igralec, ter je bilo
#število potrebnih potez boljše od vsaj enega od šestih rekordov se zabeleži nov rekord.


#IMPORT

import random
from tkinter import *
okno = Tk()
player_hp = IntVar()
stevilo_potez = IntVar()
player_stanje = StringVar()
boss_hp = IntVar()
boss_stanje = StringVar()
player_poteza = StringVar()
boss_poteza = StringVar()
strela_zap = IntVar()
strup_moc = IntVar()

##DEFENICIJE:

#ZAČETEK IGRE
def start():
    player_hp.set(200)
    stevilo_potez.set(0)
    player_stanje.set('OK')
    boss_hp.set(1000)
    boss_stanje.set('OK')
    player_poteza.set('')
    boss_poteza.set('')
    strela_zap.set(0)
    strup_moc.set(0)
    usposobi()
    
#POTEZE PLAYER-ja

def zacetek_poteze():
    boss_gori()
    stevilo_potez.set(stevilo_potez.get() + 1)
    
def konec_poteze():
    player_stanjeX()
    poteza_boss()
    preveri_igro()

def poteza(a):
    zacetek_poteze()
    if a == 'zdravljenje':
        zdravljenje()
    elif a == 'ognjena_krogla':
        ognjena_krogla()
    elif a == 'strela':
        strela()
    elif a == 'leden_vihar':
        leden_vihar()
    konec_poteze()
    
def zdravljenje():
    player_stanje.set('OK')
    strup_moc.set(0)
    player_hp.set(player_hp.get() + 40)
    if player_hp.get() > 200:
        player_hp.set(200)
    player_poteza.set('ZDRAVLJENJE +40hp!')
    strela_zap.set(0)
   
def ognjena_krogla():
    boss_hp.set(boss_hp.get() - 90)
    if random.randint(1,100) <= 50:
        boss_stanje.set('GORI')
        player_poteza.set('OGNJENA KROGLA 90dmg!'+ ' Vžig uspešen 20dmg!')
    else :
        player_poteza.set('OGNJENA KROGLA 90dmg!')
    strela_zap.set(0)

def strela():
    boss_hp.set(boss_hp.get() - (100 + strela_zap.get() * 10))
    player_poteza.set('STRELA 100(+' + str(strela_zap.get() * 10) + ')dmg!')
    strela_zap.set(strela_zap.get() + 1)
    if strela_zap.get() > 3:
        strela_zap.set(3)
        
def leden_vihar():
    boss_hp.set(boss_hp.get() - 80)    
    if random.randint(1,100) <= 40:
        boss_stanje.set('Zamrznjen')
        player_poteza.set('LEDEN VIHAR 80dmg!'+' Zamrznitev uspešna!')
    else:
         player_poteza.set('LEDEN VIHAR 80dmg!')
    strela_zap.set(0)

#STANJA
def player_stanjeX():
    if player_stanje.get() == 'Goriš!':
        player_hp.set(player_hp.get() - 15)
        player_stanje.set('OK')
        strup_moc.set(0)
    if player_stanje.get() == 'Zastrupljen!':
        player_hp.set(player_hp.get() - 10 * strup_moc.get())
            
def boss_gori():
    if boss_stanje.get() == 'GORI':
        boss_hp.set(boss_hp.get() - 20)
        boss_stanje.set('OK')
        
#POTEZE BOSS-a    
def poteza_boss():
    zmaj_poteza = random.randint(1,100)
    if boss_hp.get() <= 0:
        boss_hp.set(0)
        zmaj_poteza = 0
    elif boss_stanje.get() == 'Zamrznjen':
        boss_poteza.set('Zmaj je to rundo zamrznjen!')
        zmaj_poteza = 0
        boss_stanje.set('OK')
    elif 1 <= zmaj_poteza <= 40:
        boss_poteza.set('Zmaj te napade s kremplji. 15dmg')
        player_hp.set(player_hp.get()  -15) 
    elif 40 < zmaj_poteza <= 70:
        boss_poteza.set('Zmaj bruha ogenj. 25dmg')
        player_hp.set(player_hp.get() - 25) 
        if random.randint(1,100) <= 30:
            player_stanje.set('Goriš!')
    elif 70 < zmaj_poteza <= 90:
        boss_poteza.set('Zmaj te je ugriznil. 35dmg')
        player_hp.set(player_hp.get() - 35) 
        if random.randint(1,100) <= 50:
            player_stanje.set('Zastrupljen!')
            strup_moc.set(strup_moc.get() + 1)
    elif 90 < zmaj_poteza:
        boss_poteza.set('Zmaj te je udaril z repom, opraskal in vrgel z 20-ih metrov. 60dmg')
        player_hp.set(player_hp.get() - 60)
        
#KONEC IGRE
def preveri_igro():
    if player_hp.get() <= 0:
        player_hp.set(0)
    if player_hp.get() == 0 and boss_hp.get() == 0:
        boss_poteza.set('Zmaj je poražen, toda tudi sam si mrtev. GAME OVER')
        onesposobi()
    elif boss_hp.get() == 0:
        boss_poteza.set('Zmaj je poražen in vas je rešena =)')
        onesposobi()
        if preveri_rekord() == 'nov rekord':
            boss_poteza.set('Zmaj je poražen in vas je rešena =),NOV REKORD!')
            belezenje_rekorda()
    elif player_hp.get() == 0:
        boss_poteza.set('GAME OVER, zmaj je požgal tvoje sosede in celo vas.')
        onesposobi()
        
#BELEŽENJE REKORDA
def preveri_rekord():
    with open('rekordi.txt','r') as R :
        seznam_rekordov =[]
        for vrstica in R:
            vrstica = vrstica.strip('\n')
            rekord = vrstica.split(':')
            rekord.pop(0)
            seznam_rekordov.append(rekord)
        for REKORD in seznam_rekordov:
            if int(REKORD[0]) > stevilo_potez.get():
                return 'nov rekord'
                
def belezenje_rekorda():
    with open('rekordi.txt','r') as R :
        seznam_rekordov =[]
        for vrstica in R:
            vrstica = vrstica.strip('\n')
            rekord = vrstica.split(':')
            #rekord[0] = stevilo_potez
            rekord.pop(0)
            seznam_rekordov.append(rekord)
        mesto = 0
        n = 0
        for REKORD in seznam_rekordov:
            n += 1
            mesto += n - 1
            if int(REKORD[0]) > stevilo_potez.get():
                novi_rekord = [str(stevilo_potez.get())]
                seznam_rekordov.insert(mesto,novi_rekord)
                seznam_rekordov.pop()
                with open('rekordi.txt','r+') as B : 
                    B.seek(0)
                    cifra = 0
                    for Rekord in seznam_rekordov:
                        cifra += 1
                        text = str(cifra) + ':' + Rekord[0] + '\n'
                        B.write(text)
                    B.truncate()
                    break



##GRAFIČNI VMESNIK
    
#[0]GUMBI    
nova_igraB = Button(okno, text = 'Nova igra', command = start, width = 15)
zdravljenjeB = Button(okno, text = 'ZDRAVLJENJE', command = lambda:poteza('zdravljenje'), width = 15)
ognjena_kroglaB = Button(okno, text = 'OGNJENA KROGLA', command = lambda:poteza('ognjena_krogla'), width = 15)
strelaB = Button(okno, text = 'STRELA', command = lambda:poteza('strela'), width = 15)
leden_viharB = Button(okno, text = 'LEDEN VIHAR', command = lambda:poteza('leden_vihar') , width = 15)

nova_igraB.grid(row = 0, column = 0)
zdravljenjeB.grid(row = 2, column = 0)
ognjena_kroglaB.grid(row = 3, column = 0)
strelaB.grid(row = 4, column = 0)
leden_viharB.grid(row = 5, column = 0)

zdravljenjeB.config(state = DISABLED)
ognjena_kroglaB.config(state = DISABLED)
strelaB.config(state = DISABLED)
leden_viharB.config(state = DISABLED)

#DEFENICIJE ZA GUMBE
def onesposobi():
   zdravljenjeB.config(state = DISABLED)
   ognjena_kroglaB.config(state = DISABLED)
   strelaB.config(state = DISABLED)
   leden_viharB.config(state = DISABLED)

def usposobi(): 
   zdravljenjeB.config(state = NORMAL)
   ognjena_kroglaB.config(state = NORMAL)
   strelaB.config(state = NORMAL)
   leden_viharB.config(state = NORMAL)
    
#[1]NAPISI
potezeN = Label(okno, text = 'POTEZE', bg = 'gainsboro', width = 15)
player_potezaN = Label(okno, text = 'Poteza player:', bg = 'gainsboro', width = 15)
boss_potezaN = Label(okno, text = 'Poteza boss:', bg = 'gainsboro', width = 15)
stevilo_potezN = Label(okno, text = 'Število potez:', bg = 'gainsboro', width = 15)
player_hpN = Label(okno, text = 'Player hp:',bg = 'light blue', width = 15)
player_stanjeN = Label(okno, text = 'Player stanje:',bg = 'light blue', width = 15)
boss_hpN = Label(okno, text = 'Boss hp:', bg = 'light coral', width = 15)
boss_stanjeN = Label(okno, text = 'Boss stanje:', bg = 'light coral', width = 15)

potezeN.grid(row = 1, column = 0)
player_potezaN.grid(row = 0, column = 1)
boss_potezaN.grid(row = 1, column = 1)
stevilo_potezN.grid(row = 2, column = 1)
player_hpN.grid(row = 3, column = 1)
player_stanjeN.grid(row = 4, column = 1)
boss_hpN.grid(row = 5, column = 1)
boss_stanjeN.grid(row = 6, column = 1)

#[2]DISPLAY
player_potezaD = Label(okno, text = player_poteza.get(), textvariable = player_poteza, width = 50, bg = 'Thistle')
boss_potezaD = Label(okno, text = boss_poteza.get(), textvariable = boss_poteza, width = 50, bg ='orange')
stevilo_PotezD = Label(okno, text = stevilo_potez.get(), textvariable = stevilo_potez, width = 15)
player_hpD = Label(okno, text = player_hp.get(), textvariable = player_hp, width = 15)
player_stanjeD = Label(okno, text = player_stanje.get(), textvariable = player_stanje, width = 15)
boss_hpD = Label(okno, text = boss_hp.get(), textvariable = boss_hp, width = 15)
boss_stanjeD = Label(okno, text = boss_stanje.get(), textvariable = boss_stanje, width = 15)

player_potezaD.grid(row = 0, column = 2)
boss_potezaD.grid(row = 1, column = 2)
stevilo_PotezD.grid(row = 2, column = 2)
player_hpD.grid(row = 3, column = 2)
player_stanjeD.grid(row = 4, column = 2)
boss_hpD.grid(row = 5, column = 2)
boss_stanjeD.grid(row = 6, column = 2)


okno.mainloop()
