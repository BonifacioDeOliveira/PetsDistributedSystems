class Chat:
    def __init__(self, cpf, cnpj):
        self.cpf = cpf
        self.cnpj = cnpj


class Message:
    def __init__(self, sender_id, content, timestamp):
        self.sender = sender_id
        self.content = content
        self.timestamp = timestamp
