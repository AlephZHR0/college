class UserDTO:
    def __init__(self, user_id, name, user_name, email, password):
        self.user_id = user_id
        self.name = name
        self.user_name = user_name
        self.email = email
        self.password = password

    @staticmethod
    def from_model(model):
        return UserDTO(user_id=model.user_id, name=model.name, email=model.email, user_name=model.user_name, password=model.password)
