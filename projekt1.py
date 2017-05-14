
def pricni_igro():  
    lik = 0
    import random

#Izbira lika    
    while lik != 1 and lik != 2:
        lik = int(input('Izberi lik: [1] = vitez (...), [2] = čarovnik (...) \n'))
    if lik == 1 :
        print('Izbrali ste [VITEZ],vaše poteze so: \n ...')
        player_hp = 200
        poteze_lika = 'B1,B2,B3...'
    if lik == 2:
        print('Izbrali ste [ČAROVNIK],vaše poteze so: \n ...')
        player_hp = 100
        poteze_lika = '\
[0]-[Zdravljenje]: pozdravi se za 30hp in odtsrani možne zastrupitve \n \
[1]-[Ognjena krogla]: 90 dmg, 75% možnost vžiga \n \
[2]-[Strela]: 100 dmg, vsaka zaporedna uporaba naredi +10 dmg \n \
[3]-[Blokada]: blokiraj 80 dmg \n \
[4]-[Ledena sapa]: 80 dmg, 50% možnost zamrznitve'
        print('Izbrali ste [ČAROVNIK],vaše poteze so: \n ' + poteze_lika )

#Začetni podatki
    stevilo_potez = 0
    boss_hp = 1000
    stanje_boss = 'vse_OK'
    stanje_player = 'vse_OK'
    blokada = 0
    strela_zap = 0
#Vnos potez    
    while boss_hp > 0 and player_hp > 0:
        print('Igralec :[' + str(player_hp) + ']')
        print('Boss :['+ str(boss_hp) + ']')
        stevilo_potez += 1
        izbrana_poteza = 7
        while izbrana_poteza != 0 and izbrana_poteza != 1 and izbrana_poteza != 2 and izbrana_poteza != 3 \
        and izbrana_poteza != 4 :
            izbrana_poteza = int(input('Izberi potezo, na voljo imas: \n ' + poteze_lika + '\n'))            
#[0]-[Zdravljenje]     
        if izbrana_poteza == 0:
            stanje_player = 'vse_OK'
            player_hp += 30
            if player_hp > 100:
                player_hp = 100
            boss_hp = 0
#[1]-[Ognjena krogla]
        if izbrana_poteza == 1:
            boss_hp -= 90
            if random.randint(0,100) <= 75:
                print('Vžig uspešen!')
                stanje_boss = 'GORI'
#[2]-[Strela]
        if izbrana_poteza != 2:
            strela_zap = 0

        if izbrana_poteza == 2:
            boss_hp -= 100 + strela_zap * 10
            strela_zap += 1            

#[3]
#[4]            
            
#Kriterij za konec igre
    if player_hp <= 0:
        print('Umrli ste, vaša vas je pogorela, zmaga komunizma!!!')
    if boss_hp <= 0 :
        print('Zmaga, svet je rešen, blabla. Potrebovali ste ' + str(stevilo_potez) + ' potez.')
        
