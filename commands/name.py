from texttable import Texttable

import discord
import asyncio
import json

async def get_char_name(client, message):
    msg = message.content.split()

    name = msg[1]

    isNameFound = False

    nickname = ""
    roles = ""

    for member in message.server.members:
        if name == member.name:
            isNameFound = True
            if member.nick is not None:
                nickname = member.nick
            roles = member.roles
            break

    str = "Discord User name: " + name + "\nNickname on server " + message.server.name + ": " + nickname + "\nRoles: "
    for role in roles:
        str += (role.name + ", ")
    str = str[:-2]

    await client.send_message(message.channel, str)

async def get_own_name(client, message):
    str = ""
    if message.author.name != None: str += "Discord User name: " + message.author.name
    if message.server.name != None and message.author.nick != None:
        str += "\nNickname on server " + message.server.name + ": " + message.author.nick + "\nRoles: "
    else:
        str += "\nRoles: "
    for role in message.author.roles:
        str += (role.name + ", ")
    str = str[:-2]

    await client.send_message(message.channel, str)
