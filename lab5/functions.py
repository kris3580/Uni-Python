import re

def print_list(shopping_list):
    # DACĂ LISTA ARE ELEMENTE
    if shopping_list:
        print("Lista curentă de produse:")
        for i, product in enumerate(shopping_list, 1):
            print(f"{i}. {product}")
    else:
        print("Lista este goală.")

def add_product(shopping_list):
    product = input("Introduceți denumirea produsului: ").strip()
    if not re.fullmatch(r"[A-Za-z ]+", product):
        print("Eroare: Denumirea produsului poate conține doar litere și spații.")
        return
    product = product.lower()
    if product in shopping_list:
        print("Produsul există deja în listă.")
    else:
        shopping_list.append(product)
        print(f"Produsul '{product}' a fost adăugat în listă.")

def delete_product(shopping_list):
    product = input("Introduceți denumirea produsului de șters: ").strip().lower()
    if product in shopping_list:
        shopping_list.remove(product)
        print(f"Produsul '{product}' a fost șters din listă.")
    else:
        print("Eroare: Produsul nu există în listă.")
