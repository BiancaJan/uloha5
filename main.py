#Na prednáške si sa zoznámil s funkciou nsd(a, b), ktorá počítala najväčší spoločný deliteľ dvoch čísel. Inšpiruj sa touto funkciou a napíš funkciu nsn(a, b),
#ktorá vypočíta najmenší spoločný násobok dvoch čísel.
def nsd(a, b):
    while b:
        a, b = b, a % b
    return a

def nsn(a, b):
    return abs(a * b) // nsd(a, b)
print(nsn(129,162))
print(nsn(60,168))

# Zadaj svoje čísla
 #cislo1 = int(input("Zadaj prvé číslo: "))
 #cislo2 = int(input("Zadaj druhé číslo: "))

# Vypočítaj a vypíš najmenší spoločný násobok
 #vysledok = nsn(cislo1, cislo2)
 #print(f"Najmenší spoločný násobok čísel {cislo1} a {cislo2} je: {vysledok}")


#Napíš funkciu priemer(a, b), ktorá vypočíta priemer dvoch zadaných čísel. Funkcia nič nevypisuje,
#ale pomocou return vráti vypočítanú hodnotu. Otestuj ju s rôznymi hodnotami parametrov.
def priemer(a, b):
    return (a + b) / 2
print(priemer(1,4))
print(priemer(3.14,31.4))


#Napíš funkciu obdlznik(sirka, znak='*'), ktorá z daného znaku znak vypíše do troch riadkov výstupu obdĺžnik zadanej šírky.
def obdlznik(sirka, znak="*"):
    for riadok in range (3):
        if riadok == 1:
            print(znak+" "*(sirka - 2)+znak)
        else:
            print(znak*sirka)
obdlznik(30,"#")

#Napíš funkciu riadok(n, text=''), ktorá vypíše n znakový reťazec hviezdičiek '*', stred ktorého nahradí zadaným textom.
#Ak je tento zadaný text neprázdny, vloží na jeho začiatok aj koniec medzeru.
def riadok(n, text=''):
    if text:
        text = ' ' + text + ' '
    else:
        text = " "
    hviezdy = '*' * n
    stred = (n - len(text)) // 2
    vystup = hviezdy[:stred] + text + hviezdy[stred + len (text):]
    print(vystup)
sir = 40
riadok(sir)
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, 'a v tom tŕní chrastí rastie')
riadok(sir)




