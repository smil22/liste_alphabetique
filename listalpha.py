#Enregistrement des noms
#Création d'un tableau à deux dimensions(4 colonnes numéro, nom, prenom et sexe)
print("Formulaire d'/de ... ")
objet = input()
objet = objet.upper()
print("**** FORMULAIRE D'/DE", objet, " ****")
print("Prière de mettre les noms en majuscules.")
print("NB : Entrez '/' dans les champs quand vous aurez terminé les entrées.")
objet_formulaire = [] #formulaire
#Utilisation d'une ligne de renseignement qui sera ajoutée au formulaire
n = 1 #indiquera le nombre d'individus
while 1 :
    ligne_formulaire = [n]*4
    for j in range(1,4) :
        ligne_formulaire[j] = [0]
    print("Nom de l'individu n°", n, ":")
    ligne_formulaire[1] = input()
    print("Prénoms de l'individu n°", n, ":")
    ligne_formulaire[2] = input()
    print("Genre de l'individu n°", n, ":")
    ligne_formulaire[3] = input()
    if ligne_formulaire[1] == "/" or ligne_formulaire[3] == "/" :
        break
    else :
       objet_formulaire.append(ligne_formulaire) 
    n = n+1
#print(objet_formulaire)

#Statistiques de genre
homme,femme = 0,0
for x in objet_formulaire :
    if x[3] == "m" or x[3] == "M" :
        homme = homme+1
    elif x[3] == "f" or x[3] == "F" :
        femme = femme+1
c_homme = homme
homme = (homme/(homme+femme))*100
femme = (femme/(c_homme+femme))*100

#Classement par ordre alphabétique
#Coeur de code
longueur = len(objet_formulaire)
#print(longueur)
test = 0 #véfirie qu'un nom vient bien avant tous les autres
n = 1 #numéroter dans le fichier
import getpass
utilisateur = getpass.getuser()
fichier = open(f"./liste.txt", "w")
fichier.write("**** FORMULAIRE D'/DE ")
fichier.write(objet)
fichier.write(" ****\n\n")
i,j = 0,0
while i < longueur :
    while j < longueur :
        if objet_formulaire[i][1] < objet_formulaire[j][1] :
            test = 1
        elif objet_formulaire[i][1] > objet_formulaire[j][1] :
            test = 0
            break
        j = j+1
    if test == 1 : #si le nom est bien le premier
        fichier.write(str(n))
        fichier.write(" - ")
        fichier.write(objet_formulaire[i][1])
        fichier.write(" ")
        fichier.write(objet_formulaire[i][2])
        fichier.write("\n")
        n = n+1
        del objet_formulaire[i]
        longueur = longueur-1
    elif test == 0 : #on renvoie la ligne en fin de liste 
        ligne_formulaire = [0]*4
        ligne_formulaire = objet_formulaire[i]
        del objet_formulaire[i]
        objet_formulaire.append(ligne_formulaire)
        i = 0 #l'indice est rénitialisé
    if i != 0 : #incrémentation seulement si l'indice n'est pas rebooté
        i = i+1
fichier.write(f"\nHomme : {homme} %\nFemme : {femme} %")
fichier.close()
print("Le classement a été fait. Veuillez vérifier votre répertoire pour y trouver\
 le document.")
        
        
        
        


