import csv


class Product:
    """
    This class represents a Product unit.

    products - list of all products
    """
    products = []

    def __init__(
            self,
            name: str,
            barcode: int,
            country: str,
            price: float
    ):
        """
        Initialize product.

        :param name: Name of product
        :param barcode: Barcode of product
        :param country: Country of product
        :param price: Price of product
        """
        self.__name = name
        self.__barcode = barcode
        self.__country = country
        self.__price = price

    @property
    def name(self) -> str:
        """
        :return: Name of product
        """
        return self.__name

    @property
    def barcode(self) -> int:
        """
        :return: Barcode of product
        """
        return self.__barcode

    @property
    def country(self) -> str:
        """
        :return: Country of product
        """
        return self.__country

    @property
    def price(self) -> float:
        """
        :return: Price of product
        """
        return self.__price

    @staticmethod
    def load_products(filename: str) -> None:
        """
        :param filename: Name of file with products.
        :return: None
        """
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name, barcode, country, price = row
                Product.products.append(Product(name, int(barcode), country, float(price)))

    def __str__(self):
        return self.__name

    def __repr__(self):
        return (
            f'Name: {self.__name}\n'
            f'Barcode: {self.__barcode}\n'
            f'Country: {self.__country}\n'
            f'Price: {self.__price}'
        )


class ShoppingCart:
    """
    This class represents a shopping cart unit.
    """
    def __init__(self):
        self.__products = []
        self.__total_price = 0.0

    @property
    def products(self) -> list:
        """
        :return:  list of products
        """
        return self.__products

    @property
    def total_price(self) -> float:
        """
        :return: total price
        """
        return self.__total_price

    def add_product(self, product: Product) -> None:
        """
        :param product: Product to add
        :return: None
        """
        self.__products.append(product)
        self.__total_price += product.price

    def remove_product(self, id: int) -> None:
        """
        :param id: ID of product to remove.
        :return: None
        """
        price = self.__products[id].price
        self.__products.pop(id)
        self.__total_price -= price

    def view_cart(self) -> str:
        """
        :return: string with list of products
        """
        res = ''
        for product in self.__products:
            res += (
                f'[{self.__products.index(product)}] - '
                f'Название: {product.name}, '
                f'Штрих-код: {product.barcode}, '
                f'Страна-производитель: {product.country}, '
                f'Цена: {product.price}\n'
            )
        res += f'\nИтого: {self.__total_price}'
        return res
