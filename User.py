class User:
    def __init__(self, name, email, password, address, cpf):
        self.name = name
        self.email = email
        self.password = password
        self.address = address

    def register(self):
        pass


class Seller_Shelter:
    def __init__(self, name, email, password, address, category, cnpj, docs, description):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.category = category
        self.cnpj = cnpj
        self.docs = docs
        self.description = description
        self.pets = []
        self.photos = []

    def add_pet(self):
        pass
