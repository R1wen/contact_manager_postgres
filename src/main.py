import time

from contact import (
    add_contact,
    create_table,
    delete_contact,
    list_contact,
    update_contact,
)


def modifier_contact(id: int):
    nom = input("Nouveau nom : ").upper()
    prenom = input("Nouveau prenoms : ").title()
    telephone = input("Nouveau numéro (avec indice: +228 xxxxx) : ")
    update_contact(id, nom, prenom, telephone)
    print("Contact modifié avec succès")


def supprimer_contact():
    nom = input("Entrez le nom du contact à supprimer: ").upper()
    delete_contact(nom)
    print("Contact supprimé avec succès")


def operation(choix):
    match choix:
        case 1:
            nom = input("Nom : ").upper()
            prenom = input("Prenoms : ").title()
            telephone = input("Telephone (avec indice: +228 xxxxx) : ")
            add_contact(nom, prenom, telephone)
            print("Contact enregistré avec succès")
            time.sleep(3)
        case 2:
            print("\n***LISTE DE CONTACTS***")
            list_contact()
            time.sleep(3)
        case 3:
            supprimer_contact()
            time.sleep(3)
        case 4:
            list_contact()
            id = int(input("Quelle est l'ID du contact à modifier? "))
            modifier_contact(id)
            time.sleep(3)
        case 5:
            print("Bye bye")
            quit()


def main():
    create_table()
    list_choix = [
        "Enregistrer un contact",
        "Afficher la liste des contacts",
        "Supprimer un contact",
        "Modifier un contact",
        "Quitter"
    ]

    while True:
        print("\n***BIENVENU DANS LE GESTION DE CONTACT***")
        print("***CHOISISSEZ UNE OPTION***")
        for index, choix in enumerate(list_choix):
            print(f"{index + 1}: {choix}")
        choix = int(input("Choix: "))
        operation(choix)


if __name__ == "__main__":
    main()
