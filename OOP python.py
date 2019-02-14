class User:
    name = ''
    email = ''
    password = ''
    login = False

    def __init__(self, name: object, email: object, password: object) -> object:
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        email = input("Enter Email : ")
        password = input("Enter Password: ")


        if email == self.email and password == self.password:
            login = True
            print("Login Successful")
        else:
            print("Login Faild")
    def logout(self):
        login = False
        print("logged Out")
    def isLoggedin(self):
        if self.login:
            return True
        else:
            return False
    def profile(self):
        if self.isLoggedin():
            print(self.name, "\n", self.email)
        else:
            print("User is not Logged in")

user1 = User("hasnain", "bb@uni", "1234")
user1 = User("rok", "ht@uni", "34")

'''user1.name = "Hasnain"
user1.email = "ht@gmail.com"
user1.password = "1234"'''

user1.login()
user1.profile()

