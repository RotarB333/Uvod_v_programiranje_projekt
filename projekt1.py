
def pricni_igro():  
    lik = 0
    import random
    
    print('KRATEK UVOD in PRAVILA')

#Izbira lika    
    while lik != 1 and lik != 2:
        lik = int(input('Izberi lik: [1] = vitez (...), [2] = čarovnik (...) \n'))
    if lik == 1 :
        player_hp = 200
        M_player_hp = 200
        poteze_lika = 'B1,B2,B3...'
        print('Izbrali ste [VITEZ],vaše poteze so: \n ...')
    if lik == 2:
        player_hp = 150
        M_player_hp = 150
        poteze_lika = '\
[0]-[Zdravljenje]: pozdravi se za 30hp in odstrani možne zastrupitve \n \
[1]-[Ognjena krogla]: 90 dmg, 75% možnost vžiga \n \
[2]-[Strela]: 100 dmg, vsaka zaporedna uporaba naredi +10 dmg \n \
[3]-[Blokada]: blokiraj 80 dmg \n \
[4]-[Ledena sapa]: 80 dmg, 50% možnost zamrznitve'
        print('Izbrali ste [ČAROVNIK],vaše poteze so: \n ' + poteze_lika )

#Začetni podatki
    stevilo_potez = 0
    boss_hp = 1000
    stanje_boss = 'OK'
    stanje_player = 'OK'
    blokada = 0
    strela_zap = 0
    strup_moc = 0
#Vnos potez    
    while boss_hp > 0 and player_hp > 0:
        print('Igralec :[' + str(player_hp) + '/' + str(M_player_hp) + ']')
        print('Stanje igralca:' + stanje_player)
        print('Zmaj :['+ str(boss_hp) + ']')
        stevilo_potez += 1
        izbrana_poteza = 7
        while izbrana_poteza != 0 and izbrana_poteza != 1 and izbrana_poteza != 2 and izbrana_poteza != 3 \
        and izbrana_poteza != 4 :
            izbrana_poteza = int(input('Izberi potezo, na voljo imas: \n ' + poteze_lika + '\n'))
            
#Igralčeve poteze (lik_2):
        if lik == 2:    
#[0]-[Zdravljenje]     
            if izbrana_poteza == 0:
                stanje_player = 'OK'
                strup_moc = 0
                player_hp += 40
                if player_hp > M_player_hp:
                    player_hp = 100
#[1]-[Ognjena krogla]
            if izbrana_poteza == 1:
                boss_hp -= 90
                if random.randint(1,100) <= 75:
                    print('Vžig uspešen!')
                    stanje_boss = 'GORI'
#[2]-[Strela]
            if izbrana_poteza != 2:
                strela_zap = 0

            if izbrana_poteza == 2:
                boss_hp -= 100 + strela_zap * 10
                strela_zap += 1            
#[3]-[Bloakada]
            if izbrana_poteza == 3:
                blokada = 50    
#[4]-[Ledena sapa]
            if izbrana_poteza == 4:
                boss_hp -= 80
                if random.randint(1,100) <= 50:
                    print('Zamrznitev uspešna!')
                    stanje_boss = 'Zamrznjen'
#Stanje igralca:
            if stanje_player == 'Goriš!':
                player_hp -= 10
                print('Goriš!' + 'Igralec :[' + str(player_hp) + '/' + str(M_player_hp) + ']')
                stanje_player = 'OK'
            if stanje_player == 'Zastrupljen':
                player_hp -= 5 * strup_moc
                print('pst... Zastrupljen si!' + 'Igralec :[' + str(player_hp) + '/' + str(M_player_hp) + ']')
#Stanje šefa:
        boss_poteza = random.randint(1,100)
        if stanje_boss == 'GORI':
            print('Zmaj gori!')
            boss_hp -= 20
            print('Zmaj :['+ str(boss_hp) + ']')
            stanje_boss = 'OK'
        if stanje_boss == 'Zamrznjen':
            print('Zmaj je to rundo zamrznjen!')
            boss_poteza = 0
            stanje_boss = 'OK'

                
#Poteze šefa:
        if 1 <= boss_poteza <= 40:
            print('Zmaj te napade s kremplji.')
            if blokada >= 10 :
                print('Ni efektivno.')
            else:
                player_hp -= 10 - blokada
        if 40 < boss_poteza <= 70:
            print('Zmaj bruha ogenj')
            if blokada >= 25 :
                 print('Ni efektivno.')
            else:
                player_hp -= 25 - blokada
                if random.randint(1,100) <= 30:
                    print('......Goriš!')
                    stanje_player = 'Goriš!'
        if 70 < boss_poteza <= 90:
            print('Zmaj te je ugriznil.')
            if blokada >= 35 :
                print('Ni efektivno.')
            else:
                player_hp -= 35 - blokada
                if random.randint(1,100) <= 50:
                    print('Zmaj te je zastrupil!')
                    stanje_player = 'Zastrupljen!'
                    strup_moc += 1
        if 90 < boss_poteza:
            print('Zmaj te je udaril z repom, opraskal in vrgel z 20-ih metrov.')
            if blokada >= 60 :
                print('Ni efektivno.')
            else:
                player_hp -= 60 - blokada
            
            
            
        
            
#Kriterij za konec igre
    if player_hp <= 0:
        print('Umrli ste, zmaj je požgal vašo vas :( !!!')
    if boss_hp <= 0 :
        print('Zmaga, svet je rešen, blabla. Potrebovali ste ' + str(stevilo_potez) + ' potez.')
        
