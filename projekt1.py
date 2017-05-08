
def pricni_igro():  
    lik = 0
    while lik != 1 and lik != 2:
        lik = int(input('Izberi lik: [1] = vitez (...), [2] = čarovnik (...)'))
    if lik == 1 :
        print('Izbrali ste [VITEZ],vaše poteze so: \n ...')
        player_hp = 200
        poteze_lika = 'B1,B2,B3...'
    if lik == 2:
        print('Izbrali ste [ČAROVNIK],vaše poteze so: \n ...')
        player_hp = 100
        poteze_lika = '[0]-[Zdravljenje]: pozdravi se za 30hp \n [1]-[Ognjena krogla]: 100 dmg, 67% možnost vžiga \n [2]-[Strela]: 130 dmg \n [3]-[Blokada]: blokiraj 80 dmg'
        print('Izbrali ste [ČAROVNIK],vaše poteze so: \n ' + poteze_lika )

    stevilo_potez = 0
    boss_hp = 1000
    stanje_boss = 'vse_OK'
    stanje_player = 'vse_OK' 
    while boss_hp > 0 and player_hp > 0:
        print('Igralec :[' + str(player_hp) + ']')
        print('Boss :['+ str(boss_hp) + ']')
        stevilo_potez += 1
        izbrana_poteza = int(input('Izberi potezo, na voljo imas: \n ' + poteze_lika))
        boss_hp = 0

        
    if player_hp <= 0:
        print('Umrli ste, vaša vas je pogorela, zmaga komunizma!!!')
    if boss_hp <= 0 :
        print('Zmaga, svet je rešen, blabla. Potrebovali ste ' + str(stevilo_potez) + ' potezo.')
        
