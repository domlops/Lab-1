class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.serial = 0

    def __str__(self):
        return f"{self.name} - R${self.price:.2f}"


class TShirt(Product):
    def __init__(self, name, price, size):
        self.category = "shirt"
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"{super().__str__()}, Tamanho: {self.size} (No de Serie: {self.serial})"


class Mug(Product):
    def __init__(self, name, price, capacity):
        self.category = "mug"
        super().__init__(name, price)
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()}, Capacidade: {self.capacity:.2f}L (No de Serie: {self.serial})"


class ComicBook(Product):
    def __init__(self, name, price, author, publisher):
        self.category = "comic"
        super().__init__(name, price)
        self.author = author
        self.publisher = publisher

    def __str__(self):
        return f"{super().__str__()}, Autor: {self.author}, Editora: {self.publisher} (No de Serie: {self.serial})"

products = {
    "CAMISAS": [("VINGADORES", 39.99), ("BATMAN", 39.99), ("DEADPOOL", 39.99)],
    "CANECAS": [("RICK & MORTY", 29.99, 0.5), ("LOL", 29.99, 0.5), ("FORTNITE", 25.99, 0.35)],
    "QUADRINHOS": [("SPIDERMAN", 19.99, "ZEB WELLS", "MARVEL"), ("SANDMAN", 35.99, "NEIL GAIMAN", "DC"), ("FABLES", 29.99, "BILL WILLINGHAM", "VERTIGO")],
}
