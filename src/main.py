import discum
import os
import json
from utils import ui, handlers
from threading import Thread

# token = os.environ['token']
token = open("token.secret", "r").read()
bot = discum.Client(token=token, log=False)

# get the users friends and guilds
friends = bot.getRelationships()
friends = json.loads(friends.text)
friends = [[friend['user']['username'] + "#" + friend['user']['discriminator'], friend['user']['id']] for friend in friends]

guilds = bot.getGuilds()
guilds = json.loads(guilds.text)
guilds = [['Direct Messages', '0']] + [[guild['name'], guild['id']] for guild in guilds]

friends_list, guilds_list = [friend[0] for friend in friends], [guild[0] for guild in guilds]

# main loop
while True:
    # ask the user for a guild
    guild = guilds[ui.create_list(guilds_list, "Select a guild") - 1]

    # if the id is 0, it's a direct message so ask for a friend
    if guild[1] == '0':
        friend = friends[ui.create_list(friends_list, "Select a friend") - 1]
        dmid = json.loads(bot.createDM(friend[1]).text)['id']
        message_list = json.loads(bot.getMessages(dmid, 10).text)[::-1]
        for message in message_list:
            print(f"{message['author']['username']}#{message['author']['discriminator']} ({message['timestamp'][5:7]}/{message['timestamp'][8:10]} {message['timestamp'][11:16]}): {message['content']}")

        @bot.gateway.command
        def onMessage(resp):
            if resp.event.message:
                message = resp.parsed.auto()
                if message['channel_id'] == dmid:
                    print(f"{message['author']['username']}#{message['author']['discriminator']} ({message['timestamp'][5:7]}/{message['timestamp'][8:10]} {message['timestamp'][11:16]}): {message['content']}")
        Thread(target=bot.gateway.run).start()
        print("> Live connection started, type '.help' for commands.")
        while True:
            message = input("")
            if message.startswith(".exit"): break
            if message.startswith("."):
                handlers.command_handler(message, bot, dmid)
            else:
                bot.sendMessage(dmid, message)
        bot.gateway.close()

    else:
        channels = bot.getGuildChannels(guild[1])
        channels = json.loads(channels.text)
        channels = [channel for channel in channels if channel['type'] == 0]
        channels = [[channel['name'], channel['id']] for channel in channels]
        channels_list = [channel[0] for channel in channels]

        # ask the user for a channel
        channel = channels[ui.create_list(channels_list, "Select a channel") - 1]

        message_list = json.loads(bot.getMessages(channel[1], 10).text)[::-1]
        for message in message_list:
            print(f"{message['author']['username']}#{message['author']['discriminator']} ({message['timestamp'][5:7]}/{message['timestamp'][8:10]} {message['timestamp'][11:16]}): {message['content']}")
        @bot.gateway.command
        def onMessage(resp):
            if resp.event.message:
                message = resp.parsed.auto()
                if message['channel_id'] == channel[1]:
                    print(f"{message['author']['username']}#{message['author']['discriminator']} ({message['timestamp'][5:7]}/{message['timestamp'][8:10]} {message['timestamp'][11:16]}): {message['content']}")
        Thread(target=bot.gateway.run).start()
        print("> Live connection started, type '.help' for commands.")
        while True:
            message = input("")
            if message.startswith(".exit"): break
            if message.startswith("."):
                handlers.command_handler(message, bot, channel[1])
            else:
                bot.sendMessage(channel[1], message)
        bot.gateway.close()
        


