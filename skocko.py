from random import choice as cho
import sys

# Globalna nepromenljiva varijabla:
skocko_znaci = ('%', '#', '$', '&')

# Lista za belezenje pokusaja korisnika
pokusaji = []

# Flag odredjuje odgovor za gresku prilikom unosa
flag = 0

# Funkcije:

def kreiraj_kombinaciju():
    
    secret = ""

    for i in range(4):
        secret += cho(skocko_znaci)

    return secret

def kombinacija():
    return "Tacna kombinacija je {}.".format(secret)

def uvod():
    print()
    print("""     ***** Dobrodosli u igricicu 'Skocko'! *****
          
          Pravila:
          -Postoje 4 validna karaktera za kombinacije:
          
                % -> 'cent',
                
                $ -> 'dolar'
                
                & -> 'end'
                
                # -> 'hes'
                
          -Pokusajte da pogodite tacnu kombinaciju, ali ...
          
              ... svaki novi pokusaj (osim prvog!) Vam oduzima po 30 poena;
              
              ... imate maksimalno 8 pokusaja;
              
              ... startujete sa 250 poena.
              
              
                   *** SRECNO! ***
            """)
    
def provera_unosa(inp):
    global flag
    for i in inp:
        if i not in skocko_znaci:
            flag = 1
            return False
    if len(inp) != 4:
        flag = 2
        return False
    return True

def provera_ponavljanja(inp):
    global flag
    global pokusaji
    if inp not in pokusaji:
        pokusaji.append(inp)
        return True
    flag = 3
    return False
            
            
def totalna_provera(inp):
    while not (provera_unosa(inp) and provera_ponavljanja(inp)):
        print("Greska prilikom unosa.")
        return False
    return True

def pobeda():
    print('*' * 30)
    print(f"CESTITAM! POGODILI STE IZ {i}. POKUSAJA!")
    print(kombinacija())
    print(f'OSVOJILI STE {poeni} POENA.')
    print('*' * 30)
    sys.exit()
    

# Inicijalizacija globalnih promenljivih varijabli

i = 0

user_input = None

poeni = 250

# Kreiranje tajne kombinacije
secret = kreiraj_kombinaciju()

# Pocetak programa za korisnika
uvod()
while i < 8:
    if user_input == secret:
        pobeda()
    user_input = input("Unesite kombinaciju: ")
    while not totalna_provera(user_input):
        if flag == 1:
            print("Korisceni karakteri mogu biti: %, $, & ili #.")
        elif flag == 2:
            print("Kombinacija mora imati tacno 4 karaktera.")
        elif flag == 3:
            print("Kombinacija vec isprobana ranije.")
        user_input = input("\nPokusajte ponovo: ")
    pogodjeni = 0
    postoje = 0
    j = 0
    secret_lst = [char for char in secret]
    while j < 4:
        if user_input[j] in secret_lst:
            postoje += 1
            ind = secret_lst.index(user_input[j])
            el = secret_lst.pop(ind)
        if user_input[j] == secret[j]:
            pogodjeni += 1
        j += 1
    print('-' * 30)
    print(f'POGODJENI KARAKTERI: {postoje}')
    print(f'NA PRAVOM MESTU: {pogodjeni}')
    print(f'Broj pokusaja: {i + 1}/8')
    if i != 0:
        poeni -= 30
    print(f'Poeni: {poeni}')
    print('-' * 30)
    print()
    i += 1
if user_input == secret:
        pobeda()
print("Nazalost, nemate vise pokusaja.")
print(kombinacija())


