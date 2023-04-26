from tools import *
import colorama


def main():
    # create a menu object and show it
    menu = Menu("Test Menu", ["Start Terminal Client"], 3)
    choice = menu.showMenu()

    if choice == 0:
        colorama.init()
        print(
            colorama.Fore.BLUE +
            "Starting Terminal Client..." +
            colorama.Style.RESET_ALL)
        token = Token()
        client = Client(token=token.getToken())


main()
