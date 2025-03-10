
from dictionary import Dictionary
from traduzione import Traduzione


#importa dizionario
def getDizionario():
    with open("dictionary.txt", "r") as file:
        listaTraduzioni = file.read().splitlines()
        dizionario = Dictionary("Alieno-Italiano",[])

        for t in listaTraduzioni:
            alieno = t.split()[0]
            italiano = t.split()[1:]
            dizionario.append(Traduzione(alieno, italiano))

    return dizionario

#parte visiva
print("__________________________")
print("Translator Alien-Italian")
print("__________________________")
print("1. Aggiungi nuova parola")
print("2. Cerca una traduzione")
print("3. Cerca con wildcard")
print("4. Stampa tutto il dizionario")
print("5. Exit")
print("__________________________")

risposta= input("Cosa vuoi fare? ")
#parte di codice

if risposta == "1":
    alieno = input("Ok, quale parola vuoi aggiungere?")
    italiano= input("Qual è la sua traduzione o le sue traduzioni(separate da spazio)?")
    dizionario = getDizionario()
    #prendo le traduzioni e creo l'array con queste traduzioni
    traduzioni = italiano.split(' ')
    prova=False
    for item in dizionario.listaTraduzioni:
        ##ii è fatto da alieno traduzione
        if item.alieno == alieno:
            item.italiano+= traduzioni
            prova= True

    if not prova:
        trad = Traduzione(alieno, traduzioni)
        dizionario.append(trad)

    with open('dictionary.txt', 'w') as d:
            d.write(str(dizionario))

    print(f"aggiunta traduzione: [{alieno} ++ {traduzioni}]")

if risposta == "2":
    parola= input("inserisci parola aliena della quale vuoi la traduzione:")
    dizionario= getDizionario()
    traduzione= dizionario.cercaTraduzione(parola)
    print(f"traduzione: {traduzione}")

if risposta == "3":
    parola = input("inserisci parola aliena con WildCard della quale vuoi la traduzione:")
    dizionario = getDizionario()
    traduzione = dizionario.cercaTraduzioneWild(parola)
    print(f"traduzione: {traduzione}")


if risposta == "4":
    print("Ok, stampo tutto il dizionario")
    dict1= getDizionario()
    print(dict1)

if risposta == "5":
    print("uscita avvenuta")