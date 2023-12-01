from cart import ShoppingCart
from product import *
from random import randint

#Create product functions and add them to the cart
def create_tshirt(name, price, qty, size):
    for _ in range(qty):
        a = TShirt(f'CAMISETA {name}', price, size)
        a.serial = randint(10000, 99999) * 5
        cart.add_item(a)

def create_mug(name, price, qty, capacity):
    for _ in range(qty):
        a = Mug(f'CANECA {name}', price, capacity)
        a.serial = randint(10000, 99999) * 3
        cart.add_item(a)
def create_comic(name, price, qty, author, publisher):
    for _ in range(qty):    
        a = ComicBook(f'{name} Vol.1', price, author, publisher)
        a.serial = randint(10000, 99999) * 3
        cart.add_item(a)

# Call the correct create product function, based on user input
def add_to_cart():
    options = [x for x in range(1,10)]
    sizes = ["P", "M", "G"]
    try:
        user_select = int(input("DIGITE O NUMERO DO PRODUTO QUE DESEJA ADICIONAR AO CARRINHO:  "))
        if user_select in options:
            if user_select >= 1 and user_select <= 3:
                try:
                    while True:
                        qty = int(input("QUANTAS UNIDADES? "))
                        if qty > 5:
                            print("APENAS 5 UNIDADES DO MESMO PRODUTO SÃO PERMITIDAS POR CLIENTE")
                            continue
                        elif qty < 1:
                            print("NAO SAO PERMITIDOS NUMEROS MENORES QUE 1")
                            continue
                        while True:
                            size = input("QUAL TAMANHO? P, M OU G: ").upper()
                            if size not in sizes:
                                print("COMANDO INVÁLIDO, ESCOLHA UM DOS TAMANHOS DISPONIVEIS")
                                continue
                            else:
                                break
                        break
                except ValueError:
                    print("COMANDO INVÁLIDO")
                selected = products["CAMISAS"][user_select-1]
                create_tshirt(selected[0], selected[1], qty, size)

            elif user_select >= 4 and user_select <= 6:
                try:
                    while True:
                        qty = int(input("QUANTAS UNIDADES? "))
                        if qty > 5:
                            print("APENAS 5 UNIDADES DO MESMO PRODUTO SÃO PERMITIDAS POR CLIENTE")
                            continue
                        elif qty < 1:
                            print("NAO SAO PERMITIDOS NUMEROS MENORES QUE 1")
                            continue
                        break
                except ValueError:
                    print("COMANDO INVÁLIDO")
                selected = products["CANECAS"][user_select-4]
                create_mug(selected[0], selected[1], qty, selected[2])
            else:
                try:
                    while True:
                        qty = int(input("QUANTAS UNIDADES? "))
                        if qty > 5:
                            print("APENAS 5 UNIDADES DO MESMO PRODUTO SÃO PERMITIDAS POR CLIENTE")
                            continue
                        elif qty < 1:
                            print("NAO SAO PERMITIDOS NUMEROS MENORES QUE 1")
                            continue
                        break
                except ValueError:
                    print("COMANDO INVÁLIDO")
                selected = products["QUADRINHOS"][user_select-7]
                create_comic(selected[0], selected[1], qty, selected[2], selected[3])
        else:
            print("COMANDO INVÁLIDO, FAVOR SELECIONAR UM DOS NUMEROS DA LISTA.")
    except ValueError:
        print("COMANDO INVÁLIDO, FAVOR SELECIONAR UM DOS NUMEROS DA LISTA.")

def delete_from_cart():
    display_cart()
    try:
        del_product = int(input("DIGITE O NUMERO DO PRODUTO QUE DESEJA EXCLUIR: "))
        if del_product < 1 or del_product > len(cart.items):
            print("COMANDO INVÁLIDO, FAVOR SELECIONAR UM DOS NUMEROS DA LISTA.")
        else:
            cart.items.pop(del_product-1)
    except ValueError:
        print("COMANDO INVÁLIDO, FAVOR SELECIONAR UM DOS NUMEROS DA LISTA.")

def display_cart():
    for i, item in enumerate(cart.items):
        print(f'{i+1} - {item}')

def checkout():
    shirts = sum(1 for c in cart.items if c.category == "shirt")
    comics = sum(1 for c in cart.items if c.category == "comic")
    if comics >=5:
        cart.items = sorted(cart.items, key=lambda x: x.category)
        cart.items[0].price = 0
        cart.items = sorted(cart.items, key=lambda x: x.price)

    if shirts >= 4:
        selected = products["QUADRINHOS"][randint(0,2)]
        qty = int(shirts/4)
        create_comic(f'BRINDE>>> {selected[0]}', 0, qty, selected[2], selected[3])
    print("\nAQUI ESTÁ SUA NOTA FISCAL:\n")
    display_cart()
    print(f'\nTOTAL = R$ {cart.calculate_total():.2f}')
    print("\nOBRIGADO")
    exit()

#Display list of products
def display_list():
    disp_counter = 1
    for categoria in products:
        print(categoria)

        for product in products[categoria]:
            print(f"{disp_counter}-{product[0]} - R${product[1]}")
            disp_counter += 1
        print("---------")

print('SEJA BEM VINDO A NOSSA LOJA, ESSES SAO NOSSOS PRODUTOS DISPONIVEIS:\n')
display_list()
cart = ShoppingCart()

while True:
    options = {
        1: add_to_cart,
        2: delete_from_cart,
        3: display_cart,
        4: display_list,
        5: checkout,
    }
    print("""
O QUE VOCE GOSTARIA DE FAZER?
1 - ADICIONAR PRODUTOS AO CARRINHO
2 - EXCLUIR PRODUTO DO CARRINHO
3 - VER SEU CARRINHO
4 - LISTAR PRODUTOS
5 - CONCLUIR COMPRA
""")
    try:
        user_select = int(input(">>> "))
        if user_select in options:
            options[user_select]()
        else:
            print("COMANDO INVÁLIDO, FAVOR SELECIONAR UM DOS NUMEROS DA LISTA.")
    except ValueError:
        print("COMANDO INVÁLIDO, FAVOR SELECIONAR UM DOS NUMEROS DA LISTA.")



