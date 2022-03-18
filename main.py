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

guild_id = '747124490101588068'

#guild_id = '951610440817995836'

channel_id = '747125833818308789'

#channel_id = '951610440817995839'

members = get_members(guild_id, channel_id) #yes, the channel_id input is required

with open('data.json') as d:
    userdata = json.load(d)

for key in members.keys():
  userNamecomp1 = members[key]["username"]
  userNamecomp2 = members[key]["discriminator"]
  print(key + ": " + userNamecomp1 + "#" + userNamecomp2)

  userdata[key] = {}
  userdata[key]["displayname"] = userNamecomp1 + "#" + userNamecomp2
  userdata[key]["inserver"][guild_id] = {}
  userdata[key]["inserver"][guild_id]["servername"] = bot.gateway.session.guild(guild_id).name
  userdata[key]["inserver"][guild_id]["icon"] = bot.gateway.session.guild(guild_id).icon
  userdata[key]["inserver"][guild_id]["serverdescription"] = bot.gateway.session.guild(guild_id).description
  userdata[key]["inserver"][guild_id]["membercount"] = bot.gateway.session.guild(guild_id).memberCount
  userdata[key]["extrainfo"] = members[key]

with open('data.json', 'w') as outfile:
    json.dump(userdata, outfile, indent = 4)