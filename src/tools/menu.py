class Menu:
    def __init__(self, name, options, collums):
        self.name = name
        self.options = options
        self.collums = collums
    
    def showMenu(self):
        import colorama
        colorama.init()

        # print a menu with numbered options in the amount of collums

        print(colorama.Fore.GREEN + self.name + colorama.Style.RESET_ALL)
        for i in range(0, len(self.options), self.collums):
            for j in range(self.collums):
                if i + j < len(self.options):
                    print(colorama.Fore.GREEN + str(i + j + 1) + colorama.Style.RESET_ALL + " - " + colorama.Fore.CYAN + self.options[i + j] + colorama.Style.RESET_ALL, end=" " * (30 - len(self.options[i + j])))
            print()
        

        # get user input
        choice = input(colorama.Fore.GREEN + "Choice: " + colorama.Style.RESET_ALL)
        if "&" in choice:
            exit()
        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(self.options):
            choice = input(colorama.Fore.GREEN + "Choice: " + colorama.Style.RESET_ALL)
            if "&" in choice:
                exit()

        return int(choice) - 1
        

if __name__ == "__main__":
    # create a menu object and show it
    menu = Menu("Test Menu", ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6"], 3)
    choice = menu.showMenu()
    print(choice)

    # find what option was chosen
    print(menu.options[choice])