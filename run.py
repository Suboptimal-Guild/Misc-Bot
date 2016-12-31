#!/usr/bin/python
import argparse

import discord
import asyncio

from commands.commands import get_armory_link as gal
from commands.commands import showhelp
from commands.name import get_char_name as gcn
from commands.name import get_own_name as gon
from commands.name import get_character as getchar
from commands.logs import get_logs_page
from commands.logs import get_logs_links

# Development Constants
DEV_BOT_NAME = "Harambot-Dev"
DEV_BOT_KEY = "MjQ5NTkwMTE3MzU2Nzk3OTUz.CxIg5A.BYYtQ1H4H3l4CuLl-YrWjI50eOk"

# Production Constants
PRODUCTION_BOT_NAME = "Daddybot"
PRODUCTION_BOT_KEY = "MjY0NjE2MTY4MzMyMDY2ODE2.C0jetw.KLucfuDDqpdFgPWDYc3b6LtUCIA"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): # placeholder "bookmarks"
    # also we want to post messages in the channe lwhere the user asked, but
    # if possible make the message only viewable to them kinda like the default bot can do
    if message.author.name == DEV_BOT_NAME or message.author.name == PRODUCTION_BOT_NAME:
        pass
    elif message.content.startswith("!test"):
        await client.send_message(message.channel, 'I\'m a fuckboy.')
    elif message.content.startswith('!armory'):
        await gal(client, message)
    elif message.content.startswith('!whois'):
        await gcn(client, message)
    elif message.content.startswith('!whoami'):
        await gon(client, message)
    elif message.content.startswith('!chars'):
        await getchar(client, message)
    elif message.content == '!help':
        await showhelp(client, message)
    elif message.content.startswith('!bis'):
        pass # do nothing yet
    elif message.content.startswith('!audit') and is_officer(message.author): #officers only (unless maybe people wanna run the audit on themselves?)
        pass # do nothing yet
    elif message.content.startswith('!logs'):
        await get_logs_links(client, message)
    elif message.content.startswith('!logspage'):
        # DOES NOT WORK, see above TODO
        await get_logs_page(client, message)

def is_officer(member):
    return (is_member_of_role(member, "Officers") or
    is_member_of_role(member, "Starlord") or
    is_member_of_role(member, "admin"))

def is_member_of_role(member, role_name):
    for role in member.roles:
        if role_name == role.name:
            return True
    return False

if __name__ == "__main__":
    '''
    Add two mutually exclusive commands, where one of the two is required for the
    script to run.
    '''
    parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d','--dev',help="Run the bot in development mode.",action="store_true")
    group.add_argument('-p', '--prod',help="Run the bot in production mode.",action="store_true")
    args = parser.parse_args()

    client.accept_invite('https://discord.gg/mM5fXCe')

    if args.dev:
        client.run(DEV_BOT_KEY)
    elif args.prod:
        client.run(PRODUCTION_BOT_KEY)
    else:
        print("RIP in peace.")
