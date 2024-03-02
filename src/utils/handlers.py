def command_handler(message: str, bot, channelid):
    message = message.removeprefix(".")
    print(f"Command: {message}")

    '''
    Commands:
    .exit: exits the live connection and returns to the main menu
    .help: shows the help menu
    '''

    if message == "help":
        print("---")
        print(".exit: exits the live connection and returns to the main menu")
        print(".help: shows the help menu")
        print("---")
    elif message == "exit":
        bot.gateway.close()