from distutils.log import info
from textwrap import indent
from tokenize import Token
import discum
import json

f = open('Token.txt', "r")
myToken = f.read()

bot = discum.Client(token=myToken)

def close_after_fetching(resp, guild_id):
	if bot.gateway.finishedMemberFetching(guild_id):
		#lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
		#print(str(lenmembersfetched)+' members fetched') #this line is optional
		bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
		bot.gateway.close()

def get_members(guild_id, channel_id):
	bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #get all user attributes, wait 1 second between requests
	bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
	bot.gateway.run()
	bot.gateway.resetSession() #saves 10 seconds when gateway is run again
	return bot.gateway.session.guild(guild_id).members

def Scan_and_deposit(guild_id, channel_id):
  members = get_members(guild_id, channel_id) #yes, the channel_id input is required

  with open('data.json') as d:
      userdata = json.load(d)

  for key in members.keys():
    userNamecomp1 = members[key]["username"]
    userNamecomp2 = members[key]["discriminator"]
    print(key + ": " + userNamecomp1 + "#" + userNamecomp2)

    if key in userdata:
      #userdata[key] = {}
      userdata[key]["displayname"] = userNamecomp1 + "#" + userNamecomp2
      #userdata[key]["inserver"] = {}
      userdata[key]["inserver"][guild_id] = {}
      userdata[key]["inserver"][guild_id]["servername"] = bot.gateway.session.guild(guild_id).name
      userdata[key]["inserver"][guild_id]["icon"] = bot.gateway.session.guild(guild_id).icon
      userdata[key]["inserver"][guild_id]["serverdescription"] = bot.gateway.session.guild(guild_id).description
      userdata[key]["inserver"][guild_id]["membercount"] = bot.gateway.session.guild(guild_id).memberCount
    else:
      userdata[key] = {}
      userdata[key]["displayname"] = userNamecomp1 + "#" + userNamecomp2
      userdata[key]["inserver"] = {}
      userdata[key]["inserver"][guild_id] = {}
      userdata[key]["inserver"][guild_id]["servername"] = bot.gateway.session.guild(guild_id).name
      userdata[key]["inserver"][guild_id]["icon"] = bot.gateway.session.guild(guild_id).icon
      userdata[key]["inserver"][guild_id]["serverdescription"] = bot.gateway.session.guild(guild_id).description
      userdata[key]["inserver"][guild_id]["membercount"] = bot.gateway.session.guild(guild_id).memberCount
    #userdata[key]["extrainfo"] = members[key]

  with open('data.json', 'w') as outfile:
      json.dump(userdata, outfile, indent = 4)

################## Things for you to change if you want

guild_id = input("Enter the id of the server: ")
channel_id = input("Enter the id of a channel in the server: ")

Scan_and_deposit(guild_id, channel_id)