#!/usr/bin/python
import argparse
import os
import discord
import asyncio

from commands.commands import get_armory_link as gal
from commands.commands import showhelp
from commands.name import get_char_name as gcn
from commands.name import get_own_name as gon
from commands.logs import get_logs_page
from commands.logs import get_logs_links

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message):
    # Don't generate a message if it came from another bot. This may be added
    # later.
    if is_bot(message.author):
        pass
    # Easy check for if the bot is awake.
    elif message.content.startswith("!test"):
        await client.send_message(message.channel, "I\'m awake.")
    # Grab an armory link.
    elif message.content.startswith("!armory"):
        await gal(client, message)
    # Get the information for a discord user.
    elif message.content.startswith("!whois"):
        await gcn(client, message)
    # Get the information for yourself.
    elif message.content.startswith("!whoami"):
        await gon(client, message)
    # Get a list of all available commands.
    elif message.content == "!help":
        await showhelp(client, message)
    # Get an audit for a character.
    elif message.content.startswith("!audit") and is_officer(message.author): #officers only (unless maybe people wanna run the audit on themselves?)
        pass # do nothing yet
    # Get links to logs.
    elif message.content.startswith("!logs"):
        await get_logs_links(client, message)

def is_bot(member):
    return is_member_of_role(member, "botlords")

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
    group.add_argument("-d", "--dev", help="Run the bot in development mode.", action="store_true")
    group.add_argument("-p", "--prod", help="Run the bot in production mode.", action="store_true")
    args = parser.parse_args()

    if args.dev:
        client.run(os.environ["MISCELLANEOUS_BOT_DEVELOPMENT_TOKEN"])
    elif args.prod:
        client.run(os.environ["MISCELLANEOUS_BOT_PRODUCTION_TOKEN"])
    else:
        print("Error: Bot Environment Ambiguous")
