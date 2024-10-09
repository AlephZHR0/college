class UserDTO:
    def __init__(self, user_id, name, email, cpf, telefone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.cpf = cpf
        self.telefone = telefone

    @staticmethod
    def from_model(model):
        return UserDTO(user_id=model.user_id, name=model.name, email=model.email, cpf=model.cpf, telefone=model.telefone)
