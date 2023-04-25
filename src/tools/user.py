class User:
    def __init__(self, token):
        import discum


        self.token = token
        self.client = discum.Client(token=token, log=False)
        
        # ['id', 'username', 'avatar', 'discriminator', 'public_flags', 'flags', 'locale', 'nsfw_allowed', 'mfa_enabled', 'analytics_token', 'email', 'verified', 'phone']
        information = self.client.checkToken(self.token)

        self.id = information['id']
        self.username = information['username']
        self.avatar = information['avatar']
        self.discriminator = information['discriminator']
        self.public_flags = information['public_flags']
        self.flags = information['flags']
        self.locale = information['locale']
        self.nsfw_allowed = information['nsfw_allowed']
        self.mfa_enabled = information['mfa_enabled']
        self.analytics_token = information['analytics_token']
        self.email = information['email']
        self.verified = information['verified']
        self.phone = information['phone']

        del information
    
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


        
        