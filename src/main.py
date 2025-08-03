from contact import add_contact, create_table, list_contact


def operation(choix):
    match choix:
        case 1:
            nom = input("Nom : ")
            prenom = input("Prenom : ")
            telephone = input("Telephone : ")
            add_contact(nom, prenom, telephone)
            print("Contact enregistré avec succès")
        case 2:
            list_contact()


def main():
    create_table()
    list_choix = ["Enregistrer un contact", "Afficher la liste des contacts"]

    print("***BIENVENU DANS LE GESTION DE CONTACT***")
    print("***CHOISISSEZ UNE OPTION***")
    for index, choix in enumerate(list_choix):
        print(f"{index + 1}: {choix}")
    choix = int(input("Choix: "))
    operation(choix)


if __name__ == "__main__":
    main()
