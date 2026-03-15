JC6XN-4TT3F-8HMGY-PXHK3-C4B2Q
print("Mini calculatrice")
def afficher_menu():
    print("\n=== Mini Calculatrice ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

while True:

    afficher_menu()

    choix = input("Choisissez une option : ")

    if choix == "5":
        print("Au revoir")
        break

    a = float(input("Premier nombre : "))
    b = float(input("Deuxième nombre : "))

    if choix == "1":
        print("Résultat :", a + b)

    elif choix == "2":
        print("Résultat :", a - b)

    elif choix == "3":
        print("Résultat :", a * b)

    elif choix == "4":

        if b == 0:
            print("Erreur : division par zéro")
        else:
            print("Résultat :", a / b)
