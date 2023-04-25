class Token:
    def __init__(self, token=None):
        if token != None:
            self.token = token
        else:
            import os
            # check replit os env variable
            try: self.token = os.environ['token']
            except:
                try:
                    with open('token.txt', r) as f:
                        token = f.readlines()
                except:
                    token = input('Token: ')
        