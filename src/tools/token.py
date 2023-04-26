class Token:
    def __init__(self, token=None):
        if token is not None:
            self.token = token
        else:
            import os
            # check replit os env variable
            try:
                self.token = os.environ['token']
            except BaseException:
                try:
                    with open('token.txt', r) as f:
                        token = f.readlines()
                except BaseException:
                    import colorama
                    colorama.init()
                    token = input(
                        colorama.Fore.GREEN +
                        "Token: " +
                        colorama.Style.RESET_ALL)

    def getToken(self):
        return self.token
