algne_saldo = 100
toiming = input("Millist toimingut soovite teha? (saldo, deposiit, väljamakse): ")

def konto_haldur(algne_saldo, toiming, summa):
    if toiming == "saldo":
        return algne_saldo
    #elif toiming == "väljamakse":
        #return algne_saldo + summa
    
while True:
    if toiming == "saldo":
        print(f"Sinu saldo on: {algne_saldo}")
    if toiming == "sisse":
        print(f"Kontojääk: {algne_saldo+summa}" + " €") 
    elif toiming == "valja":
        print(f"Kontojääk: {algne_saldo-summa}" + " €")      
    break
