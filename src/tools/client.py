class Client:
    def __init__(self, token):
        from .user import User
        self.token = token
        self.user = User(token)

        self.friends = self.user.getFriends()

        self.servers = self.user.getServers()
        self.servers.insert(0, {'id': '0', 'name': 'DMs'})

        self.mainMenu()

    def mainMenu(self):
        from .menu import Menu
        from .user import User

        minimalServers = []
        for server in self.servers:
            minimalServers.append(server['name'])
        
        menu = Menu("Main Menu", minimalServers, 3)
        choice = menu.showMenu()

        # get the server ID from the choice
        serverID = self.servers[choice]['id']
        if serverID == '0':
            # DMs
            self.dmsMenu()
        else:
            # server
            self.serverMenu(serverID)
    
    def dmsMenu(self):
        from .menu import Menu
        from .user import User

        minimalFriends = []
        for friend in self.friends:
            minimalFriends.append(friend['user']['username'] + "#" + friend['user']['discriminator'])

        menu = Menu("DMs", minimalFriends, 3)
        choice = menu.showMenu()

        # get the friend ID from the choice
        friendID = self.friends[choice]['id']
        messages = self.user.getChannelMessages(channelID=self.user.getDMID(friendID=friendID), amount=15)
        for message in messages:
            print(message[1], message[0], ": ", message[2])
    
    def serverMenu(self, serverID):
        from .menu import Menu
        from .user import User

        menu = Menu("Server Menu", self.user.getServerChannels(serverID=serverID), 3)
        choice = menu.showMenu()

        if choice == 0:
            self.openChannel(serverID)
        else:
            self.mainMenu()






