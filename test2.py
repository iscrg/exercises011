from solution2 import ShoppingCart, Product

filename = input('Введите название файла для подгрузки товаров: ')
Product.load_products(filename)
shopping_cart = ShoppingCart()

while True:
    choice = int(input(
        f'Меню:\n'
        f'[1] - Просмотреть корзину\n'
        f'[2] - Просмотреть итоговую стоимость корзины\n'
        f'[3] - Добавить товар в корзину\n'
        f'[4] - Удалить товар из корзины\n'
        f'Введите действие: '
    ))

    if choice == 1:
        print(shopping_cart.view_cart())

    elif choice == 2:
        print(shopping_cart.total_price)

    elif choice == 3:
        for product in Product.products:
            print(f'[{Product.products.index(product)}] - {product}')
        choice = int(input(f'Выберите товар: '))

        print(Product.products[choice])
        shopping_cart.add_product(Product.products[choice])
        print('Товар успешно добавлен!')

    elif choice == 4:
        print(shopping_cart.view_cart())
        choice = int(input('Выберите товар, который хотите удалить: '))
        shopping_cart.remove_product(choice)
        print('Товар успешно удален!')

    else:
        print('Неверный пункт меню.')

    print('=' * 120)
