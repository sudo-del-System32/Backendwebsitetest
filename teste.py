print("HELLO WORLD!")
print("HELLO There again!")
print("and again!")
print("this really cool!")
print("coding fast!")

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email
        }
    
    def __repr__(self):
        return f"<User {self.name} {self.email}>"

user = User("pedro", "pedro@email.com")
print(user)