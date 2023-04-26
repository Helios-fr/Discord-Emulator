class User:
    def __init__(self, token):
        import discum
        import json

        self.token = token
        self.client = discum.Client(token=token, log=False)

        if self.client.checkToken(self.token) != (True, True):
            print("Invalid Token")
            exit()

        self.activeChannelID = None

    def live(self):
        import discum
        import json
        import colorama

        @self.client.gateway.command
        def _(resp):
            if resp.event.message:

                m = resp.parsed.auto()
                guildID = m['guild_id'] if 'guild_id' in m else None

                channelID = m['channel_id']
                username = m['author']['username']
                discrim = m['author']['discriminator']
                content = m['content']

                time = m['timestamp']
                time = time[:-16]
                time = time[5:7] + '/' + time[8:10] + ' ' + time[11:16]

                if channelID == self.activeChannelID:
                    # print(colorama.Fore.BLUE + message[1], message[0], ": " + colorama.Style.RESET_ALL + message[2])
                    colorama.init()
                    # print(username + ', ' + time + ': ' + content)
                    print(colorama.Fore.BLUE + time + username + '#' +
                          discrim + ': ' + colorama.Style.RESET_ALL + content)

        self.client.gateway.run(auto_reconnect=True)

    def getRelations(self):
        import discum
        import json

        relations = self.client.getRelationships()
        relations = relations.text
        relations = json.loads(relations)

        return relations

    def getFriends(self):
        relations = self.getRelations()
        '''
        [{'id': '140404044182061056', 'type': 1, 'nickname': None, 'user': {'id': '140404044182061056', 'username': 'AussieBloke', 'global_name': None, 'display_name': None, 'avatar': '9e358ef5b1089685d46d706702d723b8', 'discriminator': '0429', 'public_flags': 0, 'avatar_decoration': None}}, {'id': '230987762327748609', 'type': 1, 'nickname': None, 'user': {'id': '230987762327748609', 'username': 'Batninja', 'global_name': None, 'display_name': None, 'avatar': 'f09bd04e07659966ef6df466f55c102e', 'discriminator': '4627', 'public_flags': 0, 'avatar_decoration': None}}]
        '''
        friends = []
        for relation in relations:
            if relation['type'] == 1:
                friends.append(relation)

        return friends

    def getServers(self):
        import discum
        import json

        servers = self.client.getGuilds()
        servers = servers.text
        servers = json.loads(servers)

        return servers

    def getDMID(self, friendID):
        import discum
        import json

        r = self.client.createDM(friendID)
        r = r.text
        r = json.loads(r)

        dmID = r['id']

        return dmID

    def getServerChannels(self, serverID):
        import discum
        import json

        channels = self.client.getGuildChannels(serverID)
        channels = channels.text
        channels = json.loads(channels)

        channels.insert(0, {'id': '0', 'name': 'Exit'})

        return channels

    def getChannelMessages(self, channelID, amount=15):
        import discum
        import json

        messagesRaw = self.client.getMessages(channelID, amount)
        messagesRaw = messagesRaw.text
        messagesRaw = json.loads(messagesRaw)
        messagesRaw.reverse()
        # reverse the list so the messages are in the correct order
        messages = []
        for message in messagesRaw:
            # format the time to be more readable from
            # 2023-04-17T08:18:22.603000+00:00 to 04/17 08:18
            time = message['timestamp'][:-16]
            time = time[5:7] + '/' + time[8:10] + ' ' + time[11:16]

            # add the message to the list
            messages.append([message['author']['username'] + '#' +
                            message['author']['discriminator'], time, message['content']])

        return messages

    def sendMessage(self, channelID, message):
        import discum
        import json

        try:
            r = self.client.sendMessage(channelID, message)
            r = r.text
            r = json.loads(r)

            return r
        except Exception as e:
            return e
