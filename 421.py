import random

reponse=""
	
def check_fin_tour(choix_joueur_1):
		if choix_joueur_1.find("1")!=(-1) and choix_joueur_1.find("2")!=(-1) and choix_joueur_1.find("3")!=(-1):
			continuer="non"
		else:
			continuer="oui"
		return continuer

def change_dices(lancer, choix_joueur_1):
	if choix_joueur_1.find("1")==(-1):
		lancer[0]=random.randint(1,6)
	if choix_joueur_1.find("2")==(-1):
		lancer[1]=random.randint(1,6)
	if choix_joueur_1.find("3")==(-1):
		lancer[2]=random.randint(1,6)
	return lancer


print("Le 421")
while reponse!="Q":
	lancers=[random.randint(1,6), random.randint(1,6),random.randint(1,6)]
	print ("Lancer 1",lancers)
	nb_lancers=1
	choix_joueur=str(input("Voulez-vous garder les dés 1, 2 et/ou 3 ?"))
	continuer=check_fin_tour(choix_joueur)
	if continuer=="oui":
		lancers=change_dices(lancers, choix_joueur)
		print("Lancer 2",lancers)
		nb_lancers+=1
		choix_joueur=str(input("Voulez-vous garder les dés 1, 2 et/ou 3 ?"))
		continuer=check_fin_tour(choix_joueur)
		if continuer=="oui":
	   		lancers=change_dices(lancers, choix_joueur)
	   		print("Lancer 3",lancers)
	   		nb_lancers+=1
	if nb_lancers == 1:
		print("Résultat final :",lancers,"en", nb_lancers,"lancer.")
	else:
		print("Résultat final :",lancers,"en", nb_lancers,"lancers.")
	reponse=input("Entrée pour rejouer, Q pour quitter")
	reponse=reponse.upper()
	print("")

print("Au revoir !")