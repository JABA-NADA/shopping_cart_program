import time

items = []
prices = []
total = 0

while True:
    print("|=----------------------------------------------=|")
    print("|=------------ WELCOME TO JABA-WEB! ------------=|")
    print("|=----------------------------------------------=|")
    time.sleep(1)


    def nome_do_usuario(nome):
        for word in nome.split():
            for letter in word:
                if letter.lower() not in 'abcdefghijklmnopqrstuvwxyzç':
                    return 'Error'
            return 'Valid'


    name = str(input("Hi! What is your name please?: ")).capitalize()
    time.sleep(0.3)

    user_name = nome_do_usuario(name)

    if 'Error' in user_name:
        print(f"The name: {name}, is NOT valid!")
        name = str(input("Hi! What is your name please?: ")).capitalize()
        time.sleep(0.3)
        user_name = nome_do_usuario(name)

    option = str(input(f'Is the name: {name}, correct? [Y]/[N]:')).upper()
    time.sleep(0.3)

    while option == 'N':
        name = str(input("Hi! What is your name please?: ")).capitalize()
        time.sleep(0.3)

        option = str(input(f'Is the name: {name}, correct? [Y]/[N]:')).upper()
        time.sleep(0.3)

    if option != 'Y' and option != 'N':
        print(f'Error the option: {option}, is NOT valid!')
        time.sleep(0.3)

        name = str(input("Hi! What is your name please?: ")).capitalize()
        time.sleep(0.3)

        option = str(input(f'Is the name: {name}, correct? [Y]/[N]:')).upper()
        time.sleep(0.3)

    item = str(input(f'Ok {name} enter a item to buy:'))
    price = float(input(f'{name} enter a price to {item}: R$'))
    items.append(item)
    prices.append(price)

    answer = str(input(f'{name} do you want to buy another item ? [Y]/[N]: ')).upper()

    while answer == 'Y':
        item = str(input(f'Ok {name} enter a item to buy: '))
        price = float(input(f'{name} enter a price to {item}: R$'))
        items.append(item)
        prices.append(price)

        answer = str(input(f'{name} do you want to buy another item ? [Y]/[N]: ')).upper()

        if answer != 'Y' and answer != 'N':
            print(f'Error the answer {answer} is NOT valid!')

            item = str(input(f'Ok {name} enter a item to buy: '))
            price = float(input(f'{name} enter a price to {item}: R$'))
            items.append(item)
            prices.append(price)

            answer = str(input(f'{name} do you want to buy another item ? [Y]/[N]: ')).upper()

    print("|=------------ YOUR CART ------------=|")

    for item in items:
        print(item, end="|")

    for price in prices:
        total += price
        print()
    print(f'Your total is: R${total}')
    print('--------------------------------------')

    question = str(input(f'{name} would you like to continue? [Y]/[N]: ')).upper()

    if question == 'N':
        print('The end')
        break
