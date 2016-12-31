from texttable import Texttable

import discord
import asyncio

#TODO: modularize code more and split into multiple files, im exhausted as fuck so just cramming it in here for now, it works though

# for some reason, there is a massive stink with this??? i think maybe python 2.7 vs 3.5 conflict... ill keep working in the google_sheets_interface file to get functionality down before linking it up
from google.sheets import get_main_character_name as gmcn

def get_help_strings():
    header_text = ":banana: Currently I know the following commands: :banana:"
    t = Texttable()
    t.add_rows([["Command", "Description"],
                ["!armory <character_name> <server> (if not from ED)", "Generates an armory link for the given character."],
                #["!chars <discord_name>", "Generates a list of the discord user's World of Warcraft characters."],
                ["!roster add <name>", "Adds to the raid roster."],
                ["!roster remove <name>", "Removes from the raid roster."],
                ["!roster status <name>", "Prints out current raid roster."],
                ["!whoami", "Prints out your Discord info."],
                ["!whois <discord_name>", "Prints out the Discord info of a user."],
                ["!epgp", "Prints the entire EPGP leaderboard."],
                ["!epgp leaderboard <params>", "Prints EPGP leaderboard for the parameters specified."],
                ["!epgp export <export string>", "Update the EPGP spreadsheet."]
                ])

    str1 = "```"
    str1 += t.draw()
    str1 += "```"

    t = Texttable()
    t.add_rows([["Command", "Description"],
                ["!postout <startdate> <starttime> <enddate> <endtime>", "Create a calendar event to post out for a given time period.\n" +
                                                                         "Date Format: (mm/dd/yy)\n" +
                                                                         "Time Format: (hh:mm{AM/PM}) OR use (hh:mm) in military time"],
                ["!late <date>", "Create a calendar event to specify that you will be late on a given night\n" +
                                 "Date Format: (mm/dd/yy)"],
                ["!absent <date>", "Create a calendar event to specify that you will be absent on a given night\n" +
                                 "Date Format: (mm/dd/yy)"],
                #["!bis",""],
                #["!audit",""],
                ["mention the word \"joke\"", "I will tell you a joke."],
                ["!logs", "Posts the WarcraftLogs links."],
                #["!logspage <character name> <server> (if not from ED)", "Generates the URL for a player's page on WarcraftLogs."]
                ])

    str2 = "```"
    str2 += t.draw()
    str2 += "```"

    footer_text = "\n:monkey_face: I'm a work in progress with more commands coming each and every day- if you have any suggestions forward them to my overlords Mortivius and Ian! :monkey_face:"
    return header_text, str1, str2, footer_text

async def showhelp(client, message):
    # prints out all commands that Harambot currently knows
    header, str1, str2, footer = get_help_strings()

    await client.send_message(message.channel, header)
    await client.send_message(message.channel, str1)
    await client.send_message(message.channel, str2)
    await client.send_message(message.channel, footer)

async def get_armory_link(client, message):
    # format: !armory <name> <optional server>
    s = message.content.split()

    if len(s) == 2:
        link = "http://us.battle.net/wow/en/character/emerald-dream/" + s[1].title() + "/advanced"
        await client.send_message(message.channel, ":banana: Armory link for **" + str(s[1]) + "**: " + link + " :banana:")
    elif len(s) == 3:
        link = "http://us.battle.net/wow/en/character/" + s[2].lower() + "/" + s[1].title() + "/advanced"
        await client.send_message(message.channel, ":banana: Armory link for **" + str(s[1]) + "**: " + link + " :banana:")
    #TODO: we sure there are no realms that are 3 words???
    else:
        link = "http://us.battle.net/wow/en/character/" + s[2].lower() + "-" + s[3].lower() + "/" + s[1].title() + "/advanced"
        await client.send_message(message.channel, ":banana: Armory link for **" + str(s[1]) + "**: " + link + " :banana:")
