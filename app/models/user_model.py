class UserModel:

    @staticmethod
    def build(data):

        return {
            "cedula": data["cedula"],
            "nombres": data["nombres"],
            "email": data["email"]
        }