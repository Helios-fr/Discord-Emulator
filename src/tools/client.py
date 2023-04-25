class Client:
    def __init__(self, token):
        from .user import User
        self.token = token
        self.user = User(token)

        self.friends = self.user.getFriends()

        self.servers = self.user.getServers()
        self.servers.insert(0, {'id': '0', 'name': 'DMs'})

    def mainMenu(self):
        from .menu import Menu
        from .user import User

        minimalServers = []
        for server in self.servers:
            minimalServers.append([server['name'], server['id']])
        
        menu = Menu("Main Menu", minimalServers, 3)
        choice = menu.showMenu()

