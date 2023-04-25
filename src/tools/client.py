class Client:
    def __init__(self, token):
        from .user import User
        from threading import Thread

        self.token = token
        self.user = User(token)

        self.userThread = Thread(target=self.user.live)
        self.userThread.start()

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
        import colorama

        minimalFriends = []
        for friend in self.friends:
            minimalFriends.append(friend['user']['username'] + "#" + friend['user']['discriminator'])

        menu = Menu("DMs", minimalFriends, 3)
        choice = menu.showMenu()

        # get the friend ID from the choice
        friendID = self.friends[choice]['id']
        friendDMID = self.user.getDMID(friendID=friendID)
        messages = self.user.getChannelMessages(channelID=friendDMID, amount=100)
        colorama.init()
        for message in messages:
            # print(message[1], message[0], ": ", message[2])
            print(colorama.Fore.BLUE + message[1], message[0], ": " + colorama.Style.RESET_ALL + message[2])
        
        self.user.activeChannelID = friendDMID

        while True:
            message = input()
            if "&" in message:
                break
            self.user.sendMessage(channelID=friendDMID, message=message)
        
        self.mainMenu()
    
    def serverMenu(self, serverID):
        from .menu import Menu
        from .user import User
        import colorama

        minimalChannels = []
        channels = self.user.getServerChannels(serverID=serverID)
        for channel in channels:
            minimalChannels.append(channel['name'])
        
        menu = Menu("Server Menu", minimalChannels, 3)
        choice = menu.showMenu()

        # get the channel ID from the choice
        channelID = channels[choice]['id']
        messages = self.user.getChannelMessages(channelID=channelID, amount=100)
        colorama.init()
        for message in messages:
            # print(message[1], message[0], ": ", message[2])
            print(colorama.Fore.BLUE + message[1], message[0], ": " + colorama.Style.RESET_ALL + message[2])
        
        self.user.activeChannelID = channelID

        while True:
            message = input()
            if "&" in message:
                break
            self.user.sendMessage(channelID=channelID, message=message)
        
        self.mainMenu()








