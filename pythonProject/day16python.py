# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# def printTable():
#     table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
#     table.add_column("Type",["Electric","Water","Fire"])
#     table.align = "l"
#     print(table)

# Create Class

class User:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001","lamvan")

print(user1.username)