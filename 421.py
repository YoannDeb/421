import random

reponse = ""
lancers =[]

def relancer(lancer):
	choix_joueur=str(input("voulez-vous relancer les dés 1, 2 et/ou 3?"))
	if choix_joueur.find("1")!=(-1):
		lancer[0]=random.randint(1,6)
	if choix_joueur.find("2")!=(-1):
		lancer[1]=random.randint(1,6)
	if choix_joueur.find("3")!=(-1):
		lancer[2]=random.randint(1,6)
	return lancer


print("Le 421")
lancers=[random.randint(1,6), random.randint(1,6),random.randint(1,6)]
print ("Lancer 1",lancers)
reponse_lancer=input("Voulez-vous relancer les dés ? O=oui, N=non")
if reponse_lancer=="O":
  relancer(lancers)
  print("Lancer 2",lancers)
  reponse_lancer=input("Voulez-vous relancer les dés ? O=oui, N=non")
  if reponse_lancer=="O":
    relancer(lancers)
    print("Lancer 3",lancers)
  
print("résultat final :",lancers)
print("Au revoir")